#!/bin/bash

# Burokrat.site Deployment Script
# Deploys the FastHTML application to Netlify

set -e  # Exit on error

echo "🚀 Starting deployment process for burokrat.site..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Netlify CLI is installed
if ! command -v netlify &> /dev/null; then
    echo -e "${RED}❌ Netlify CLI is not installed${NC}"
    echo "Install it with: npm install -g netlify-cli"
    exit 1
fi

echo -e "${BLUE}📋 Step 1: Building static site...${NC}"
python3 build_static.py

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Build failed${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}📋 Step 2: Checking Netlify status...${NC}"
netlify status

echo ""
echo -e "${BLUE}📋 Step 3: Deploying to Netlify...${NC}"

# Ask for confirmation
read -p "Deploy to production? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    netlify deploy --prod
    
    if [ $? -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✅ Deployment successful!${NC}"
        echo -e "${GREEN}🌐 Your site is live at: https://burokrat.netlify.app${NC}"
    else
        echo -e "${RED}❌ Deployment failed${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️  Deployment cancelled${NC}"
    echo "To deploy later, run: netlify deploy --prod"
fi
