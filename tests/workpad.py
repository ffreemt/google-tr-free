import requests
import js2py

# import logzero
# from logzero import logger

URL = 'http://translate.google.cn/translate_a/single'

TL = \
    """function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };"""

GEN_TOKEN = js2py.eval_js(TL)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

content = "test this and that"
from_lang = "en"
to_lang = "zh"

token = GEN_TOKEN(content)
data = dict(
    client="t",
    sl=from_lang,
    tl=to_lang,
    hl=to_lang,
    dt=["at", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t", ],
    ie="UTF-8",
    oe="UTF-8",
    clearbtn=1,
    otf=1,
    pc=1,
    srcrom=0,
    ssel=0,
    tsel=0,
    kc=2,
    tk=token,
    q=content,
)

resp = requests.get(URL, params=data, headers=HEADERS)

print(resp.ok)
print(resp)

if resp.ok:
    prin(resp.json())