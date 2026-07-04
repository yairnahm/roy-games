# מפרט תמונות לתוכן חדש — המרכז של רועי

מסמך זה מיועד ליאיר: פרומפטים מוכנים לייצור תמונות ב-AI (בסגנון הקיים) עבור הרחבות תוכן עתידיות.
לאחר יצירת התמונות — לשמור בשמות ובנתיבים המדויקים שלמטה, ולבקש מ-Claude "חבר את התמונות החדשות" — החיבור הוא תוספת דאטה בלבד.

## כללי סגנון (לכל התמונות)
- סגנון: איור תלת-ממד רך בסגנון פיקסאר, צבעים פסטליים חמים, רקע פשוט ולא עמוס.
- אותה דמות ילד בכל התמונות: ילד עם שיער שחור קצר וחולצה צהובה (הדמות הקיימת במשחקים — ראה `images/whatneeds/child_forward.png`).
- ללא טקסט בתוך התמונה. הבעות פנים ברורות ופשוטות (חשוב ל-ASD).
- גודל: 1024×1024, לשמור כ-PNG או WEBP (עד ~300KB — אפשר לבקש מ-Claude לכווץ).

## 1. סצינות חדשות ל"מה צריך?" (whatneeds) — דורש תמונות חדשות
כבר נוספו 5 סצינות מנכסים קיימים (סה"כ 12). להרחבה נוספת חסרות תמונות surround חדשות:

| קובץ | פרומפט |
|---|---|
| `images/whatneeds/surrounds/coat.png` | Pixar-style soft 3D illustration of a warm blue winter coat on a hanger, plain pastel background, no text |
| `images/whatneeds/surrounds/flashlight.png` | Pixar-style soft 3D illustration of a small yellow flashlight turned on, plain pastel background, no text |
| `images/whatneeds/surrounds/sandwich.png` | Pixar-style soft 3D illustration of a fresh sandwich on a plate, plain pastel background, no text |
| `images/whatneeds/surrounds/bed.png` | Pixar-style soft 3D illustration of a cozy child's bed with blue blanket, plain pastel background, no text |
| `images/whatneeds/surrounds/soap.png` | Pixar-style soft 3D illustration of a bar of soap with bubbles next to a faucet, plain pastel background, no text |
| `images/whatneeds/surrounds/boots.png` | Pixar-style soft 3D illustration of red rain boots in a small puddle, plain pastel background, no text |

סצינות מתוכננות (קר→מעיל, חושך→פנס, רעב→כריך, עייף→מיטה, ידיים מלוכלכות→סבון, גשם→מגפיים).

## 2. תרחישים חדשים ל"טוב או לא טוב?" — דורש זוגות תמונות
כבר נוספו 8 תרחישים מתמונות קיימות (מגלשה, החלפת צעצועים, סיפור עם אימא, שטיח). לזוגות חדשים:

| תיקייה | טוב (bechira_tova) | לא טוב (bechira_raa) |
|---|---|---|
| `images/sharing_scenes/11_shulchan/` | Two boys setting the table together with mom, green banner at bottom | One boy throwing food on the floor, red banner at bottom |
| `images/sharing_scenes/12_kav/` | Children standing nicely in line at kindergarten door, green banner | One boy cutting the line pushing others, red banner |
| `images/sharing_scenes/13_yadaim/` | Boy washing hands with soap before eating, smiling, green banner | Boy refusing to wash hands, dirty hands near food, red banner |

(שים לב לפורמט הקיים: פס ירוק בתחתית לתמונת "טוב", פס אדום לתמונת "לא טוב", עם אייקונים לבנים קטנים — כמו בתמונות הקיימות בתיקיות 01-10.)

## 3. סצינות חדשות ל"לחלוק ולהצליח" (sharing)
כל סצינה = תיקייה `images/sharing_scenes/NN_shem/` עם 3 קבצים:
- `matzav_bsisi.webp` — מצב פתיחה נייטרלי (שני ילדים + אובייקט אחד)
- `bechira_tova.webp` — הבחירה הטובה (משתפים/מחכים בתור), פס ירוק
- `bechira_raa.webp` — הבחירה הרעה (חוטפים/מתעלמים), פס אדום

רעיונות: נדנדה אחת בגן (תורות), עפיפון אחד בפארק, מחשב אחד בבית.

## מה קורה אחרי שהתמונות מוכנות
1. לשים את הקבצים בנתיבים למעלה.
2. להגיד ל-Claude: "חבר את התמונות החדשות של [whatneeds/goodbad/sharing]".
3. Claude יוסיף את הדאטה, ייצר שמע gTTS לשאלות ולמשוב, יריץ check_audio, ויפרוס עם העלאת cache.
