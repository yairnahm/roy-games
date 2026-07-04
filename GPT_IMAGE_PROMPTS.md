# פרומפטים ליצירת תמונות עם ChatGPT (GPT / DALL-E) — עולם המשחקים של רועי

## 1. הוראות שימוש

1. פותחים שיחה עם ChatGPT (עדיף GPT-4o / "Images").
2. מדביקים **פרומפט אחד בכל פעם** מתוך הבלוקים למטה (הפרומפט כולל את תיאור הסגנון + הסצנה הספציפית).
3. שומרים את התמונה שמתקבלת **בדיוק** תחת השם שכתוב מעל כל פרומפט (השם באנגלית, עם הנתיב המלא כפי שמופיע).
4. מידות: **ריבוע 1024x1024**. פורמט: **PNG**.
5. אחרי שכל התמונות בקבוצה (או בכל הרשימה) נשמרות במחשב, אומרים ל-Claude: **"חבר את התמונות החדשות"** — הוא כבר ידע לשבץ אותן בקוד ובנתיבים הנכונים.

אין צורך לשנות שום דבר בפרומפט חוץ מהחלק שמתאר את הסצנה — שורת הסגנון בהתחלה חייבת להישאר קבועה בכל התמונות, כדי שהדמות תיראה אותו הדבר בכל המשחקים.

---

## 2. סגנון אחיד — קידומת חובה לכל פרומפט

כל פרומפט מתחיל באותה שורת סגנון קבועה, כדי לשמור על אחידות חזותית של הדמות הראשית (הילד) בכל התמונות באתר:

```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts.
```

זו בדיוק הדמות הקיימת במשחק — חשוב לשמור על התיאור הזה מילה במילה בכל פרומפט שכולל את הילד.

---

## 3. משחק "סדר יום" (Routine Sequencing) — 16 תמונות

4 רצפים (בוקר / לילה / גן / ארוחה) × 4 שלבים כל אחד. **שמות הקבצים חייבים להיות מדויקים** — הקוד כבר כתוב ומצפה לשמות האלה בדיוק.

### רצף בוקר (morning)

`images/routine/morning_1.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy waking up in his bed, stretching his arms with a sleepy happy smile, soft morning light coming through the window. Consistent character across all images in this series.
```

`images/routine/morning_2.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy brushing his teeth at the bathroom sink, holding a toothbrush, small mirror in the background. Consistent character across all images in this series.
```

`images/routine/morning_3.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy getting dressed in his bedroom, in the middle of putting on his yellow t-shirt, happy expression. Consistent character across all images in this series.
```

`images/routine/morning_4.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy eating breakfast cereal at the kitchen table, holding a spoon, bowl of cereal in front of him, cheerful morning mood. Consistent character across all images in this series.
```

### רצף לילה (bedtime)

`images/routine/bedtime_1.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy taking a bubble bath in the evening, washing himself, lots of soft soap bubbles, relaxed happy expression. Consistent character across all images in this series.
```

`images/routine/bedtime_2.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy putting on blue pajamas in his bedroom in the evening, sleepy happy smile. Consistent character across all images in this series.
```

`images/routine/bedtime_3.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy sitting in bed listening to a bedtime story being read by his mom, who is sitting on the edge of the bed holding an open book, warm cozy lamp light. Consistent character across all images in this series.
```

`images/routine/bedtime_4.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy sleeping peacefully in bed, blanket tucked in, a calm moon visible through the window, soft nighttime colors. Consistent character across all images in this series.
```

### רצף גן (gan / kindergarten)

`images/routine/gan_1.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy putting on a small backpack at home by the front door, ready to leave, cheerful expression. Consistent character across all images in this series.
```

`images/routine/gan_2.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy walking hand-in-hand with his dad along a sidewalk on the way to kindergarten, both smiling, small backpack on the boy. Consistent character across all images in this series.
```

`images/routine/gan_3.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy waving hello with a big smile to a friendly kindergarten teacher standing at the kindergarten door. Consistent character across all images in this series.
```

