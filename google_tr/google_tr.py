'''
google translate for free

'''
# pylint: disable=line-too-long, broad-except

from pathlib import Path

import requests
import js2py

import requests_cache

CACHE_NAME = (Path().home() / Path(__file__).stem).as_posix()

requests_cache.configure(cache_name=CACHE_NAME, expire_after=36000)  # 10 hrs

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

SESS = requests.Session()
SESS.get(URL)


def google_tr(content, from_lang='auto', to_lang='zh-CN', cache=True):
    ''' google_tr'''
    if len(content) > 4891:
        content = content[:4891]

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

    if cache:
        try:
            resp = SESS.get(URL, params=data, headers=HEADERS)
        except Exception as exc:
            resp = str(exc)
    else:
        with requests_cache.disabled():
            try:
                resp = SESS.get(URL, params=data, headers=HEADERS)
            except Exception as exc:
                resp = str(exc)

    try:
        jdata = resp.json()
    except Exception as exc:
        jdata = str(exc)

    google_tr.json = jdata

    try:
        res = [elm for elm in jdata[0] if elm[0] or elm[1]]
    except Exception as exc:
        res = str(exc)

    google_tr.dual = res
    return ' '.join([str(elm[0]) for elm in res])


def test_0():
    ''' test 0'''
    text = \
    '''There is now some uncertainty about the future of Google News in Europe after the European Union finalized its controversial new copyright legislation.

    Google had previously showed how dramatically its search results could be affected, and warned that it may shut down the service in Europe …

    The EU Copyright Directive is well-intentioned, requiring tech giants to license the right to reproduce copyrighted material on their own websites. However, the legislation as originally proposed would have made it impossible for Google to display brief snippets and photos from news stories in its search results without paying the news sites.

    Google last month showed how its news search results would appear without photos and text excerpts, rendering the service all but useless. The company had previously said that its only option might be to shut down Google News in Europe.'''
    trtext = google_tr(text)
    assert len(google_tr.dual) == 6
    assert len(trtext) > 200
