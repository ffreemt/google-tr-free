# google-tr-free

Google translate for free -- local cache plus throttling. Let's hope it lasts.

### Install
* Install (pip or whatever) necessary requirements, e.g. ```
pip install requests_cache js2py``` or ```
pip -r requirements.txt```
* Drop the file google_tr.py in any folder in your PYTHONPATH (check with import sys; print(sys.path)
* or clone the repo (e.g., ```git clone git@github.com:ffreemt/google-tr-free.git``` or download https://github.com/ffreemt/google-tr-free/archive/master.zip and unzip) and change to the google-tr-free folder and do a ```
python setup.py develop```

### Usage

```
from google_tr import google_tr
print(google_tr('hello world'))  # ->'你好，世界'
print(google_tr('hello world', to_lang='de'))  # ->'Hallo Welt'
print(google_tr('hello world', to_lang='fr'))  # ->'Bonjour le monde'
print(google_tr('hello world', to_lang='ja'))  # ->'こんにちは世界'
```

### Acknowledgments

* Thanks to everyone whose code was used
