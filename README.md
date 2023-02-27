# Pentatoniq

An exploratory proyect for making music with quantum computers.

The idea for this proyect is to be a first approach to making music with quantum computers. Here we explore how phases can create sound, how entanglement might sound, and how randomness can create quantum music.

## How it works

The basis of the music are 8 notes that can be played over 8 beats.
8 qubits are used to encode the music.
This means that we have 256 superpositions available to encode music.

- first three qubits indicate the note played (2^3 = 8 --> 8 notes)
- next three qubits indicate the beat played (2^3 = 8 --> 8 beats)
- last qubit indicates duration (0 = 1 beat, 1 = 2 beats)
- amplitude indicates probability of playing the note

Based on these 4 basic principles, a wide variety of sounds can be generated, where some even sound like music.

## Files

## Examples

## Interesting ideas

As we explored the working, we found out that entanglement could be a way to play specific notes, as it limits the measurements to only a few possibilities.
