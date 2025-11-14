# ZombieGang v1.0.0 - Ubuntu VPS CLI Edition

## Release Date: 2025

## Overview
This release transforms ZombieGang into a streamlined CLI-only botnet framework optimized for Ubuntu VPS deployment with enhanced security features including Telegram notifications and Tor v3 hidden service support.

## 🎯 Key Features

### CLI-Only Design
- Removed Flask web interface and all web dependencies
- Reduced memory footprint and complexity
- Faster startup and operation
- Ideal for headless VPS environments

### Telegram Integration
- Real-time notifications for all events
- Secure bot-based communication
- Notifications for:
  - Master login/logout
  - Zombie connections/disconnections
  - Remote shell sessions start/stop
  - Task completions and failures
  - Critical errors and warnings

### Tor v3 Hidden Service Support
- Full support for v3 .onion addresses (56 characters)
- DNS resolution through SOCKS proxy (socks5h://)
- Complete anonymity for CC server
- No public IP required
- End-to-end encrypted communication

### Bug Fixes
- Fixed bare `except:` clauses with proper exception handling
- Fixed `json.load()` vs `json.loads()` bug in data.py
- Improved error messages and logging
- Better exception handling throughout codebase

### Ubuntu VPS Optimization
- Designed specifically for Ubuntu 18.04+ LTS
- Automated setup scripts
- Environment-based configuration
- systemd service support
- Resource-efficient operation

## 📦 New Files

### Documentation
- `CLI_SETUP_UBUNTU.md` - Complete setup guide for Ubuntu VPS
- `CLI_QUICK_START.md` - Quick reference guide
- `master-client/README_CLI.md` - Comprehensive CLI documentation
- `CHANGELOG_v1.0.0.md` - This file

### Configuration
- `.gitignore` - Proper ignore patterns for Python projects
- `master-client/.env.example` - Example environment configuration
- `master-client/start_cli.sh` - Automated startup script with checks

### Code
- `master-client/app/components/telegram_notifier.py` - Telegram notification system

## 🔧 Modified Files

### Dependencies
**master-client/requirements.txt**
- Removed: `flask`, `flask-wtf`
- Added: `requests[socks]`, `python-telegram-bot==20.7`, `stem`

### Configuration
**master-client/config.py**
- Added Telegram bot token configuration
- Added Telegram chat ID configuration
- Added Tor SOCKS proxy configuration
- Added environment variable support

### CLI Application
**master-client/cli.py**
- Updated version to 1.0.0
- Added Telegram notification integration
- Added notifications for login events
- Added notifications for session start/stop
- Added notifications for task completion
- Commented out test credentials
- Improved error handling

### Core Application
**master-client/app/__init__.py**
- Removed Flask app factory
- Removed web route blueprints
- Added TelegramNotifier initialization
- Simplified initialization for CLI-only use

### Components
**master-client/app/components/__init__.py**
- Added TelegramNotifier import

**master-client/app/components/proxy.py**
- Changed `socks5://` to `socks5h://` for DNS resolution through proxy
- Fixed bare except clause with proper exception handling
- Improved error messages

### Models
**master-client/app/models/data.py**
- Fixed bare except clauses with specific exception types
- Fixed `json.load()` bug (changed to `json.loads()`)
- Added error logging for debugging

## 🔒 Security Improvements

### Code Quality
- Replaced bare `except:` with specific exception types
- Added proper error logging
- Improved input validation
- Better error messages for debugging

### Security Features
- Tor v3 hidden service support for anonymity
- SOCKS5 proxy with hostname resolution
- Environment-based configuration (no hardcoded secrets)
- Secure password input (getpass)
- JWT token-based authentication

### CodeQL Analysis
- Passed CodeQL security scan with 0 alerts
- No security vulnerabilities detected

## 🚀 Installation

### Quick Install (Ubuntu)
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip mariadb-server tor

# Install Python dependencies
cd master-client
pip3 install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Add your Telegram credentials

# Start CLI
./start_cli.sh
```

### With Tor Hidden Service
```bash
# Configure Tor
sudo nano /etc/tor/torrc
# Add:
# HiddenServiceDir /var/lib/tor/zombiegang/
# HiddenServiceVersion 3
# HiddenServicePort 80 127.0.0.1:8080

# Restart Tor
sudo systemctl restart tor

# Get your onion address
sudo cat /var/lib/tor/zombiegang/hostname
```

## 📊 Compatibility

### Backward Compatibility
- ✅ Existing zombie clients work without modifications
- ✅ CC server API unchanged
- ✅ Database schema compatible
- ✅ Authentication system unchanged
- ✅ Task system compatible

### System Requirements
- Ubuntu 18.04 LTS or newer
- Python 3.8 or higher
- 1GB RAM minimum
- 10GB disk space
- Internet connection (or Tor)

### Tested On
- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Python 3.8, 3.9, 3.10, 3.12

## 📝 Usage Examples

### Basic Usage
```bash
# Start CLI
python3 cli.py

# Set credentials
set USER myusername
set PSWD
set RHOST localhost:8080
login

# List zombies
get zombies

# Start remote shell
start 1
whoami
```

### With Tor
```bash
# Enable Tor proxy
set PXHOST 127.0.0.1
set PXPORT 9050
proxy

# Connect to hidden service
set RHOST abcd1234...onion
login
```

### Telegram Notifications
```bash
# Set environment variables
export TELEGRAM_BOT_TOKEN='your-token'
export TELEGRAM_CHAT_ID='your-chat-id'

# Start CLI (will auto-detect and enable)
python3 cli.py
```

## 🐛 Known Issues

### Minor Issues
- None currently known

### Limitations
- Telegram requires internet connectivity
- Tor adds latency to connections
- CLI requires terminal access

## 🔮 Future Enhancements

### Planned Features
- [ ] Interactive session history
- [ ] Command autocomplete improvements
- [ ] Multi-master support
- [ ] Enhanced logging system
- [ ] Plugin system for custom notifications
- [ ] REST API for external integrations

### Under Consideration
- Discord notification support
- Slack integration
- Email notifications
- Web dashboard as optional component

## 📚 Documentation

### Available Guides
1. **CLI_SETUP_UBUNTU.md** - Complete setup guide
2. **CLI_QUICK_START.md** - Quick reference
3. **master-client/README_CLI.md** - CLI documentation
4. **CHANGELOG_v1.0.0.md** - This file

### External Resources
- Original Project: https://github.com/r3nt0n/zombiegang
- Telegram Bot API: https://core.telegram.org/bots/api
- Tor Project: https://www.torproject.org/

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

GNU General Public License v3.0

## 🙏 Acknowledgments

- **r3nt0n** - Original ZombieGang framework
- **Telegram Team** - Telegram Bot API
- **Tor Project** - Anonymity network
- **Community** - Bug reports and feedback

## ⚠️ Legal Disclaimer

This software is for educational and authorized security testing purposes only. Unauthorized use against systems you don't own or have permission to test is illegal. The authors are not responsible for misuse.

## 📞 Support

For issues, questions, or contributions:
- GitHub Issues: https://github.com/bitbybit91/zombiegang/issues
- Email: (see repository)

---

**Version**: 1.0.0  
**Status**: Stable  
**Platform**: Ubuntu VPS  
**Release Date**: 2025
