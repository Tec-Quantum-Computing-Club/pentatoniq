import numpy as np


# A collection of simple hamiltonians in their matrix representation
def XY_Ising_H(J):
    """
    A Hamiltonian for a ferromagnetic 3-qubit system: https://www.scielo.org.mx/pdf/cys/v23n2/1405-5546-cys-23-02-469.pdf
    Returns a np array

    Args:
        J (float): Coupling constant

    Returns:
        H (np.array[8x8]): The hamiltonian describing the system
    """
    return (J / 2) * np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
