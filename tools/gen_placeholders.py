import os
import math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = os.path.join(ROOT, "photos", "coloring-books")
PAGES = os.path.join(ROOT, "photos", "coloring-pages")

LINE = 'fill="white" stroke="black" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"'
INK = 'fill="none" stroke="black" stroke-width="3"'


def write(path, inner):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    body = '<rect width="400" height="500" fill="#ffffff" stroke="none"></rect>\n' + inner
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="400" height="500">\n' + body + '\n</svg>\n'
    with open(path, "w") as f:
        f.write(svg)


def sparkle(cx, cy, r=9, stroke="black", width="3"):
    return '<path d="M{} {} v{} M{} {} h{}" stroke="{}" stroke-width="{}" fill="none"/>'.format(
        cx, cy - r, r * 2, cx - r, cy, r * 2, stroke, width)


def star_path(cx, cy, outer, inner):
    pts = []
    for i in range(10):
        r = outer if i % 2 == 0 else inner
        a = math.pi / 2 + i * math.pi / 5
        pts.append("{:.1f},{:.1f}".format(cx + r * math.cos(a), cy - r * math.sin(a)))
    return "M" + " L".join(pts) + " Z"


def rocket():
    e = []
    e.append('<path d="M200 62 L188 84 Q200 78 212 84 Z" {}></path>'.format(LINE))
    e.append('<ellipse cx="200" cy="215" rx="52" ry="140" {}></ellipse>'.format(LINE))
    e.append('<path d="M148 158 L116 248 L163 214 Z" {}></path>'.format(LINE))
    e.append('<path d="M252 158 L284 248 L237 214 Z" {}></path>'.format(LINE))
    e.append('<circle cx="200" cy="142" r="22" {}></circle>'.format(LINE))
    e.append('<circle cx="209" cy="133" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<path d="M178 348 Q162 402 148 436 M200 354 Q200 410 200 442 M222 348 Q238 402 252 436" {}></path>'.format(INK))
    for x, y, r in [(70, 80, 9), (330, 70, 9), (70, 400, 9), (335, 335, 9), (330, 180, 6), (60, 250, 6), (70, 330, 6), (345, 90, 6), (55, 120, 6)]:
        e.append(sparkle(x, y, r))
    e.append('<path d="M172 268 q12 10 24 0 M172 288 q12 10 24 0" {}></path>'.format(INK))
    return "\n".join(e)


def planet():
    e = []
    e.append('<circle cx="200" cy="240" r="115" {}></circle>'.format(LINE))
    e.append('<ellipse cx="200" cy="240" rx="205" ry="62" transform="rotate(-20 200 240)" {}></ellipse>'.format(INK))
    for cx, cy, r in [(155, 220, 16), (245, 275, 14), (215, 195, 10), (265, 210, 8), (150, 300, 9)]:
        e.append('<circle cx="{}" cy="{}" r="{}" {}></circle>'.format(cx, cy, r, LINE))
        e.append('<circle cx="{}" cy="{}" r="{}" stroke="black" stroke-width="2" fill="none"></circle>'.format(cx - 5, cy - 5, 3))
    for x, y, r in [(60, 70, 9), (335, 70, 9), (340, 300, 9), (52, 320, 6), (60, 200, 6), (325, 165, 6), (230, 60, 6), (120, 120, 6)]:
        e.append(sparkle(x, y, r))
    e.append('<path d="M150 70 q7 14 14 0 M320 210 q7 14 14 0" {}></path>'.format(INK))
    return "\n".join(e)


