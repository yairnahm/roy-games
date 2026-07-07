# -*- coding: utf-8 -*-
"""Regenerate all game voice MP3s with corrected Hebrew texts (gTTS female voice).

Fixes:
- "KOL HAKAVOD" pronunciation: uses holam (only in TTS text) so gTTS says KOL, not KAL.
- intro-boy.mp3 contained a Thai character inside the Hebrew word "to play".
- sharing/q5.mp3 contained a Latin 'm' inside the Hebrew word "tower" (read letter-by-letter).
- English family names were ALL CAPS (spelled out letter-by-letter) - now proper case with "and".
- Missing files that previously fell back to unreliable live TTS are now pregenerated:
  coop_turn_roy, tidy instructions/errors per category combo, tower blocks per tower type.
- feelwhen game (questions q1-q8 + emotion labels) pregenerated.

Run from the project root: python gen_fix_audio.py [filter]
  filter (optional): generate only files whose relative path contains this substring,
  e.g. `python gen_fix_audio.py feelwhen` regenerates only audio/feelwhen/*.

כלל ברזל: כל הפניה חדשה לקובץ mp3 ב-index.html חייבת ערך כאן + הרצה של הסקריפט.
קובץ חסר = נפילה ל-TTS של הדפדפן = סיכון לקול גברי (Asaf בווינדוס).
"""
import os
import sys
import time
from gtts import gTTS

BASE = os.path.abspath(os.path.dirname(__file__))
AUDIO = os.path.join(BASE, "audio")

# "kol" forced with holam
KOL = "כֹּל"  # כֹּל

ROOT_HE = {
    "intro-boy.mp3": "שָׁלוֹם רוֹעִי! בָּרוּךְ הַבָּא לְמֶרְכַּז הַמִּשְׂחָקִים שֶׁלְּךָ. בַּמֶּה נִרְצֶה לְשַׂחֵק הַיּוֹם?",
    "b-reg1.mp3": f"{KOL} הַכָּבוֹד רוֹעִי!",
    "b-kap1.mp3": f"{KOL} הַכָּבוֹד חֲבִיבִי!",
    "b-kap2.mp3": "אַתָּה פָּשׁוּט אַלּוּף!",
    "b-life1.mp3": f"אֵיזֶה יֹפִי, סִיַּמְתָּ אֶת {KOL} הַשְּׁלָבִים!",
    "b-life2.mp3": f"{KOL} הַכָּבוֹד רוֹעִי, אַתָּה מַדְהִים!",
    "g-reg1.mp3": f"{KOL} הַכָּבוֹד!",
    "g-kap1.mp3": f"{KOL} הַכָּבוֹד חֲבִיבָה!",
    "g-kap2.mp3": "אַתְּ אַלּוּפָה!",
    "g-life1.mp3": f"אֵיזֶה יֹפִי, סִיַּמְתְּ אֶת {KOL} הַשְּׁלָבִים!",
    "g-life2.mp3": f"{KOL} הַכָּבוֹד, אַתְּ מַדְהִימָה!",
    "shared-reg2.mp3": "יֹפִי שֶׁל עֲבוֹדָה!",
    "shared-reg3.mp3": "מְצֻיָּן!",
}

