# QPARC Challenge - Quantum Information

## Background
Recent years saw a great advance both in hardware and software of quantum computing, and its practical use is believed to happen very soon. One of the most promising application would be quantum chemistry; we have Quantum Phase Estimation algorithm, which can exactly calculate the ground state energy efficiently when an initial state of moderate quality is given, although we have to wait for a fully fault-tolerant device to run the algorithm.

Another algorithm that is believed to be useful for quantum chemistry is Variational Quantum Eigensolver (VQE). VQE is an algorithm that searches for the lowest energy state, with a given form of parametrized quantum circuit. Because of its variational nature and the use of shallow circuits, VQE is expected to be executable even with the level of physical noise of near-term devices, often classified as Noisy Intermediate-Scale Quantum (NISQ) devices. Although VQE is a heuristic algorithm and has no performance guarantee, it surely can do something that classical computers cannot do efficiently, and is one of the most interesting application of NISQ devices.

Although promising, VQE has some challenges to overcome. 
- **Statistical error** due to the sampling uncertainty. During VQE, the energy expectation value is calculated by sampling the state in various basis, and the statistical error increases significantly, although not exponentially, as the system size grows. This means that a large number of shots is required to achieve certain accuracy.
- **Large number of iterations** for the optimization process. It is also important to reduce the number of iterations during the VQE calculation, which grows as the system size increases. Moreover, there is a phenomenon called the barren plateau problem, which basically states that it will be exponentially difficult to proceed optimization from a random state, as the system size get larger. To solve those problems, it will be important to have a good initial state that is close to the exact ground state, and also to engineer ansatz and optimizer so that we will not need many iterations, and will not stuck in a random state.

It is crucial to have a strategy to reduce the number of shots at each iteration by reducing the statistical error, and also to reduce the number of iterations, thereby reducing the total number of shots required for the entire VQE run. It would also be desirable to have an alternative algorithm to VQE that reduces the number of total shots. This leads to the task for this challenge, described in the following.

## Problem Description
- Your task is to find the ground state energy of an H4 molecule, a linear hydrogen chain of length 4, as accurate as possible, with an algorithm that is executable on NISQ devices.
- More specifically, you are allowed to use 10^8 shots, i.e. to execute 10^8 quantum circuits, on a sampling simulator with no physical noise, and are asked to obtain the ground state energy of the molecule as close as the Full-CI energy, using the result of the 10^8 shots.
- The participants are expected to submit a slide presentation that explains your idea, and a code that implements it. We will evaluate both the result of the code, and also your idea itself.

### The scope of your idea
- Improvements of VQE. The example code is implementing a simple VQE. Improvements will be possible in, for example,
    - Better state preparation than the Hartree-Fock state
    - Better ansatz
    - Better choice of optimizer
    - Shot allocation
    - Grouping the Pauli terms
    - Reducing the number of qubits by exploiting the symmetries
- Alternatives of VQE. We highly evaluate if you come up with an algorithm beyond VQE. 
    - The algorithm should be executable on NISQ devices with a moderate fidelity, i.e. the algorithm should not have a circuit depth comparable to that of Quantum Phase Estimation.

### Evaluation criteria for the slides
- Novelty
    - The idea will be highly evaluated if the idea has a significant novelty.
- Scalability for a larger system size
    - The idea must be useful for larger systems, not just for a H4 molecule.
- Resilience for the noise of the NISQ devices.
    - The idea that has resilience for the noise will be highly evaluated, as it is an important factor to be useful in near future.

### Evaluation criteria for the codes
- The average accuracy of ten runs of the code.
    - You will be allowed to use 10^8 shots for each run, and your task is to maximize the accuracy, defined by the absolute difference of resulting energy and the Full-CI energy.
    - An example code is given as `example.ipynb`, and the participants are expected to implement their own algorithms in a similar format.

### Technical details
- You can modify any content of `example.ipynb`, but you should execute your quantum circuits always through `QulacsExecutor`, and the energy value, stored in `QulacsExecutor.current_value`, at the time when `QulacsExecutor.record_result()` is called will be evaluated.
- The content of `qparc.py` should be kept untouched, unless there is a serious problem, or you find it incompatible with your idea. In the latter case, you should modify it in a manner that we can clearly keep track of the total shots.
- The choice of initial parameters should be done in a scalable manner. For example, you can choose how random the initial parameters can be from the all-zero array, but you cannot hard-code a good parameter set that is close to the ground state.
- You may use some ancilla qubits, but we should be able to test your code on a laptop in less than ten minutes per run.
- We will rerun the final evaluation `QulacsExecutor.evaluate_final_result()` by ourselves, and you will be evaluated by the result.