def astronaut():
    e = []
    e.append('<rect x="270" y="205" width="46" height="98" rx="12" {}></rect>'.format(LINE))
    e.append('<path d="M296 205 L220 165" {}></path>'.format(INK))
    e.append('<circle cx="200" cy="150" r="58" {}></circle>'.format(LINE))
    e.append('<circle cx="200" cy="150" r="40" {}></circle>'.format(LINE))
    e.append('<circle cx="200" cy="150" r="30" {}></circle>'.format(INK))
    e.append('<circle cx="188" cy="144" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<circle cx="212" cy="144" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<path d="M190 162 Q200 170 210 162" {}></path>'.format(INK))
    e.append('<rect x="152" y="205" width="96" height="124" rx="30" {}></rect>'.format(LINE))
    e.append('<rect x="116" y="220" width="28" height="84" rx="14" {}></rect>'.format(LINE))
    e.append('<rect x="256" y="220" width="28" height="84" rx="14" {}></rect>'.format(LINE))
    e.append('<circle cx="130" cy="304" r="15" {}></circle>'.format(LINE))
    e.append('<circle cx="270" cy="304" r="15" {}></circle>'.format(LINE))
    e.append('<rect x="164" y="329" width="30" height="92" rx="15" {}></rect>'.format(LINE))
    e.append('<rect x="206" y="329" width="30" height="92" rx="15" {}></rect>'.format(LINE))
    e.append('<circle cx="179" cy="421" r="16" {}></circle>'.format(LINE))
    e.append('<circle cx="221" cy="421" r="16" {}></circle>'.format(LINE))
    e.append('<rect x="170" y="250" width="60" height="50" rx="10" {}></rect>'.format(LINE))
    e.append('<circle cx="185" cy="275" r="8" {}></circle>'.format(LINE))
    e.append('<circle cx="215" cy="275" r="8" {}></circle>'.format(LINE))
    e.append('<circle cx="60" cy="420" r="70" {}></circle>'.format(LINE))
    e.append('<circle cx="42" cy="408" r="12" {}></circle>'.format(LINE))
    e.append('<circle cx="78" cy="428" r="9" {}></circle>'.format(LINE))
    for x, y, r in [(335, 70, 9), (60, 80, 6), (345, 300, 6), (340, 165, 6), (70, 200, 6)]:
        e.append(sparkle(x, y, r))
    return "\n".join(e)


def fish():
    e = []
    e.append('<ellipse cx="195" cy="255" rx="100" ry="65" {}></ellipse>'.format(LINE))
    e.append('<polygon points="288,255 358,203 358,307" {}></polygon>'.format(LINE))
    e.append('<circle cx="160" cy="232" r="13" {}></circle>'.format(LINE))
    e.append('<circle cx="166" cy="226" r="4" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<path d="M148 284 Q168 300 194 290" {}></path>'.format(INK))
    e.append('<path d="M232 210 Q240 255 226 298" {}></path>'.format(INK))
    e.append('<polygon points="168,198 198,128 226,198" {}></polygon>'.format(LINE))
    e.append('<polygon points="176,318 202,362 226,326" {}></polygon>'.format(LINE))
    e.append('<path d="M120 255 Q135 235 146 252" {}></path>'.format(INK))
    e.append('<path d="M172 268 q14 9 28 0 M186 290 q12 8 24 0" {}></path>'.format(INK))
    e.append('<circle cx="120" cy="120" r="8" {}></circle>'.format(LINE))
    e.append('<circle cx="96" cy="150" r="5" {}></circle>'.format(LINE))
    e.append('<circle cx="140" cy="170" r="4" {}></circle>'.format(LINE))
    e.append('<circle cx="108" cy="200" r="3" {}></circle>'.format(LINE))
    e.append('<path d="M310 330 L330 305 M350 350 L370 325" {}></path>'.format(INK))
    return "\n".join(e)


def octopus():
    e = []
    e.append('<path d="M120 300 A80 80 0 0 1 280 300 Z" {}></path>'.format(LINE))
    for i, dx in enumerate([-6, -3, 0, 3, 6]):
        x = 132 + i * 34
        e.append('<path d="M{} 300 q{} 30 0 58" {}></path>'.format(x, dx, INK))
        e.append('<circle cx="{}" cy="368" r="5" {}></circle>'.format(x, LINE))
    e.append('<circle cx="168" cy="240" r="11" {}></circle>'.format(LINE))
    e.append('<circle cx="232" cy="240" r="11" {}></circle>'.format(LINE))
    e.append('<circle cx="172" cy="236" r="4" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<circle cx="228" cy="236" r="4" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<path d="M176 276 Q200 296 224 276" {}></path>'.format(INK))
    for cx, cy in [(150, 210), (240, 205), (130, 255), (268, 250), (200, 195), (150, 275), (248, 282)]:
        e.append('<circle cx="{}" cy="{}" r="4" {}></circle>'.format(cx, cy, INK))
    e.append('<path d="M30 90 h20 M40 80 v20 M345 110 h22 M356 99 v22 M325 60 h18 M334 51 v18" {}></path>'.format(INK))
    return "\n".join(e)