`images/routine/gan_4.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy sitting on the floor playing with colorful building blocks together with other kids in the kindergarten classroom, happy engaged expressions. Consistent character across all images in this series.
```

### רצף ארוחה (meal)

`images/routine/meal_1.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy washing his hands with soap at the sink before a meal, bubbles on his hands, focused happy expression. Consistent character across all images in this series.
```

`images/routine/meal_2.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy sitting down at a nicely set table, with a plate, cup, and fork in front of him, ready to eat. Consistent character across all images in this series.
```

`images/routine/meal_3.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy eating a meal happily at the table, holding a fork, big smile, plate of food in front of him. Consistent character across all images in this series.
```

`images/routine/meal_4.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Main character: a young boy with short black hair wearing a yellow t-shirt and dark blue shorts. Scene: the boy standing at the kitchen counter, bringing his empty plate to place it on the counter, proud satisfied expression. Consistent character across all images in this series.
```

---

## 4. משחק "מה צריך?" — 6 תמונות אובייקט (ללא הילד)

תמונות של חפץ בודד בלבד, על רקע פסטל פשוט ואחיד, בלי הילד ובלי טקסט.

`images/whatneeds/surrounds/coat.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A single warm blue winter coat hanging on a wooden hanger, centered in frame, no people.
```

`images/whatneeds/surrounds/flashlight.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A single small yellow flashlight, turned on with a glowing beam of light, centered in frame, no people.
```

`images/whatneeds/surrounds/sandwich.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A single fresh sandwich sitting on a plate, centered in frame, no people.
```

`images/whatneeds/surrounds/bed.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A cozy child's bed with a soft blue blanket and a pillow, centered in frame, no people.
```

`images/whatneeds/surrounds/soap.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A single bar of soap with soft bubbles around it, centered in frame, no people.
```

`images/whatneeds/surrounds/boots.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A pair of red rain boots standing in a small puddle, centered in frame, no people.
```

---

## 5. משחק "טוב או לא טוב?" — 3 זוגות תרחישים חדשים

לכל תרחיש שתי תמונות: **תמונה טובה** עם פס ירוק מעוגל רחב בתחתית התמונה ובו סילואטות לבנות קטנות שמסמלות את הפעולה החיובית, ו**תמונה רעה** עם אותו פס אך באדום. זה תואם בדיוק את הסגנון הקיים במשחק — חשוב לשמור על הפס הצבעוני בתחתית בשתי התמונות.

### 11 — שולחן (shulchan)

`images/sharing_scenes/11_shulchan/bechira_tova.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Two young boys happily setting the dinner table together with their mom, placing plates and cups, everyone smiling. At the very bottom of the image add a wide green rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing setting a table together.
```

`images/sharing_scenes/11_shulchan/bechira_raa.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. One young boy throwing food on the floor at the dinner table, his mom standing nearby looking sad and concerned. At the very bottom of the image add a wide red rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing throwing food on the floor.
```

### 12 — תור (kav)

`images/sharing_scenes/12_kav/bechira_tova.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. A group of children standing nicely in an orderly line at the kindergarten door, calm and happy, waiting their turn. At the very bottom of the image add a wide green rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing standing in line.
```

`images/sharing_scenes/12_kav/bechira_raa.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. One boy pushing past other children and cutting in front of the line at the kindergarten door, the other kids look upset and surprised. At the very bottom of the image add a wide red rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing cutting in line.
```

### 13 — ידיים (yadaim)

`images/sharing_scenes/13_yadaim/bechira_tova.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. A young boy washing his hands with soap and water at the sink before eating, smiling happily. At the very bottom of the image add a wide green rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing washing hands.
```

`images/sharing_scenes/13_yadaim/bechira_raa.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. A young boy with visibly dirty hands reaching for food at the table, turning away and refusing to go to the sink, unhappy expression. At the very bottom of the image add a wide red rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing dirty hands refusing to wash.
```

---

## 6. הרחבת משחקי השיתוף (sharing) — 2 שלשות תמונות חדשות

