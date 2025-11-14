#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Telegram notification system for zombiegang

import asyncio
import threading
from typing import Optional
from datetime import datetime


class TelegramNotifier:
    """
    Telegram notification system for zombiegang events.
    Sends notifications about zombie connections, task completions, and errors.
    """
    
    def __init__(self, bot_token: Optional[str] = None, chat_id: Optional[str] = None):
        """
        Initialize the Telegram notifier.
        
        Args:
            bot_token: Telegram bot token from BotFather
            chat_id: Telegram chat ID to send messages to
        """
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.enabled = bool(bot_token and chat_id)
        self.bot = None
        self._loop = None
        self._thread = None
        
        if self.enabled:
            self._initialize_bot()
    
    def _initialize_bot(self):
        """Initialize the Telegram bot in a separate thread with its own event loop."""
        try:
            from telegram import Bot
            self.bot = Bot(token=self.bot_token)
            
            # Create a new event loop for the thread
            self._loop = asyncio.new_event_loop()
            
            # Start the event loop in a separate thread
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()
            
        except ImportError:
            from app import logger
            logger.log('python-telegram-bot not installed. Telegram notifications disabled.', 'WARNING')
            self.enabled = False
        except Exception as e:
            from app import logger
            logger.log(f'Error initializing Telegram bot: {e}', 'ERROR')
            self.enabled = False
    
    def _run_loop(self):
        """Run the event loop in the thread."""
        asyncio.set_event_loop(self._loop)
        self._loop.run_forever()
    
    def send_message(self, message: str, parse_mode: str = 'HTML'):
        """
        Send a message via Telegram.
        
        Args:
            message: Message text to send
            parse_mode: Parse mode for message formatting (HTML or Markdown)
        """
        if not self.enabled:
            return
        
        try:
            # Schedule the coroutine in the event loop
            future = asyncio.run_coroutine_threadsafe(
                self.bot.send_message(
                    chat_id=self.chat_id,
                    text=message,
                    parse_mode=parse_mode
                ),
                self._loop
            )
            # Wait for the result with a timeout
            future.result(timeout=10)
        except Exception as e:
            from app import logger
            logger.log(f'Error sending Telegram message: {e}', 'ERROR')
    
    def notify_zombie_connected(self, zombie_username: str, zombie_id: str):
        """Notify when a zombie connects."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"🧟 <b>Zombie Connected</b>\n\n"
        message += f"Username: <code>{zombie_username}</code>\n"
        message += f"ID: <code>{zombie_id}</code>\n"
        message += f"Time: {timestamp}"
        self.send_message(message)
    
    def notify_zombie_disconnected(self, zombie_username: str, zombie_id: str):
        """Notify when a zombie disconnects."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"💀 <b>Zombie Disconnected</b>\n\n"
        message += f"Username: <code>{zombie_username}</code>\n"
        message += f"ID: <code>{zombie_id}</code>\n"
        message += f"Time: {timestamp}"
        self.send_message(message)
    
    def notify_task_completed(self, task_name: str, zombie_username: str, result: str):
        """Notify when a task is completed."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"✅ <b>Task Completed</b>\n\n"
        message += f"Task: <code>{task_name}</code>\n"
        message += f"Zombie: <code>{zombie_username}</code>\n"
        message += f"Time: {timestamp}\n\n"
        
        # Truncate result if too long
        if result and len(result) > 500:
            message += f"Result: <code>{result[:500]}...</code>"
        elif result:
            message += f"Result: <code>{result}</code>"
        
        self.send_message(message)
    
    def notify_task_failed(self, task_name: str, zombie_username: str, error: str):
        """Notify when a task fails."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"❌ <b>Task Failed</b>\n\n"
        message += f"Task: <code>{task_name}</code>\n"
        message += f"Zombie: <code>{zombie_username}</code>\n"
        message += f"Time: {timestamp}\n\n"
        message += f"Error: <code>{error}</code>"
        self.send_message(message)
    
    def notify_session_started(self, zombie_username: str, zombie_id: str):
        """Notify when a remote shell session is started."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"🔗 <b>Session Started</b>\n\n"
        message += f"Zombie: <code>{zombie_username}</code>\n"
        message += f"ID: <code>{zombie_id}</code>\n"
        message += f"Time: {timestamp}"
        self.send_message(message)
    
    def notify_session_stopped(self, zombie_username: str, zombie_id: str):
        """Notify when a remote shell session is stopped."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"🔌 <b>Session Stopped</b>\n\n"
        message += f"Zombie: <code>{zombie_username}</code>\n"
        message += f"ID: <code>{zombie_id}</code>\n"
        message += f"Time: {timestamp}"
        self.send_message(message)
    
    def notify_error(self, error_message: str):
        """Notify about errors."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"⚠️ <b>Error</b>\n\n"
        message += f"Time: {timestamp}\n\n"
        message += f"<code>{error_message}</code>"
        self.send_message(message)
    
    def notify_login(self, username: str, remote_host: str):
        """Notify when master logs in."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"🔐 <b>Master Login</b>\n\n"
        message += f"User: <code>{username}</code>\n"
        message += f"Host: <code>{remote_host}</code>\n"
        message += f"Time: {timestamp}"
        self.send_message(message)
    
    def __del__(self):
        """Clean up resources."""
        if self._loop and self._loop.is_running():
            self._loop.call_soon_threadsafe(self._loop.stop)
