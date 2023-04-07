from setuptools import setup, find_packages

setup(
    name="quantum_density_matrix",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "qutip",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "quantum-density-matrix=qdm.cli:main",
        ],
    },
)
