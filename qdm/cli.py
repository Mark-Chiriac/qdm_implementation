import click
from qdm.simulator import create_density_matrix, create_hamiltonian, evolve_density_matrix

@click.group()
def cli():
    pass

@cli.command()
@click.option('--num-qubits', type=int, default=2, help='Number of qubits')
def density_matrix(num_qubits):
    rho = create_density_matrix(num_qubits)
    click.echo(rho)

@cli.command()
@click.option('--num-qubits', type=int, default=2, help='Number of qubits')
@click.option('--couplings', type=float, multiple=True, help='Couplings')
def hamiltonian(num_qubits, couplings):
    H = create_hamiltonian(num_qubits, couplings)
    click.echo(H)

@cli.command()
@click.option('--num-qubits', type=int, default=2, help='Number of qubits')
@click.option('--couplings', type=float, multiple=True, help='Couplings')
@click.option('--time', type=float, default=1.0, help='Evolution time')
def evolution(num_qubits, couplings, time):
    rho = create_density_matrix(num_qubits)
    H = create_hamiltonian(num_qubits, couplings)
    rho_evolved = evolve_density_matrix(rho, H, time, num_qubits)
    click.echo(rho_evolved)
