from collections import OrderedDict

A4=440
OCTAVE=["C", "C#/Db", "D", "Eb/D#", "E", "F", "F#/Gb", "G", "Ab/G#", "A", "Bb/A#", "B"]
assert len(OCTAVE) == 12

NOTES = OrderedDict()

for n in range(-2*12, 2*12): #C2 - B5
    offset, note_number = divmod(n, 12)
    note_in_octave = OCTAVE[note_number]
    which_octave = 4 + offset
    note = f"{note_in_octave}_{which_octave}"
    NOTES[note] = A4 * (2**((n-9) / 12))

NOTES_KEYS = list(NOTES.keys())

def _find_closest_note(frequency):
    distance = 10000
    for note, freq in NOTES.items():
        if abs(frequency - freq) < distance:
            distance = abs(frequency - freq)
            closest_note = note
    return closest_note
        
def _get_neighbours(note):
    idx = NOTES_KEYS.index(note)
    left_neighbour = NOTES_KEYS[idx - 1]
    right_neighbour = NOTES_KEYS[idx + 1]
    return left_neighbour, right_neighbour


def get_error_and_neighbours(frequency):
    note = _find_closest_note(frequency)
    proper_frequency = NOTES[note]
    left_neighbour, right_neighbour = _get_neighbours(note)
    error = frequency - proper_frequency
    result = {
        "left_neighbour": left_neighbour,
        "closest_note": note,
        "right_neighbour": right_neighbour,
        "error": error, 
    }
    return result
    
