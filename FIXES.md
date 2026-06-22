# תיקונים מוצעים — roy-games/index.html
> כל שינוי מתייחס לקובץ `index.html` אלא אם צוין אחרת.

---

## תיקון 1 — גובה מסך מלא (100dvh)

**בעיה:** ה-`body` מוגדר עם `min-height: 100vh` אך הילדים הישירים לא מתרחבים לגובה המלא, ולכן נוצר ריק לבן בתחתית במכשירים ניידים.

**מיקום:** שורה ~18 (CSS של `body`) ושורות ~1250, ~1284, ~1332, ~1360 (מסכי Hub/diff/gender/active)

### שינוי 1א — גוף הדף

```css
/* לפני: */
body { 
    font-family: 'Rubik', sans-serif; min-height: 100vh; ...
}

/* אחרי: */
body { 
    font-family: 'Rubik', sans-serif; min-height: 100dvh; ...
}
```

### שינוי 1ב — מסכים שצריכים לתפוס את כל הגובה

הוסף `flex: 1` לכל `div` שמייצג מסך ראשי, כך שיתפוס את השטח הנותר בתוך ה-`body` הפלקס:

```css
/* הוסף בסקציית ה-CSS: */
#hub-screen,
#gender-screen,
#unified-diff-screen,
#missing-lang-screen,
#active-game-container {
    flex: 1;
    display: flex;
    flex-direction: column;
}
```

> **הערה:** `#active-game-container:has(.numwar-layout) { height: 100svh; }` כבר קיים לנומוור — אל תמחק אותו.

---

## תיקון 2 — skeleton animation על תמונות בטעינה

**בעיה:** `.image-box` מציג רקע לבן/אפור (`#f8f9fa`) בזמן שהתמונה נטענת (~3 שניות ב-habitat). אין אינדיקציה ויזואלית לטעינה.

**מיקום:** CSS של `.image-box` (שורה ~100-110 בערך)

```css
/* הוסף לבלוק ה-CSS: */
@keyframes shimmer {
    0%   { background-position: -400px 0; }
    100% { background-position:  400px 0; }
}

.image-box {
    /* ... שאר המאפיינים הקיימים ... */
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 800px 100%;
    animation: shimmer 1.5s infinite linear, popIn 0.5s;
}

.image-box.loaded {
    background: none;
    animation: popIn 0.5s;
}
```

**ב-JavaScript** — בכל מקום שיוצרים `<img class="image-box">`, הוסף:

```js
img.onload = () => img.classList.add('loaded');
```

---

## תיקון 3 — preload תמונות לפני תחילת רמה (Habitat)

**בעיה:** תמונות ה-habitat נטענות רק ברגע הצגת השאלה — גורם לעיכוב של ~3 שניות.

**מיקום:** פונקציית `initHabitatGame` (שורה ~2214)

```js
/* לפני: */
function initHabitatGame() {
    get('active-game-title').textContent = 'מי גר כאן? 🏠';
    get('game-workspace').innerHTML = `...`;
    habOrder = shuffle(createRange(habData.length)).slice(0, 4);
    loadHabitatRound();
}

/* אחרי: */
function initHabitatGame() {
    get('active-game-title').textContent = 'מי גר כאן? 🏠';
    get('game-workspace').innerHTML = `<div id="tool-target-area" class="large-target"></div><div id="tool-options-area" class="opts-row"></div>`;
    habOrder = shuffle(createRange(habData.length)).slice(0, 4);

    // preload all images for this round before first display
    const toLoad = habOrder.map(i => [habData[i].qImg, habData[i].aImg]).flat();
    let loaded = 0;
    toLoad.forEach(src => {
        const img = new Image();
        img.onload = img.onerror = () => { if (++loaded === toLoad.length) loadHabitatRound(); };
        img.src = src;
    });
}
```

> אפשר להחיל את אותו דפוס גם ל-`initToolsGame`, `initContextGame`, `initVPartsGame`.

---

## תיקון 4 — שמות בעברית בכפתורי התשובה (Habitat)

**בעיה:** כפתורי התשובה ב-habitat מציגים תמונה בלבד ללא תווית — קשה לילד לדעת על מה הוא לוחץ לפני הלחיצה.

**מיקום:** פונקציית `loadHabitatRound` (שורה ~2239-2245)

