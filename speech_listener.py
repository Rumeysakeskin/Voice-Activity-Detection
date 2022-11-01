from vad_inferencer import VadInferencer
import pyaudio
import threading
import time
from time import monotonic
import math
from collections import deque

class VoiceListener:

    def __init__(self):

        self.listening_thread = None
        self.silent_time = None
        self.has_started_speaking = False
        self.has_finished_speaking = False

        # listener parameters
        self.CHUNK = 512
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 48000

        self.MAX_WAIT = 1.0
        self.vad_frame_queue = deque(maxlen=8)

        self.vad = VadInferencer()
        self.setup_audio_stream()


    def setup_audio_stream(self):
        p = pyaudio.PyAudio()

        self.stream = p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.RATE,
                             input=True,
                             frames_per_buffer=self.CHUNK)

    def start_listening(self):
        self.listening_thread = threading.Thread(target=self.listener, args=(), daemon=True)
        self.listening_thread.start()

    def listener(self):
        while True:
            data = self.stream.read(self.CHUNK, exception_on_overflow=False)
            self.vad_frame_queue.append(data)

    def vad_(self):

        if len(self.vad_frame_queue) >= 8:
            bytes = b''
            for frame in self.vad_frame_queue:
                bytes += frame
            self.vad_frame_queue.clear()
            if self.vad.has_speech_activity(audio_chunk=bytes):
                self.silent_time = None

                if not self.has_started_speaking:
                    self.has_started_speaking = True
                    print("Speech activity detected!")

            elif self.has_started_speaking:
                if self.silent_time is None:
                    self.silent_time = monotonic()
                elif monotonic() - self.silent_time > self.MAX_WAIT:
                    self.has_finished_speaking = True
                    print("Speech has ended!")

            if self.has_finished_speaking:
                self.has_finished_speaking = False
                self.has_started_speaking = False

if __name__ == '__main__':
    voice_listener = VoiceListener()
    print("waiting for speech...")
    voice_listener.start_listening()
    while True:
        voice_listener.vad_()

