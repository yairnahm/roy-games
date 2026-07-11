# תיקון קבוע: קריינות נשית בלבד — לעולם לא קול גבר

**תאריך:** 2026-07-10
**דרישה מקורית של יאיר:** "כל פעם שמשדרגים הקול של הקריין הופך במשחק זה או אחר לקול של גבר. תקן את התקלה הזאת אחת ולתמיד. אל תאפשר לתיקונים עתידיים לשנות את קול הקריינות מאישה לגבר."

## שורש הבעיה

כל שדרוג שהוסיף משחק חדש יצר הפניות לקבצי mp3 **בלי לייצר אותם בפועל** בפייפליין ה-gTTS.
כשקובץ שמע חסר, הקוד נופל לקריין המובנה של הדפדפן (`speechSynthesis`) — ובווינדוס (ובחלק
מהטאבלטים) הקול העברי היחיד המובנה הוא **Asaf, קול גברי**. בנוסף, פונקציית בחירת הקול הייתה
מוכנה להחזיר קול גברי אם לא נמצא קול נשי מתאים, וסקריפט בדיקת השלמות של קבצי השמע החמיץ
חוסרים אמיתיים בגלל באג התאמת שמות-קבצים.

## מה תוקן

### 1. `roy-games` (הפרויקט החי, https://yairnahm.github.io/roy-games/)
קומיט `3654a39` (v45), נדחף ל-`origin/master`.

- **`index.html`** — `pickFemaleVoice()` מחזירה `null` (במקום קול גברי) כשאין קול נשי
  בשפה המבוקשת; `useNativeSpeechSynthesis()` מדלגת על הדיבור בשקט אם לא נמצא קול מאומת —
  לעולם לא תדבר בקול גבר, גם לא כ-fallback.
- **`gen_fix_audio.py`** — נוספו טקסטי משחק "feelwhen" שהיו חסרים, ארגומנט `filter`
  אופציונלי (ייצור תת-קבוצה בלבד), ויצירת תיקיות audio חסרות אוטומטית.
- **`.git/hooks/pre-commit`** (חדש) — מריץ את `check_audio.py` וחוסם כל קומיט עתידי
  שמכיל הפניה לקובץ mp3 חסר. חובה: כל mp3 חדש ב-`index.html` מחייב ערך תואם
  ב-`gen_fix_audio.py` + הרצה שלו, אחרת הקומיט נחסם.
- **`check_audio.py`** (בסקיל, לא בריפו) — תוקן באג שגרם לחוסרים אמיתיים (למשל
  `feelwhen/q1.mp3`) להיחשב בטעות "קיימים" בגלל קובץ באותו שם בתיקייה אחרת.

### 2. `RoiGame` (הפרויקט השני, js/audio.js)
נבדק ואומת: המנוע החי משתמש רק ב-Google Translate TTS (URL ישיר), **בלי** נפילה
ל-`speechSynthesis` בכלל — אין כאן וקטור לתקלה. לא נדרש שינוי.

### 3. `RoiGame\index-deployed.html`
קובץ ישן, **לא במעקב git, לא מקושר מ-`index.html`/מ-`manifest.json`, לא מפורסם ב-Netlify**
בפועל — אך נשא אותה תקלה בדיוק (`speakLetter()` בלי סינון קול כלל, ו-`playAudioWithCallback()`
עם נפילה ל"כל קול עברי" כולל גברי). על פי בחירת יאיר תוקן גם הוא (אותו דפוס
`pickFemaleVoice()`), אף שאינו בשימוש בפועל כרגע. אין קומיט git לקובץ זה — התיקון קיים
רק על הדיסק.

## מניעה לעתיד (תיעוד קבוע)

- **סקיל `roy-games-world`** (`~/.claude/skills/roy-games-world/SKILL.md`) — כלל ברזל #4:
  קריינות נשית תמיד, אסור להחליש את `pickFemaleVoice()`/`useNativeSpeechSynthesis()`,
  כל mp3 חדש מחייב ערך ב-`gen_fix_audio.py` באותו שינוי, אסור לעקוף את ה-pre-commit hook
  עם `--no-verify`.
- **זיכרון Claude** (`project_roy_games.md`) — עודכן עם תיאור מלא של התקלה, השורש והתיקון,
  כך שכל שיחה עתידית (כולל שיחות מקבילות) תדע על הכלל הזה לפני שהיא נוגעת בקוד השמע.

## נתיבים מקומיים רלוונטיים

- קובץ זה: `C:\Users\yairl\OneDrive\Desktop\roy-games\FEMALE_VOICE_FIX.md`
- `C:\Users\yairl\OneDrive\Desktop\roy-games\index.html`
- `C:\Users\yairl\OneDrive\Desktop\roy-games\gen_fix_audio.py`
- `C:\Users\yairl\OneDrive\Desktop\roy-games\.git\hooks\pre-commit`
- `C:\Users\yairl\.claude\skills\roy-games-world\scripts\check_audio.py`
- `C:\Users\yairl\.claude\skills\roy-games-world\SKILL.md`
- `C:\Users\yairl\OneDrive\Desktop\RoiGame\index-deployed.html`
