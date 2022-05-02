# QPARC Challenge - Quantum Chemistry

## Background
The materials around us are constructed from molecules and the microscopic behavior is dominated by quantum mechanics.
Quantum chemistry computation, which is a powerful tool to understand the chemical phenomena from first principles view, is widely used in academical studies and material design in industries.
It is known that the commonly used method, density functional theory (DFT), does not have enough accuracy for describing some systems such as strongly correlated electronic states and electronically excicted states. 
Whereas configuration interaction (CI) method, which in principal can be improved systematically towards the exact solution, is an alternative method to tackle these problems. 
However, since the computational cost increases exponentially with the molecular size and easily reaches the limitation on classical computers, the accurate CI calculation is only available for small molecular systems.

Quantum computers are expected to be a powerful tool for quantum chemistry computation because the computational cost can be suppressed into the polynomial scale.
Recent years, great improvements can be seen in the quantum computing algorithm for quantum chemistry. 
Quantum phase estimation algorithm (QPE) has been proposed to compute the eigenenergies of electronic states for fault tolerant quantum computers (FTQC), and variational eigenvalue solver (VQE) algorithm has been reported in recent years to utilize current noisy intermediate-scale quantum (NISQ) devices.

However, it is still far from the real usecase in academic studies and industrial development because of the lack of useful quantum algorithms to calculate molecular properties and the demonstration to show the advantages of quantum algorithms. 
In this challenge, the participants are expected to show a demonstration that is relevant to real usecase of quantum chemistry and has academical or industrial significance using quantum computing algorithms.

## Problem Description
- Your task is to make a quantum chemistry demonstration which has academical or industrial significance using quantum algorithms. 
- The participants can use proposed algorithms or build new algorithms for both NISQ and FTQC.
- The participants can use any quantum computing libraries (Qulacs, Qiskit, Cirq, Pennylane, Qamuy, etc).
- The participants are expected to submit a slide presentation that explains your idea, and a code that implements it. We will evaluate both the result of the code, and also your idea itself.

### The scope of your idea
- Demonstraion based on VQE. For example,
    - Photochemical simulation using [oscillator strength based on VQD (Variational Quantum Deflation)](https://arxiv.org/abs/2002.11724)
    - [Computation of periodic materials using VQE](https://arxiv.org/abs/2008.09492) 
    - Conical intersection optimization using [analytical energy gradient for state-averaged orbital-optimized VQE](https://arxiv.org/abs/2107.12705)
    - A divide-and-conquer method for solving a larger problem with smaller size quantum computers: [deep VQE](https://arxiv.org/abs/2007.10917)
    - Chemical reaction path search using [gradient and hessian computation algorithms](https://arxiv.org/abs/1905.04054)
    - Nonadiabatic dynamics calculation using [gradients and nonadiabatic couplings within state-averaged orbital-optimized VQE](https://arxiv.org/abs/2009.11417)
    
- Demonstraion based on the method beyond VQE. We highly evaluate if you come up with an algorithm beyond VQE.
    - You can use proposed algorithms or build new methods based on the algorithm beyond VQE to compute significant molecular properties.

### Evaluation criteria
- Originality
    - The idea will be highly evaluated if the idea has high originality.

- Academically / industrially significance
    - The idea is expected to have academic impact or relevance to industrial usecases.

- Scalability compared to classical algorithms
    - The idea is expected to have advantages over classical algorithms.