def crab():
    e = []
    e.append('<ellipse cx="200" cy="250" rx="95" ry="70" {}></ellipse>'.format(LINE))
    e.append('<path d="M172 184 L160 146 M228 184 L240 146" {}></path>'.format(INK))
    e.append('<circle cx="160" cy="146" r="14" {}></circle>'.format(LINE))
    e.append('<circle cx="240" cy="146" r="14" {}></circle>'.format(LINE))
    e.append('<circle cx="160" cy="146" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<circle cx="240" cy="146" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<path d="M170 300 Q150 345 168 372 M185 310 Q178 352 196 376 M215 310 Q222 352 204 376 M230 300 Q250 345 232 372" {}></path>'.format(INK))
    e.append('<path d="M150 322 Q126 310 118 290 M232 322 Q256 310 264 290" {}></path>'.format(INK))
    e.append('<circle cx="118" cy="290" r="26" {}></circle>'.format(LINE))
    e.append('<circle cx="282" cy="290" r="26" {}></circle>'.format(LINE))
    e.append('<circle cx="98" cy="272" r="9" {}></circle>'.format(LINE))
    e.append('<circle cx="302" cy="272" r="9" {}></circle>'.format(LINE))
    e.append('<path d="M118 290 L128 304 M282 290 L272 304" {}></path>'.format(INK))
    e.append('<path d="M175 250 Q190 262 200 250 Q210 262 225 250" {}></path>'.format(INK))
    for cx, cy in [(170, 225), (230, 225), (148, 262), (252, 262)]:
        e.append('<circle cx="{}" cy="{}" r="4" {}></circle>'.format(cx, cy, INK))
    e.append(sparkle(80, 90))
    e.append(sparkle(320, 80))
    e.append('<path d="M40 180 h14 M330 160 h20" {}></path>'.format(INK))
    return "\n".join(e)


def star():
    e = []
    e.append('<path d="{}" {}></path>'.format(star_path(200, 245, 120, 52), LINE))
    e.append('<circle cx="200" cy="245" r="14" {}></circle>'.format(LINE))
    for x, y, r in [(60, 90, 9), (335, 120, 6), (70, 400, 7), (330, 380, 9), (90, 300, 5), (310, 300, 5), (60, 200, 5), (345, 220, 7)]:
        e.append(sparkle(x, y, r))
    e.append('<path d="M80 60 q8 16 16 0 M310 60 q8 16 16 0" {}></path>'.format(INK))
    return "\n".join(e)


def flower():
    e = []
    parts = []
    for i in range(8):
        a = i * math.pi / 4
        px = 200 + 78 * math.cos(a)
        py = 250 + 78 * math.sin(a)
        parts.append('<ellipse cx="{:.0f}" cy="{:.0f}" rx="34" ry="52" transform="rotate({:.0f} {:.0f} {:.0f})" {}></ellipse>'.format(px, py, math.degrees(a) + 90, px, py, LINE))
    e.append("\n".join(parts))
    e.append('<circle cx="200" cy="250" r="26" {}></circle>'.format(LINE))
    e.append('<path d="M200 328 v110" {}></path>'.format(INK))
    e.append('<path d="M200 385 Q235 375 252 340 M200 445 Q170 445 158 420" {}></path>'.format(INK))
    e.append('<circle cx="57" cy="70" r="5" {}></circle>'.format(LINE))
    e.append(sparkle(340, 70))
    e.append('<path d="M330 420 h28 M344 406 v28" {}></path>'.format(INK))
    return "\n".join(e)


