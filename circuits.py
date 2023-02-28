from qiskit import QuantumCircuit
from qiskit.extensions import UnitaryGate, HamiltonianGate
from qiskit.quantum_info import Pauli
from numpy import pi
from random import random
from hamiltonians import XY_Ising_H as ising


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

    return qc


def duration_gate():
    """
    Randomly rotates a qubit
    Args:
    """
    qc = QuantumCircuit(1)
    theta = random() * 2 * pi
    qc.rx(theta, 0)

    return qc


def superpose_qutrit(i, j, k):
    """
    A circuit that applies H gate to bits i j k when set to 1.
    Additionally, CNOTs are applied between 0-1 and 0-2.
    This implementation can create entangled qutrits.

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


def hamiltonian_circuit(n, t, hamiltonian, label, qubits):
    """
    Circuit that couples a hamiltonian to a quantum circuit only to the desired qubits

    Args:
      n (int): amount of qubits
      t (int): time to insert to the hamiltonian
      label (string): label for the hamiltonian gate
      qubits (list[int]): array of qubits where hamiltonian gate will be placed

    Returns:
      QuantumCircuit
    """
    qc = QuantumCircuit(n)
    H = UnitaryGate(H)
    H = HamiltonianGate(H, t, label)
    qc = qc.append(hamiltonian, qubits)

    return qc


def ising_xy_temporal(J, t):
    H = ising(J)
    H = UnitaryGate(H)
    return HamiltonianGate(H, t, "ising")


def spin_circuit(t):
    H = Pauli(([True, True, True], [True, True, True]))
    H = UnitaryGate(H)
    return HamiltonianGate(H, t, "spin")