SHARING = {
    "q5.mp3": "אוֹרִי וְנוֹעַם רוֹצִים לִבְנוֹת מִגְדָּל, אֲבָל יֵשׁ רַק קֻפְסַת קֻבִּיּוֹת אַחַת. מָה יַעֲשֶׂה אוֹרִי?",
    "fb1.mp3": f"{KOL} הַכָּבוֹד! אוֹרִי מְשַׂחֵק בַּמַּשָּׂאִית יַחַד עִם נוֹעַם, וּשְׁנֵיהֶם נֶהֱנִים!",
    "fb2.mp3": f"{KOL} הַכָּבוֹד! אוֹרִי מַצִּיעַ לְנוֹעַם לַעֲשׂוֹת תּוֹרוֹת בַּטַּאבְּלֶט, וּשְׁנֵיהֶם נֶהֱנִים!",
    "fb3.mp3": f"{KOL} הַכָּבוֹד! אוֹרִי חוֹצֶה אֶת הָעוּגִיָּה לִשְׁנַיִם וְחוֹלֵק אוֹתָהּ עִם נוֹעַם!",
    "fb4.mp3": f"{KOL} הַכָּבוֹד! אוֹרִי מְחַכֶּה בְּסַבְלָנוּת בַּתּוֹר שֶׁלּוֹ לַגַּלְשָׁן!",
    "fb5.mp3": f"{KOL} הַכָּבוֹד! אוֹרִי מְשַׂחֵק בְּקֻבִּיּוֹת יַחַד עִם נוֹעַם, וּשְׁנֵיהֶם בּוֹנִים מִגְדָּל גָּדוֹל יַחַד!",
    "fb6.mp3": f"{KOL} הַכָּבוֹד! אוֹרִי מְחַלֵּק אֶת הַצְּבָעִים עִם נוֹעַם, וּשְׁנֵיהֶם מְצַיְּרִים יַחַד!",
    "q11.mp3": "לְעוֹמֶר יֵשׁ סֻכָּרִיָּה אַחַת עַכְשָׁו, וְאִם יְחַכֶּה קְצָת הוּא יְקַבֵּל שְׁתֵּי סֻכָּרִיּוֹת. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb11.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר חִכָּה בְּסַבְלָנוּת וְקִבֵּל שְׁתֵּי סֻכָּרִיּוֹת!",
    "q12.mp3": "עוֹמֶר מְנַסֶּה לְחַכּוֹת בְּלִי לְהִתְפַּתּוֹת מֵהַסֻּכָּרִיָּה. בַּמֶּה כְּדַאי לוֹ לַחְשׁוֹב?",
    "fb12.mp3": "יָפֶה מְאֹד! לַחְשׁוֹב עַל מַשֶּׁהוּ אַחֵר עוֹזֵר לְחַכּוֹת בְּסַבְלָנוּת!",
    "q13.mp3": "עוֹמֶר רוֹצֶה לְהַצְלִיחַ לְחַכּוֹת. מָה כְּדַאי לוֹ לְהַגִּיד לְעַצְמוֹ?",
    "fb13.mp3": f"{KOL} הַכָּבוֹד! לְהַזְכִּיר לְעַצְמוֹ שֶׁחֲכִיָּה שָׁוָה יוֹתֵר עוֹזֵר לְעוֹמֶר לְהִתְאַפֵּק!",
    "q14.mp3": "אִמָּא יָצְאָה לְרֶגַע מֵהַחֶדֶר וְאָמְרָה שֶׁהִיא תַּחְזֹר. מָה יַרְגִּישׁ עוֹמֶר?",
    "fb14.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר בּוֹטֵחַ שֶׁאִמָּא תַּחְזֹר כְּמוֹ שֶׁהִבְטִיחָה!",
    "q15.mp3": "יֵשׁ לְעוֹמֶר מְשִׁימָה קְצָת קָשָׁה, וְגַם מִשְׂחָק כֵּיפִי לְיָדָהּ. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb15.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר הִתְאַמֵּץ וְהִתְמַקֵּד בַּמְּשִׂימָה שֶׁלּוֹ!",
    "q16.mp3": "עוֹמֶר טָעָה בְּתַרְגִּיל בְּדַף הָעֲבוֹדָה שֶׁלּוֹ. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb16.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר לֹא מְוַתֵּר, הוּא מְתַקֵּן אֶת הַטָּעוּת וּמַמְשִׁיךְ!",
    "q17.mp3": "עוֹמֶר יָכוֹל לִבְחֹר חִידָה קַלָּה אוֹ חִידָה קָשָׁה יוֹתֵר. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb17.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר בּוֹחֵר לְהִתְאַתְגֵּר עִם הַחִידָה הַקָּשָׁה!",
    "q18.mp3": "עוֹמֶר עוֹבֵד עַל חִידָה מְאַתְגֶּרֶת. מָה עוֹבֵר לוֹ בָּרֹאשׁ?",
    "fb18.mp3": "יָפֶה מְאֹד! לֵהָנוֹת מֵהָאֶתְגָּר עוֹזֵר לְעוֹמֶר לְהַתְמִיד!",
    "q19.mp3": "עוֹמֶר סִיֵּם חִידָה אַחַת בְּהַצְלָחָה. אֵיזוֹ חִידָה יִבְחַר הַפַּעַם?",
    "fb19.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר מַמְשִׁיךְ לְהִתְאַתְגֵּר גַּם אַחֲרֵי הַצְלָחָה!",
    "q20.mp3": "עוֹמֶר לֹא הִצְלִיחַ לְהַשְׁלִים אֶת הַחִידָה. מָה יַגִּיד לְעַצְמוֹ?",
    "fb20.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר מַאֲמִין שֶׁהוּא יָכוֹל לְהִשְׁתַּפֵּר עִם תִּרְגּוּל!",
    "q21.mp3": "הַפָּאזֶל שֶׁל עוֹמֶר נַעֲשָׂה קְצָת מְשַׁעֲמֵם. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb21.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר הִתְמִיד עַד שֶׁסִּיֵּם אֶת הַפָּאזֶל!",
    "q22.mp3": "אִמָּא נָתְנָה לְעוֹמֶר שְׁתֵּי הוֹרָאוֹת בְּרֶצֶף. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb22.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר עָקַב אַחֲרֵי שְׁתֵּי הַהוֹרָאוֹת עַד הַסּוֹף!",
    "q23.mp3": "יֵשׁ קִשּׁוּט שָׁבִיר עַל הַמַּדָּף עִם סִימָן אַל תִּגַּע. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb23.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר שׁוֹלֵט בְּעַצְמוֹ וְלֹא נוֹגֵעַ בַּקִּשּׁוּט!",
    "q24.mp3": "עוֹמֶר רָאָה חִפּוּשִׂית צִבְעוֹנִית עַל עָלֶה בַּגִּנָּה. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb24.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר הִתְקָרֵב בְּסַקְרָנוּת לִבְדֹּק אֶת הַחִפּוּשִׂית!",
    "q25.mp3": "אִמָּא קָרְאָה לְעוֹמֶר סִפּוּר לִפְנֵי הַשֵּׁנָה וּבוֹ מִלָּה שֶׁהוּא לֹא מַכִּיר. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb25.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר שָׁאַל עַל הַמִּלָּה שֶׁהוּא לֹא הֵבִין!",
    "q26.mp3": "לְעוֹמֶר יֵשׁ שָׁעוֹן צַעֲצוּעַ עִם גַּלְגַּלֵּי שִׁנַּיִם נִרְאִים בִּפְנִים. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb26.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר בָּדַק בְּעִנְיָן אֵיךְ הַמַּנְגָּנוֹן עוֹבֵד!",
    "q27.mp3": "בְּמַהֲלַךְ טִיּוּל מִשְׁפַּחְתִּי עוֹמֶר רָאָה שֶׁלֶט לְיַד עֵץ עַתִּיק בַּפַּארְק. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb27.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר שָׁאַל עַל הַשֶּׁלֶט וְרָצָה לָדַעַת עוֹד!",
    "q28.mp3": "עוֹמֶר מַגִּיעַ לְמַעֲבַר חֲצִיָּה שָׁקֵט לְיַד הַבַּיִת. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb28.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר עָצַר וְהִבִּיט לִשְׁנֵי הַצְּדָדִים לִפְנֵי שֶׁחָצָה!",
    "q29.mp3": "חָבֵר הִשְׁאִיל לְעוֹמֶר עִפָּרוֹן צִבְעוֹנִי לְיוֹם אֶחָד. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb29.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר הֶחְזִיר אֶת הָעִפָּרוֹן לֶחָבֵר בַּזְּמַן וּבִשְׁלֵמוּתוֹ!",
    "q30.mp3": "לְעוֹמֶר יֵשׁ עֲבוֹדַת בַּיִת אֲרֻכָּה עִם הַרְבֵּה דַּפִּים לְהַשְׁלִים. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb30.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר הִתְמִיד עַד שֶׁסִּיֵּם אֶת כָּל הַפְּרוֹיֶקְט!",
    "q31.mp3": "עוֹמֶר מְמַלֵּא דַּף תַּרְגִּילִים בַּכִּתָּה. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb31.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר מִלֵּא אֶת הַדַּף בְּקִפְּדָנוּת וּבְנִקָּיוֹן!",
    "q32.mp3": "לְעוֹמֶר יֵשׁ רְשִׁימָה שֶׁל דְּבָרִים לָקַחַת לְבֵית הַסֵּפֶר מָחָר. מָה יַעֲשֶׂה עוֹמֶר?",
    "fb32.mp3": f"{KOL} הַכָּבוֹד! עוֹמֶר אָרַז אֶת הַתִּיק לְפִי הָרְשִׁימָה בְּעַצְמוֹ!",
}

