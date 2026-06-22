"""Generate Hebrew female-voice MP3s for Roy's Games using gTTS."""
import os
from gtts import gTTS

AUDIO_DIR = r"c:\Users\Yairn\Desktop\roy-games\audio"
SHARING_DIR = os.path.join(AUDIO_DIR, "sharing")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(SHARING_DIR, exist_ok=True)

# 1. Base Welcome and Success files
VOICES = {
    # Intro
    "intro-boy.mp3": "שלום רועי! ברוך הבא למרכז המשחקים שלך. במה נרצה לשחק היום?",
    
    # Boy success
    "b-reg1.mp3": "כל הכבוד רועי!",
    "b-kap1.mp3": "כל הכבוד חביבי!",
    "b-kap2.mp3": "אתה פשוט אלוף!",
    "b-life1.mp3": "איזה יופי, סיימת את כל השלבים!",
    "b-life2.mp3": "כל הכבוד רועי, אתה מדהים!",
    
    # Girl success
    "g-reg1.mp3": "כל הכבוד!",
    "g-kap1.mp3": "כל הכבוד חביבה!",
    "g-kap2.mp3": "את אלופה!",
    "g-life1.mp3": "איזה יופי, סיימת את כל השלבים!",
    "g-life2.mp3": "כל הכבוד, את מדהימה!",
    
    # Shared success
    "shared-reg2.mp3": "יופי של עבודה!",
    "shared-reg3.mp3": "מצוין!"
}

# 2. Sharing Game files
SHARING_VOICES = {
    "q1.mp3": "אורי ונועם רוצים לשחק עם המשאית האדומה, אבל יש רק אחת. מה יעשה אורי?",
    "fb1.mp3": "כל הכבוד! אורי משחק במשאית יחד עם נועם, ושניהם נהנים!",
    
    "q2.mp3": "אורי משחק בטאבלט. נועם רוצה גם לשחק. מה יעשה אורי?",
    "fb2.mp3": "כל הכבוד! אורי מציע לנועם לעשות תורות בטאבלט, ושניהם נהנים!",
    
    "q3.mp3": "נשארה עוגייה אחת. גם אורי וגם נועם רוצים אותה. מה יעשה אורי?",
    "fb3.mp3": "כל הכבוד! אורי חוצה את העוגייה לשניים וחולק אותה עם נועם!",
    
    "q4.mp3": "אורי רוצה לרדת בגלשן, אבל ילדים אחרים מחכים בתור. מה יעשה אורי?",
    "fb4.mp3": "כל הכבוד! אורי מחכה בסבלנות בתור שלו לגלשן!",
    
    "q5.mp3": "אורי ונועם רוצים לבנות מגדל, אבל יש רק קופסת קוביות אחת. מה יעשה אורי?",
    "fb5.mp3": "כל הכבוד! אורי משחק בקוביות יחד עם נועם, ושניהם בונים מגדל גדול יחד!",
    
    "q6.mp3": "אורי ונועם רוצים לצייר, אבל יש קופסה אחת עם צבעים. מה יעשה אורי?",
    "fb6.mp3": "כל הכבוד! אורי מחלק את הצבעים עם נועם, ושניהם מציירים יחד!",
    
    "q7.mp3": "אורי מחזיק כדור. נועם רוצה לשחק יחד. מה יעשה אורי?",
    "fb7.mp3": "נכון מאוד! אורי מוסר את הכדור לנועם. כל אחד מקבל תור!",
    
    "q8.mp3": "לאורי יש מכונית, לנועם יש כדור. נועם רוצה לנסות את המכונית. מה יעשה אורי?",
    "fb8.mp3": "מצוין! אורי ונועם מחליפים צעצועים לזמן קצר. שניהם מנסים משהו חדש!",
    
    "q9.mp3": "אמא קוראת סיפור לאורי. נועם גם רוצה לשמוע. מה יעשה אורי?",
    "fb9.mp3": "יופי! אורי מפנה מקום לנועם ליד אמא. כולם נהנים מהסיפור יחד!",
    
    "q10.mp3": "יש שטיח אחד בחדר. אורי יושב עליו. נועם גם רוצה לשבת. מה יעשה אורי?",
    "fb10.mp3": "מעולה! אורי משאיר מקום על השטיח לנועם, ושניהם יושבים יחד!"
}

print("Starting audio generation...")

# Generate general voices
for filename, text in VOICES.items():
    filepath = os.path.join(AUDIO_DIR, filename)
    print(f"Generating {filename} -> '{text}'")
    gTTS(text=text, lang="iw", slow=False).save(filepath)

# Generate sharing game voices
for filename, text in SHARING_VOICES.items():
    filepath = os.path.join(SHARING_DIR, filename)
    print(f"Generating sharing/{filename} -> '{text}'")
    gTTS(text=text, lang="iw", slow=False).save(filepath)

print("\nDone! All voice files generated in female Hebrew voice.")
