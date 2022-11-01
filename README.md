# Real-Time Voice Activity Detector

This repository designed for real-time streaming using only the prediction of the silero-vad model.

#### Model Description
[Silero VAD](https://github.com/snakers4/silero-vad) is pre-trained enterprise-grade Voice Activity Detector.

Note that this model is intended to run on CPU only and was optimized for performance on 1 CPU thread and the model is quantized.

- #### High Quality
Silero VAD has [excellent performance](https://github.com/snakers4/silero-vad/wiki/Quality-Metrics#vs-other-available-solutions) on speech detection tasks compared to other algorithms (WebRTC, Picovoice, SpeechBrain).


- #### Fast
One audio chunk (30+ ms) [takes](https://github.com/snakers4/silero-vad/wiki/Performance-Metrics#silero-vad-performance-metrics) less than 1ms to be processed on a single CPU thread.
Under certain conditions ONNX may even run up to 4-5x faster.

- #### Modern
Silero VAD was trained on huge corpora that include over 100 languages and it performs well on audios from different domains with various background noise and quality levels.

- #### Public
Published under permissive license (MIT) Silero VAD has zero strings attached - no telemetry, no keys, no registration, no built-in expiration, no keys or vendor lock.