def house():
    e = []
    e.append('<path d="M200 110 L104 210 L296 210 Z" {}></path>'.format(LINE))
    e.append('<rect x="116" y="210" width="168" height="160" {}></rect>'.format(LINE))
    e.append('<path d="M116 210 H80 V370 H116 M284 210 H320 V370 H284" {}></path>'.format(INK))
    e.append('<rect x="185" y="272" width="30" height="98" {}></rect>'.format(LINE))
    e.append('<circle cx="200" cy="282" r="4" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<rect x="134" y="236" width="38" height="38" {}></rect>'.format(LINE))
    e.append('<path d="M134 236 l19 19 l19 -19" {}></path>'.format(INK))
    e.append('<rect x="228" y="236" width="38" height="38" {}></rect>'.format(LINE))
    e.append('<path d="M228 236 l19 19 l19 -19" {}></path>'.format(INK))
    e.append('<rect x="218" y="126" width="26" height="52" {}></rect>'.format(LINE))
    e.append('<path d="M205 126 h52 M205 152 h52 M205 178 h52" {}></path>'.format(INK))
    e.append('<path d="M270 126 q12 -14 24 0 M294 126 q12 -14 24 0 M318 126 q12 -14 24 0" {}></path>'.format(INK))
    e.append('<path d="M60 370 h280" {}></path>'.format(INK))
    e.append('<path d="M90 60 H180 M135 15 V105" {}></path>'.format(INK))
    e.append('<circle cx="345" cy="60" r="8" {}></circle>'.format(LINE))
    return "\n".join(e)


def robot():
    e = []
    e.append('<path d="M200 58 v34" {}></path>'.format(INK))
    e.append('<circle cx="200" cy="48" r="12" {}></circle>'.format(LINE))
    e.append('<rect x="148" y="92" width="104" height="82" rx="16" {}></rect>'.format(LINE))
    e.append('<circle cx="184" cy="133" r="13" {}></circle>'.format(LINE))
    e.append('<circle cx="216" cy="133" r="13" {}></circle>'.format(LINE))
    e.append('<circle cx="184" cy="133" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<circle cx="216" cy="133" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<path d="M186 168 h28" {}></path>'.format(INK))
    e.append('<rect x="172" y="174" width="56" height="14" {}></rect>'.format(LINE))
    e.append('<rect x="176" y="188" width="48" height="14" rx="4" {}></rect>'.format(LINE))
    e.append('<rect x="146" y="202" width="108" height="112" rx="20" {}></rect>'.format(LINE))
    e.append('<circle cx="200" cy="238" r="10" {}></circle>'.format(LINE))
    e.append('<rect x="170" y="262" width="12" height="12" {}></rect>'.format(LINE))
    e.append('<rect x="218" y="262" width="12" height="12" {}></rect>'.format(LINE))
    e.append('<rect x="100" y="218" width="34" height="86" rx="17" {}></rect>'.format(LINE))
    e.append('<rect x="266" y="218" width="34" height="86" rx="17" {}></rect>'.format(LINE))
    e.append('<rect x="176" y="314" width="20" height="86" rx="10" {}></rect>'.format(LINE))
    e.append('<rect x="204" y="314" width="20" height="86" rx="10" {}></rect>'.format(LINE))
    e.append('<path d="M60 90 h20 M340 140 h16" {}></path>'.format(INK))
    e.append(sparkle(320, 80))
    e.append('<circle cx="70" cy="420" r="20" {}></circle>'.format(LINE))
    e.append('<circle cx="70" cy="420" r="8" {}></circle>'.format(LINE))
    return "\n".join(e)


