#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def sendNotify(successful):
    url = "https://notify-api.line.me/api/notify"
    token = "アクセストークン"
    headers = {"Authorization" : "Bearer "+ token}

    message = successful
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)