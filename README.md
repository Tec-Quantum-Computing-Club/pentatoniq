![pentatoniq logo](/media/logo2.png)

# Pentatoniq

Produce sound through entanglement and rotations. Listen to your quantum circuit's thoughts.

An exploratory proyect for making music with quantum computers.

The idea for this proyect is to be a first approach to making music with quantum computers. Here we explore how phases can create sound, how entanglement might sound, and how hamiltonians can create quantum music.

Inspiration: `Quantum Art`

## How it works

The basis of the music are 8 notes that can be played over 8 beats.
8 qubits are used to encode the music.
This means that we have 256 superpositions available to encode music.

- first three qubits indicate the note played (2^3 = 8 --> 8 notes)
- next three qubits indicate the beat played (2^3 = 8 --> 8 beats)
- last qubit indicates duration (0 = 1 beat, 1 = 2 beats)
- amplitude indicates probability of playing the note (threshold function will dictate if note is played at its corresponding time)

Based on these 4 basic principles, a wide variety of sounds can be generated, where some even sound like music.

### Example

|0101001> with 0.15 of amplitude

- 010 = 3rd note
- 100 = 5th beat
- 1 = duration of 2 beats
- Depending on threshold function, note might be played

## Features

This project includes:

1. Music extraction, which takes a histogram generated by a Qiskit `QuantumCircuit` and returns an array with a pair - [melody, beats]
2. Music player, which takes an array of [melody, beats] pair and plays them
3. Custom sounds
4. A couple of circuits which can generate interesting sounds
5. A function which takes a hamiltonian and returns a circuit using said hamiltonian

These features can get you started to making your own Quantum Music!

Checkout our examples [here!](/pentatoniq.ipynb)

## Files

On the [pentanoiq](/pentatoniq.ipynb) JupyterNotebook, there are ready examples for you to test out!

The [audio](/audio/) folder has the necessary files for base sounds, feel free to add more!

Our [circuits](/circuits.py) file has our basic buidling blocks for our circuits, but are really just generators of quantum circuits. It contains the hamiltonian function (generates a circuit which applies a hamiltonian to some qubits).

The [examples](/examples.py) has the examples used in the `pentatoniq.ipynb`.

Our [player](/qplayer.py) has our decoding functions for any histogram generated by a Qiskit quantum circuit, this file plays the sounds.

Audio files are included in the [audio](/audio/) folder. You'll find different synth-sounds (self made samples) and the percussion sounds (sampled from an 808-drum machine), but you cand include your own. Try using a different mode or scale!

## Examples

On the [pentanoiq](/pentatoniq.ipynb) JupyterNotebook, there are ready examples for you to test out! Otherwise, check out this youtube demo:

[![IMAGE_ALT](/media/screen1.png)](https://www.youtube.com/watch?v=byJk92w3AgY)

## Interesting ideas

### Entanglement's role in quantum music

As we explored this funny idea, we found out that entanglement could be a way to play specific notes, as it limits the measurements to only a few possibilities. An idea that would be interesting to further explore, is how to exploit entanglement to generate music purposely.

### Natural hamiltonian sounds

Could we somehow encode hamiltonians from nature (harmonic oscillators, electric potentials, etc.) and try to make music with them? How would "quantum natural" music sound?

### Machine learning mixing

We could probably leverage machine learning techniques to create really interesting sounds.

There could also be research on how machine learning can find quantum algorithms which generate music that is enjoyable for humans.

## Next steps

Future features aim to include a melody encoder and decoder.

Try to make "quantum natural" music.

Resarch on how entanglement can create sound.
