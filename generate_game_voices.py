import os
from gtts import gTTS

AUDIO_DIR = r"c:\Users\Yairn\Desktop\roy-games\audio"
HABITAT_DIR = os.path.join(AUDIO_DIR, "habitat")
COOP_DIR = os.path.join(AUDIO_DIR, "coop")

os.makedirs(HABITAT_DIR, exist_ok=True)
os.makedirs(COOP_DIR, exist_ok=True)

# Habitat voices
HABITAT_VOICES = {
    "bee.mp3": "דבורה",
    "beehive.mp3": "כוורת",
    "dog.mp3": "כלב",
    "doghouse.mp3": "מלונה",
    "bird.mp3": "ציפור",
    "nest.mp3": "קן ציפור",
    "fish.mp3": "דג",
    "ocean.mp3": "ים",
    "spider.mp3": "עכביש",
    "spiderweb.mp3": "קורי עכביש",
    "horse.mp3": "סוס",
    "stable.mp3": "אורווה",
    "king.mp3": "מלך",
    "castle.mp3": "ארמון",
    "frog.mp3": "צפרדע",
    "lilypad.mp3": "שושנת מים",
    "bat.mp3": "עטלף",
    "cave.mp3": "מערה",
    "monkey.mp3": "קוף",
    "palmtree.mp3": "עץ דקל",
}

# Coop/Tidyup/Tower voices
COOP_VOICES = {
    "tidy_instructions.mp3": "בואו נעשה סדר בחדר! רועי מסדר צעצועים וחפצים, ואבא יאיר מסדר פירות וחיות.",
    "towertalk_turn_roy.mp3": "תור רועי לשים קובייה.",
    "towertalk_turn_aba.mp3": "תור אבא יאיר לשים קובייה."
}

print("Generating Habitat voices...")
for filename, text in HABITAT_VOICES.items():
    filepath = os.path.join(HABITAT_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Generating {filepath} -> '{text}'")
        gTTS(text=text, lang="iw", slow=False).save(filepath)
    else:
        print(f"Already exists: {filepath}")

print("\nGenerating Coop/Tidyup/Tower voices...")
for filename, text in COOP_VOICES.items():
    filepath = os.path.join(COOP_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Generating {filepath} -> '{text}'")
        gTTS(text=text, lang="iw", slow=False).save(filepath)
    else:
        print(f"Already exists: {filepath}")

print("\nDone generating audio files!")