COOP = {
    # puzzle
    "coop_roy_win.mp3": f"{KOL} הכבוד רועי!",
    "coop_aba_win.mp3": f"{KOL} הכבוד אבא!",
    "coop_puzzle_victory.mp3": f"איזה יופי! הרכבנו את הפאזל יחד!",
    "coop_puzzle_err.mp3": "לא שם, בוא ננסה מקום אחר!",
    "coop_turn_roy.mp3": "רועי, בחר חלק פאזל ולחץ על המקום הנכון",
    # number war
    "numwar_roy_win.mp3": f"{KOL} הכבוד! ניצחת את אבא!",
    "numwar_aba_win.mp3": f"אבא ניצח הפעם! {KOL} הכבוד על המשחק!",
    "numwar_tie.mp3": f"תיקו! {KOL} הכבוד על המשחק!",
    "numwar_turn_roy.mp3": "תור רועי",
    "numwar_turn_aba.mp3": "תור אבא",
    # tower talk
    "towertalk_turn_roy.mp3": "תור רועי לשים קובייה",
    "towertalk_turn_aba.mp3": "תור אבא יאיר לשים קובייה",
    "towertalk_victory.mp3": f"בנינו מגדל מדהים ביחד! {KOL} הכבוד!",
    # tidy up
    "tidy_victory.mp3": f"{KOL} הכבוד! סידרנו את {KOL} החדר ביחד!",
}

