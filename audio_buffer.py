import pyaudio
import numpy as np
from collections import deque
import threading
from time import sleep


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
        self.thread = threading.Thread(target=self._collect_data, daemon=True)
        self.frames = deque(maxlen=self.chunks)
    
    @property
    def audio(self):
        return np.concatenate(self.frames)
    
    def start(self):
        self.thread.start()
        
    def _collect_data(self):
        while True:
            raw_data = self.stream.read(self.CHUNK)
            decoded = np.frombuffer(raw_data, np.int16)
            self.frames.append(decoded)


if __name__ == "__main__":
    audio_buffer = AudioBuffer()
    audio_buffer.start()
    sleep(0.5) # wait until the buffer is not empty
    print(audio_buffer.audio.shape)