לכל תיקייה 3 תמונות: **matzav_bsisi.png** — מצב פתיחה ניטרלי, שני ילדים וחפץ אחד בלבד, **בלי פס צבעוני**; **bechira_tova.png** — פס ירוק, שיתוף/כיבוד תורות; **bechira_raa.png** — פס אדום, חטיפה/סירוב.

### 14 — נדנדה (nadneda)

`images/sharing_scenes/14_nadneda/matzav_bsisi.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Two young boys standing next to a single swing in a playground, looking at it, neutral curious expressions. No banner or strip in this image.
```

`images/sharing_scenes/14_nadneda/bechira_tova.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Two young boys at a playground swing, one gently pushing the other on the swing and smiling, clearly taking turns happily. At the very bottom of the image add a wide green rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing taking turns on a swing.
```

`images/sharing_scenes/14_nadneda/bechira_raa.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Two young boys at a playground swing, one boy grabbing the swing and refusing to let the other boy have a turn, the other boy looking upset. At the very bottom of the image add a wide red rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing refusing to share a swing.
```

### 15 — עפיפון (afifon)

`images/sharing_scenes/15_afifon/matzav_bsisi.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Two young boys standing in a park looking at a single colorful kite lying on the grass, neutral curious expressions. No banner or strip in this image.
```

`images/sharing_scenes/15_afifon/bechira_tova.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Two young boys in a park flying a kite together, taking turns holding the string, both smiling and looking up at the kite happily. At the very bottom of the image add a wide green rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing sharing a kite.
```

`images/sharing_scenes/15_afifon/bechira_raa.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered background, no text anywhere in the image, clear simple facial expressions. Two young boys in a park, one boy grabbing the kite string away from the other boy and turning away, the other boy looking upset and reaching for it. At the very bottom of the image add a wide red rounded banner strip spanning the width of the image, containing small simple white icon silhouettes representing grabbing a kite away.
```

---

## 7. הרחבת "מגדל קוביות" — סוג מגדל חדש: גשר (bridge)

5 תמונות, אובייקט מבודד על רקע פשוט, בלי הילד — מציגות גשר צעצוע שנבנה בהדרגה מקובייה אחת עד חמש קוביות.

`images/towertalk/bridge_1.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A toy bridge made of colorful building blocks, at its very first stage with just 1 block placed, centered in frame, no people.
```

`images/towertalk/bridge_2.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A toy bridge made of colorful building blocks, partially built with 2 blocks placed, centered in frame, no people.
```

`images/towertalk/bridge_3.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A toy bridge made of colorful building blocks, partially built with 3 blocks placed, starting to take the shape of a small bridge, centered in frame, no people.
```

`images/towertalk/bridge_4.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A toy bridge made of colorful building blocks, almost complete with 4 blocks placed, clearly recognizable as a bridge shape, centered in frame, no people.
```

`images/towertalk/bridge_5.png`
```
Soft Pixar-style 3D illustration for a children's educational game, warm pastel colors, simple uncluttered plain pastel background, no text anywhere in the image. A complete toy bridge made of 5 colorful building blocks, fully built and recognizable as a bridge with an arch to walk under, centered in frame, no people.
```

---

## 8. קולות אמיתיים ללוטו צלילים — הערה

**GPT ל-Images לא יכול ליצור קבצי שמע** (רק תמונות) — לכן אי אפשר לייצר צלילים אמיתיים של בעלי חיים/כלי רכב בדרך הזו.

**המלצה:** להוריד קליפים חופשיים מרישיון (CC0) מהאתר [freesound.org](https://freesound.org) — לחפש למשל:
- cow moo (פרה גועה)
- dog bark (כלב נובח)
- cat meow (חתול מיילל)
- rooster crow (תרנגול קורא)
- car horn (צפירת מכונית)
- train whistle (שריקת רכבת)

לשמור כל קובץ בשם המתאים תחת: `audio/sfx/<name>.mp3`

לאחר ההורדה — לבקש מ-Claude לחבר את קבצי השמע לקוד.