```js
/* לפני: */
b.innerHTML = `<img src="${opt.aImg}" alt="${opt.aDesc}" style="width:100%; height:100%; object-fit:cover;">`;

/* אחרי: */
b.style.display = 'flex';
b.style.flexDirection = 'column';
b.style.alignItems = 'center';
b.style.gap = '4px';
b.innerHTML = `
    <img src="${opt.aImg}" alt="${opt.aDesc}" 
         style="width:100%; flex:1; object-fit:cover; border-radius:8px;">
    <span style="font-size:clamp(11px,2.5vmin,16px); font-weight:700; color:#333; padding:2px 0;">
        ${opt.aDesc}
    </span>`;
```

---

## תיקון 5 — סדר רמות הפוך (קשה → קל)

**בעיה:** מסך בחירת הרמה מציג: 🟢 קל → 🟡 בינוני → 🔴 קשה, כלומר הכי קל בהתחלה. ילדים שכבר יודעים מסיימים לחיצה על רמה 1 ואז רמה 2. רצוי שיתחילו לבחור מהקל אבל שהסדר הוויזואלי ייראה כמו התקדמות — שמור על הסדר הנוכחי (קל לקשה), אך הדגש את הרמה שהושלמה לאחרונה.

**חלופה — הצגת רמה מומלצת:**

**מיקום:** `openDifficultyScreen` (שורה ~1502) ו-CSS

```css
/* הוסף ב-CSS: */
.level-card.level-recommended {
    border-color: #FF9800 !important;
    box-shadow: 0 0 0 3px #FF980055, 0 6px 15px rgba(0,0,0,0.15);
    position: relative;
}
.level-card.level-recommended::after {
    content: '▶ מומלץ';
    position: absolute;
    top: -10px; left: 50%; transform: translateX(-50%);
    background: #FF9800; color: white;
    font-size: 11px; font-weight: 900;
    padding: 2px 8px; border-radius: 10px;
}
```

```js
/* ב-openDifficultyScreen, אחרי לולאת [1,2,3,4,5]: */
// סמן את הרמה הבאה המומלצת
const recommendedLevel = [1,2,3,4,5].find(l =>
    !(typeof awardedStars !== 'undefined' && awardedStars[gameId + '-' + l])
) || 1;
const recBtn = document.querySelector(`.level-card[onclick="startGameEngine(${recommendedLevel})"]`);
if (recBtn) recBtn.classList.add('level-recommended');
```

---

## תיקון 6 — שם המשחק בשורת Top-Bar במסך המשחק הפעיל

**בעיה:** `#active-game-container` מציג `top-bar` עם כפתור יציאה, אך ה-`h2#active-game-title` נמצא מחוץ ל-`top-bar` ולפעמים לא מוצג כלל במשחקים ספציפיים.

**מיקום:** שורה ~1347 (ה-HTML של `active-game-container`) ופונקציות `init*` של כל משחק

```html
<!-- לפני: -->
<div id="active-game-container" class="hidden">
    <div class="top-bar">
        <button class="exit-btn" onclick="backToHub()">➜ יציאה<\button>
        <div id="active-progress-container" class="progress-container"></div>
    </div>
    <h2 id="active-game-title" style="margin-bottom:16px;"></h2>
    ...
</div>

<!-- אחרי — העבר את הכותרת פנימה ל-top-bar: -->
<div id="active-game-container" class="hidden">
    <div class="top-bar">
        <button class="exit-btn" onclick="backToHub()">➜ יציאה<\button>
        <h2 id="active-game-title" style="margin:0; font-size:clamp(14px,3vmin,22px);"></h2>
        <div id="active-progress-container" class="progress-container"></div>
    </div>
    ...
</div>
```

> וודא שב-`top-bar` יש `justify-content: space-between` ו-`align-items: center`.

---

## תיקון 7 — דגלים (🇮🇱 / 🇬🇧) במקום טקסט "he/en"

**הקיים כבר עובד** — מסך `faces-lang-screen` (שורה ~1287) כבר משתמש ב-🇮🇱 ו-🇬🇧.

**בעיה:** מסך בחירת השפה של "איזו אות חסרה" (missing-lang-screen, שורה ~1225) משתמש ב"אבג"/"ABC" ללא דגל.

