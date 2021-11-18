"""One note piano keyboard."""

import pgzrun

BLACK_KEY_WIDTH = 16
"""Integer width in pixels of the black keys."""

WHITE_KEY_WIDTH = 20
"""Integer width in pixels of the white keys."""

DURATION = 0.1
"""Float duration in seconds to play each note."""

NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
"""List of string notes from the lowest to the highest."""

OCTAVE_COUNT = 9
"""Integer number of octaves on the piano."""

WIDTH = WHITE_KEY_WIDTH * len(NOTES) * OCTAVE_COUNT
HEIGHT = 100
TITLE = 'piano'

BLACK_KEY_HEIGHT = HEIGHT // 2
"""Integer height in pixels of the black keys."""

blackKeys = []
whiteKeys = []
for octave in range(OCTAVE_COUNT):
    for j, note in enumerate(NOTES):
        key = ZRect(((octave * len(NOTES)) + j) * WHITE_KEY_WIDTH, 0,
                    WHITE_KEY_WIDTH, HEIGHT)
        key.note = note + str(octave)
        whiteKeys.append(key)

        if note in 'CDFGA':
            key = ZRect((((octave * len(NOTES)) + j + 1) * WHITE_KEY_WIDTH) -
                        (BLACK_KEY_WIDTH // 2), 0,
                        BLACK_KEY_WIDTH, BLACK_KEY_HEIGHT)
            key.note = note + '#' + str(octave)
            blackKeys.append(key)

def draw():
    for k in whiteKeys:
        screen.draw.filled_rect(k, 'white')
        screen.draw.rect(k, 'black')
    # Draw black keys on top of the white keys
    for k in blackKeys:
        screen.draw.filled_rect(k, 'black')

def on_mouse_down(pos):
    # Detect clicking on a black key before a white key
    # because black keys are on top
    for pianoKeys in [blackKeys, whiteKeys]:
        for k in pianoKeys:
            if k.collidepoint(pos):
                tone.play(k.note, DURATION)
                return

pgzrun.go()
