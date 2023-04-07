import matplotlib.pyplot as plt

def plot_density_matrix(rho):
    fig, ax = plt.subplots()
    im = ax.imshow(np.abs(rho.full()), cmap="viridis", interpolation="nearest")
    plt.colorbar(im)
    ax.set_title("Density Matrix Magnitudes")
    plt.show()

def plot_eigenvalues(rho):
    eigenvalues = rho.eigenenergies()
    plt.stem(range(len(eigenvalues)), eigenvalues, basefmt=" ")
    plt.xlabel("Eigenvalue index")
    plt.ylabel("Eigenvalue")
    plt.title("Eigenvalues of the Density Matrix")
    plt.show()

def plot_purity_and_fidelity(time_points, purities, fidelities):
    """Plot the time evolution of purity and fidelity."""
    fig, ax1 = plt.subplots()

    color = "tab:red"
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Purity", color=color)
    ax1.plot(time_points, purities, color=color)
    ax1.tick_params(axis="y", labelcolor=color)

    ax2 = ax1.twinx()
    color = "tab:blue"
    ax2.set_ylabel("Fidelity", color=color)
    ax2.plot(time_points, fidelities, color=color)
    ax2.tick_params(axis="y", labelcolor=color)

    fig.tight_layout()
    plt.title("Time Evolution of Purity and Fidelity")
    plt.show()