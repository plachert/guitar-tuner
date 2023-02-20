import numpy as np
from audio_buffer import AudioBuffer
from pitch_notation import get_error_and_neighbours
import signal_processing as sp


class GuitarTuner:
    def __init__(self, audio_buffer: AudioBuffer) -> None:
        self.buffer = audio_buffer
        self.sr = self.buffer.RATE
        
    def run(self):
        while True:
            data = self.buffer()
            fundamental = sp.get_fundamental(data, sr=self.sr)
            result = get_error_and_neighbours(fundamental)
            print(fundamental)
            
if __name__ == "__main__":
    audio_buffer = AudioBuffer()
    audio_buffer.start()
    tuner = GuitarTuner(audio_buffer=audio_buffer)
    tuner.run()