# Tower blocks - one set per tower type (previously one shared set spoke castle
# texts for every tower type)
TOWER_BLOCKS = {
    "castle": ["בסיס הטירה", "חומת לבנים", "חלון המגדל", "צריח הטירה", "גג ודגל"],
    "building": ["כניסת הבניין", "קומות ראשונות", "קומות אמצעיות", "קומות עליונות", "גג הבניין"],
    "spaceship": ["מנועי החללית", "גוף החללית", "חלון החללית", "חרטום החללית", "ראש החללית"],
}
for ttype, texts in TOWER_BLOCKS.items():
    for i, t in enumerate(texts, 1):
        COOP[f"towertalk_{ttype}_block{i}.mp3"] = t

# Tidy-up dynamic instructions/errors per selected-categories combo
CAT_NAMES = {"toys": "צעצועים וחפצים", "animals": "חיות מתוקות", "fruits": "פירות טעימים"}
CAT_ORDER = ["toys", "animals", "fruits"]
for a_i in range(len(CAT_ORDER)):
    for b_i in range(a_i + 1, len(CAT_ORDER)):
        combo = [CAT_ORDER[a_i], CAT_ORDER[b_i]]
        key = "_".join(combo)
        roy_str = f"{CAT_NAMES[combo[0]]} ו{CAT_NAMES[combo[1]]}"
        aba_cat = next(c for c in CAT_ORDER if c not in combo)
        aba_str = CAT_NAMES[aba_cat]
        COOP[f"tidy_instructions_{key}.mp3"] = (
            f"בואו נעשה סדר בחדר! רועי מסדר {roy_str}, ואבא יאיר מסדר {aba_str}."
        )
        COOP[f"tidy_err_roy_{key}.mp3"] = f"זה מתאים לסל של אבא יאיר! רועי מסדר {roy_str}!"
        COOP[f"tidy_err_aba_{key}.mp3"] = f"זה מתאים לסל של רועי! אבא יאיר מסדר {aba_str}!"

# "מה מרגישים כש..." - questions + emotion answer labels
FEELWHEN = {
    "q1.mp3": "הַיְלָדִים מְשַׂחֲקִים יַחַד בַּמַּשָּׂאִית. מָה הֵם מַרְגִּישִׁים?",
    "q2.mp3": "הַיֶּלֶד גּוֹלֵשׁ בַּמַּגְלֵשָׁה בְּכֵיף. מָה הוּא מַרְגִּישׁ?",
    "q3.mp3": "אִמָּא מַקְרִיאָה סִפּוּר לַיְלָדִים. מָה הֵם מַרְגִּישִׁים?",
    "q4.mp3": "לַיֶּלֶד לֹא נִשְׁאַר כְּלוּם מֵהָעוּגִיָּה. מָה הוּא מַרְגִּישׁ?",
    "q5.mp3": "הֶחָבֵר לֹא נוֹתֵן לַיֶּלֶד לִרְאוֹת בַּטַּאבְּלֶט. מָה מַרְגִּישׁ הַיֶּלֶד שֶׁבַּצַּד?",
    "q6.mp3": "הַיֶּלֶד לֹא רוֹצֶה לָתֵת אַף קֻבִּיָּה. אֵיךְ הוּא נִרְאֶה?",
    "q7.mp3": "הַחֲבֵרִים רָבִים עַל הַצְּבָעִים. מָה הֵם מַרְגִּישִׁים?",
    "q8.mp3": "דּוֹחֲפִים אֶת הַיֶּלֶד עַל הַסֻּלָּם. מָה הוּא מַרְגִּישׁ?",
    "feel_happy.mp3": "שָׂמֵחַ",
    "feel_sad.mp3": "עָצוּב",
    "feel_angry.mp3": "כּוֹעֵס",
    "feel_scared.mp3": "מְפֻחָד",
}

