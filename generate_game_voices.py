import os
from gtts import gTTS

AUDIO_DIR = r"c:\Users\Yairn\Desktop\roy-games\audio"
HABITAT_DIR = os.path.join(AUDIO_DIR, "habitat")
COOP_DIR = os.path.join(AUDIO_DIR, "coop")

os.makedirs(HABITAT_DIR, exist_ok=True)
os.makedirs(COOP_DIR, exist_ok=True)

# Habitat voices
HABITAT_VOICES = {
    "bee.mp3": "דְּבוֹרָה",
    "beehive.mp3": "כַּוֶּרֶת",
    "dog.mp3": "כֶּלֶב",
    "doghouse.mp3": "מְלוּנָה",
    "bird.mp3": "צִפּוֹר",
    "nest.mp3": "קֵן צִפּוֹר",
    "fish.mp3": "דָּג",
    "ocean.mp3": "יָם",
    "spider.mp3": "עַכָּבִישׁ",
    "spiderweb.mp3": "קוּרֵי עַכָּבִישׁ",
    "horse.mp3": "סוּס",
    "stable.mp3": "אֻרְוָה",
    "king.mp3": "מֶלֶךְ",
    "castle.mp3": "אַרְמוֹן",
    "frog.mp3": "צְפַרְדֵּעַ",
    "lilypad.mp3": "שׁוֹשַׁנַּת מַיִם",
    "bat.mp3": "עֲטַלֵּף",
    "cave.mp3": "מְעָרָה",
    "monkey.mp3": "קוֹף",
    "palmtree.mp3": "עֵץ דֶּקֶל",
}

# Coop/Tidyup/Tower voices
COOP_VOICES = {
    "tidy_instructions.mp3": "בּוֹאוּ נַעֲשֶׂה סֵדֶר בַּחֶדֶר! רוֹעִי מְסַדֵּר צַעֲצוּעִים וַחֲפָצִים, וְאַבָּא יָאִיר מְסַדֵּר פֵּרוֹת וְחַיּוֹת.",
    "towertalk_turn_roy.mp3": "תּוֹר רוֹעִי לָשִׂים קֻבִּיָּה.",
    "towertalk_turn_aba.mp3": "תּוֹר אַבָּא יָאִיר לָשִׂים קֻבִּיָּה."
}

print("Generating Habitat voices...")
for filename, text in HABITAT_VOICES.items():
    filepath = os.path.join(HABITAT_DIR, filename)
    print(f"Generating {filepath} -> '{text}'")
    gTTS(text=text, lang="iw", slow=False).save(filepath)

print("\nGenerating Coop/Tidyup/Tower voices...")
for filename, text in COOP_VOICES.items():
    filepath = os.path.join(COOP_DIR, filename)
    print(f"Generating {filepath} -> '{text}'")
    gTTS(text=text, lang="iw", slow=False).save(filepath)

print("\nDone generating audio files!")
