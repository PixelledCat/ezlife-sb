# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'EzLife.py'
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import hashlib
import time
import binascii
from uuid import uuid4
import discord
import asyncio
import json
import json as jsond
import fade
import re
import aiohttp
import warnings
import ast
import requests
import art
import logging
import websockets
import datetime
import hmac
import hashlib
from werkzeug.security import check_password_hash
import yaml
from decimal import Decimal
from discord.ext import commands, tasks
from discord import Forbidden
from datetime import datetime
from datetime import timedelta
import platform
import psutil
from dateutil import parser
from dhooks import Webhook, Embed
from discord.ext import commands, tasks
from discord.errors import Forbidden, HTTPException
from discord.ext.commands import has_permissions, CheckFailure
from asyncio import sleep
import aiofiles
import math
import base64
import random
import string
import subprocess
import threading
import configparser
from bs4 import BeautifulSoup
from threading import Thread
from tasksio import TaskPool
from html import escape
from colorama import Fore, Style
def ensure_runtime_files():
    defaults = {
        'config.ini': '[EzLife]\ntoken =\nuserid =\nprefix =!\n\n[DeleteMsgWebhook]\ndeleted_logs = False\ndeletemsgwebhookurl =\n\n[SniperWebhook]\nsniperwebhookurl =\n\n[CryptoWebhook]\ncryptowebhookurl =\n\n[Misc]\nwebhookurl =\n',
        'config.json': json.dumps({'enabled': False, 'ping_webhook_url': None}, indent=4) + '\n',
        'ltc.yaml': 'apikey: ""\naddress: ""\nsignatureid: ""\n',
    }
    for filename, content in defaults.items():
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(content)
            print(f'Created {filename}')
ensure_runtime_files()
config = configparser.ConfigParser()
config.read('config.ini')
if os.name == 'nt':
    import ctypes
try:
    if os.name == 'nt':
        import win32security
    import requests
    from Crypto.Cipher import AES
    from Crypto.Hash import SHA256
    from Crypto.Util.Padding import pad, unpad
except ModuleNotFoundError:
    print('Exception when importing modules')
    print('Installing necessary modules....')
    if os.path.isfile('requirements.txt'):
        os.system('pip install -r requirements.txt')
    else:
        os.system('pip install pywin32')
        os.system('pip install pycryptodome')
        os.system('pip install requests')
    print('Modules installed!')
    time.sleep(1.5)
    os._exit(1)
try:
    s = requests.Session()
    s.get('https://google.com')
except requests.exceptions.RequestException as e:
    print(e)
    time.sleep(3)
    os._exit(1)
