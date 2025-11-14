#!/bin/bash
# ZombieGang CLI Startup Script
# This script loads environment variables and starts the CLI

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}==================================${NC}"
echo -e "${GREEN}  ZombieGang CLI v1.0.0${NC}"
echo -e "${GREEN}  Ubuntu VPS Edition${NC}"
echo -e "${GREEN}==================================${NC}"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    echo "Install it with: sudo apt-get install python3"
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}Error: pip3 is not installed${NC}"
    echo "Install it with: sudo apt-get install python3-pip"
    exit 1
fi

# Load environment variables from .env if it exists
if [ -f .env ]; then
    echo -e "${GREEN}✓${NC} Loading environment from .env"
    export $(cat .env | grep -v '^#' | xargs)
else
    echo -e "${YELLOW}⚠${NC} No .env file found (optional)"
    echo "  Copy .env.example to .env to configure Telegram and Tor"
fi

# Check if dependencies are installed
echo -e "${GREEN}✓${NC} Checking dependencies..."
if ! python3 -c "import requests" 2>/dev/null; then
    echo -e "${YELLOW}⚠${NC} Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Check Telegram configuration
if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ -z "$TELEGRAM_CHAT_ID" ]; then
    echo -e "${YELLOW}⚠${NC} Telegram not configured (notifications disabled)"
    echo "  Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in .env to enable"
else
    echo -e "${GREEN}✓${NC} Telegram configured"
fi

# Check if Tor is running (optional)
if command -v tor &> /dev/null; then
    if systemctl is-active --quiet tor 2>/dev/null || pgrep -x tor > /dev/null; then
        echo -e "${GREEN}✓${NC} Tor is running (use 'proxy' command in CLI)"
    else
        echo -e "${YELLOW}⚠${NC} Tor is installed but not running"
        echo "  Start it with: sudo systemctl start tor"
    fi
else
    echo -e "${YELLOW}⚠${NC} Tor not installed (optional)"
    echo "  Install it with: sudo apt-get install tor"
fi

echo ""
echo -e "${GREEN}Starting CLI...${NC}"
echo ""

# Start the CLI
python3 cli.py

echo ""
echo -e "${GREEN}CLI exited.${NC}"
