from pygame import mixer
import pygame
from time import sleep, gmtime, strftime
import numpy as np
from os import listdir, mkdir
from pathlib import Path

pygame.init()

# Constants
NOTES = [mixer.Sound("./audio/synth1/" + ii) for ii in listdir("./audio/synth1")]

NOTES2 = [mixer.Sound("./audio/synth2/" + ii) for ii in listdir("./audio/synth2")]

NOTES3 = [mixer.Sound("./audio/synth3/" + ii) for ii in listdir("./audio/synth3")]

BPM = 160
BPS = BPM / 60
BEATS = 8
TIME_INTERVAL = 1 / BPS


out_data = []


def player(measures, sound=1):
    """
    Receives a list of melody-time pairs generated by extract_music(hist).
    A choice of 3 sounds can be given with an int

    Args:
        measures (list[list[int]]): List containing melody-time pairs
        sound (int): 1, 2, or 3 for sound choice
    """
    # Choose sound
    note_choice = []
    if sound == 1:
        note_choice = NOTES
    elif sound == 2:
        note_choice = NOTES2
    else:
        note_choice = NOTES3

    # loops all measures and extracts the meldoy and beats
    for melody, beats in measures:
        # plays melody
        for i in range(BEATS):
            # i is current beat
            mask = beats == i

            # filter for notes on current beat
            current_notes = melody[mask]

            # Loop notes and play them
            for n in current_notes:
                note_choice[n].play()

                out_data.append([i, sound, n])

            sleep(TIME_INTERVAL / 2)  # sleep time

    file_path = (
        "./saved_songs/pentatoniq-" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ".txt"
    )
    Path("./saved_songs").mkdir(parents=True, exist_ok=True)
    np.savetxt(file_path, out_data)


def extract_music(hist):
    """
    Receives a quantum circuit histogram (Qiskit) and returns the melody and time information

    Args:
      hist (dict[str, int]): Historam with circuit measurement

    Returns:
      list[int], [int]
    """
    # Extract keys and vals
    keys = np.array(list(hist.keys()))
    amplitudes = np.array(list(hist.values()))

    # Filter data
    thresh = 1 / (2 * len(keys))
    mask = amplitudes > thresh

    # Filter with boolean mask
    keys = keys[mask]
    amplitudes = amplitudes[mask]

    # select sequences to play
    counts = len(keys)

    # For storing
    melody_index = []
    time_index = []

    for i in range(counts):
        # Correct order
        qubits = keys[i][::-1]

        # First three are note in binary
        note = int(qubits[0:3], 2)

        # 4, 5, 6 are beat in binary
        beat = int(qubits[3:6], 2)

        # Append
        melody_index.append(note)
        time_index.append(beat)

    # To np array
    melody_index = np.array(melody_index)
    time_index = np.array(time_index)

    return melody_index, time_index
