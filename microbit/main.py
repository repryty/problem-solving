from microbit import *
import music

display.clear()
buzzer=pin1
def play(tone):
    music.pitch(tone, -1, buzzer)
    sleep(500)
    music.pitch(0, -1, buzzer)
    sleep(100)

while True:
    for i in range(2):
        play(262)
        play(330)
        play(392)

    for i in range(3):
        play(440)
    play(392)

    