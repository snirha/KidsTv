# prompts

**פרק 002 — Real Animal Sounds: Zoo Edition** | פורמט B | יחס תמונה: 16:9 (פרק מלא, לא Short)

## קבועים (לשימוש מילולי בכל פרומפט למטה — לפי `ai-visual-consistency`)

**Pip base prompt (verbatim, `bible/characters/pip.md` §4):**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design
```

**Style suffix (verbatim, `bible/style-bible.md`):**
```
, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
```

**Negative prompt block (verbatim, `bible/style-bible.md`):**
```
no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons
```

**Pip's Meadow home-base environment prompt (verbatim, `bible/locations/pips-meadow.md`) — לשימוש בכל סצנה שבה Pip "בבית" (OPEN/RECAP/CLOSE):**
```
Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated colors, simple rounded shapes, consistent background design
```

**⚠️ הערה: קיימת תמונת רפרנס מאושרת ונעולה של הבית** — `bible/locations/pips-meadow.md` §סטטוס: `bible/locations/assets/pips-meadow-with-pip-approved.jpg`. יש להשתמש בתמונה הזו כ-Frames-to-Video / Character-reference בפועל עבור OPEN/RECAP/CLOSE של הפרק הזה, ולא רק בטקסט — הטקסט כאן הוא הגיבוי/בדיקת עקביות (כלל 1+2 ב-`ai-visual-consistency`).

**Pip's Meadow Zoo — סביבת AI קבועה לפריטים 1–4 (חדשה לפרק 002, לשימוש מילולי ואחיד בכל ארבעת הפריטים — לא לנסח מחדש בין פריט לפריט):**
```
a cheerful cartoon zoo habitat clearing, low rounded pale-wood viewing fence in the foreground, soft green grass, a few smooth round beige rocks, two or three small rounded leafy green bushes, warm bright blue sky with a simple stylized cartoon sun, no cages, no metal bars, no concrete walls, no zoo visitors, no crowds, no signage, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, consistent background design
```
**Negative prompt נוסף לסביבת הזואו (בנוסף לבלוק הקבוע):**
```
no cages, no metal bars, no concrete enclosure, no zoo visitors, no crowds, no signage, no vehicles
```

כל פרומפט למטה בנוי לפי התבנית: `[Pip base prompt] + [action/scene clause, כולל את מחרוזת הסביבה הרלוונטית מילה במילה] + [style suffix] + Negative prompt: [negative block]`. השתמשו ב-Character asset שמור של Pip (ותמונת הרפרנס הנעולה של הבית, לסצנות OPEN/RECAP/CLOSE) במקום להקליד את התיאור מחדש, כשהכלי תומך בכך — הטקסט המלא נשמר כאן כגיבוי/פולבק ולבדיקת עקביות.

**⚠️ הערת lip-sync קריטית (לפי CLAUDE.md §5 + status.md, לקח מפרק 001) — חלה על ITEM 1–4:** כל פרומפט Image/Image→Video למטה לפריטים 1-4 מציג **Pip + החיה יחד** בקליפ ה-AI, וזה תקין לשלב ה-generation ב-Google Flow. **אבל בשלב ה-lip-sync (avatar-generation, fal-ai/kling-video/ai-avatar/v2) יש לחתוך/להפיק רפרנס Pip-בלבד** (בלי החיה בפריים) מהתמונה/קליפ המאושר, ולא לשלוח את הרפרנס עם שתי הדמויות למודל ה-avatar — אחרת המודל עלול להנפיש גם את פי החיה כאילו היא מדברת (בעיה שחזרה על עצמה ב-4 מתוך 5 מקטעי Pip בפרק 001). לשקול קומפוזיציה מחדש בעריכה (Pip-לבד מסונכרן + החיה מורכבת בחזרה כשכבה נפרדת) אם השוט המשולב חשוב לשמר.

---

## OPEN — Pip's Meadow, home base

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, wiggling his nose three times, big excited eyes looking straight at camera, welcoming pose, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, consistent background design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no dark shadows, no dense dark forest
```

