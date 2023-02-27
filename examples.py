import numpy as np

from qiskit import QuantumCircuit, Aer, assemble
from numpy import pi

from qplayer import extract_music, player
from circuits import rotation_circuit, duration_gate, superpose_qutrit


def phase_music(iters, basis):
    """
    Implements quantum algorithm where phases are added to each qubit based on the basis.
    Iterates the algorithm to store various measures, and the plays them

    Args:
        iters (int): How many measures to make
        basis (float): Fraction of rotationts
    """
    svsim = Aer.get_backend("aer_simulator")

    measures = []

    for i in range(iters):
        phase = i * 2 * pi / basis
        qc = QuantumCircuit(7)
        rotations = rotation_circuit(
            7, [phase, phase / 2, phase / 3, phase / 4, phase / 5, phase / 6]
        )
        duration = duration_gate()

        qc = qc.compose(rotations).compose(duration, 6)

        qc.save_statevector()
        qobj = assemble(qc)
        result = svsim.run(qobj).result()
        hist = result.get_counts()

        notes, beats = extract_music(hist)

        measures.append([notes, beats])

    player(measures)


def entanglement_music(iters):
    svsim = Aer.get_backend("aer_simulator")

    measures = []

    for i in range(iters):
        qc = QuantumCircuit(7)
        duration = duration_gate()

        qc = qc.compose(duration, 6)
        time_circuit = superpose_qutrit(1, 0, 0)
        note_circuit = superpose_qutrit(1, 0, 0)

        qc = qc.compose(time_circuit, [0, 1, 2]).compose(note_circuit, [3, 4, 5])

        qc.save_statevector()
        qobj = assemble(qc)
        result = svsim.run(qobj).result()
        hist = result.get_counts()

        notes, beats = extract_music(hist)

        measures.append([notes, beats])

    player(measures)
