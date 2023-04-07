import numpy as np
from qutip import basis, tensor, sigmax, identity, Qobj, sesolve

def create_density_matrix(num_qubits):
    psi0 = tensor([basis(2, 0) for _ in range(num_qubits)])
    return psi0

def create_hamiltonian(num_qubits, couplings):
    H = sum(couplings[i] * tensor([sigmax() if j == i else identity(2) for j in range(num_qubits)]) for i in range(num_qubits))
    return H

def lindblad_rhs(t, psi_vec, H, num_qubits):
    psi = Qobj(psi_vec.reshape((2 ** num_qubits, 1)), dims=[[2] * num_qubits, [1]])
    rho = psi * psi.dag()
    rhs = -1j * (H * rho - rho * H).data
    return rhs.full().flatten()

def evolve_density_matrix(rho, H, time, num_qubits):
    psi0 = Qobj(rho.full(), dims=[rho.dims, [1] * 2 * num_qubits])
    psi0_vec = psi0.full().ravel()
    result = sesolve(lindblad_rhs, psi0_vec, [0, time], [], args=(H, num_qubits))
    rho_evolved = Qobj(result.states[-1].reshape((2 ** num_qubits, 2 ** num_qubits)))

    return rho_evolved