def butterfly():
    e = []
    e.append('<ellipse cx="200" cy="255" rx="13" ry="85" {}></ellipse>'.format(LINE))
    e.append('<path d="M196 170 C96 128 54 192 138 252 C156 264 180 240 196 220 Z" {}></path>'.format(LINE))
    e.append('<path d="M204 170 C304 128 346 192 262 252 C244 264 220 240 204 220 Z" {}></path>'.format(LINE))
    e.append('<path d="M194 300 C104 330 84 396 160 382 C180 377 192 350 194 320 Z" {}></path>'.format(LINE))
    e.append('<path d="M206 300 C296 330 316 396 240 382 C220 377 208 350 206 320 Z" {}></path>'.format(LINE))
    e.append('<circle cx="120" cy="218" r="9" {}></circle>'.format(LINE))
    e.append('<circle cx="280" cy="218" r="9" {}></circle>'.format(LINE))
    e.append('<circle cx="112" cy="252" r="8" {}></circle>'.format(LINE))
    e.append('<circle cx="288" cy="252" r="8" {}></circle>'.format(LINE))
    e.append('<circle cx="124" cy="356" r="9" {}></circle>'.format(LINE))
    e.append('<circle cx="276" cy="356" r="9" {}></circle>'.format(LINE))
    e.append('<path d="M200 170 C196 118 210 96 250 70 M200 170 C204 118 190 96 150 70" {}></path>'.format(INK))
    e.append('<circle cx="250" cy="60" r="5" {}></circle>'.format(LINE))
    e.append('<circle cx="150" cy="60" r="5" {}></circle>'.format(LINE))
    e.append('<path d="M196 260 C200 268 200 268 204 260 M192 330 C196 338 196 338 200 330" {}></path>'.format(INK))
    e.append(sparkle(340, 80))
    e.append('<path d="M60 380 h24 M72 368 v24" {}></path>'.format(INK))
    return "\n".join(e)


def castle():
    e = []
    e.append('<path d="M70 430 h260" {}></path>'.format(INK))
    e.append('<rect x="95" y="210" width="70" height="220" {}></rect>'.format(LINE))
    e.append('<rect x="235" y="210" width="70" height="220" {}></rect>'.format(LINE))
    for rx in [95, 150, 235, 290]:
        e.append('<rect x="{}" y="196" width="15" height="22" {}></rect>'.format(rx, LINE))
    e.append('<rect x="130" y="210" width="140" height="220" {}></rect>'.format(LINE))
    e.append('<path d="M165 430 v-72 a35 35 0 0 1 70 0 v72 Z" {}></path>'.format(LINE))
    e.append('<rect x="112" y="270" width="30" height="46" {}></rect>'.format(LINE))
    e.append('<rect x="258" y="270" width="30" height="46" {}></rect>'.format(LINE))
    e.append('<path d="M130 200 l-18 -52 M272 200 l16 -52" {}></path>'.format(INK))
    e.append('<circle cx="173" cy="405" r="5" stroke="black" stroke-width="3" fill="black"></circle>')
    e.append('<path d="M130 148 l-35 0 M272 148 l35 0" {}></path>'.format(INK))
    e.append('<path d="M40 90 q10 20 20 0 M60 150 q10 20 20 0" {}></path>'.format(INK))
    e.append('<path d="M360 90 q10 20 20 0" {}></path>'.format(INK))
    e.append(sparkle(300, 70))
    e.append('<circle cx="55" cy="45" r="6" {}></circle>'.format(LINE))
    return "\n".join(e)


