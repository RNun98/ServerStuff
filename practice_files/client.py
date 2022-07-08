#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import requests
from http import HTTPStatus

url = 'http://127.0.0.1:8080/upload'
files = {'ufile': open('alphabet.txt', 'rb')}

r = requests.post(url, files = files)

print(r.status_code)