**מיקום:** שורה ~1225-1235

```html
<!-- לפני: -->
<div class="grid-card" onclick="openFacesModeScreen('he')" style="...">
    <div style="font-size:clamp(40px, 8vw, 80px);">אבג</div><h2>עברית</h2>
</div>
<div class="grid-card" onclick="openFacesModeScreen('en')" style="...">
    <div style="font-size:clamp(40px, 8vw, 80px);">ABC</div><h2>English</h2>
</div>

<!-- אחרי: -->
<div class="grid-card" onclick="startMissingGame('he')" style="...">
    <div style="font-size:clamp(40px, 8vw, 80px);">🇮🇱</div><h2>עברית</h2>
</div>
<div class="grid-card" onclick="startMissingGame('en')" style="...">
    <div style="font-size:clamp(40px, 8vw, 80px);">🇬🇧</div><h2>English</h2>
</div>
```

---

## תיקון 8 — tooltip/תיאור לכפתורי עגלה/מטבעות/פח

**בעיה:** ה-top-bar ב-hub מכיל אייקוני 🛒/💰/🗑️ ללא תיאור מה הם עושים. ילד שלא מכיר את ממשק לא יודע.

**מיקום:** CSS + HTML של כפתורי ה-top-bar ב-`hub-screen`

```css
/* הוסף ב-CSS: */
.icon-tooltip {
    position: relative;
    display: inline-flex;
    align-items: center;
}
.icon-tooltip::after {
    content: attr(data-tip);
    position: absolute;
    bottom: calc(100% + 6px);
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.75);
    color: white;
    font-size: 12px;
    white-space: nowrap;
    padding: 4px 8px;
    border-radius: 6px;
    pointer-events: none;
    opacity: 0;
    transition: opacity 0.2s;
    z-index: 100;
}
.icon-tooltip:hover::after,
.icon-tooltip:focus::after {
    opacity: 1;
}
```

```html
<!-- דוגמה — עטפו כל כפתור אייקון: -->
<button class="icon-tooltip" data-tip="עגלת הקניות" onclick="openShop()">🛒</button>
<button class="icon-tooltip" data-tip="המטבעות שלי" onclick="openWallet()">💰</button>
<button class="icon-tooltip" data-tip="מחיקת נתונים" onclick="confirmReset()">🗑️</button>
```

---

## תיקון 9 — שם הילד/ה בכותרת Hub (פרסונליזציה)

**הקיים:** ה-`setGender` כבר מעדכן את `hub-header` עם "המרכז של רועי / מיה".

**בעיה:** ה-`<h1>` בדף ה-HTML המקורי (שורה ~1203) מכיל hardcoded `המרכז של רועי` שנראה לרגע לפני שה-JS מתעדכן.

**מיקום:** שורה ~1203

```html
<!-- לפני: -->
<h1 style="margin-top: 3vh;" id="hub-header">המרכז של רועי</h1>

<!-- אחרי — ריק עד שה-JS יכתוב: -->
<h1 style="margin-top: 3vh;" id="hub-header">המרכז של&nbsp;...</h1>
```

וב-`setGender`:

```js
// כבר קיים, אך הוסף smooth transition:
const header = get('hub-header');
header.style.opacity = '0';
header.textContent = 'המרכז של ' + name;
requestAnimationFrame(() => {
    header.style.transition = 'opacity 0.4s';
    header.style.opacity = '1';
});
```

---

## סדר עדיפות מומלץ לביצוע

| # | תיקון | השפעה | קושי |
|---|--------|--------|------|
| 1 | גובה 100dvh (תיקון 1) | גבוהה | קל |
| 2 | Preload תמונות habitat (תיקון 3) | גבוהה | קל |
| 3 | תוויות שמות על כפתורי habitat (תיקון 4) | גבוהה | קל |
| 4 | Skeleton animation (תיקון 2) | בינונית | בינוני |
| 5 | שם המשחק ב-top-bar (תיקון 6) | בינונית | קל |
| 6 | דגלי שפה (תיקון 7) | נמוכה | קל |
| 7 | Tooltips על אייקונים (תיקון 8) | נמוכה | קל |
| 8 | Smooth personalization (תיקון 9) | נמוכה | קל |
| 9 | רמה מומלצת (תיקון 5) | בינונית | בינוני |
