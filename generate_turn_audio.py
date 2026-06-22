import os
from gtts import gTTS

# Path to audio/coop directory relative to this script
base_dir = os.path.abspath(os.path.dirname(__file__))
audio_dir = os.path.join(base_dir, 'audio', 'coop')
os.makedirs(audio_dir, exist_ok=True)

samples = [
    ("תור רועי", "numwar_turn_roy.mp3"),
    ("תור אבא", "numwar_turn_aba.mp3")
]

for text, filename in samples:
    out_path = os.path.join(audio_dir, filename)
    if not os.path.isfile(out_path):
        tts = gTTS(text=text, lang='he')
        tts.save(out_path)
        print(f'Generated {out_path}')
    else:
        print(f'Already exists: {out_path}')