**(2) Image→Video prompt (motion: signature nose-wiggle x3, then wave):**
```
Animate this exact image of Pip in Pip's Meadow: Pip wiggles his nose three quick times (signature gesture), eyes widening with excitement on each wiggle, then breaks into a warm wave toward camera with one paw, gentle idle sway of the scarf in a light breeze, soft bounce on his feet, camera holds a static friendly medium shot, no camera shake, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no tall trees, keeping the same open meadow with only rolling hills and round bushes at the edges
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing, no trees, no forest, no new background elements
```

**(3) קובץ:** `002-open-pip-meadow.png` / `002-open-pip-meadow.mp4`

---

## ITEM 1 — LION

**(1) Image prompt (Pip + AI-cartoon lion together):**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in a cheerful cartoon zoo habitat clearing, low rounded pale-wood viewing fence in the foreground, soft green grass, a few smooth round beige rocks, two or three small rounded leafy green bushes, warm bright blue sky with a simple stylized cartoon sun, no cages, no metal bars, no concrete walls, no zoo visitors, no crowds, no signage, pointing excitedly at a friendly round cartoon lion beside him — the lion has a big soft rounded golden-tan mane made of simple puffy shapes, big gentle round eyes, a soft rounded 3D-cartoon body matching Pip's art style, warm closed-mouth smile, both characters facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no cages, no metal bars, no concrete enclosure, no zoo visitors, no crowds, no signage, no vehicles
```

**(2) Image→Video prompt (motion: point, lion roars playfully, Pip reacts):**
```
Animate this exact image: Pip points at the cartoon lion with one paw and leans forward, curious; the lion opens its mouth in a big playful-cute "ROAR" (exaggerated friendly mouth shape, round eyes staying warm and gentle, not fierce), its puffy mane bounces softly once, Pip's ears perk up and he nods along, then Pip wiggles his nose three times before turning back to camera, gentle grass sway in background, static warm medium shot, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no cages, no metal bars, no concrete enclosure
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing, no bared fangs, no aggressive pose, no cages, no metal bars
```

**(3) קובץ:** `002-item1-lion-ai.png` / `002-item1-lion-ai.mp4`

**חלופה לתיקון בטיימליין (alt, לשימוש אם התוצאה הראשונה לא עומדת בבדיקת drift):**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, sitting on a smooth round rock next to a small round cartoon lion with a soft puffy golden-tan mane and big gentle eyes, both smiling at camera, low rounded wooden zoo fence softly blurred in background, no cages, no bars, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no cages, no metal bars
```

---

## ITEM 2 — ELEPHANT

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in a cheerful cartoon zoo habitat clearing, low rounded pale-wood viewing fence in the foreground, soft green grass, a few smooth round beige rocks, two or three small rounded leafy green bushes, warm bright blue sky with a simple stylized cartoon sun, no cages, no metal bars, no concrete walls, no zoo visitors, no crowds, no signage, standing next to a friendly round cartoon elephant with soft grey rounded skin, big floppy rounded ears, a gently curled trunk, big gentle eyes, soft rounded 3D-cartoon body matching Pip's art style, both facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no cages, no metal bars, no concrete enclosure, no zoo visitors, no crowds, no signage, no vehicles
```

**(2) Image→Video prompt (motion: elephant trumpets/toots, Pip marvels at the ears):**
```
Animate this exact image: the cartoon elephant lifts its trunk and gives a cheerful soft "TOOT" like a small round horn, its big floppy ears flap gently once, Pip wiggles his nose three times, then tilts his head back in wide-eyed wonder looking up at the elephant's big ears, gasping softly ("Whoa!") and gesturing with both paws to show how big they are, camera holds a static warm medium shot, gentle grass sway in background, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no cages, no metal bars, no concrete enclosure
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing, no cages, no metal bars
```

**(3) קובץ:** `002-item2-elephant-ai.png` / `002-item2-elephant-ai.mp4`

**חלופה לתיקון בטיימליין:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing beside a small round soft-grey cartoon elephant with big floppy ears near a low rounded wooden zoo fence, warm afternoon light, no cages, no bars, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no cages, no metal bars
```