class api:
    name = ownerid = secret = version = hash_to_check = ''
    def __init__(self, name, ownerid, secret, version, hash_to_check):
        self.name = name
        self.ownerid = ownerid
        self.secret = secret
        self.version = version
        self.hash_to_check = hash_to_check
        self.init()
    sessionid = enckey = ''
    initialized = False
    def init(self):
        if self.sessionid != '':
            print('You\'ve already initialized!')
            time.sleep(2)
            os._exit(1)
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        self.enckey = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('init'.encode()), 'ver': encryption.encrypt(self.version, self.secret, init_iv), 'hash': self.hash_to_check, 'enckey': encryption.encrypt(self.enckey, self.secret, init_iv), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        if response == 'KeyAuth_Invalid':
            print('The application doesn\'t exist')
            os._exit(1)
        response = encryption.decrypt(response, self.secret, init_iv)
        json = jsond.loads(response)
        if json['message'] == 'invalidver':
            if json['download'] != '':
                print(f'New version available: {json["download"]}')
                print('Update manually, then restart.')
                os._exit(1)
            else:
                print('Invalid Version, Contact owner to add download link to latest app version')
                os._exit(1)
        if not json['success']:
            print(json['message'])
            os._exit(1)
        self.sessionid = json['sessionid']
        self.initialized = True
        self.__load_app_data(json['appinfo'])
    def register(self, user, password, license, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('register'.encode()), 'username': encryption.encrypt(user, self.enckey, init_iv), 'pass': encryption.encrypt(password, self.enckey, init_iv), 'key': encryption.encrypt(license, self.enckey, init_iv), 'hwid': encryption.encrypt(hwid, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            print('successfully registered')
            self.__load_user_data(json['info'])
        else:
            print(json['message'])
            os._exit(1)
    def upgrade(self, user, license):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('upgrade'.encode()), 'username': encryption.encrypt(user, self.enckey, init_iv), 'key': encryption.encrypt(license, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            print('successfully upgraded user')
            print('please restart program and login')
            time.sleep(2)
            os._exit(1)
        else:
            print(json['message'])
            os._exit(1)
    def login(self, user, password, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('login'.encode()), 'username': encryption.encrypt(user, self.enckey, init_iv), 'pass': encryption.encrypt(password, self.enckey, init_iv), 'hwid': encryption.encrypt(hwid, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            self.__load_user_data(json['info'])
            print('successfully logged in')
        else:
            print(json['message'])
            os._exit(1)
    def license(self, key, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('license'.encode()), 'key': encryption.encrypt(key, self.enckey, init_iv), 'hwid': encryption.encrypt(hwid, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            self.__load_user_data(json['info'])
            print('EzLife Access Granted')
        else:
            print(json['message'])
            os._exit(1)
    def var(self, name):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('var'.encode()), 'varid': encryption.encrypt(name, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return json['message']
        else:
            print(json['message'])
            time.sleep(5)
            os._exit(1)
    def getvar(self, var_name):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('getvar'.encode()), 'var': encryption.encrypt(var_name, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return json['response']
        else:
            print(json['message'])
            time.sleep(5)
            os._exit(1)
    def setvar(self, var_name, var_data):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('setvar'.encode()), 'var': encryption.encrypt(var_name, self.enckey, init_iv), 'data': encryption.encrypt(var_data, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return True
        else:
            print(json['message'])
            time.sleep(5)
            os._exit(1)
    def ban(self):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('ban'.encode()), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return True
        else:
            print(json['message'])
            time.sleep(5)
            os._exit(1)
    def file(self, fileid):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('file'.encode()), 'fileid': encryption.encrypt(fileid, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if not json['success']:
            print(json['message'])
            time.sleep(5)
            os._exit(1)
        return binascii.unhexlify(json['contents'])
    def webhook(self, webid, param, body='', conttype=''):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('webhook'.encode()), 'webid': encryption.encrypt(webid, self.enckey, init_iv), 'params': encryption.encrypt(param, self.enckey, init_iv), 'body': encryption.encrypt(body, self.enckey, init_iv), 'conttype': encryption.encrypt(conttype, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return json['message']
        else:
            print(json['message'])
            time.sleep(5)
            os._exit(1)
    def check(self):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('check'.encode()), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return True
        else:
            return False
    def checkblacklist(self):
        self.checkinit()
        hwid = others.get_hwid()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('checkblacklist'.encode()), 'hwid': encryption.encrypt(hwid, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return True
        else:
            return False
    def log(self, message):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('log'.encode()), 'pcuser': encryption.encrypt(os.getenv('username'), self.enckey, init_iv), 'message': encryption.encrypt(message, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        self.__do_request(post_data)
    def fetchOnline(self):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('fetchOnline'.encode()), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            if len(json['users']) == 0:
                return
            else:
                return json['users']
        else:
            return None
    def chatGet(self, channel):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('chatget'.encode()), 'channel': encryption.encrypt(channel, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return json['messages']
        else:
            return None
    def chatSend(self, message, channel):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {'type': binascii.hexlify('chatsend'.encode()), 'message': encryption.encrypt(message, self.enckey, init_iv), 'channel': encryption.encrypt(channel, self.enckey, init_iv), 'sessionid': binascii.hexlify(self.sessionid.encode()), 'name': binascii.hexlify(self.name.encode()), 'ownerid': binascii.hexlify(self.ownerid.encode()), 'init_iv': init_iv}
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)
        if json['success']:
            return True
        else:
            return False
    def checkinit(self):
        if not self.initialized:
            print('Initialize first, in order to use the functions')
            time.sleep(2)
            os._exit(1)
    def __do_request(self, post_data):
        try:
            rq_out = s.post('https://keyauth.win/api/1.0/', data=post_data, timeout=30)
            return rq_out.text
        except requests.exceptions.Timeout:
            print('Request timed out')
            return None
    class application_data_class:
        numUsers = numKeys = app_ver = customer_panel = onlineUsers = ''
    class user_data_class:
        username = ip = hwid = expires = createdate = lastlogin = subscription = subscriptions = ''
    user_data = user_data_class()
    app_data = application_data_class()
    def __load_app_data(self, data):
        self.app_data.numUsers = data['numUsers']
        self.app_data.numKeys = data['numKeys']
        self.app_data.app_ver = data['version']
        self.app_data.customer_panel = data['customerPanelLink']
        self.app_data.onlineUsers = data['numOnlineUsers']
    def __load_user_data(self, data):
        self.user_data.username = data['username']
        self.user_data.ip = data['ip']
        self.user_data.hwid = data['hwid']
        self.user_data.expires = data['subscriptions'][0]['expiry']
        self.user_data.createdate = data['createdate']
        self.user_data.lastlogin = data['lastlogin']
        self.user_data.subscription = data['subscriptions'][0]['subscription']
        self.user_data.subscriptions = data['subscriptions']
class others:
    @staticmethod
    def get_hwid():
        if platform.system() == 'Linux':
            with open('/etc/machine-id') as f:
                hwid = f.read()
                return hwid
        else:
            if platform.system() == 'Windows':
                winuser = os.getlogin()
                sid = win32security.LookupAccountName(None, winuser)[0]
                hwid = win32security.ConvertSidToStringSid(sid)
                return hwid
            else:
                if platform.system() == 'Darwin':
                    output = subprocess.Popen('ioreg -l | grep IOPlatformSerialNumber', stdout=subprocess.PIPE, shell=True).communicate()[0]
                    serial = output.decode().split('=', 1)[1].replace(' ', '')
                    hwid = serial[1:(-2)]
                    return hwid
class encryption:
    @staticmethod
    def encrypt_string(plain_text, key, iv):
        plain_text = pad(plain_text, 16)
        aes_instance = AES.new(key, AES.MODE_CBC, iv)
        raw_out = aes_instance.encrypt(plain_text)
        return binascii.hexlify(raw_out)
    @staticmethod
    def decrypt_string(cipher_text, key, iv):
        cipher_text = binascii.unhexlify(cipher_text)
        aes_instance = AES.new(key, AES.MODE_CBC, iv)
        cipher_text = aes_instance.decrypt(cipher_text)
        return unpad(cipher_text, 16)
    @staticmethod
    def encrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]
            _iv = SHA256.new(iv.encode()).hexdigest()[:16]
            return encryption.encrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
        except:
            print('Invalid Application Information. Long text is secret short text is ownerid. Name is supposed to be app name not username')
            os._exit(1)
    @staticmethod
    def decrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]
            _iv = SHA256.new(iv.encode()).hexdigest()[:16]
            return encryption.decrypt_string(message.encode(), _key.encode(), _iv.encode()).decode()
        except:
            print('Invalid Application Information. Long text is secret short text is ownerid. Name is supposed to be app name not username')
            os._exit(1)

command_prefix = config.get('EzLife', 'prefix')
bot = commands.Bot(
    command_prefix=command_prefix,
    self_bot=True,
    help_command=None,
    chunk_guilds_at_startup=False,
    guild_subscription_options=discord.GuildSubscriptionOptions.disabled(),
)
authorized_user = int(config.get('EzLife', 'userid'))
@bot.event
async def on_message(message):
    if message.author != bot.user:
        return
    else:
        await bot.process_commands(message)
def ezlife():
    def predicate(ctx):
        return ctx.author.id == authorized_user
    return commands.check(predicate) and commands.cooldown(1, 3, commands.BucketType.user)
@bot.command()
@ezlife()
async def help(ctx, *, query=None):
    prefix = command_prefix
    await ctx.message.delete()
    if not query:
        cogs = bot.cogs.keys()
        help_text = '# **EzLife**\n'
        help_text += '- ' + prefix + 'help <modules> to see cmds\n'
        for cog in cogs:
            help_text += f'_{cog}_, '
        help_text = help_text[:(-2)]
        await ctx.send(help_text, delete_after=30)
        return
    else:
        query = query.lower()
        found_cog = None
        for cog in bot.cogs:
            if query == cog.lower():
                found_cog = bot.get_cog(cog)
                break
        if not found_cog:
            await ctx.send('Module Not Found', delete_after=5)
            return
        else:
            cog_commands = found_cog.get_commands()
            help_text = f'**## EzLife {found_cog.qualified_name} Cmds**\n\n'
            for command in cog_commands:
                help_text += f'_{command.name}_, '
            help_text = help_text[:(-2)]
            await ctx.send(help_text, delete_after=30)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'### `{ctx.command.signature}`', delete_after=30)
    else:
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('### Error executing the command. Please check the cmd usage', delete_after=30)
            print(f'Error: {error}')
        else:
            await ctx.send(f'An error occurred: {error}')
@bot.command()
@ezlife()
async def allcmds(ctx):
    command_list = bot.commands
    sorted_commands = sorted(command_list, key=lambda x: x.name)
    response = '# **EzLife Cmds**\n\n'
    for command in sorted_commands:
        response += f'_{command.name}_, '
    await ctx.send(response, delete_after=30)
token = config.get('EzLife', 'token')
@bot.event
async def on_ready():
    banner = fade.purplepink('\n _____       _      _   __       \n| ____| ____| |    (_) / _|  ___ \n|  _|  |_  /| |    | || |_  / _ \\\n| |___  / / | |___ | ||  _||  __/\n|_____|/___||_____||_||_|   \\___|\n                                 \n')
    print(banner)
    print(f"{'⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝'}")
    print(f'        Logged in as: {bot.user.name}')
    print(f'        USER ID: {bot.user.id}')
    print(f"{'⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝⇝'}\n")
    print('EzLife is connected')
    print(f"{'••••••••••••••••••••••••••••••'}")
    print(f'   Username: {bot.user.name}')
    print(f'   Guilds: {len(bot.guilds)}')
    print(f'   Total Members: {sum([guild.member_count for guild in bot.guilds])}')
    print(f"{'••••••••••••••••••••••••••••••'}")
    print('Owner - P H I N X Z')
    print('Made for FUN ')
class Automsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_messages = {}
        self.auto_message_tasks = {}
        self.load_auto_messages()
        self.start_auto_messages()
    def cog_unload(self):
        for task in self.auto_message_tasks.values():
            task.cancel()
    def load_auto_messages(self):
        try:
            with open('auto_messages.json', 'r') as file:
                self.auto_messages = json.load(file)
        except FileNotFoundError:
            self.auto_messages = {}
    def save_auto_messages(self):
        with open('auto_messages.json', 'w') as file:
            json.dump(self.auto_messages, file, indent=4)
    def start_auto_messages(self):
        for message_id, data in self.auto_messages.items():
            self.auto_message_tasks[message_id] = self.bot.loop.create_task(self.send_auto_message(message_id, **data))
    async def send_auto_message(self, message_id, channel_id, content, interval, repeat):
        while True:
            channel = self.bot.get_channel(channel_id)
            if channel is not None:
                await channel.send(content)
            if not repeat:
                return
            else:
                await asyncio.sleep(interval)
    @commands.command(name='startauto', aliases=['am'], brief='Set auto message', usage='.startauto <time> <true/false> <mention.channel> <message>')
    @ezlife()
    async def startauto(self, ctx, interval: int, repeat: bool, channel: discord.TextChannel, *, content):
        message_id = str(ctx.message.id)
        channel_id = channel.id
        data = {'channel_id': channel_id, 'content': content, 'interval': interval, 'repeat': repeat}
        self.auto_messages[message_id] = data
        self.auto_message_tasks[message_id] = self.bot.loop.create_task(self.send_auto_message(message_id, **data))
        self.save_auto_messages()
        await ctx.send('Auto message scheduled', delete_after=5)
    @commands.command(name='listauto', aliases=['lam', 'listam'], brief='Show list of auto messages', usage='.listauto')
    @ezlife()
    async def listauto(self, ctx):
        response = 'Scheduled Auto Messages:\n\n'
        for message_id, data in self.auto_messages.items():
            channel_id = data['channel_id']
            channel = self.bot.get_channel(channel_id)
            channel_name = channel.name if channel is not None else 'Unknown Channel'
            interval = data['interval']
            response += f'Auto Message ID: {message_id}\n'
            response += f'Channel: {channel_name}\n'
            response += f'Interval: {interval}s\n'
            if data['repeat']:
                response += 'Repeat: Yes\n'
            else:
                response += 'Repeat: No\n'
            response += '\n'
        await ctx.send(response, delete_after=30)
    @commands.command(name='stopauto', aliases=['sam', 'stopam'], brief='Stop auto message', usage='.stopauto <auto.message.id>')
    @ezlife()
    async def stopauto(self, ctx, message_id: int):
        str_message_id = str(message_id)
        if str_message_id not in self.auto_messages:
            await ctx.send('No auto message found with the specified ID')
            return
        else:
            self.auto_message_tasks[str_message_id].cancel()
            del self.auto_message_tasks[str_message_id]
            del self.auto_messages[str_message_id]
            self.save_auto_messages()
            await ctx.send('Auto message stopped', delete_after=5)
    @commands.command(name='deleteallauto', aliases=['daa', 'deleteamall'], brief='Delete all auto messages', usage='.deleteallauto')
    @ezlife()
    async def deleteallauto(self, ctx):
        self.auto_messages.clear()
        for task in self.auto_message_tasks.values():
            task.cancel()
        self.auto_message_tasks.clear()
        self.save_auto_messages()
        await ctx.send('All auto messages deleted', delete_after=5)
def setup(bot):
    bot.add_cog(Automsg(bot))
class Dump(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='alldump', usage='<channel>', description='Dump all from a channel')
    @ezlife()
    async def alldump(self, ctx, channel: discord.TextChannel):
        if not os.path.exists(f'data/dumping/all/{channel.guild.name}/{channel.name}'):
            os.makedirs(f'data/dumping/all/{channel.guild.name}/{channel.name}')
        try:
            async for message in channel.history(limit=None):
                for attachment in message.attachments:
                    r = requests.get(attachment.url, stream=True)
                    with open(f'data/dumping/all/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb') as f:
                        f.write(r.content)
            await ctx.send('Dumped all content.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='imgdump', usage='<channel>', description='Dump images from a channel')
    @ezlife()
    async def imgdump(self, ctx, channel: discord.TextChannel):
        if not os.path.exists(f'data/dumping/images/{channel.guild.name}/{channel.name}'):
            os.makedirs(f'data/dumping/images/{channel.guild.name}/{channel.name}')
        try:
            async for message in channel.history(limit=None):
                for attachment in message.attachments:
                    if attachment.url.endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        r = requests.get(attachment.url, stream=True)
                        with open(f'data/dumping/images/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb') as f:
                            f.write(r.content)
            await ctx.send('Dumped images.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='audiodump', usage='<channel>', description='Dump audio from a channel')
    @ezlife()
    async def audiodump(self, ctx, channel: discord.TextChannel):
        if not os.path.exists(f'data/dumping/audio/{channel.guild.name}/{channel.name}'):
            os.makedirs(f'data/dumping/audio/{channel.guild.name}/{channel.name}')
        try:
            async for message in channel.history(limit=None):
                for attachment in message.attachments:
                    if attachment.url.endswith('.mp3'):
                        r = requests.get(attachment.url, stream=True)
                        with open(f'data/dumping/audio/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb') as f:
                            f.write(r.content)
            await ctx.send('Dumped audio.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='videodump', usage='<channel>', description='Dump videos from a channel')
    @ezlife()
    async def videodump(self, ctx, channel: discord.TextChannel):
        if not os.path.exists(f'data/dumping/videos/{channel.guild.name}/{channel.name}'):
            os.makedirs(f'data/dumping/videos/{channel.guild.name}/{channel.name}')
        try:
            async for message in channel.history(limit=None):
                for attachment in message.attachments:
                    if attachment.url.endswith(('.mp4', '.mov')):
                        r = requests.get(attachment.url, stream=True)
                        with open(f'data/dumping/videos/{channel.guild.name}/{channel.name}/{attachment.filename}', 'wb') as f:
                            f.write(r.content)
            await ctx.send('Dumped videos.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='textdump', usage='<channel>', description='Dump text from a channel')
    @ezlife()
    async def textdump(self, ctx, channel: discord.TextChannel):
        if not os.path.exists(f'data/dumping/text/{channel.guild.name}/{channel.name}'):
            os.makedirs(f'data/dumping/text/{channel.guild.name}/{channel.name}')
        try:
            async for message in channel.history(limit=1000):
                text = f'{message.author.name}#{message.author.discriminator}: {message.content}\n'
                with open(f'data/dumping/text/{channel.guild.name}/{channel.name}/{channel.name}.txt', 'a', encoding='utf-8') as f:
                    f.write(text)
            await ctx.send('Dumped text.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='emojidump', usage='<guild>', description='Dump all emojis from a guild')
    @ezlife()
    async def emojidump(self, ctx, guild: discord.Guild):
        if not os.path.exists(f'data/dumping/emojis/{guild.name}'):
            os.makedirs(f'data/dumping/emojis/{guild.name}')
        try:
            for emoji in guild.emojis:
                url = str(emoji.url)
                name = str(emoji.name)
                r = requests.get(url, stream=True)
                if '.png' in url:
                    with open(f'data/dumping/emojis/{guild.name}/{name}.png', 'wb') as f:
                        f.write(r.content)
                else:
                    if '.gif' in url:
                        with open(f'data/dumping/emojis/{guild.name}/{name}.gif', 'wb') as f:
                            f.write(r.content)
            await ctx.send('Dumped emojis.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='emojidownload', usage='<guild> <emoji>', description='Download an emoji')
    @ezlife()
    async def emojidownload(self, ctx, guild: discord.Guild, emoji: discord.Emoji):
        if not os.path.exists(f'data/dumping/emojis/{guild.name}'):
            os.makedirs(f'data/dumping/emojis/{guild.name}')
        try:
            url = str(emoji.url)
            name = str(emoji.name)
            r = requests.get(url, stream=True)
            if '.png' in url:
                with open(f'data/dumping/emojis/{guild.name}/{name}.png', 'wb') as f:
                    f.write(r.content)
            else:
                if '.gif' in url:
                    with open(f'data/dumping/emojis/{guild.name}/{name}.gif', 'wb') as f:
                        f.write(r.content)
            await ctx.send('Downloaded emoji.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='avatardump', usage='<guild>', description='Dump avatars from a guild')
    @ezlife()
    async def avatardump(self, ctx, guild: discord.Guild):
        if not os.path.exists(f'data/dumping/avatars/{guild.name}'):
            os.makedirs(f'data/dumping/avatars/{guild.name}')
        try:
            for member in guild.members:
                url = str(member.avatar_url)
                name = str(member.name)
                r = requests.get(url, stream=True)
                if '.png' in url:
                    with open(f'data/dumping/avatars/{guild.name}/{name}.png', 'wb') as f:
                        f.write(r.content)
                else:
                    if '.gif' in url:
                        with open(f'data/dumping/avatars/{guild.name}/{name}.gif', 'wb') as f:
                            f.write(r.content)
            await ctx.send('Dumped avatars.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='channeldump', usage='<guild>', description='Dump channels from a guild')
    @ezlife()
    async def channeldump(self, ctx, guild: discord.Guild):
        if not os.path.exists(f'data/dumping/channels/{guild.name}'):
            os.makedirs(f'data/dumping/channels/{guild.name}')
        try:
            for channel in guild.channels:
                name = str(channel.name)
                with open(f'data/dumping/channels/{guild.name}/{name}.txt', 'w') as f:
                    f.write(name)
            await ctx.send('Dumped channel names.')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
def setup(bot):
    bot.add_cog(Dump(bot))
log = logging.getLogger('sniper')
class Sniper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_webhook_url = config.get('SniperWebhook', 'sniperwebhookurl')
        self.processed_links = set()
        self.sniper_enabled = False
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.sniper_enabled and message.author != self.bot.user:
                gift_link_pattern = re.compile('(discord\\.gift/|discord\\.com/gifts/|discordapp\\.com/gifts/)([a-zA-Z0-9]+)')
                match = gift_link_pattern.search(message.content)
                if match:
                    code = match.group(2)
                    if code in self.processed_links:
                        return
                    else:
                        await self.redeem_gift_code(code, message)
                        self.processed_links.add(code)
    @commands.command(name='togglesniper', aliases=['toggle_sniper'])
    @ezlife()
    async def toggle_sniper(self, ctx):
        self.sniper_enabled = not self.sniper_enabled
        status = 'enabled' if self.sniper_enabled else 'disabled'
        await ctx.send(f'EzLife Nitro Sniper is now {status}', delete_after=30)
    async def redeem_gift_code(self, code, message):
        async with aiohttp.ClientSession() as session:
            headers = {'authorization': self.bot.http.token, 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0', 'content-type': 'application/json'}
            async with session.post(f'https://canary.discord.com/api/v9/entitlements/gift-codes/{code}/redeem', headers=headers, json={}) as resp:
                j = await resp.json()
                log.info(f'Status: {resp.status} Nitro Redeem response: {j}')
                x = message.author.name
                xx = message.channel.name
                xxx = message.guild.name
                embed = Embed(title='EzLife Nitro Sniper', description=f'Gift Code: {code}\nResult: {j}', color=16777215)
                embed2 = Embed(title='Sniper Info', description=f'- Sniped From ~ {x}\n- Channel Name ~ {xx} \n- Server ~ {xxx}', color=16777215)
                log_webhook = Webhook(url=self.log_webhook_url)
                sexx = '@everyone'
                log_webhook.send(content=sexx, embeds=[embed, embed2])
def setup(bot):
    bot.add_cog(Sniper(bot))
class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.snipe_message = {}
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.snipe_message[message.channel.id] = message
    @commands.command(name='snipe', brief='Retrieve deleted messages', usage='.snipe')
    async def snipe(self, ctx: commands.Context):
        msg = ctx.message
        channel = ctx.channel
        try:
            message = self.snipe_message.get(channel.id)
            if message:
                clean = message.content.replace('`', '')
                snipe_content = f'```yaml\n- {message.author} | {message.created_at}\n   {clean}```'
                await msg.edit(content=snipe_content)
            else:
                await msg.edit(content='```yaml\nThere have been no recently deleted msges in the past 2 minutes```')
        except KeyError:
            await msg.edit(content='```yaml\nThere have been no recently deleted msges in the past 2 minutes```')
def setup(bot):
    bot.add_cog(Snipe(bot))
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nicknames = {}
        self.contexts = {}
        self.indexes = {}
        self.change_nicknames.start()
        self.token = config.get('EzLife', 'token')
    def cog_unload(self):
        self.change_nicknames.cancel()
    async def delete_message(self, message, delay=None):
        try:
            await message.delete(delay=delay)
        except discord.Forbidden:
            return None
    @commands.command()
    @ezlife()
    async def calc(self, ctx, *, expression):
        allowed_chars = '0123456789+-*/(). '
        if all((char in allowed_chars for char in expression)):
            try:
                result = eval(expression)
                await ctx.send(f'**{result}**', delete_after=30)
            except Exception as e:
                await ctx.send(f'Error: {e}')
        else:
            await ctx.send('Not Allowed', delete_after=5)
        await ctx.message.delete()
    @commands.command(name='nickscan', aliases=['scan'], brief='Scans for servers where I have nicknames', usage='.nickscan')
    @ezlife()
    async def nickscan(self, ctx):
        response = '**Here are the servers where I have nicknames set:**\n'
        for guild in self.bot.guilds:
            if guild.me.nick:
                response += f'Server ID: {guild.id}, Server Name: {guild.name}, Nickname: {guild.me.nick}\n'
        if response == '**Here are the servers where I have nicknames set:**\n':
            response = 'I don\'t have nicknames set in any server.'
        await ctx.send(response, delete_after=30)
        await self.delete_message(ctx.message)
    @commands.command(name='adminscan', brief='Scans for servers where I have admins', usage='.adminscan')
    @ezlife()
    async def adminscan(self, ctx):
        guilds_with_admin = [f'Server ID: {guild.id}, Server Name: {guild.name}' for guild in self.bot.guilds if guild.me.guild_permissions.administrator]
        response = '__Servers where I have admins:__\n\n' + '\n'.join(guilds_with_admin)
        await ctx.send(response, delete_after=30)
        await self.delete_message(ctx.message)
    @commands.command(name='scrape', brief='Scrapes msges in a channel', usage='.scrape <no.>')
    @ezlife()
    async def scrape(self, ctx, num_messages: int):
        messages = []
        async for message in ctx.channel.history(limit=num_messages):
            content = escape(message.content)
            timestamp = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
            messages.append(f'{message.author.name} ({timestamp}): {content}\n')
        file_name = f'scrape_{ctx.message.id}.txt'
        text_content = ''.join(reversed(messages))
        async with aiofiles.open(file_name, mode='w') as f:
            await f.write(text_content)
        await ctx.send(file=discord.File(file_name), delete_after=30)
        await self.delete_message(ctx.message)
        os.remove(file_name)
    @commands.command(name='asci', aliases=['ascii'], brief='Generate ASCII art', usage='.asci <text>')
    @ezlife()
    async def ascii(self, ctx, *, text: str):
        try:
            ascii_art = art.text2art(text)
            await ctx.send(f'```{ascii_art}```', delete_after=30)
        except Exception as e:
            await ctx.send(f'⚠️ Error generating ASCII art:\n `{str(e)}`', delete_after=30)
        await self.delete_message(ctx.message)
    @commands.command(name='massleave', aliases=['leaveserver'], brief='Leaves all servers', usage='.massleave')
    @ezlife()
    async def massleave(self, ctx):
        confirmation_message = '**~ Type ezlife to continue**'
        await ctx.send(confirmation_message)
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and (msg.content.lower() in ['ezlife', 'no'])
        try:
            message = await self.bot.wait_for('message', check=check, timeout=60)
        except TimeoutError:
            await ctx.send('Time out... Please try the cmd again.')
            return None
        if message.content.lower() == 'ezlife':
            guild_counter = len(self.bot.guilds)
            index = 0
            for guild in self.bot.guilds:
                index += 1
                if guild.owner_id == self.bot.user.id:
                    await ctx.send(f'Im the owner of {guild.name}, Seems like cant leave')
                    continue
                else:
                    try:
                        await guild.leave()
                        await ctx.send(f'[{index}/{guild_counter}] Left {guild.name}')
                        await asyncio.sleep(2)
                    except Exception as e:
                        await ctx.send(f'[{index}/{guild_counter}] Couldn\'t leave {guild.name} - {e}')
        else:
            if message.content.lower() == 'no':
                await ctx.send('Phew...')
    @commands.command(name='serverlist', aliases=['slist', 'listserver'], brief='Shows user server lists', usage='.serverlist <no.>')
    @ezlife()
    async def serverlist(self, ctx, page_number: int):
        await ctx.message.delete()
        if page_number < 1:
            await ctx.send('Page number must be at least 1.', delete_after=30)
            return
        else:
            servers = self.bot.guilds
            servers_per_page = 10
            pages = math.ceil(len(servers) / servers_per_page)
            if page_number > pages:
                await ctx.send(f'Page no. is out of range. Please enter a no. between 1 and {pages}.', delete_after=30)
                return
            else:
                start = (page_number - 1) * servers_per_page
                end = start + servers_per_page
                server_list = '\n'.join([f'{server.name} ({server.id})' for server in servers[start:end]])
                await ctx.send(f'**~ List {page_number}**\n```\n{server_list}\n```', delete_after=30)
    @commands.command(name='firstmsg', aliases=['firstm'], brief='Shows first message of channel/dm', usage='.firstmsg')
    @ezlife()
    async def firstmsg(self, ctx):
        message = await ctx.channel.history(limit=1, oldest_first=True).next()
        bot_response = await ctx.send(message.jump_url)
        await ctx.message.delete()
        await asyncio.sleep(30)
        await bot_response.delete()
    @commands.command(name='nickloop', aliases=['nnloop'], brief='Loop through different nicknames', usage='.nickloop nick1 nick2 nick3')
    @ezlife()
    async def nickloop(self, ctx, *args):
        self.nicknames[ctx.guild.id] = args
        self.contexts[ctx.guild.id] = ctx
        self.indexes[ctx.guild.id] = 0
        await ctx.send('Started the nickname loop', delete_after=5)
    @commands.command(name='stopnickname', aliases=['snnloop'], brief='Stop looping nicknames', usage='.stopnickname')
    @ezlife()
    async def stopnickloop(self, ctx):
        if ctx.guild.id in self.nicknames:
            del self.nicknames[ctx.guild.id]
            del self.contexts[ctx.guild.id]
            del self.indexes[ctx.guild.id]
            await ctx.send('Stopped the nickname loop.')
        else:
            await ctx.send('No nickname loop is currently running', delete_after=5)
    @tasks.loop(seconds=10)
    async def change_nicknames(self):
        for guild_id in list(self.nicknames.keys()):
            try:
                await self.contexts[guild_id].guild.me.edit(nick=self.nicknames[guild_id][self.indexes[guild_id]])
                self.indexes[guild_id] = (self.indexes[guild_id] + 1) % len(self.nicknames[guild_id])
            except discord.Forbidden:
                await self.contexts[guild_id].send('I do not have permission to change my nickname')
    @nickloop.error
    async def nickloop_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Try again')
    @commands.command(name='servercopy', aliases=['clone'], brief='Clones any server', usage='.servercopy')
    @ezlife()
    async def servercopy(self, ctx, destination_guild_id: int):
        try:
            source_guild = ctx.guild
            destination_guild = self.bot.get_guild(destination_guild_id)
            if destination_guild is None:
                await ctx.send('Server not found', delete_after=5)
            else:
                for channel in destination_guild.channels:
                    try:
                        await channel.delete()
                        await sleep(1)
                    except HTTPException as e:
                        await ctx.send(f'Error deleting channel {channel.name}: {e}')
                    except Forbidden:
                        await ctx.send(f'Not enough permissions to delete channel {channel.name}')
                for role in destination_guild.roles:
                    if not role.managed and role.name != '@everyone':
                        try:
                            await role.delete()
                            await sleep(1)
                        except HTTPException as e:
                            await ctx.send(f'Error deleting role {role.name}: {e}')
                        except Forbidden:
                            await ctx.send(f'Not enough permissions to delete role {role.name}')
                for role in reversed(source_guild.roles):
                    if not role.managed and role.name != '@everyone':
                        try:
                            await destination_guild.create_role(name=role.name, permissions=role.permissions, colour=role.color, hoist=role.hoist, mentionable=role.mentionable)
                            await sleep(1)
                        except HTTPException as e:
                            await ctx.send(f'Error creating role {role.name}: {e}')
                        except Forbidden:
                            await ctx.send(f'Not enough permissions to create role {role.name}')
                channels = sorted(source_guild.channels, key=lambda x: x.position)
                category_mapping = {}
                for channel in channels:
                    overwrites = {target: perm for target, perm in channel.overwrites.items() if not (isinstance(target, discord.Role) and target.managed)}
                    try:
                        if isinstance(channel, discord.CategoryChannel):
                            new_category = await destination_guild.create_category(name=channel.name, overwrites=overwrites)
                            category_mapping[channel.id] = new_category
                        else:
                            if isinstance(channel, discord.TextChannel):
                                category = category_mapping.get(channel.category_id, None)
                                await destination_guild.create_text_channel(name=channel.name, overwrites=overwrites, category=category)
                            else:
                                if isinstance(channel, discord.VoiceChannel):
                                    category = category_mapping.get(channel.category_id, None)
                                    await destination_guild.create_voice_channel(name=channel.name, overwrites=overwrites, category=category)
                        await sleep(1)
                    except HTTPException as e:
                        await ctx.send(f'Error creating channel {channel.name}: {e}')
                    except Forbidden:
                        await ctx.send(f'Not enough permissions to create channel {channel.name}')
                await destination_guild.edit(name=source_guild.name, icon=source_guild.icon)
        except Forbidden:
            await ctx.send('I dont have enough permissions to do that!', delete_after=3)
        except Exception as e:
            await ctx.send(f'An error occurred: {str(e)}')
    @commands.command(name='status', aliases=['mode'], brief='Change your activity', usage='.status <mode> <message>')
    @ezlife()
    async def status(self, ctx, activity_type: str, *, activity_message: str):
        if activity_type.lower() == 'playing':
            await self.bot.change_presence(activity=discord.Game(name=activity_message))
        else:
            if activity_type.lower() == 'streaming':
                await self.bot.change_presence(activity=discord.Streaming(name=activity_message, url='https://github.com/pixelledcat'))
            else:
                if activity_type.lower() == 'listening':
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity_message))
                else:
                    await ctx.send('Invalid Use either \"playing\", \"streaming\", or \"listening\" \n- status <mode> <message>')
        await ctx.message.delete()
    @commands.command(name='checkpromo', aliases=['promo'], brief='Check promos', usage='.checkpromo <check.promo>')
    @ezlife()
    async def checkpromo(self, ctx, *, promo_links: str):
        await ctx.message.delete()
        if not isinstance(promo_links, str):
            await ctx.send('Enter promos', delete_after=5)
            return
        else:
            links = promo_links.split('\n')
            async with aiohttp.ClientSession() as session:
                for link in links:
                    try:
                        promo_code = self.extract_promo_code(link)
                        if promo_code:
                            result = await self.check_promo(session, promo_code)
                            await ctx.send(result)
                        else:
                            await ctx.send(f'Invalid promo link: {link}')
                    except Exception as e:
                        await ctx.send(f'An error occurred while processing the link: {link}. Error: {str(e)}')
    async def check_promo(self, session, promo_code):
        url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'
        try:
            async with session.get(url) as response:
                if response.status in [200, 204, 201]:
                    data = await response.json()
                    if 'uses' in data and 'max_uses' in data and (data['uses'] == data['max_uses']):
                        return f'**~ Already Claimed: {promo_code}**'
                    elif 'expires_at' in data and 'promotion' in data and ('inbound_header_text' in data['promotion']):
                        exp_at = data['expires_at'].split('.')[0]
                        parsed = parser.parse(exp_at)
                        unix_timestamp = int(parsed.timestamp())
                        title = data['promotion']['inbound_header_text']
                        return f'**~ Valid: {promo_code}  \n~ Expires At: <t:{unix_timestamp}:R>  \n~ Offer: {title}**'
                elif response.status == 429:
                    retry_after = response.headers.get('retry-after', 'Unknown')
                    return f'Rate Limited for {retry_after} seconds'
                else:
                    return f'Invalid Code -> {promo_code}'
        except Exception as e:
            return f'An error occurred while checking the promo code: {promo_code}. Error: {str(e)}'
    def extract_promo_code(self, promo_link):
        try:
            promo_code = promo_link.split('/')[(-1)]
            return promo_code
        except Exception as e:
            return None
    @commands.command(name='hypesquad', usage='<bravery/brilliance/balance>', description='Change Hypesquad house')
    @ezlife()
    async def hypesquad(self, ctx, house: str):
        ttoken = self.token
        headers = {'Authorization': ttoken, 'Content-Type': 'application/json'}
        if house.lower() in ['bravery', 'brilliance', 'balance']:
            payload = {'house_id': {'bravery': 1, 'brilliance': 2, 'balance': 3}[house.lower()]}
            try:
                response = requests.post('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                response.raise_for_status()
                await ctx.send(f'Changed your Hypesquad house to {house.capitalize()}..', delete_after=30)
            except requests.RequestException:
                await ctx.send('Failed to change Hypesquad house', delete_after=5)
        else:
            await ctx.send('Invalid Hypesquad. Choose from bravery, brilliance, or balance', delete_after=10)
    @commands.command(name='screenshot', aliases=['ss'])
    @ezlife()
    async def screenshot(self, ctx, url):
        screenshot_key = '9be0f4'
        endpoint = 'https://api.screenshotmachine.com'
        params = {'key': screenshot_key, 'url': url, 'dimension': '1024xfull', 'format': 'png', 'cacheLimit': '0', 'timeout': '200'}
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            with open('ezlife.png', 'wb') as f:
                f.write(response.content)
            await ctx.message.delete()
            await ctx.send(file=discord.File('ezlife.png'), delete_after=30)
        except requests.exceptions.RequestException as e:
            await ctx.send('- Failed to take SS {}'.format(str(e)), delete_after=3)
        except Exception as e:
            await ctx.send('An error occurred: {}'.format(str(e)))
        finally:
            os.remove('ezlife.png')
    @commands.command(aliases=['findphoto', 'showphoto'])
    @ezlife()
    async def search(self, ctx, *, query):
        google_api_key = 'AIzaSyDVaNy89jV_K6KP-ks5pdqJR839g3iLbdo'
        search_engine_id = '47f928af66b3d4185'
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {'key': google_api_key, 'cx': search_engine_id, 'q': query, 'searchType': 'image', 'num': 1}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'items' in data and len(data['items']) > 0:
                image_url = data['items'][0]['link']
                await ctx.send(image_url, delete_after=30)
            else:
                await ctx.send('Couldnt Find', delete_after=3)
        else:
            await ctx.send('Error Occured/ Ratelimited', delete_after=3)
    @commands.command()
    @ezlife()
    async def vanity(self, ctx, vanity_url: str):
        api_url = f'https://discord.com/api/v8/invites/{vanity_url}?with_counts=true'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if 'code' in data:
                guild_id = data['guild']['id']
                guild_name = data['guild']['name']
                member_count = data['approximate_member_count']
                online_members = data['approximate_presence_count']
                guild_icon_id = data['guild'].get('icon', 'No Icon')
                if guild_icon_id:
                    guild_icon_url = f'https://cdn.discordapp.com/icons/{guild_id}/{guild_icon_id}.png'
                else:
                    guild_icon_url = 'No Icon'
                response_msg = f'- Vanity `{vanity_url}` is taken\n- Server Name: `{guild_name}`\n- ID: `{guild_id}`\n- Members: `{member_count}`\n- Online Members: `{online_members}`\n- Server Icon: [EzLife]({guild_icon_url})'
                await ctx.send(response_msg)
            else:
                await ctx.send(f'Vanity `{vanity_url}` is not taken', delete_after=8)
        else:
            if response.status_code == 404:
                await ctx.send(f'Vanity `{vanity_url}` is not taken', delete_after=7)
            else:
                await ctx.send('An error occurred while checking the vanity', delete_after=3)
def setup(bot):
    bot.add_cog(Utility(bot))
class ARs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_responses = {}
        self.load_auto_responses()
        self.is_listing_responses = False
    def cog_unload(self):
        self.save_auto_responses()
    def load_auto_responses(self):
        try:
            with open('auto_responses.json', 'r') as file:
                self.auto_responses = json.load(file)
        except FileNotFoundError:
            self.auto_responses = {}
    def save_auto_responses(self):
        with open('auto_responses.json', 'w') as file:
            json.dump(self.auto_responses, file, indent=4)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author != self.bot.user:
            return
        else:
            trigger = message.content.lower()
            if trigger in self.auto_responses:
                response = self.auto_responses[trigger]
                await message.delete()
                await message.channel.send(response)
    @commands.command(name='addar', aliases=['aa'], brief='Add auto response', usage='.addar <trigger> <response>')
    @ezlife()
    async def addar(self, ctx, trigger: str, *, response: str):
        trigger = trigger.lower()
        if trigger in self.auto_responses:
            await ctx.send('Auto response for this trigger already exists.')
            return
        else:
            self.auto_responses[trigger] = response
            self.save_auto_responses()
            await ctx.send('AR Added', delete_after=5)
    @commands.command(name='deletear', aliases=['ra', 'removear', 'delar'], brief='Remove auto response', usage='.removear <trigger>')
    @ezlife()
    async def removear(self, ctx, trigger: str):
        trigger = trigger.lower()
        if trigger not in self.auto_responses:
            await ctx.send('No AR Found', delete_after=5)
            return
        else:
            self.auto_responses.pop(trigger)
            self.save_auto_responses()
            await ctx.send('AR Deleted', delete_after=5)
    @commands.command(name='listar', aliases=['la'], brief='List all auto responses', usage='.listar')
    @ezlife()
    async def listauto(self, ctx):
        self.is_listing_responses = True
        response = 'Auto Responses:\n\n'
        for trigger, response_text in self.auto_responses.items():
            response += f'**Trigger**: {trigger}\n'
            response += f'**Response**: `{response_text}`\n\n'
        await ctx.send(response, delete_after=5)
        self.is_listing_responses = False
def setup(bot):
    bot.add_cog(ARs(bot))
rate_limits = {}
warnings.filterwarnings('ignore', category=DeprecationWarning)
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.forced_nicks = {}
        self.token = config.get('EzLife', 'token')
        self.bot.session = aiohttp.ClientSession()
    @commands.command(name='savebans', aliases=['saveban'], brief='Save bans list', usage='.saveban <any.name>')
    @ezlife()
    async def savebans(self, ctx, file_name):
        try:
            ban_list = await ctx.guild.bans()
            data = []
            for entry in ban_list:
                data.append({'id': entry.user.id, 'reason': str(entry.reason)})
            with open(f'{file_name}.json', 'w') as f:
                json.dump(data, f)
            await ctx.send(f'Ban list has been saved to {file_name}.json')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')
    @commands.command(name='exportbans', aliases=['exportban'], brief='Export bans list', usage='.exportban <filename>')
    @commands.has_permissions(ban_members=True)
    @ezlife()
    async def exportbans(self, ctx, file_name):
        try:
            if not os.path.isfile(f'{file_name}.json'):
                await ctx.send(f'File {file_name}.json does not exist.')
                return
            with open(f'{file_name}.json', 'r') as f:
                ban_list = json.load(f)
            async with aiohttp.ClientSession() as session:
                for ban_entry in ban_list:
                    user_id = ban_entry['id']
                    if user_id in rate_limits and rate_limits[user_id] > datetime.now():
                        await asyncio.sleep((rate_limits[user_id] - datetime.now()).total_seconds())
                    try:
                        async with session.get(f'https://discord.com/api/v10/users/{user_id}') as response:
                            if response.status == 429:
                                retry_after = int(response.headers.get('Retry-After'))
                                rate_limits[user_id] = datetime.now() + timedelta(seconds=retry_after)
                                await asyncio.sleep(retry_after)
                                continue
                            user_data = await response.json()
                        user = self.bot.get_user(user_id)
                        if user is None:
                            user = await self.bot.fetch_user(user_id)
                        await ctx.guild.ban(user, reason=ban_entry['reason'])
                    except Exception as e:
                        await ctx.send(f'An unexpected error occurred: {e}', delete_after=30)
            await ctx.send(f'Ban list has been imported from {file_name}.json', delete_after=30)
        except Exception as e:
            await ctx.send(f'An unexpected error occurred: {e}')
    @commands.command(name='nuke', aliases=['fuckchannel'], brief='Instant nuke the channel', usage='.nuke')
    @ezlife()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, channel: discord.TextChannel=None):
        if channel is None:
            channel = ctx.channel
        new_channel = await channel.clone()
        await new_channel.edit(position=channel.position)
        await channel.delete()
        await new_channel.send(f'**Nuked by {ctx.author.name}**')
    @commands.command(name='forcenick', aliases=['fucknick', 'fn'], brief='Force a users nickname', usage='.forcenick <mention.user> <nick.name>')
    @ezlife()
    async def forcenick(self, ctx, user: discord.Member, *, nickname: str):
        self.forced_nicks[user.id] = nickname
        try:
            await user.edit(nick=nickname)
            await ctx.send(f'Fucked nickname \'{nickname}\' on {user.display_name}.')
        except discord.Forbidden:
            await ctx.send('I dont have perms to edit nn')
    @commands.command(name='stopforcenick', aliases=['sfn', 'stopfucknick'], brief='Stop force kicking the user', usage='.stopforcenick <mention.user>')
    @ezlife()
    async def stopforcenick(self, ctx, user: discord.Member):
        if user.id in self.forced_nicks:
            del self.forced_nicks[user.id]
            try:
                await user.edit(nick=None)
                await ctx.send(f'Stopped fucking nickname on {user.display_name}.')
            except discord.Forbidden:
                await ctx.send('I dont have perms to edit nn')
        else:
            await ctx.send(f'No forced nickname found for {user.display_name}.')
    @commands.command(name='kick', usage='<@member> [reason]', description='Kick a user')
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @ezlife()
    async def kick(self, ctx, user: discord.Member, *, reason: str=None):
        await user.kick(reason=reason)
        await ctx.send(f'- {user.name} has been kicked.\nReason~ {reason}')
    @commands.command(name='softban', usage='<@member> [reason]', description='Softban a user')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @ezlife()
    async def softban(self, ctx, user: discord.Member, *, reason: str=None):
        await user.ban(reason=reason)
        await user.unban()
        await ctx.send(f'- {user.name} has been softbanned.\nReason~ {reason}', delete_after=30)
    @commands.command(name='ban', aliases=['machuda', 'nikal'], usage='<@member> [reason]', description='Ban a user')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @ezlife()
    async def ban(self, ctx, user: discord.Member, *, reason: str=None):
        await user.ban(reason=reason)
        await ctx.send(f'- {user.name} has been banned.\nReason~ {reason}', delete_after=30)
    @commands.command(name='unban', usage='<user_id>', description='Unban a user')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @ezlife()
    async def unban(self, ctx, user_id: int):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.id == user_id:
                await ctx.guild.unban(user)
                await ctx.send(f'- {user.name} has been unbanned', delete_after=30)
                return
        await ctx.send(f'No banned user with the ID {user_id} was found', delete_after=30)
    async def timeout_user(self, user_id: int, guild_id: int, until):
        headers = {'Authorization': f'{self.bot.http.token}'}
        url = f'https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}'
        timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
        json = {'communication_disabled_until': timeout}
        async with self.bot.session.patch(url, json=json, headers=headers) as session:
            if session.status in range(200, 299):
                return True
            else:
                return False
    @commands.command(aliases=['tm', 'chup'])
    @ezlife()
    async def mute(self, ctx: commands.Context, member: discord.Member, until: int):
        handshake = await self.timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
        if handshake:
            await ctx.send(f'Muted for {until} mins')
        else:
            await ctx.send('Something went wrong')
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if after.id in self.forced_nicks and after.nick != self.forced_nicks[after.id]:
                try:
                    await after.edit(nick=self.forced_nicks[after.id])
                except discord.Forbidden:
                    return
    @forcenick.error
    async def forcenick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You need to have admin perms')
        else:
            if isinstance(error, commands.BadArgument):
                await ctx.send('Invalid user or nickname provided.')
            else:
                await ctx.send('An error occurred while executing the cmd')
    @stopforcenick.error
    async def stopforcenick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You need to have admin perms to use this cmd')
        else:
            if isinstance(error, commands.BadArgument):
                await ctx.send('Invalid user provided.')
            else:
                await ctx.send('An error occurred while executing the cmd')
def setup(bot):
    bot.add_cog(Admin(bot))
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.token = config.get('EzLife', 'token')
        self.mocking = False
        self.mock_user = None
    async def _spam(self, ctx, msg):
        await ctx.send(msg)
    @commands.command()
    @ezlife()
    async def spam(self, ctx, times: int, *msg):
        print('command received')
        msg = ' '.join(msg)
        async with TaskPool(1000) as pool:
            for i in range(times):
                await pool.put(self._spam(ctx, msg))
    @commands.command(name='massreact', aliases=['mreact'], brief='Mass react on last message', usage='.massreact')
    @ezlife()
    async def massreact(self, ctx):
        try:
            message = await ctx.channel.history(limit=2).flatten()
            message = message[1]
            emojis = ['❤️', '🤍', '🖤', '💜', '🔥', '💧', '💨', '🍎', '🍇', '🍓', '🍒', '🌸', '🌺', '🌹', '🌷', '🌈', '⭐', '🌟', '🌙', '☀️']
            random.shuffle(emojis)
            for emoji in emojis[:20]:
                try:
                    await message.add_reaction(emoji)
                    await asyncio.sleep(1)
                except discord.errors.HTTPException as e:
                    if 'You are being rate limited.' in str(e):
                        delay = e.retry_after
                        await asyncio.sleep(delay)
                        await message.add_reaction(emoji)
                    else:
                        raise e
        except Exception as e:
            error_message = f'An error occurred: {type(e).__name__} - {str(e)}'
            await ctx.send(error_message)
            await ctx.message.delete()
    @massreact.error
    async def massreact_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            error_message = 'Sorry, Error Occured'
            await ctx.send(error_message)
    @commands.command(name='mock')
    async def mock(self, ctx, user: discord.User):
        if self.mocking:
            await ctx.send('Already mocking. Use `mockstop` to stop mocking', delete_after=7)
            return
        else:
            def check(message):
                return message.author == user
            await ctx.message.delete()
            await ctx.send(f'Started mocking {user.mention}', delete_after=7)
            self.mocking = True
            self.mock_user = user
            while self.mocking:
                try:
                    message = await self.bot.wait_for('message', check=check, timeout=60)
                    await ctx.send(message.content)
                except asyncio.TimeoutError:
                    await ctx.send(f'Stopped mocking {user.mention}', delete_after=7)
                    self.mocking = False
                    self.mock_user = None
    @commands.command(name='mockstop')
    async def stop_mock(self, ctx):
        if not self.mocking:
            await ctx.send('Not currently mocking', delete_after=7)
            return
        else:
            await ctx.send(f'Stopped mocking {self.mock_user.mention}', delete_after=7)
            self.mocking = False
            self.mock_user = None
    @commands.command()
    @ezlife()
    async def clear(self, ctx, amount: int=0, links: bool=False):
        if not amount:
            await ctx.send('- `.clear 10 1`~ Delete 10 messages with links\n- `.clear -1`~ Delete all messages (may take time)', delete_after=15)
            return
        count = 0
        async for message in self.get_messages(ctx, amount, links):
            await message.delete()
            count += 1
            print(f"Deleted {count}/{(amount if amount > 0 else 'all')} messages.")
            await asyncio.sleep(1)
        print(f"---- EzLife Task done, deleted {count} {('message' if count == 1 else 'messages')} ----")
        await ctx.send(f'- Deleted `{count}` messages', delete_after=5)
    async def get_messages(self, ctx, amount, links):
        count = 0
        async for message in ctx.channel.history(limit=None):
            if count == amount:
                return
            else:
                if message.author != ctx.author:
                    continue
                else:
                    if links:
                        if 'http://' in message.content or 'https://' in message.content:
                            count += 1
                            yield message
                    else:
                        count += 1
                        yield message
    @commands.command()
    @ezlife()
    async def massmention(self, ctx, *, message=None):
        await ctx.message.delete()
        if len(list(ctx.guild.members)) >= 50:
            userList = list(ctx.guild.members)
            random.shuffle(userList)
            sampling = random.choices(userList, k=50)
            if message is None:
                post_message = ''
                for user in sampling:
                    post_message += user.mention
                await ctx.send(post_message)
            else:
                post_message = message + '\n\n'
                for user in sampling:
                    post_message += user.mention
                await ctx.send(post_message)
        else:
            if message is None:
                post_message = ''
                for user in list(ctx.guild.members):
                    post_message += user.mention
                await ctx.send(post_message)
            else:
                post_message = message + '\n\n'
                for user in list(ctx.guild.members):
                    post_message += user.mention
                await ctx.send(post_message)
    @commands.command(name='cum', aliases=['muth'], brief='Wanna cum?', usage='.cum')
    @ezlife()
    async def cum(self, ctx):
        await ctx.message.delete()
        message = await ctx.send('\n                :ok_hand:            :smile:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8=:punch:=D \n                 :trumpet:      :eggplant:')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                          :ok_hand:            :smiley:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8==:punch:D \n                 :trumpet:      :eggplant:  \n         ')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                          :ok_hand:            :grimacing:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8=:punch:=D \n                 :trumpet:      :eggplant:  \n         ')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                          :ok_hand:            :persevere:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8==:punch:D \n                 :trumpet:      :eggplant:   \n         ')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                          :ok_hand:            :confounded:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8=:punch:=D \n                 :trumpet:      :eggplant: \n         ')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                           :ok_hand:            :tired_face:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8==:punch:D \n                 :trumpet:      :eggplant:    \n             ')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                           :ok_hand:            :weary:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8=:punch:= D:sweat_drops:\n                 :trumpet:      :eggplant:        \n         ')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                           :ok_hand:            :dizzy_face:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8==:punch:D :sweat_drops:\n                 :trumpet:      :eggplant:                 :sweat_drops:\n         ')
        await asyncio.sleep(0.5)
        await message.edit(content='\n                           :ok_hand:            :drooling_face:\n       :eggplant: :zzz: :necktie: :eggplant: \n                       :oil:     :nose:\n                     :zap: 8==:punch:D :sweat_drops:\n                 :trumpet:      :eggplant:                 :sweat_drops:', delete_after=60)
    @commands.command(name='fakenitro', aliases=['nitro'], brief='Give nitros', usage='.fakenitro')
    @ezlife()
    async def fakenitro(self, ctx):
        nitro_code = self.generate_nitro_code()
        fake_link = f'discord.gift/{nitro_code}'
        await ctx.send(fake_link, delete_after=30)
    def generate_nitro_code(self):
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
        nitro_code = self.generate_random_string(16, characters)
        return nitro_code
    def generate_random_string(self, length, characters):
        return ''.join(random.choices(characters, k=length))
    @commands.command(name='infect', usage='[@member] <infection>', description='Animated prank message')
    @ezlife()
    async def infect(self, ctx, user: discord.Member=None, *, infection: str='trojan'):
        user = user or ctx.author
        start = await ctx.send(f'{ctx.author.mention} has started to spread {infection}')
        animation_list = (f'``[▓▓▓                    ] / {infection}-infection.exe Packing files.``', f'``[▓▓▓▓▓▓▓                ] - {infection}-infection.exe Packing files..``', f'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] {infection}-infection.exe Packing files..``', f'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {infection}-infection.exe Packing files..``', f'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {infection}-infection.exe Packing files..``', f'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {infection}-infection.exe Packing files..``', f'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] {infection}-infection.exe Packing files..``', f'``Successfully downloaded {infection}-infection.exe``', '``Injecting infection.   |``', '``Injecting infection..  /``', '``Injecting infection... -``', f'``Successfully Injected {infection}-infection.exe into {user.name}``')
        for i in animation_list:
            await asyncio.sleep(1.5)
            await start.edit(content=i)
    @commands.command(name='spamgp', usage='<delay> <amount> <@member>', aliases=['spg', 'spamghostping', 'sghostping'], description='Ghostpings')
    @ezlife()
    async def spamgp(self, ctx, delay: int=None, amount: int=None, user: discord.Member=None):
        try:
            if delay is None or amount is None or user is None:
                await ctx.send(f'Usage: {self.bot.prefix}spamghostping <delay> <amount> <@member>')
            else:
                for _ in range(amount):
                    await asyncio.sleep(delay)
                    await ctx.send(user.mention, delete_after=0)
        except Exception as e:
            await ctx.send(f'Error: {e}')
    @commands.command(name='spamdm', usage='<delay> <amount> <@user> <message>', description='DMs')
    @ezlife()
    async def spamdm(self, ctx, delay: int, amount: int, user: discord.User, *, message: str):
        try:
            for _ in range(amount):
                await asyncio.sleep(delay)
                await user.send(f'{message}')
        except Exception as e:
            await ctx.send(f'Error: {e}')
    @commands.command(name='spamrep', usage='<message_id> <amount>', aliases=['spamreport'], description='Reports')
    async def spamrep(self, ctx, message_id: str, amount: int):
        try:
            print('Spam report started...')
            for _ in range(amount):
                await asyncio.sleep(2)
                reason = 'Illegal Content'
                payload = {'message_id': message_id, 'reason': reason}
                requests.post('https://discord.com/api/v9/report', json=payload, headers={'authorization': self.token, 'user-agent': 'Mozilla/5.0'})
            print('Spam report finished')
            await ctx.send(f'- Msg **{message_id}** has been reported __{amount}__ times', delete_after=10)
        except Exception as e:
            await ctx.send(f'Error: {e}')
def setup(bot):
    bot.add_cog(Fun(bot))
class Wizz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ban_rate_limit = commands.CooldownMapping.from_cooldown(1, 10, commands.BucketType.guild)
        self.session = aiohttp.ClientSession()
        self.token = config.get('EzLife', 'token')
    def cog_unload(self):
        asyncio.create_task(self.session.close())
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        else:
            await ctx.send(f'Error: {str(error)}')
    @commands.command()
    @ezlife()
    async def randomban(self, ctx, count: int):
        if count <= 0:
            await ctx.send('- Missing Number', delete_after=5)
            return
        else:
            guild = ctx.guild
            members = list(guild.members)
            random.shuffle(members)
            banned_count = 0
            async with aiohttp.ClientSession() as session:
                tasks = []
                for member in members[:count]:
                    tasks.append(self.ban_member(session, guild, member))
                results = await asyncio.gather(*tasks)
                banned_count = sum(results)
            await ctx.send(f'Randomly banned {banned_count} mem\\s', delete_after=30)
    async def ban_member(self, session, guild, member):
        try:
            await guild.ban(member, reason='Random ban')
        except discord.Forbidden:
            return 0
        else:
            return 1
    @commands.command(name='nukechannels', aliases=['wizzc'], brief='Nukes all channel', usage='.nukechannels')
    @ezlife()
    async def nukechannels(self, ctx):
        nuked_count = 0
        failed_count = 0
        confirmation_msg = await ctx.send('you sure ? type yes')
        try:
            response = await self.bot.wait_for('message', timeout=15.0, check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
        except asyncio.TimeoutError:
            await confirmation_msg.edit(content='Command timed out. wizzing channel canceled')
            return None
        if response.content.lower() != 'yes':
            await confirmation_msg.edit(content='Wizzing channel canceled')
            return
        else:
            spinner_msg = await ctx.send('Nuking channels...')
            async with spinner_msg.channel.typing():
                for channel in ctx.guild.channels:
                    if channel.permissions_for(ctx.me).manage_channels:
                        try:
                            await channel.delete()
                            nuked_count += 1
                        except:
                            failed_count += 1
            await spinner_msg.edit(content=f'Nuked {nuked_count} channels. Failed to delete {failed_count} channels', delete_after=5)
    @nukechannels.error
    async def nukechannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('I donthave the required perms to initiate a channel delete', delete_after=30)
        else:
            await ctx.send('An error occurred while executing the channel delete', delete_after=30)
    @commands.command(name='servername', aliases=['sname'], brief='Changes server name', usage='.servername <new.name>')
    @ezlife()
    async def servername(self, ctx, new_name):
        try:
            await ctx.guild.edit(name=new_name)
            await ctx.send(f'Server name changed to {new_name}')
        except discord.Forbidden:
            await ctx.send('I do not have permission to change the server name', delete_after=5)
        except discord.HTTPException as e:
            await ctx.send(f'Failed to change server name: {str(e)}', delete_after=5)
    @commands.command(name='servericon', aliases=['spfp', 'sicon'], brief='Change server icon', usage='.servericon <image.url>')
    @ezlife()
    async def servericon(self, ctx, icon_url):
        try:
            async with self.session.get(icon_url) as response:
                if response.status == 200:
                    data = await response.read()
                    await ctx.guild.edit(icon=data)
                    await ctx.send('Server icon changed', delete_after=30)
                else:
                    await ctx.send('Failed to download the image.')
        except discord.Forbidden:
            await ctx.send('I do not have permission to change the server icon', delete_after=5)
        except discord.HTTPException as e:
            await ctx.send(f'Failed to change server icon: {str(e)}', delete_after=5)
    @commands.command()
    @ezlife()
    async def massban(self, ctx, delay: int=5, *, reason: str='Mass ban reason', member_ids: commands.Greedy[int]):
        guild = ctx.guild
        banned_count = 0
        failed_count = 0
        for member_id in member_ids:
            member = guild.get_member(member_id)
            if member:
                try:
                    await guild.ban(member, reason=reason)
                    banned_count += 1
                    await asyncio.sleep(delay)
                except discord.Forbidden:
                    failed_count += 1
                except discord.HTTPException as e:
                    print(f'An error occurred while banning {member_id}: {e}')
                    failed_count += 1
        await ctx.send(f'- Banned {banned_count} mems \n - {failed_count} bans failed', delete_after=10)
    @commands.command()
    @ezlife()
    async def massunban(self, ctx, *member_ids: int):
        guild = ctx.guild
        unbanned_count = 0
        failed_count = 0
        for member_id in member_ids:
            try:
                await guild.unban(discord.Object(id=member_id))
                unbanned_count += 1
            except discord.Forbidden:
                failed_count += 1
            except discord.HTTPException as e:
                print(f'An error occurred while unbanning {member_id}: {e}')
                failed_count += 1
        await ctx.send(f'- Unbanned {unbanned_count} members \n- {failed_count} unbans failed', delete_after=10)
    @commands.command(name='massdm', aliases=['dmall'], brief='mass dm server members', usage='.massdm <context>')
    @ezlife()
    async def dmannounce(self, ctx, *, message):
        for member in ctx.guild.members:
            if not member.bot:
                try:
                    await member.send(message)
                except:
                    print(f'Couldn\'t send DM to {member.name}')
    @commands.command(aliases=['spamch'])
    @ezlife()
    async def spamchannels(self, ctx, name, tmkc=300):
        await ctx.message.delete()
        guild = ctx.guild
        for i in range(tmkc):
            await guild.create_text_channel(name)
            await asyncio.sleep(0.25)
        await ctx.send(f'{tmkc} channels created with the name \"{name}\"')
    @commands.command()
    @ezlife()
    async def dmclean(self, ctx):
        dms = [channel for channel in self.bot.private_channels if isinstance(channel, discord.DMChannel)]
        for dms in dms:
            chid = dms.id
            api = f'https://discord.com/api/v9/channels/{chid}'
            headers = {'Authorization': self.token, 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
            response = requests.delete(api, headers=headers)
            if response.status_code == 204:
                print(f'{chid}')
            else:
                print(f'{chid}')
def setup(bot):
    bot.add_cog(Wizz(bot))
class AFK(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.afk_data = {}
        self.user_cooldowns = {}
    def save_afk_data(self):
        with open('afk_data.json', 'w') as f:
            json.dump(self.afk_data, f)
    def load_afk_data(self):
        try:
            with open('afk_data.json', 'r') as f:
                self.afk_data = json.load(f)
        except FileNotFoundError:
            self.afk_data = {}
    @commands.command()
    @ezlife()
    async def afk(self, ctx, *, reason=':)'):
        user_id = str(ctx.author.id)
        unix_timestamp = datetime.now().timestamp()
        self.afk_data[user_id] = {'reason': reason, 'timestamp': unix_timestamp}
        await ctx.send('You are now AFK..')
        self.save_afk_data()
    @commands.command()
    @ezlife()
    async def unafk(self, ctx):
        user_id = str(ctx.author.id)
        if user_id in self.afk_data:
            del self.afk_data[user_id]
            await ctx.send('You are no longer AFK')
            self.save_afk_data()
        else:
            await ctx.send('You are not AFK')
    async def ignore_user_for_duration(self, user_id, duration):
        self.user_cooldowns[user_id] = True
        await asyncio.sleep(duration)
        del self.user_cooldowns[user_id]
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            if isinstance(message.channel, discord.DMChannel):
                pass
            afk_data_copy = self.afk_data.copy()
            for user_id, data in self.afk_data.items():
                if f'<@{user_id}>' in message.content:
                    if message.author.id not in self.user_cooldowns:
                        unix_timestamp = datetime.now().timestamp()
                        response_message = f"**I** am afk since <t:{int(data['timestamp'])}:R> - **{data['reason']}**"
                        await message.channel.send(response_message)
                        await self.ignore_user_for_duration(message.author.id, 30)
                    return None
                else:
                    if message.reference and message.reference.cached_message:
                            replied_to_user = message.reference.cached_message.author
                            if str(replied_to_user.id) == user_id and message.author.id not in self.user_cooldowns:
                                    unix_timestamp = datetime.now().timestamp()
                                    response_message = f"**I** am afk since <t:{int(data['timestamp'])}:R> - **{data['reason']}**"
                                    await message.channel.send(response_message)
                                    await self.ignore_user_for_duration(message.author.id, 30)
def setup(bot):
    cog = AFK(bot)
    cog.load_afk_data()
    bot.add_cog(cog)
class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deleted_log_webhook_url = config.get('DeleteMsgWebhook', 'deletemsgwebhookurl')
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await self.log_deleted_message(message)
    async def log_deleted_message(self, message):
        logging_enabled = config.getboolean('DeleteMsgWebhook', 'deleted_logs')
        if not logging_enabled:
            return
        else:
            if message.author == self.bot.user or message.author.bot:
                return None
            else:
                if isinstance(message.channel, discord.TextChannel):
                    server = message.guild.name if message.guild else 'DM'
                    channel_name = message.channel.name
                else:
                    if isinstance(message.channel, discord.DMChannel):
                        server = 'DM'
                        channel_name = None
                log_message = f'- {message.author.name} `({message.author.id})`\n- **Server** ~ {server}\n- **Message** ~ {message.content}\n\n'
                if message.attachments:
                    attachment_urls = [a.url for a in message.attachments]
                    image_attachments = [url for url in attachment_urls if url.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
                    video_attachments = [url for url in attachment_urls if url.endswith(('.mp4', '.mov', '.avi', '.mkv', '.webm'))]
                    if image_attachments:
                        log_message += f"- **Images** ~ {', '.join(image_attachments)}\n\n"
                    if video_attachments:
                        log_message += f"- **Videos** ~ {', '.join(video_attachments)}\n\n"
                log_message += f'- **Channel** ~ <#{message.channel.id}>\n- **Channel Name** ~ {channel_name}'
                embed = Embed(title='Deleted Message', description=log_message, color=16777215, timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                thumbnail_url = str(message.author.avatar_url)
                embed.set_thumbnail(url=thumbnail_url)
                deleted_log_webhook = Webhook(url=self.deleted_log_webhook_url)
                deleted_log_webhook.send(embed=embed)
    def setup(self, bot):
        bot.add_cog(self)
def setup(bot):
    deleted_message_logger = Logs(bot)
    deleted_message_logger.setup(bot)
languages = {'en': 'English', 'es': 'Spanish', 'fr': 'French'}
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = 'a91c8e0d5897462581c0c923ada079e5'
        self.token = config.get('EzLife', 'token')
        self.log_webhook_url = config.get('Misc', 'webhookurl')
    @commands.command(name='saveuser')
    async def save_user_info(self, ctx, user: discord.User):
        user = await bot.fetch_user(user.id)
        avatar_url = f'https://cdn.discordapp.com/avatars/{user.id}/{user.avatar}.png'
        color = user.color
        color_hex = f'#{user.color.value:0>6x}'
        user_id = user.id
        creation_date = user.created_at.strftime('%Y-%m-%d %H:%M:%S')
        embed = discord.Embed(title='User Information', color=color)
        embed.set_author(name=user.display_name, icon_url=avatar_url)
        embed.add_field(name='User ID', value=user_id, inline=False)
        embed.add_field(name='Creation Date', value=creation_date, inline=False)
        embed.add_field(name='Profile Color', value=color_hex, inline=False)
        embed.add_field(name='Profile Picture', value=avatar_url, inline=False)
        embed.set_thumbnail(url=avatar_url)
        log_webhook = Webhook(url=self.log_webhook_url)
        log_webhook.send(embed=embed)
    @commands.command(name='avatar', aliases=['av', 'ava'], brief='Shows user avatar', usage='.avatar <mention.user>')
    @ezlife()
    async def avatar(self, ctx, *, member: discord.Member=None):
        if not member:
            member = ctx.author
        await ctx.send(member.avatar_url, delete_after=30)
    @commands.command(name='userinfo', usage='<@member>', description='Show user info')
    @ezlife()
    async def userinfo(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        owner_ids = {authorized_user: 'Owner Of EzLife'}
        special = owner_ids.get(user.id, '')
        date_format = '%a, %d %b %Y %I:%M %p'
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at or ctx.guild.created_at)
        role_string = ', '.join([r.name for r in user.roles][1:])
        perm_string = ', '.join([str(p[0]).replace('_', ' ').title() for p in user.guild_permissions if p[1]])
        whois = f'- User » {user.mention}\n- User info\n\n- Joined » {user.joined_at.strftime(date_format)}\n- Join position » {members.index(user) + 1}\n- Registered » {user.created_at.strftime(date_format)}\n\n- User server Info\n\n- Roles Count » {len(user.roles) - 1}\n- Roles\n\n{role_string}\n\n- Perms\n\n{perm_string}{special}'
        await ctx.send(whois, delete_after=30)
    @commands.command(name='whois', usage='[user_id]', description='User information')
    @ezlife()
    async def whois(self, ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
        r = requests.get(f'https://discord.com/api/v9/users/{user.id}', headers={'authorization': self.token, 'user-agent': 'Mozilla/5.0'}).json()
        req = await self.bot.http.request(discord.http.Route('GET', '/users/{uid}', uid=user.id))
        banner_id = req.get('banner')
        if banner_id:
            banner_url = f'https://cdn.discordapp.com/banners/{user.id}/{banner_id}'
            if not banner_url.endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                banner_url += '.png'
        else:
            banner_url = None
        response = ''.join([
            '- **EzLife Userinfo**\n\n- ',
            f"{'User':12}", ' ~ ', f'{user.name}', '#', f'{user.discriminator}',
            '\n- ', f"{'ID':12}", ' ~ ', f'{user.id}',
            '\n- ', f"{'Status':12}", ' ~ ', f'{user.status}',
            '\n- ', f"{'Bot':12}", ' ~ ', f'{user.bot}',
            '\n- ', f"{'Public Flags':12}", ' ~ ', f"{r['public_flags']}",
            '\n- ', f"{'Banner Color':12}", ' ~ ', f"{r['banner_color']}",
            '\n- ', f"{'Accent Color':12}", ' ~ ', f"{r['accent_color']}",
            '\n\n- Created at:\n - ', f'{user.created_at}',
            '\n\n- Profile Img Info\n\n- Avatar URL:\n - ', f'{user.avatar_url}',
            '\n\n- Banner URL:\n - ', f'{banner_url}',
        ])
        await ctx.send(response, delete_after=30)
    @commands.command(name='stats', aliases=['info'], brief='EzLife Stats', usage='.stats')
    @ezlife()
    async def stats(self, ctx):
        await ctx.message.delete()
        process = psutil.Process(os.getpid())
        ram_usage = process.memory_info().rss / 1048576
        cpu_usage = psutil.cpu_percent()
        total_commands = len(self.bot.commands)
        statsinfo = '# **__EzLife__**\n\n'
        statsinfo += '**• EzLife: x2\n'
        statsinfo += f'• Total Cmds: {total_commands}\n'
        statsinfo += f'• OS: {platform.system()}\n'
        statsinfo += f'• RAM Usage: {ram_usage:.2f} MB\n'
        statsinfo += f'• CPU Usage: {cpu_usage}%\n'
        statsinfo += f'• Python: {platform.python_version()}\n\n'
        statsinfo += '• Owner: [P H I N X Z](<https://github.com/pixelledcat>)\n'
        await ctx.send(statsinfo, delete_after=30)
    @commands.command(name='ping', aliases=['pong'], brief='Shows Selfbot Latency', usage='.ping')
    @ezlife()
    async def ping(self, ctx):
        await ctx.message.delete()
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'**~ {latency}ms**', delete_after=30)
    @commands.command(name='tokeninfo', aliases=['tdox'], brief='Shows token info', usage='.tokeninfo <user.token>')
    @ezlife()
    async def tokeninfo(self, ctx, _token):
        await ctx.message.delete()
        headers = {'Authorization': _token, 'Content-Type': 'application/json'}
        try:
            res = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = f'<t:{int(((int(user_id) >> 22) + 1420070400000) / 1000)}:R>'
        except KeyError:
            headers = {'Authorization': 'Bot ' + _token, 'Content-Type': 'application/json'}
            try:
                res = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers)
                res = res.json()
                user_id = res['id']
                locale = res['locale']
                avatar_id = res['avatar']
                language = languages.get(locale)
                creation_date = f'<t:{int(((int(user_id) >> 22) + 1420070400000) / 1000)}:R>'
                message = f"**~ Name: {res['username']}#{res['discriminator']}  **Token is BOT**\n~ ID: {res['id']}\n~ Email: {res['email']}\n~ Created on: {creation_date}`"
                fields = [{'name': '~ Flags', 'value': res['flags']}, {'name': '~ Lang', 'value': res['locale']}, {'name': '~ Verified', 'value': res['verified']}]
                for field in fields:
                    if field['value']:
                        message += f"\n{field['name']}: {field['value']}"
                message += f'\n~ [Avatar](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}) **'
                return await ctx.send(message)
            except KeyError:
                return await ctx.send('Invalid token', delete_after=30)
        message = f"**~ Name: {res['username']}#{res['discriminator']}\n~ ID: {res['id']}\n~ Created On: {creation_date}"
        nitro_type = 'None'
        if 'premium_type' in res:
            if res['premium_type'] == 2:
                nitro_type = 'Nitro Boost'
            elif res['premium_type'] == 3:
                nitro_type = 'Nitro Basic'
        fields = [{'name': '~ Phone', 'value': res['phone']}, {'name': '~ Flags', 'value': res['flags']}, {'name': '~ Lang', 'value': res['locale']}, {'name': '~ 2FA', 'value': res['mfa_enabled']}, {'name': '~ Verified', 'value': res['verified']}, {'name': '~ Nitro', 'value': nitro_type}]
        for field in fields:
            if field['value']:
                message += f"\n{field['name']}: {field['value']}"
        message += f'\n~ [Avatar](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}) **'
        await ctx.send(message, delete_after=30)

    @commands.command(name='iplook', aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'], brief='Looks for IP', usage='.iplook <ip.address>')
    @ezlife()
    async def iplook(self, ctx, ip):
        api_url = f'https://api.ipgeolocation.io/ipgeo?apiKey={self.api_key}&ip={ip}'
        response = requests.get(api_url)
        data = response.json()
        if 'country_name' in data:
            country = data['country_name']
            city = data['city']
            isp = data['isp']
            current_time_unix = data['time_zone']['current_time_unix']
            current_time_formatted = f'<t:{int(current_time_unix)}:f>'
            message = f'IP Lookup Results for {ip}:\n'
            message += f'Country: {country}\n'
            message += f'City: {city}\n'
            message += f'ISP: {isp}\n'
            message += f'Current Time: {current_time_formatted}\n'
            await ctx.send(message, delete_after=30)
        else:
            await ctx.send('Invalid IP address', delete_after=30)
    @commands.command(name='id', aliases=['snowflake'], brief='Shows dev id of target', usage='.id <target>')
    @ezlife()
    async def id(self, ctx, *targets):
        if not targets:
            await ctx.send(f'Your ID is: {ctx.author.id}')
            return
        else:
            for target in targets:
                if target.lower() == 'server':
                    await ctx.send('**~ ID of the server is**', delete_after=30)
                    await ctx.send(ctx.guild.id, delete_after=30)
                else:
                    if len(ctx.message.mentions) > 0:
                        for member in ctx.message.mentions:
                            await ctx.send(f'**~ ID of {member.name} is**', delete_after=30)
                            await ctx.send(member.id, delete_after=30)
                    else:
                        if len(ctx.message.channel_mentions) > 0:
                            for channel in ctx.message.channel_mentions:
                                await ctx.send(f'**~ ID of {channel.name} is**', delete_after=30)
                                await ctx.send(channel.id, delete_after=30)
                        else:
                            if len(ctx.message.role_mentions) > 0:
                                for role in ctx.message.role_mentions:
                                    await ctx.send(f'**~ ID of {role.name} role is**', delete_after=30)
                                    await ctx.send(role.id, delete_after=30)
                            else:
                                await ctx.send(f'~ Cant look for this mention: {target}', delete_after=30)
def setup(bot):
    bot.add_cog(Info(bot))
class Vc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = {}
        self.channel_id = None
    async def check_permissions(self, ctx, member: discord.Member):
        if not ctx.author.guild_permissions.move_members:
            await ctx.send('I dont have perms')
            return False
        else:
            return True
    @commands.command(name='vc247', aliases=['247'], brief='24/7 a vc', usage='.vc247 <vc.channel.id>')
    @ezlife()
    async def vc247(self, ctx, channel_id: int=None):
        await ctx.message.delete()
        if channel_id is not None:
            self.channel_id = channel_id
            channel = self.bot.get_channel(channel_id)
            if isinstance(channel, discord.VoiceChannel):
                self.vc[ctx.guild.id] = await channel.connect()
            else:
                await ctx.send('This is not a valid voice channel ID.')
        else:
            if self.vc.get(ctx.guild.id):
                await self.vc[ctx.guild.id].disconnect()
                del self.vc[ctx.guild.id]
                self.channel_id = None
    @commands.command(name='vckick', aliases=['vkick'], brief='Kicks vc user', usage='.vckick <mention.user>')
    @ezlife()
    async def vckick(self, ctx, user: discord.Member):
        await ctx.message.delete()
        if await self.check_permissions(ctx, user) and user.voice and user.voice.channel:
                    await user.move_to(None)
    @commands.command(name='vcmoveall', aliases=['moveall'], brief='Moves all users to another vc', usage='.vcmoveall <from.channel.id> <to.channel.id>')
    @ezlife()
    async def vcmoveall(self, ctx, channel1_id: int, channel2_id: int):
        await ctx.message.delete()
        channel1 = self.bot.get_channel(channel1_id)
        channel2 = self.bot.get_channel(channel2_id)
        if isinstance(channel1, discord.VoiceChannel) and isinstance(channel2, discord.VoiceChannel):
            members = channel1.members
            for member in members:
                if await self.check_permissions(ctx, member):
                    await member.move_to(channel2)
    @commands.command(name='vcmute', aliases=['stfu'], brief='Mutes a vc user', usage='.vcmute <mention.user>')
    @ezlife()
    async def vcmute(self, ctx, user: discord.Member):
        await ctx.message.delete()
        if await self.check_permissions(ctx, user) and user.voice and user.voice.channel:
                    await user.edit(mute=True)
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.vc.get(member.guild.id) is not None and member.id == config['userid'] and (before.channel is not None) and (after.channel is None):
                        channel = self.bot.get_channel(self.channel_id)
                        if channel is not None:
                            self.vc[member.guild.id] = await channel.connect()
def setup(bot):
    bot.add_cog(Vc(bot))
SUBSCRIBE_JSON_FILE = 'subscribe.json'
class Crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.supported_currencies = {'btc': 'bitcoin', 'eth': 'ethereum', 'ltc': 'litecoin', 'xrp': 'ripple', 'usdt': 'tether', 'usdc': 'usd-coin', 'doge': 'dogecoin'}
        self.subscribed_addresses = self.load_subscribed_addresses()
        self.hookie_webhook_url = config.get('CryptoWebhook', 'cryptowebhookurl')
        self.config = self.loadd_config()
    def loadd_config(self):
        try:
            with open('ltc.yaml', 'r') as file:
                config = yaml.safe_load(file)
            return config
        except FileNotFoundError:
            print('Config file not found')
            return {}
        except yaml.YAMLError as e:
            print(f'Error loading YAML config: {e}')
            return {}
    def save_subscribed_addresses(self):
        with open(SUBSCRIBE_JSON_FILE, 'w') as file:
            json.dump(self.subscribed_addresses, file)
    def load_subscribed_addresses(self):
        try:
            with open(SUBSCRIBE_JSON_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    async def get_ltc_to_usd_rate(self):
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['litecoin']['usd']
                print(f'Failed to fetch LTC to USD rate: HTTP {response.status}')
                return None
    async def send_update(self, address, transaction):
        if address in self.subscribed_addresses:
            try:
                ltc_to_usd_rate = await self.get_ltc_to_usd_rate()
                if ltc_to_usd_rate is None:
                    ltc_to_usd_rate = 0
                trans_id = transaction['txid']
                first_seen = transaction['firstSeen']
                amount_ltc = transaction['vout'][0]['value'] / 100000000.0
                amount_usd = amount_ltc * ltc_to_usd_rate
                fee_ltc = transaction['fee'] / 100000000.0
                fee_usd = fee_ltc * ltc_to_usd_rate
                embed = discord.Embed(title='New LTC Transaction Detected (Unconfirmed)', color=15132410)
                embed.add_field(name='Address', value=f'[{address}](https://blockchair.com/litecoin/address/{address})', inline=False)
                embed.add_field(name='Transaction ID', value=f'[{trans_id}](https://blockchair.com/litecoin/transaction/{trans_id})', inline=False)
                embed.add_field(name='Time First Seen', value=f'<t:{first_seen}>', inline=False)
                embed.add_field(name='Amount', value=f'${amount_usd:.3f}\n({amount_ltc:.8f} LTC)', inline=False)
                embed.add_field(name='Fee', value=f'${fee_usd:.3f}\n({fee_ltc:.8f} LTC)', inline=False)
                embed.set_footer(text='EzLife - Premium Selfbot')
                hookie = Webhook(url=self.hookie_webhook_url)
                hookie.send(embed=embed)
            except Exception as e:
                print(f'Error sending update to {address}: {str(e)}')
    async def listen_for_transactions(self, address):
        uri = 'wss://litecoinspace.org/api/v1/ws'
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({'action': 'init'}))
            await websocket.send(json.dumps({'track-address': address}))
            try:
                while True:
                    message = await websocket.recv()
                    data = json.loads(message)
                    if 'address-transactions' in data and data['address-transactions'][0]['address'] == address:
                        tx = data['address-transactions'][0]['transaction']
                        await self.send_update(address, tx)
            except websockets.exceptions.ConnectionClosed:
                pass
            except Exception as e:
                print(f'Error in listen_for_transactions: {str(e)}')
    @commands.command()
    async def ltcsubscribe(self, ctx, ltc_address):
        if ltc_address in self.subscribed_addresses:
            await ctx.send(f'You are already subscribed to updates for LTC addy: {ltc_address}', delete_after=5)
            return
        else:
            try:
                self.subscribed_addresses[ltc_address] = ctx.channel.id
                await ctx.send(f'Subscribed to updates for LTC addy: {ltc_address}', delete_after=15)
                asyncio.create_task(self.listen_for_transactions(ltc_address))
                self.save_subscribed_addresses()
            except Exception as e:
                await ctx.send(f'Failed to subscribe to updates for LTC addy: {ltc_address}', delete_after=5)
                print(f'Error: {str(e)}')
    @commands.Cog.listener()
    async def on_ready(self):
        if self.subscribed_addresses:
            for address in self.subscribed_addresses:
                asyncio.create_task(self.listen_for_transactions(address))
    async def delete_message(self, message, delay=None):
        try:
            await message.delete(delay=delay)
        except discord.Forbidden:
            return None
    def gett_ltc_price(self):
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data.get('litecoin', {}).get('usd')
        else:
            return None
    @commands.command()
    @ezlife()
    async def payltc(self, ctx, amount_usd: float, to_address: str):
        if not self.config:
            await ctx.send('ltc.yaml is not loaded')
            return
        else:
            api_key = self.config.get('apikey')
            from_address = self.config.get('address')
            signature_id = self.config.get('signatureid')
            if not signature_id:
                await ctx.send('signatureid is missing from ltc.yaml')
                return
            ltc_price = self.gett_ltc_price()
            if ltc_price is None:
                await ctx.send('- Crypto Fetch API Ratelimited')
                return
            else:
                amount_ltc = amount_usd / ltc_price
                amount_ltc = round(amount_ltc, 8)
                url = 'https://api.tatum.io/v3/litecoin/transaction'
                payload = {'fromAddress': [{'address': from_address, 'signatureId': signature_id}], 'to': [{'address': to_address, 'value': amount_ltc}], 'fee': '0.00005', 'changeAddress': from_address}
                headers = {'Content-Type': 'application/json', 'x-api-key': api_key}
                response = requests.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    tx_id = response.json().get('txId', 'N/A')
                    success_msg = f'# - Sent **${amount_usd} LTC**\n - To ~ [{to_address}](<https://blockchair.com/litecoin/address/{to_address}>)\n - TxID/Hash ~ [{tx_id}](https://blockchair.com/litecoin/transaction/{tx_id})'
                    await ctx.send(success_msg)
                else:
                    error_msg = '# - Transaction Failed \n- Invalid API/Signature ID \n- Insufficient Bal \n- Wrong Addy'
                    await ctx.send(error_msg)
    @commands.command(name='getbal', aliases=['bal', 'ltcbal'], brief='Shows User LTC Bal', usage='.getbal <ltc.addy>')
    @ezlife()
    async def getbal(self, ctx, ltcaddress: str=None):
        if ltcaddress is None:
            await ctx.send('- Please provide a LTC Address', delete_after=5)
            return
        else:
            if len(ltcaddress) not in [34, 43]:
                await ctx.reply('- The provided LTC address isnt valid', delete_after=5)
                return
            else:
                response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')
                if response.status_code != 200:
                    if response.status_code == 400:
                        await ctx.send('Invalid LTC address.')
                    else:
                        await ctx.send(f'Failed to retrieve balance. Error {response.status_code}. Please try again later', delete_after=5)
                    return None
                else:
                    data = response.json()
                    balance = data['balance'] / 100000000
                    total_balance = data['total_received'] / 100000000
                    unconfirmed_balance = data['unconfirmed_balance'] / 100000000
                    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
                    if cg_response.status_code != 200:
                        await ctx.send(f'Failed to retrieve the current price of LTC. Error {cg_response.status_code}. Please try again later', delete_after=5)
                        return
                    else:
                        usd_price = cg_response.json()['litecoin']['usd']
                        usd_balance = balance * usd_price
                        usd_total_balance = total_balance * usd_price
                        usd_unconfirmed_balance = unconfirmed_balance * usd_price
                        message = f'LTC Address: `{ltcaddress}`\n'
                        message += f'__Current LTC__ ~ **${usd_balance:.2f} USD**\n'
                        message += f'__Total LTC Received__ ~ **${usd_total_balance:.2f} USD**\n'
                        message += f'__Unconfirmed LTC__ ~ **${usd_unconfirmed_balance:.2f} USD**'
                        await ctx.send(message, delete_after=30)
                        await self.delete_message(ctx.message)
    @commands.command(name='price', aliases=['current'], brief='Shows current crypto prices', usage='.price <crypto.name>')
    @ezlife()
    async def price(self, ctx, crypto='ltc'):
        if crypto not in self.supported_currencies:
            error_message = await ctx.send(f"~ Invalid crypto \n~ Supported currencies are \n~ ***{', '.join(self.supported_currencies.keys())}***", delete_after=20)
            await ctx.message.delete()
            return
        else:
            crypto_full = self.supported_currencies[crypto]
            coingecko_url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_full}&vs_currencies=usd'
            try:
                response = requests.get(coingecko_url).json()
                price = response[crypto_full]['usd']
                price_msg = await ctx.send(f'- The current price of **{crypto}** is **__${price}__**', delete_after=30)
                await ctx.message.delete()
                await asyncio.sleep(15)
                await price_msg.delete()
            except Exception as e:
                await ctx.send('Error occurred while fetching crypto')
                print(e)
    @commands.command(name='getbtcbal', aliases=['btcbal'], brief='Shows User BTC Bal', usage='.getbtcbal <btc.addy>')
    @ezlife()
    async def getbtcbal(self, ctx, btcaddress: str=None):
        if btcaddress is None:
            await ctx.reply('- Please provide a BTC Addy', delete_after=5)
            return
        else:
            if len(btcaddress) not in [34, 43, 42]:
                await ctx.reply('- The provided BTC address isnt valid', delete_after=5)
                return
            else:
                response = requests.get(f'https://api.blockcypher.com/v1/btc/main/addrs/{btcaddress}/balance')
                if response.status_code != 200:
                    if response.status_code == 400:
                        await ctx.reply('Invalid BTC Addy')
                    else:
                        await ctx.reply(f'Failed to retrieve balance. Error {response.status_code}. Please try again later', delete_after=5)
                    return None
                else:
                    data = response.json()
                    balance = data['balance'] / 100000000
                    total_received = data['total_received'] / 100000000
                    unconfirmed_balance = data['unconfirmed_balance'] / 100000000
                    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
                    if cg_response.status_code != 200:
                        await ctx.reply(f'Failed to retrieve the current price of BTC. Error {cg_response.status_code}. Please try again later', delete_after=5)
                        return
                    else:
                        usd_price = cg_response.json()['bitcoin']['usd']
                        usd_balance = balance * usd_price
                        usd_total_received = total_received * usd_price
                        usd_unconfirmed_balance = unconfirmed_balance * usd_price
                        message = f'BTC Address: `{btcaddress}`\n'
                        message += f'__Current BTC__ ~ **${usd_balance:.2f} USD**\n'
                        message += f'__Total BTC Received__ ~ **${usd_total_received:.2f} USD**\n'
                        message += f'__Unconfirmed BTC__ ~ **${usd_unconfirmed_balance:.2f} USD**'
                        await ctx.reply(message, delete_after=30)
    @commands.command(name='getethbal', aliases=['ethbal'], brief='Shows User ETH Bal', usage='.getethbal <eth.addy>')
    @ezlife()
    async def getethbal(self, ctx, ethaddress: str=None):
        if ethaddress is None:
            await ctx.reply('Please provide an ETH address', delete_after=5)
            return
        else:
            if len(ethaddress) != 42:
                await ctx.reply('The provided ETH addy isnt valid', delete_after=5)
                return
            else:
                response = requests.get(f'https://api.blockcypher.com/v1/eth/main/addrs/{ethaddress}/balance')
                if response.status_code != 200:
                    if response.status_code == 400:
                        await ctx.reply('Invalid ETH Addy')
                    else:
                        await ctx.reply(f'Failed to retrieve balance. Error {response.status_code}. Please try again later', delete_after=5)
                    return None
                else:
                    data = response.json()
                    balance = int(data['balance']) / 1000000000000000000
                    total_received = int(data['total_received']) / 1000000000000000000
                    unconfirmed_balance = int(data['unconfirmed_balance']) / 1000000000000000000
                    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
                    if cg_response.status_code != 200:
                        await ctx.reply(f'Failed to retrieve the current price of ETH. Error {cg_response.status_code}. Please try again later', delete_after=5)
                        return
                    else:
                        usd_price = cg_response.json()['ethereum']['usd']
                        usd_balance = balance * usd_price
                        usd_total_received = total_received * usd_price
                        usd_unconfirmed_balance = unconfirmed_balance * usd_price
                        message = f'ETH Address: `{ethaddress}`\n'
                        message += f'__Current ETH__ ~ **${usd_balance:.2f} USD**\n'
                        message += f'__Total ETH Received__ ~ **${usd_total_received:.2f} USD**\n'
                        message += f'__Unconfirmed ETH__ ~ **${usd_unconfirmed_balance:.2f} USD**'
                        await ctx.reply(message, delete_after=30)
    @commands.command(name='convert', aliases=['con'], brief='Convert cryptos', usage='.convert <amt> <from> <to>')
    @ezlife()
    async def convert(self, ctx, amount: float, _from: str, _to: str):
        if _from not in self.supported_currencies or _to not in self.supported_currencies:
            error_msg = await ctx.reply(f"~ Invalid crypto \n~ Supported currencies are \n~ ***{', '.join(self.supported_currencies.keys())}***")
            await asyncio.sleep(5)
            await error_msg.delete()
            return
        else:
            _from_full = self.supported_currencies[_from]
            _to_full = self.supported_currencies[_to]
            coingecko_url = f'https://api.coingecko.com/api/v3/simple/price?ids={_from_full},{_to_full}&vs_currencies=usd'
            try:
                response = requests.get(coingecko_url).json()
                conversion_rate = response[_from_full]['usd'] / response[_to_full]['usd']
                converted_amount = amount * conversion_rate
                conversion_msg = await ctx.reply(f'{amount} {_from} = **__{converted_amount:.6f}__** {_to}', delete_after=30)
                await asyncio.sleep(30)
            except Exception as e:
                await ctx.reply('Error occurred while converting', delete_after=5)
                print(e)
def setup(bot):
    bot.add_cog(Crypto(bot))
class Nsfw(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command()
    @ezlife()
    async def nrandom(self, ctx):
        async with ctx.typing():
            headers = {'Content-type': 'application/json'}
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get('https://nekos.pro/api/irl-random') as resp:
                    if resp.status == 200:
                        image_data = await resp.json()
                        image_url = image_data['url']
                        await ctx.send(image_url)
                    else:
                        if resp.status == 429:
                            await ctx.send('~ API Ratelimited', delete_after=5)
                        else:
                            await ctx.send('~ Rare error occured while fetching some ykw', delete_after=5)
    @commands.command()
    @ezlife()
    async def ass(self, ctx):
        async with ctx.typing():
            headers = {'Content-type': 'application/json'}
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get('https://nekos.pro/api/irl-ass') as resp:
                    if resp.status == 200:
                        image_data = await resp.json()
                        image_url = image_data['url']
                        await ctx.send(image_url)
                    else:
                        if resp.status == 429:
                            await ctx.send('~ API Ratelimited', delete_after=5)
                        else:
                            await ctx.send('~ Rare error occured while fetching some ykw', delete_after=5)
    @commands.command()
    @ezlife()
    async def boobs(self, ctx):
        async with ctx.typing():
            headers = {'Content-type': 'application/json'}
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get('https://nekos.pro/api/irl-boobs') as resp:
                    if resp.status == 200:
                        image_data = await resp.json()
                        image_url = image_data['url']
                        await ctx.send(image_url)
                    else:
                        if resp.status == 429:
                            await ctx.send('~ API Ratelimited', delete_after=5)
                        else:
                            await ctx.send('~ Rare error occured while fetching some ykw', delete_after=5)
    @commands.command()
    @ezlife()
    async def pussy(self, ctx):
        async with ctx.typing():
            headers = {'Content-type': 'application/json'}
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get('https://nekos.pro/api/irl-pussy') as resp:
                    if resp.status == 200:
                        image_data = await resp.json()
                        image_url = image_data['url']
                        await ctx.send(image_url)
                    else:
                        if resp.status == 429:
                            await ctx.send('~ API Ratelimited', delete_after=5)
                        else:
                            await ctx.send('~ Rare error occured while fetching some ykw', delete_after=5)
    @commands.command()
    @ezlife()
    async def nsfwai(self, ctx):
        async with ctx.typing():
            headers = {'Content-type': 'application/json'}
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get('https://nekos.pro/api/ai') as resp:
                    if resp.status == 200:
                        image_data = await resp.json()
                        image_url = image_data['url']
                        await ctx.send(image_url)
                    else:
                        if resp.status == 429:
                            await ctx.send('~ API Ratelimited', delete_after=5)
                        else:
                            await ctx.send('~ Rare error occured while fetching some ykw', delete_after=5)
def setup(bot):
    bot.add_cog(Nsfw(bot))
class Vouch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vouch_data = self.load_data()
    def load_data(self):
        try:
            with open('vouch_data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        return data
    def save_data(self):
        with open('vouch_data.json', 'w') as f:
            json.dump(self.vouch_data, f, indent=4)
    @commands.command(name='createvouch')
    @ezlife()
    async def create_vouch(self, ctx, trigger, *vouch_format):
        if len(vouch_format) >= 2 and '{price}' in vouch_format and ('{product}' in vouch_format):
            vouch_format_str = ' '.join(vouch_format)
            self.vouch_data[trigger] = vouch_format_str
            self.save_data()
            await ctx.send(f'Trigger \'{trigger}\' created with format- {vouch_format_str}', delete_after=30)
        else:
            await ctx.send('To create a vouch trigger, use the cmd `createvouch` with the following syntax:\n`-createvouch <trigger> <vouch_format>`\n\nFor example:\n`-createvouch my_trigger Legit Got {price} for {product}`\n\nThis will create a vouch trigger named \'my_trigger\' with the format \'Legit Got {price} for {product}\'.\nYou can then use this trigger with the `-v` cmd to send vouch messages.', delete_after=30)
    @commands.command(name='v')
    @ezlife()
    async def vouch(self, ctx, trigger, *price_product):
        if trigger in self.vouch_data:
            vouch_format_str = self.vouch_data[trigger]
            price_product_str = ' '.join(price_product)
            price, product = map(str.strip, price_product_str.split(','))
            vouch_message = f"+rep {ctx.author.id} {vouch_format_str.replace('{price}', price).replace('{product}', product)}"
            await ctx.send(vouch_message)
            await ctx.message.delete()
        else:
            await ctx.send(f'Vouch trigger \'{trigger}\' not found', delete_after=30)
    @commands.command(name='showtriggers')
    @ezlife()
    async def show_triggers(self, ctx):
        triggers = list(self.vouch_data.keys())
        if triggers:
            await ctx.send(f"All Triggers\n **{', '.join(triggers)}**", delete_after=30)
        else:
            await ctx.send('No Triggers found', delete_after=30)
    @commands.command(name='showformat')
    @ezlife()
    async def show_format(self, ctx, trigger):
        if trigger in self.vouch_data:
            vouch_format_str = self.vouch_data[trigger]
            await ctx.send(f'The format for Trigger \'{trigger}\' is- \n`{vouch_format_str}`', delete_after=30)
        else:
            await ctx.send(f'Trigger \'{trigger}\' not found', delete_after=30)
    @commands.command(name='deletevouch')
    @ezlife()
    async def delete_vouch(self, ctx, trigger):
        if trigger in self.vouch_data:
            del self.vouch_data[trigger]
            self.save_data()
            await ctx.send(f'Trigger \'{trigger}\' has been deleted', delete_after=30)
        else:
            await ctx.send(f'Trigger \'{trigger}\' not found. Nothing to delete', delete_after=30)
def setup(bot):
    bot.add_cog(Vouch(bot))
apisex = 'https://discord.com/api/v8/users/@me/settings'
class RotateStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.status_list = []
        self.current_status_index = 0
        self.rotate_status_task = None
    async def save_statuses(self):
        with open('statuses.txt', 'w') as file:
            for status in self.status_list:
                file.write(f'{status}\n')
    async def load_statuses(self):
        try:
            with open('statuses.txt', 'r') as file:
                self.status_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return None
    async def change_discord_status(self, message):
        headers = {'Authorization': self.bot.http.token}
        jsonData = {'status': 'online', 'custom_status': {'text': message}}
        response = requests.patch(apisex, headers=headers, json=jsonData)
        print(response.text)
    @commands.command(name='rotatestatus', aliases=['rs'])
    @ezlife()
    async def rotate_status(self, ctx, *statuses):
        self.status_list = [status.strip() for status in ' '.join(statuses).split(',')]
        await self.save_statuses()
        await ctx.send('Status list updated', delete_after=30)
    @commands.command(name='rotatestatusstart', aliases=['rss'])
    @ezlife()
    async def rotate_status_start(self, ctx):
        if not self.rotate_status_task:
            await self.load_statuses()
            self.rotate_status_task = self.rotate_status_loop.start(ctx)
            await ctx.send('Rotating statuses started', delete_after=30)
        else:
            await ctx.send('Rotating statuses is already running', delete_after=5)
    @commands.command(name='rotatestatusstop', aliases=['rst'])
    @ezlife()
    async def rotate_status_stop(self, ctx):
        if self.rotate_status_task:
            self.rotate_status_loop.cancel()
            self.rotate_status_task = None
            await ctx.send('Rotating statuses stopped', delete_after=30)
        else:
            await ctx.send('Rotating statuses is not running', delete_after=5)
    @commands.command(name='rotatestatusclear', aliases=['rsc'])
    @ezlife()
    async def rotate_status_clear(self, ctx):
        self.status_list = []
        await self.save_statuses()
        await ctx.send('Status list cleared', delete_after=30)
    @tasks.loop(seconds=10)
    async def rotate_status_loop(self, ctx):
        if self.status_list:
            await self.change_discord_status(self.status_list[self.current_status_index])
            self.current_status_index = (self.current_status_index + 1) % len(self.status_list)
    @rotate_status_loop.before_loop
    async def before_rotate_status_loop(self):
        await self.bot.wait_until_ready()
def setup(bot):
    bot.add_cog(RotateStatus(bot))
class Pings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = 'config.json'
        self.enabled = False
        self.ping_webhook_url = self.load_webhook_url()
        self.load_config()
    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.enabled = config.get('enabled', False)
        except FileNotFoundError:
            self.save_config()
    def load_webhook_url(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                return config.get('ping_webhook_url', None)
        except FileNotFoundError:
            return None
    def save_config(self):
        config = {'enabled': self.enabled, 'ping_webhook_url': self.ping_webhook_url}
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
    @commands.command(name='togglepings')
    @ezlife()
    async def toggle_mention(self, ctx):
        self.enabled = not self.enabled
        if self.enabled and self.ping_webhook_url is None:
            await ctx.send('Pings Log is now enabled, Provide Webhook URL', delete_after=30)
            try:
                webhook_url = await self.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=30.0)
                self.ping_webhook_url = webhook_url.content.strip()
                self.save_config()
                await ctx.send('Webhook URL saved successfully', delete_after=30)
            except TimeoutError:
                self.enabled = False
                await ctx.send('Webhook Setup Failed !, Pings Log remains disabled', delete_after=30)
        else:
            self.save_config()
            await ctx.send(f"Pings Log {('enabled' if self.enabled else 'disabled')}", delete_after=30)
    async def send_mention_notification(self, mention_author, message_content, server_name, channel_name):
        embed = discord.Embed(title='Ping Detection', color=mention_author.color)
        embed.add_field(name='Extra Info', value=f'{mention_author.name} has pinged you', inline=False)
        embed.add_field(name='Server', value=server_name, inline=True)
        embed.add_field(name='Channel', value=channel_name, inline=True)
        embed.add_field(name='Msg', value=message_content, inline=False)
        embed.set_thumbnail(url=mention_author.avatar_url)
        embed.set_footer(text='EzLife')
        log_webhook = Webhook(url=self.ping_webhook_url)
        log_webhook.send(embed=embed)
    @commands.Cog.listener()
    async def on_message(self, message):
        if self.enabled and message.author.id == self.bot.user.id:
                return
        if self.enabled:
            if re.search(f'<@!?{self.bot.user.id}>', message.content) or str(self.bot.user.id) in message.content:
                server_name = message.guild.name if message.guild else 'DMS'
                channel_name = message.channel.name if message.guild else 'N/A'
                await self.send_mention_notification(message.author, message.content, server_name, channel_name)
def setup(bot):
    bot.add_cog(Pings(bot))
cog_classes = [AFK, ARs, Admin, Automsg, Crypto, Dump, Fun, Info, Logs, Nsfw, Pings, RotateStatus, Snipe, Sniper, Utility, Vc, Vouch, Wizz]
for cog_class in cog_classes:
    cog = cog_class(bot)
    bot.add_cog(cog)
try:
    bot.run(token, reconnect=True)
except discord.LoginFailure:
    print(Fore.MAGENTA + 'Couldn\'t connect, Your acc token might be invalid If it\'s not, Report to Phinxz https://discord.gg/stellar-shop' + Style.RESET_ALL)
