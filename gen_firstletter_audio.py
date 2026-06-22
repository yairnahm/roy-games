"""Generate Hebrew female-voice MP3s for the firstletter game using gTTS (Google TTS)."""
import os
from gtts import gTTS

OUT = r"C:\Users\Yairn\Desktop\roy-games\audio\firstletter\he"
os.makedirs(OUT, exist_ok=True)

# Each entry: img-name, full word (for reading aloud), sound (letter + vowel sound)
WORDS = [
    ("dog",      "כֶּלֶב",     "כַ"),
    ("apple",    "תַּפּוּחַ",   "תַ"),
    ("house",    "בַּיִת",     "בַ"),
    ("horse",    "סוּס",       "סַ"),
    ("bird",     "צִפּוֹר",    "צַ"),
    ("fish",     "דָּג",       "דַ"),
    ("elephant", "פִּיל",      "פַ"),
    ("sun",      "שֶׁמֶשׁ",    "שַׁ"),
    ("heart",    "לֵב",        "לַ"),
    ("car",      "מְכוֹנִית",  "מַ"),
    ("snake",    "נָחָשׁ",     "נַ"),
    ("train",    "רַכֶּבֶת",   "רַ"),
    ("carrot",   "גֶּזֶר",     "גַ"),
    ("flower",   "פֶּרַח",     "פַ"),
    ("star",     "כּוֹכָב",    "כַ"),
    ("banana",   "בָּנָנָה",   "בַ"),
    ("ball",     "כַּדּוּר",   "כַ"),
    ("cat",      "חָתוּל",     "חַ"),
    ("door",     "דֶּלֶת",     "דַ"),
    ("computer", "מַחְשֵׁב",   "מַ"),
    ("clock",    "שָׁעוֹן",    "שַׁ"),
    ("phone",    "טֶלֶפוֹן",   "טַ"),
]

for img, word, sound in WORDS:
    word_file  = os.path.join(OUT, f"word-{img}.mp3")
    sound_file = os.path.join(OUT, f"sound-{img}.mp3")

    if not os.path.exists(word_file):
        print(f"Generating word: {img}")
        gTTS(text=word, lang="iw", slow=True).save(word_file)
    else:
        print(f"  skip: word-{img}.mp3")

    if not os.path.exists(sound_file):
        print(f"Generating sound: {img}")
        gTTS(text=sound, lang="iw", slow=False).save(sound_file)
    else:
        print(f"  skip: sound-{img}.mp3")

print("\nDone! All files in:", OUT)
