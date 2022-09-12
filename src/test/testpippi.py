
#TODO install pippi
from pippi import dsp, soundfont

# Play a piano sound from a soundfont with general MIDI support (program change is zero-indexed)
tada = soundfont.play('my-cool-soundfont.sf2', length=30, freq=345.9, amp=0.5, voice=0)

# Save copy to your hard disk
tada.write('tada.wav')