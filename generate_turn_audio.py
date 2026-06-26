import os
from gtts import gTTS

# Path to audio/coop directory relative to this script
base_dir = os.path.abspath(os.path.dirname(__file__))
audio_dir = os.path.join(base_dir, 'audio', 'coop')
os.makedirs(audio_dir, exist_ok=True)

samples = [
    ("תּוֹר רוֹעִי", "numwar_turn_roy.mp3"),
    ("תּוֹר אַבָּא", "numwar_turn_aba.mp3")
]

for text, filename in samples:
    out_path = os.path.join(audio_dir, filename)
    tts = gTTS(text=text, lang='iw')
    tts.save(out_path)
    print(f'Generated {out_path}')
