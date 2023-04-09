"""A font downloader for developers."""

import shutil
import requests
BASE_URL = "https://fonts.google.com/download?family="

def download(font_name: str):
    """Meat and balls"""
    try:
        font_name_encoded = font_name.replace(" ", "+")
        spl = font_name_encoded.split("+")
        print(spl)
        fntname = ""
        for i in spl:
            fntname += i.capitalize()
            fntname += "+"
        print(fntname[0:-1:])
        fname = font_name + ".zip"
        r = requests.get(BASE_URL+fntname[0:-1:], stream=True)
        print(r.status_code)
        with r as font:
            with open(fname, 'wb') as files:
                shutil.copyfileobj(font.raw, files)
    except Exception as e:
        print(e)
