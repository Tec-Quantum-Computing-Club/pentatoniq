import numpy as np

from qiskit import QuantumCircuit, Aer, assemble, transpile
from numpy import pi

from qplayer import extract_music, player
from circuits import rotation_circuit, duration_gate, superpose_qutrit, spin_circuit


def phase_music(iters, basis, sound=1):
    """
    Implements quantum algorithm where phases are added to each qubit based on the basis.
    Iterates the algorithm to store various measures, and the plays them

    Args:
        iters (int): How many measures to make
        basis (float): Fraction of rotationts
        sound (int): 1, 2, or 3 for sound choice
    """
    svsim = Aer.get_backend("aer_simulator")

    measures = []

    for i in range(iters):
        phase = i * 2 * pi / basis
        qc = QuantumCircuit(7)
        rotations = rotation_circuit(
            7, [phase / 1, phase / 1, phase / 1, phase / 1, phase / 1, phase / 1]
        )
        duration = duration_gate()

        qc = qc.compose(rotations).compose(duration, 6)

        qc.save_statevector()
        qobj = assemble(qc)
        result = svsim.run(qobj).result()
        hist = result.get_counts()

        notes, beats = extract_music(hist)

        measures.append([notes, beats])

    player(measures, sound)


def entanglement_music_1(iters, sound=1):
    """
    Implements quantum algorithm that generates a GHZ state

    Args:
        iters (int): How many measures to make
        sound (int): 1, 2, or 3 for sound choice
    """
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

    player(measures, sound)


def entanglement_music_2(iters, sound=1):
    """
    Implements quantum algorithm that generates a GHZ state

    Args:
        iters (int): How many measures to make
        sound (int): 1, 2, or 3 for sound choice
    """
    svsim = Aer.get_backend("aer_simulator")

    measures = []

    for i in range(iters):
        qc = QuantumCircuit(7)
        duration = duration_gate()

        qc = qc.compose(duration, 6)
        time_circuit = superpose_qutrit(0, 1, 0)
        note_circuit = superpose_qutrit(0, 1, 0)

        qc = qc.compose(time_circuit, [0, 1, 2]).compose(note_circuit, [3, 4, 5])

        qc.save_statevector()
        qobj = assemble(qc)
        result = svsim.run(qobj).result()
        hist = result.get_counts()

        notes, beats = extract_music(hist)

        measures.append([notes, beats])

    player(measures, sound)


def entanglement_music_3(iters, sound=1):
    """
    Implements quantum algorithm that generates a GHZ state

    Args:
        iters (int): How many measures to make
        sound (int): 1, 2, or 3 for sound choice
    """
    svsim = Aer.get_backend("aer_simulator")

    measures = []

    for i in range(iters):
        qc = QuantumCircuit(7)
        duration = duration_gate()

        qc = qc.compose(duration, 6)
        time_circuit = superpose_qutrit(0, 0, 1)
        note_circuit = superpose_qutrit(0, 0, 1)

        qc = qc.compose(time_circuit, [0, 1, 2]).compose(note_circuit, [3, 4, 5])

        qc.save_statevector()
        qobj = assemble(qc)
        result = svsim.run(qobj).result()
        hist = result.get_counts()

        notes, beats = extract_music(hist)

        measures.append([notes, beats])

    player(measures, sound)


def spin_temporal(time, sound=1):
    svsim = Aer.get_backend("aer_simulator")

    measures = []

    for t in range(time):
        qc = QuantumCircuit(7)
        note_gate = spin_circuit(t)
        time_gate = superpose_qutrit(0, 1, 0)

        qc.append(note_gate, [0, 1, 2])
        qc.compose(time_gate, [3, 4, 5])
        qc.measure_all()

        t_qc = transpile(qc, svsim)
        qobj = assemble(t_qc, shots=1)
        result = svsim.run(qobj, memory=True).result()
        hist = result.get_counts()

        notes, beats = extract_music(hist)

        measures.append([notes, beats])

    player(measures, sound)