# Family faces - Hebrew (from images/manifest.json nameHe)
FACES_HE = {
    "aba-yair.mp3": "אבא יאיר",
    "alin.mp3": "אלין",
    "arya-aba.mp3": "אריאה ואבא",
    "arya.mp3": "אריאה",
    "yahel.mp3": "יהל",
    "yahli.mp3": "יהלי",
    "saba.mp3": "סבא",
    "savta.mp3": "סבתא",
    "adi.mp3": "עדי",
    "roy-ohad.mp3": "רועי ואבא אוהד",
    "roy-aba-yair.mp3": "רועי ואבא יאיר",
    "roy-emily.mp3": "רועי ואמילי",
    "roy-yahli-alin.mp3": "רועי, יהלי ואלין",
    "roy-yona.mp3": "רועי ויונה",
    "roy-abas.mp3": "רועי, אבא יאיר ואוהד",
    "roy.mp3": "רועי",
    "savta-roy.mp3": "סבתא ורועי",
    "aba-savta.mp3": "אבא וסבתא",
    "aba-savta-arya.mp3": "אבא, סבתא ואריאה",
}

# Family faces - English (proper case so gTTS reads names, not letters)
FACES_EN = {
    "aba-yair.mp3": "Aba Yair",
    "alin.mp3": "Alin",
    "arya-aba.mp3": "Arya and Aba",
    "arya.mp3": "Arya",
    "yahel.mp3": "Yahel",
    "yahli.mp3": "Yahli",
    "saba.mp3": "Saba",
    "savta.mp3": "Savta",
    "adi.mp3": "Adi",
    "roy-ohad.mp3": "Roy and Ohad",
    "roy-aba-yair.mp3": "Roy and Aba Yair",
    "roy-emily.mp3": "Roy and Emily",
    "roy-yahli-alin.mp3": "Roy, Yahli and Alin",
    "roy-yona.mp3": "Roy and Yona",
    "roy-abas.mp3": "Roy, Aba Yair and Ohad",
    "roy.mp3": "Roy",
    "savta-roy.mp3": "Savta and Roy",
    "aba-savta.mp3": "Aba and Savta",
    "aba-savta-arya.mp3": "Aba, Savta and Arya",
}

# First-letter game - English words (proper case, not ALL CAPS)
FL_EN_WORDS = [
    "house", "door", "dog", "heart", "car", "snake", "elephant", "train", "horse",
    "apple", "flower", "lemon", "banana", "ball", "fish", "candle", "computer",
    "orange", "cup", "star",
]

JOBS = []  # (path, text, lang, slow)
for f, t in ROOT_HE.items():
    JOBS.append((os.path.join(AUDIO, f), t, "iw", False))
for f, t in SHARING.items():
    JOBS.append((os.path.join(AUDIO, "sharing", f), t, "iw", False))
for f, t in COOP.items():
    JOBS.append((os.path.join(AUDIO, "coop", f), t, "iw", False))
for f, t in FEELWHEN.items():
    JOBS.append((os.path.join(AUDIO, "feelwhen", f), t, "iw", False))
for f, t in FACES_HE.items():
    JOBS.append((os.path.join(AUDIO, "he", f), t, "iw", False))
for f, t in FACES_EN.items():
    JOBS.append((os.path.join(AUDIO, "en", f), t, "en", False))
for w in FL_EN_WORDS:
    JOBS.append((os.path.join(AUDIO, "firstletter", "en", f"word-{w}.mp3"), w, "en", True))

FILTER = sys.argv[1] if len(sys.argv) > 1 else None
if FILTER:
    JOBS = [j for j in JOBS
            if FILTER in os.path.relpath(j[0], AUDIO).replace("\\", "/")]
    print(f"filter '{FILTER}': {len(JOBS)} files")

failed = []
for path, text, lang, slow in JOBS:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    rel = os.path.relpath(path, AUDIO)
    for attempt in range(3):
        try:
            gTTS(text=text, lang=lang, slow=slow).save(path)
            print(f"OK  {rel}")
            break
        except Exception as e:
            print(f"RETRY {rel}: {e}")
            time.sleep(3 * (attempt + 1))
    else:
        failed.append(rel)
    time.sleep(0.4)

print(f"\nDone. {len(JOBS) - len(failed)}/{len(JOBS)} files generated.")
if failed:
    print("FAILED:", *failed, sep="\n  ")
    raise SystemExit(1)
