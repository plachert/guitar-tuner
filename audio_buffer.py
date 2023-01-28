import pyaudio
import numpy as np


class AudioBuffer:

    RATE = 8000
    CHUNK = int(RATE / 10)
    
    def __init__(self, chunks: int = 5) -> None:
        self.chunks = chunks
        self.stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK,
            )
    
    @property
    def audio(self):
        raw_data = self.stream.read(self.CHUNK)
        decoded = np.frombuffer(raw_data, np.int16)
        return decoded


if __name__ == "__main__":
    audio_buffer = AudioBuffer()
    print(audio_buffer.audio.shape)
