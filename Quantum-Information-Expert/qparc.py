from typing import List, Tuple, Union

from openfermion import FermionOperator
from openfermion.chem import MolecularData
from openfermion.transforms import get_fermion_operator
from openfermionpyscf import run_pyscf
from qulacs import Observable as QulacsObservable
from qulacs import QuantumCircuit as QulacsQuantumCircuit
from qulacs import QuantumState as QulacsQuantumState
from qulacs.observable import (
    create_observable_from_openfermion_text as qulacs_create_observable_from_openfermion_text,
)
import warnings
import numpy as np

MAX_SHOTS = int(1e8)


class QulacsExecutor:
    """QulacsExecutor
    Executor for the challenge.
    Attributes:
        total_shots:
            Total shots used in the current run.
        total_jobs:
            Total jobs ran in the current run.
        self.fci_energy:
            Full-CI energy.
        self.hf_energy:
            Hartree-Fock energy.
    """

    def __init__(self) -> None:
        self.total_shots = 0
        self.total_jobs = 0
        self._current_value = 0
        self._result = []
        self.fci_energy = 0
        self.hf_energy = 0

    def get_problem_hamiltonian(self) -> Tuple[FermionOperator, int]:
        """get_problem_hamiltonian
        Returns the problem Hamiltonian and the number of qubits for the problem.

        Returns:
            fermionic_hamiltonian:
                Hamiltonian for the problem.
            n_qubits:
                The number of qubits.
        """
        basis = "sto-3g"
        multiplicity = 1
        charge = 0
        distance = 1.0
        geometry = [["H", [0, 0, distance * i]] for i in range(4)]
        description = "H4"
        molecule = MolecularData(geometry, basis, multiplicity, charge, description)
        molecule = run_pyscf(molecule, run_scf=1, run_fci=1)
        self.hf_energy = molecule.hf_energy
        self.fci_energy = molecule.fci_energy
        n_qubits = molecule.n_qubits
        # n_electron = molecule.n_electrons
        fermionic_hamiltonian = get_fermion_operator(
            molecule.get_molecular_hamiltonian()
        )
        return fermionic_hamiltonian, n_qubits

    def sampling(
        self,
        circuit: Union[QulacsQuantumCircuit, List[QulacsQuantumCircuit]],
        state_int: int,
        n_qubits: int,
        n_shots: Union[int, float],
    ) -> List[int]:
        """sampling
        Returns the problem Hamiltonian and the number of qubits for the problem.

        Args:
            circuit:
                The quantum circuit to be applied to the initial state before sampling.
            state_int:
                The integer defining the initial state in the computational basis.
            n_qubits:
                The number of qubits.
            n_shots:
                The number of shots for the sampling.

        Returns:
            The list of integers corresponding to the sampled bit strings.
        """
        if self.total_shots + n_shots > MAX_SHOTS:
            raise TotalShotsExceeded()
        self.total_jobs += 1
        self.total_shots += n_shots

        _state = QulacsQuantumState(n_qubits)
        _state.set_computational_basis(state_int)
        if isinstance(circuit, QulacsQuantumCircuit):
            circuit.update_quantum_state(_state)
        else:
            for circuit_ in circuit:
                circuit_.update_quantum_state(_state)
        return _state.sampling(n_shots)

    @property
    def current_value(self):
        pass

    @current_value.getter
    def current_value(self):
        return self._current_value

    @current_value.setter
    def current_value(self, value):
        self._current_value = value

    def record_result(self, verbose: bool = True) -> None:
        self._result.append(self._current_value)
        if verbose:
            print("\n############## Result ##############")
            print(f"Resulting energy = {self._current_value}")
            print(f"total_shots =", self.total_shots)
            print("------------------------------------")
            print(f"FCI energy = {self.fci_energy}")
            print(f"HF energy = {self.hf_energy}")
            print("####################################\n")
        self.total_shots = 0
        self.total_jobs = 0
        self._current_value = 0

    def reset(self):
        self.total_shots = 0
        self.total_jobs = 0
        self._current_value = 0
        self._result = []

    def evaluate_final_result(self):
        if len(self._result) > 10:
            warnings.warning("We will evaluate final ten results.")
            self._result = self._result[-10:]
        elif len(self._result) < 10:
            raise ValueError("You should record the result ten times.")

        print("\n############## Final Result ##############")
        print(f"Average energy:", np.average(self._result))
        print(
            f"Average accuracy:",
            np.average([np.abs(res - self.fci_energy) for res in self._result]),
        )
        print("------------------------------------------")
        print(f"FCI energy = {self.fci_energy}")
        print(f"HF energy = {self.hf_energy}")
        print("##########################################")


class Observable(QulacsObservable):
    def get_expectation_value(self, state):
        raise NotImplementedError(
            "You cannot use a statevector simulator. Use qulacs.Observable for debugging."
        )

    def get_transition_amplitude(self, state1, state2):
        raise NotImplementedError(
            "You cannot use a statevector simulator. Use qulacs.Observable for debugging."
        )


def create_observable_from_openfermion_text(str):
    obs2 = qulacs_create_observable_from_openfermion_text(str)
    n_qubits = obs2.get_qubit_count()
    obs = Observable(n_qubits)
    for i_term in range(obs2.get_term_count()):
        obs.add_operator(obs2.get_term(i_term))
    return obs


class TotalShotsExceeded(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The number of total shots exceeded the limit."
