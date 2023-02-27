from qiskit import QuantumCircuit, Aer, assemble
from numpy import pi
from random import random


def rotation_circuit(n, thetas):
    """
    Creates a circuit with rotated qubits (Cx)

    Args:
      n (int): Numbers of qubits
      thetas (list(ints)): Array of rotation angles

    Returns:
      QuantumCircuit
    """

    qc = QuantumCircuit(n)

    for i in range(n - 1):
        qc.rx(thetas[i], i)

    qc.barrier()

    return qc


def duration_gate():
    """
    Randomly rotates a qubit
    Args:
    """
    qc = QuantumCircuit(1)
    theta = random() * 2 * pi
    qc.rx(theta, 0)
    qc.barrier()

    return qc


def superpose_qutrit(i, j, k):
    """
    Args:
      i (int): Classical bit, 0 or 1
      j (int): Classical bit, 0 or 1
      k (int): Classical bit, 0 or 1

    Returns:
      QuantumCircuit: Circuit after applying H gates and CNOTs
    """
    qc = QuantumCircuit(3)

    if i == 1:
        qc.h(0)
    if j == 1:
        qc.h(1)
    if k == 1:
        qc.h(2)

    qc.cx(0, 1)
    qc.cx(0, 2)

    return qc
