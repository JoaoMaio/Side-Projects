from mido import Message, MetaMessage, MidiFile, MidiTrack

# Create a new MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set tempo (78 bpm)
# Add tempo as a MetaMessage
track.append(MetaMessage('set_tempo', tempo=int(60_000_000 / 78)))

# Define scale notes for D major (or B minor)
scale_notes = [62, 64, 66, 67, 69, 71, 73, 74]  # D, E, F#, G, A, B, C#, D

# Define chord roots for the progression (mapped to MIDI notes for D major scale)
# Chords: 3 (F# minor), 1 (D major), 6 (B minor), 4 (G major)
chord_progression = [
    [66, 69, 73],  # F# minor
    [62, 66, 69],  # D major
    [71, 74, 78],  # B minor
    [67, 71, 74]   # G major
]

# Add chords to the track
# Adjust chord progression indices to match zero-based list index
for chord in [chord_progression[i - 1] for i in [3, 1, 6, 4, 4, 4, 4, 1] if 1 <= i <= 4]:
    for note in chord:
        track.append(Message('note_on', note=note, velocity=60, time=0))
    track.append(Message('note_off', note=chord[0], velocity=60, time=480))  # Hold chord for one beat
    for note in chord[1:]:
        track.append(Message('note_off', note=note, velocity=60, time=0))

# Add melodies to the track
melody_pattern = [
    [5, 0, 0, 0, 0, 8, 0, 8],
    [0, 8, 8, 8, 8, 8, 8, 8],
    [8, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 8, 8, 8, 8, 8, 8]
  ]

# Convert each melody note to its MIDI equivalent, or rest if it's '0'
for melody in melody_pattern:
    for step in melody:
        if step != 0:
            note = scale_notes[step - 1]  # Map step to note in D major scale
            track.append(Message('note_on', note=note, velocity=50, time=240))
            track.append(Message('note_off', note=note, velocity=50, time=240))
        else:
            # Rest for this beat
            track.append(Message('note_off', note=0, velocity=0, time=240))

# Save to MIDI file
mid.save('output_music.mid')
