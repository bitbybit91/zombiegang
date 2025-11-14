#!/usr/bin/env python
# -*- coding: utf-8 -*-
# r3nt0n

import os

class Config(object):
    DEBUG = False
    #BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.getcwd()
    APP_DIR = os.path.join(BASE_DIR, 'app/')
    DATA_DIR = os.path.join(APP_DIR, 'data/')
    TEMP_DIR = os.path.join(DATA_DIR, 'tmp/')

    # used for CSRF protection in wtf-forms (hidden_tag)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # comment second condition in PRD
    # future use to local authentication operations required (enable/disable proxy)
    
    # Telegram Bot Configuration
    # To enable Telegram notifications:
    # 1. Create a bot with @BotFather on Telegram
    # 2. Get your bot token
    # 3. Get your chat ID (use @userinfobot)
    # 4. Set these environment variables or update them here
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
    
    # Tor Configuration for v3 hidden services
    # Default Tor SOCKS proxy port
    TOR_SOCKS_PORT = int(os.environ.get('TOR_SOCKS_PORT', '9050'))
    TOR_SOCKS_HOST = os.environ.get('TOR_SOCKS_HOST', '127.0.0.1')