---

## ITEM 3 — MONKEY

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in a cheerful cartoon zoo habitat clearing, low rounded pale-wood viewing fence in the foreground, soft green grass, a few smooth round beige rocks, two or three small rounded leafy green bushes, warm bright blue sky with a simple stylized cartoon sun, no cages, no metal bars, no concrete walls, no zoo visitors, no crowds, no signage, beside a friendly round cartoon monkey with soft warm-brown fur, a small rounded pale face, big gentle eyes, a long curled tail, mid-playful pose hanging from a short sturdy rounded tree branch beside the fence, soft rounded 3D-cartoon body matching Pip's art style, both facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no cages, no metal bars, no concrete enclosure, no zoo visitors, no crowds, no signage, no vehicles
```

**(2) Image→Video prompt (motion: monkey swings and calls, Pip mimics playfully):**
```
Animate this exact image: the cartoon monkey swings once on the branch and calls out a playful soft "OOH OOH AH AH" with a big happy open-mouth grin (friendly, not aggressive, no bared fangs), its tail curls and uncurls once, Pip wiggles his nose three times and hops in place mimicking the rhythm, then turns to camera smiling, gentle leaf sway on the branch in background, static warm medium shot, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no cages, no metal bars, no concrete enclosure
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing, no bared fangs, no aggressive pose, no threatening posture, no cages, no metal bars
```

**(3) קובץ:** `002-item3-monkey-ai.png` / `002-item3-monkey-ai.mp4`

**חלופה לתיקון בטיימליין:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, sitting on a smooth round rock next to a small round warm-brown cartoon monkey perched calmly on a low sturdy branch, low rounded wooden zoo fence softly blurred in background, no cages, no bars, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no cages, no metal bars
```

---

## ITEM 4 — SNAKE

**⚠️ הערת בטיחות/עיצוב ייעודית לפריט זה (לפי הנחיית המשתמש + fact-checker):** הנחש חייב להיראות **ידידותי ולא מאיים בשום פריים** — עיניים גדולות ועגולות (לא חרירי-עין דמויי-זוחל), פה סגור או חייכן-רגוע, **בלי שיניים/ניבים חשופים בשום שלב**, גוף מגובב-עגול (לא מתפתל בצורה תוקפנית), ללא תנוחת התקפה. זה מיושם בפרומפטים למטה גם ב-Image וגם ב-Image→Video, כולל negative prompt מוגבר.

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in a cheerful cartoon zoo habitat clearing, low rounded pale-wood viewing fence in the foreground, soft green grass, a few smooth round beige rocks, two or three small rounded leafy green bushes, warm bright blue sky with a simple stylized cartoon sun, no cages, no metal bars, no concrete walls, no zoo visitors, no crowds, no signage, beside a friendly round cartoon snake coiled in a soft gentle loop on a warm rock, bright cheerful green-and-yellow rounded pattern, big round oversized cartoon eyes with visible warm brown pupils, closed friendly smiling mouth, no visible teeth or fangs, soft rounded 3D-cartoon body with no sharp angles, relaxed non-threatening coiled pose, both characters facing camera, daytime, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no aggressive pose, no bared fangs, no threatening posture, no cages, no metal bars, no concrete enclosure, no zoo visitors, no crowds, no signage, no vehicles
```

**(2) Image→Video prompt (motion: snake hisses gently and friendly, Pip mimics playfully):**
```
Animate this exact image: the cartoon snake lifts its head gently and gives a soft playful "HISS" with its mouth staying closed or in a small friendly closed-lip smile shape (no open mouth, no visible teeth or fangs), big round eyes staying warm and cheerful throughout, its coiled body sways slowly and gently side to side like a slow wave, no lunging or striking motion, Pip wiggles his nose three times and sways playfully in the same slow gentle rhythm, then turns to camera smiling, static warm medium shot, smooth slow toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no cages, no metal bars, no concrete enclosure
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing, no aggressive pose, no bared fangs, no threatening posture, no striking motion, no lunging, no cages, no metal bars
```

**(3) קובץ:** `002-item4-snake-ai.png` / `002-item4-snake-ai.mp4`

**חלופה לתיקון בטיימליין:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, sitting beside a small round bright green-and-yellow cartoon snake coiled calmly on a warm flat rock, big round friendly eyes, closed smiling mouth, no fangs visible, low rounded wooden zoo fence softly blurred in background, no cages, no bars, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no aggressive pose, no bared fangs, no threatening posture, no cages, no metal bars
```

