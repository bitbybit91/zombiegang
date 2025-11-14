#!/usr/bin/env python
# -*- coding: utf-8 -*-
# r3nt0n


from config import Config

from app.components import Logger, RemoteZession, Buffer, Proxy, TelegramNotifier

#config = Config

logger = Logger(debug=Config.DEBUG)
#logger.set_level(logger.console_handler, 'DEBUG')
# logger.set_level(logger.console_handler, 'INFO')
# logger.set_level(logger.file_handler, 'DEBUG')

zession = RemoteZession()
buffer = Buffer()
proxy = Proxy()
#proxy.get_socks5_session('127.0.0.1', 9050)

# Initialize Telegram notifier
telegram = TelegramNotifier(
    bot_token=Config.TELEGRAM_BOT_TOKEN,
    chat_id=Config.TELEGRAM_CHAT_ID
)
