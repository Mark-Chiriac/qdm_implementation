from qutip import fidelity, Qobj
import json
import numpy as np

def validate_num_qubits(num_qubits):
    if num_qubits <= 0:
        raise ValueError("Number of qubits must be a positive integer.")

def validate_couplings(couplings, num_qubits):
    if len(couplings) != num_qubits:
        raise ValueError("The number of couplings must be equal to the number of qubits.")
def format_complex_number(z):
    return f"{z.real:.4f} {'+' if z.imag >= 0 else '-'} {abs(z.imag):.4f}i"

def format_matrix(matrix):
    rows = [" ".join(format_complex_number(z) for z in row) for row in matrix]
    return "\n".join(rows)

def calculate_state_fidelity(rho1, rho2):
    """Calculate the fidelity between two density matrices."""
    return fidelity(rho1, rho2)

def calculate_purity(rho):
    """Calculate the purity of a density matrix."""
    return (rho * rho).tr()

def save_density_matrix_to_file(rho, filename):
    """Save the density matrix to a file in JSON format."""
    data = {
        "dims": rho.dims,
        "data": [[z.real, z.imag] for z in rho.full().flatten()]
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_density_matrix_from_file(filename):
    """Load a density matrix from a file in JSON format."""
    with open(filename, "r") as f:
        data = json.load(f)
    rho_data = [complex(z[0], z[1]) for z in data["data"]]
    rho = Qobj(np.array(rho_data).reshape(data["dims"][0]), dims=data["dims"])
    return rho