---

## RECAP — Pip's Meadow, home base, with 4 animal icons

**⚠️ הערת ייצור לפי הפתרון שנעל בפרק 001 (גרסה 3, CLAUDE.md §5):** את התמונה/קליפ הזה יש לייצר ולאשר **כווידאו נקי אחד** (Pip + 4 בועות מונפשות, מצביע עליהן בזה אחר זה) ב-Google Flow — **ללא** מעורבות שלב ה-lip-sync avatar-generation. רק **בשלב ה-lip-sync בפועל** יש לחתוך/להפיק מהתמונה המאושרת רפרנס **Pip-בלבד** (ללא הבועות בפריים) לשליחה ל-fal-ai/kling-video/ai-avatar/v2 — כדי למנוע מהמודל לסטות את אחת הבועות לצורה לא-קשורה (כמו שקרה לבועת הכבשה בפרק 001, שסטתה לפרצוף דמוי-תינוק-אנושי). לאחר קבלת הפלט המסונכרן של Pip-בלבד, ארבע הבועות המונפשות המקוריות (מהקליפ הנקי המאושר) יורכבו בחזרה כ-overlay נפרד עם מסכת אלפא עגולה, בדיוק כמו ב-RECAP של פרק 001 — לא לשלוח את הבועות למודל ה-avatar בשום שלב.

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, four small simple round cartoon icons floating gently around Pip at chest height — a lion, an elephant, a monkey, and a snake, each matching the art style of their earlier zoo scenes, each friendly and non-threatening (lion's mane soft and round, snake with big round eyes and closed mouth, no fangs on any icon), evenly spaced, Pip smiling at camera pointing at the icons one by one, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, consistent background design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no dark shadows, no dense dark forest, no bared fangs, no aggressive pose, no threatening posture
```

**(2) Image→Video prompt (motion: Pip points to each icon in turn as its sound is said):**
```
Animate this exact image: Pip points to the lion icon as "roar" is heard, then the elephant icon as "toot" is heard, then the monkey icon as "ooh ooh ah ah" is heard, then the snake icon as "hiss" is heard, each icon gently bounces once when pointed at (the snake icon stays coiled and calm, big round eyes, closed friendly mouth, no lunging), Pip's expression stays warm and encouraging throughout, camera holds a static friendly medium shot, smooth toddler-paced motion, duration 5-6 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no tall trees, keeping the same open meadow with only rolling hills and round bushes at the edges
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing, no trees, no forest, no new background elements, no bared fangs, no aggressive pose, no threatening posture
```

**(3) קובץ:** `002-recap-pip-meadow.png` / `002-recap-pip-meadow.mp4`

---

## CLOSE — Pip's Meadow, home base

**(1) Image prompt:**
```
Pip the quokka, small round toddler-friendly 3D cartoon character, chubby soft marsupial body, warm sandy-brown fur (#C68958), cream belly patch (#F5E6D3), big round dark brown eyes spaced wide apart, small rounded ears, permanent gentle smile, wearing a bright teal scarf (#2EC4B6) with a tiny white star patch, soft 3D cartoon style, warm soft lighting, simple rounded shapes, no sharp edges, toddler animation style, consistent character design, standing in Pip's Meadow home base, a small sunny open meadow clearing, soft rounded green hills in the background, bright warm blue sky with a simple stylized cartoon sun, one or two round soft green bushes on the sides, warm green grass, no dark forest, no tall trees, no shadows or scary elements, waving one paw at camera, warm happy closing expression, golden late-afternoon light, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, consistent background design
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no dark shadows, no dense dark forest
```

**(2) Image→Video prompt (motion: wave + nose-wiggle x3 sign-off):**
```
Animate this exact image of Pip in Pip's Meadow: Pip waves warmly at camera with one paw for about a second, then wiggles his nose three quick times (signature closing gesture), eyes crinkling with a happy gentle smile, soft idle sway of the scarf in a light breeze, camera holds a static friendly medium shot, no camera shake, gentle fade-ready final frame, smooth toddler-paced motion, duration 4-5 seconds, soft 3D cartoon style, warm soft pastel lighting, toddler animation style, bright saturated primary colors, simple rounded shapes, no sharp edges, consistent character design, no tall trees, keeping the same open meadow with only rolling hills and round bushes at the edges
Negative prompt: no text, no watermark, no extra limbs, no scary face, no realistic human anatomy, no violence, no weapons, no fast whip-pans, no strobing, no trees, no forest, no new background elements
```

**(3) קובץ:** `002-close-pip-meadow.png` / `002-close-pip-meadow.mp4`

---

## הערות למפיק/עורך

- כל 6 הפריטים (open, lion, elephant, monkey, snake, close) + RECAP משתמשים במחרוזת הבסיס המדויקת של Pip מ-`bible/characters/pip.md` §4, ללא כל שינוי מילה — לפי כלל 3 ב-`ai-visual-consistency`. מומלץ להשתמש ב-Character asset שמור של Pip (Google Flow Ingredient) כשמפיקים בפועל, ולא רק בתיאור הטקסטואלי; ל-OPEN/RECAP/CLOSE יש כבר תמונת רפרנס נעולה של הבית (`bible/locations/assets/pips-meadow-with-pip-approved.jpg`) — יש להשתמש בה כ-Frames to Video, לא ליצור סביבה מחדש מטקסט.
- סביבת הזואו (סעיף "קבועים" למעלה) חדשה לפרק זה ואינה מבוססת עוד על תמונת רפרנס מאושרת — בדיוק כמו ב-OPEN של פרק 001, יש להריץ ולאשר תוצאה אחת (למשל ITEM 1 — LION) ולשמור אותה כרפרנס/Ingredient לשימוש חוזר בפריטים 2-4, כדי שכל ארבעת סצנות הזואו יתבססו על אותה תמונה מאושרת בפועל, לא רק על אותו טקסט.
- **לקח מפרק 001 שיושם כאן במפורש:** כל פרומפט לפריטים 1-4 מזכיר Pip+חיה יחד לשלב ה-Flow generation, אך יש הערה נפרדת (לעיל, אחרי "קבועים") שמורה במפורש לשלב ה-lip-sync לחתוך רפרנס Pip-בלבד לפני avatar-generation. RECAP מזכיר במפורש את פתרון-הבועות (גרסה 3) מפרק 001.
- **הנחש (ITEM 4):** בנוסף לכללי "no scary face" הגלובליים, נוספו לכל הפרומפטים של הנחש — Image, Image→Video וה-alt — התיאור המפורש "big round eyes, closed/smiling mouth, no visible teeth or fangs" ו-negative prompt מוגבר: `no aggressive pose, no bared fangs, no threatening posture` (וב-video גם `no striking motion, no lunging`).
- כל וידאו הוא image-to-video (כלל 7 בסקיל) מהתמונה הנעולה של אותה סצנה, לא text-to-video עצמאי.
- משך כל שוט ≤6 שניות (4-6s כאן), בהתאם לחוקי הקצב ל-toddlers (`toddler-content-pacing`).
- אם תוצאה סוטה מה-Bible (צבע, יחס ראש-גוף, צעיף חסר, נחש שנראה מאיים) — יש להשתמש בפרומפט החלופי ולהתחיל מחדש מהבסיס הקבוע, לא "לתקן" תוצאה שגויה (regenerate, not patch — לפי הסקיל).