def space_cover():
    e = []
    e.append('<rect width="400" height="500" fill="#0d1f3d"></rect>')
    e.append('<circle cx="320" cy="80" r="3" fill="#ffffff"></circle>')
    e.append('<circle cx="60" cy="120" r="2" fill="#ffffff"></circle>')
    e.append('<circle cx="340" cy="420" r="3" fill="#ffffff"></circle>')
    e.append('<circle cx="70" cy="340" r="2" fill="#ffffff"></circle>')
    e.append('<circle cx="150" cy="60" r="2" fill="#ffffff"></circle>')
    e.append('<text x="200" y="120" text-anchor="middle" font-family="Arial, sans-serif" font-size="46" font-weight="bold" fill="#ffd54f">SPACE</text>')
    e.append('<text x="200" y="166" text-anchor="middle" font-family="Arial, sans-serif" font-size="28" font-weight="bold" letter-spacing="4" fill="#81d4fa">ADVENTURES</text>')
    e.append('<ellipse cx="200" cy="300" rx="32" ry="88" fill="#eef0f2" stroke="#1b263b" stroke-width="3"></ellipse>')
    e.append('<polygon points="168,308 138,348 176,342" fill="#ef6f6c" stroke="#1b263b" stroke-width="3"></polygon>')
    e.append('<polygon points="232,308 262,348 224,342" fill="#ef6f6c" stroke="#1b263b" stroke-width="3"></polygon>')
    e.append('<polygon points="200,388 180,424 220,424" fill="#ef6f6c" stroke="#1b263b" stroke-width="3"></polygon>')
    e.append('<circle cx="200" cy="270" r="16" fill="#66c2ff" stroke="#1b263b" stroke-width="3"></circle>')
    e.append('<path d="M200 388 Q184 418 200 448 Q216 418 200 388" fill="#ffb347"></path>')
    e.append('<text x="200" y="480" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" letter-spacing="3" fill="#9db7d6">COLORING BOOK</text>')
    return "\n".join(e)


def sea_cover():
    e = []
    e.append('<path d="M0 250 Q50 220 100 250 T200 250 T300 250 T400 250 V500 H0 Z" fill="#0b3d45"></path>')
    e.append('<rect y="0" width="400" height="250" fill="#11707f"></rect>')
    e.append('<text x="200" y="100" text-anchor="middle" font-family="Arial, sans-serif" font-size="34" font-weight="bold" fill="#ffee58">UNDER THE</text>')
    e.append('<text x="200" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-size="46" font-weight="bold" letter-spacing="6" fill="#b2ebf2">SEA</text>')
    e.append('<ellipse cx="200" cy="320" rx="95" ry="58" fill="#ffd166" stroke="#123c4a" stroke-width="3"></ellipse>')
    e.append('<polygon points="295,320 355,272 355,368" fill="#ef6f6c" stroke="#123c4a" stroke-width="3"></polygon>')
    e.append('<path d="M180 258 q-20 0 -26 22" stroke="#123c4a" stroke-width="3" fill="#ffd166"></path>')
    e.append('<circle cx="168" cy="300" r="12" fill="#ffffff" stroke="#123c4a" stroke-width="3"></circle>')
    e.append('<circle cx="172" cy="296" r="4" fill="#123c4a"></circle>')
    e.append('<path d="M176 352 q24 14 48 0" fill="none" stroke="#123c4a" stroke-width="3"></path>')
    e.append('<circle cx="80" cy="70" r="6" fill="#ffffff" opacity="0.8"></circle>')
    e.append('<circle cx="300" cy="60" r="4" fill="#ffffff" opacity="0.8"></circle>')
    e.append('<circle cx="340" cy="120" r="7" fill="#ffffff" opacity="0.8"></circle>')
    e.append('<circle cx="60" cy="190" r="4" fill="#ffffff" opacity="0.8"></circle>')
    e.append('<text x="200" y="470" text-anchor="middle" font-family="Arial, sans-serif" font-size="13" letter-spacing="3" fill="#93c5c9">COLORING BOOK</text>')
    return "\n".join(e)


PLAN = {
    BOOKS: [
        ("space", [("cover.svg", space_cover), ("page-1.svg", rocket), ("page-2.svg", planet), ("page-3.svg", astronaut)]),
        ("sea", [("cover.svg", sea_cover), ("page-1.svg", fish), ("page-2.svg", octopus), ("page-3.svg", crab)]),
    ],
    PAGES: [
        ("star.svg", star),
        ("flower.svg", flower),
        ("house.svg", house),
        ("robot.svg", robot),
        ("butterfly.svg", butterfly),
        ("castle.svg", castle),
    ],
}

for base, entries in PLAN.items():
    for name, files in entries:
        if isinstance(files, list):
            for fname, fn in files:
                write(os.path.join(base, name, fname), fn())
        else:
            write(os.path.join(base, name), files())

print("generated placeholders")