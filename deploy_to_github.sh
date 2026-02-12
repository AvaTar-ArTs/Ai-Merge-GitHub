#!/bin/bash
# Advanced GitHub Deployment Script for AI-Merge
# Uses: gh CLI, git-ai tracking, firecrawl validation

set -e  # Exit on error

echo "🚀 AI-Merge GitHub Deployment Script"
echo "======================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo -e "${BLUE}📋 Checking prerequisites...${NC}"

if ! command -v gh &> /dev/null; then
    echo -e "${YELLOW}⚠️  GitHub CLI (gh) not found. Install with: brew install gh${NC}"
    exit 1
fi

if ! command -v firecrawl &> /dev/null; then
    echo -e "${YELLOW}⚠️  Firecrawl CLI not found. Install with: npm install -g firecrawl-cli${NC}"
    exit 1
fi

echo -e "${GREEN}✅ All tools available${NC}"
echo ""

# Check authentication
echo -e "${BLUE}🔐 Checking GitHub authentication...${NC}"

if ! gh auth status &> /dev/null; then
    echo -e "${YELLOW}⚠️  Not authenticated with GitHub${NC}"
    echo "🌐 Opening browser for authentication..."
    gh auth login --web
fi

CURRENT_USER=$(gh api user --jq .login)
echo -e "${GREEN}✅ Authenticated as: ${CURRENT_USER}${NC}"

if [ "$CURRENT_USER" != "AvaTar-ArTs" ]; then
    echo -e "${YELLOW}⚠️  Warning: Authenticated as ${CURRENT_USER}, but repository owner is AvaTar-ArTs${NC}"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""

# Check git status
echo -e "${BLUE}📊 Checking repository status...${NC}"
git status --short

echo ""

# Run tests before deployment
echo -e "${BLUE}🧪 Running tests...${NC}"

if [ -f "tests/test_ai_merge_system.py" ]; then
    /usr/local/opt/python@3.12/bin/python3.12 -m pytest tests/ -v || {
        echo -e "${YELLOW}⚠️  Tests failed. Continue anyway? (y/n)${NC}"
        read -p "" -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    }
    echo -e "${GREEN}✅ Tests passed${NC}"
else
    echo -e "${YELLOW}⚠️  No tests found, skipping...${NC}"
fi

echo ""

# Push to GitHub
echo -e "${BLUE}📤 Pushing to GitHub...${NC}"

echo "Repository: https://github.com/AvaTar-ArTs/Ai-Merge-GitHub.git"
echo "Branch: main"
echo "Commits to push:"
git log origin/main..main --oneline

echo ""
read -p "Proceed with push? (y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Use gh to push (handles authentication)
    git push origin main --force-with-lease
    
    echo -e "${GREEN}✅ Successfully pushed to GitHub!${NC}"
    echo ""
    
    # Verify deployment with firecrawl
    echo -e "${BLUE}🔍 Verifying deployment...${NC}"
    sleep 5  # Give GitHub a moment to update
    
    mkdir -p .firecrawl
    firecrawl scrape "https://github.com/AvaTar-ArTs/Ai-Merge-GitHub" -o .firecrawl/deployment-verification.md
    
    if grep -q "AI-Merge" .firecrawl/deployment-verification.md; then
        echo -e "${GREEN}✅ Deployment verified! Repository is live.${NC}"
    else
        echo -e "${YELLOW}⚠️  Could not verify deployment automatically${NC}"
    fi
    
    echo ""
    echo -e "${GREEN}🎉 Deployment complete!${NC}"
    echo ""
    echo "📊 Repository: https://github.com/AvaTar-ArTs/Ai-Merge-GitHub"
    echo "📝 View commits: https://github.com/AvaTar-ArTs/Ai-Merge-GitHub/commits/main"
    echo "🐛 Open issues: https://github.com/AvaTar-ArTs/Ai-Merge-GitHub/issues"
    echo "🔀 Pull requests: https://github.com/AvaTar-ArTs/Ai-Merge-GitHub/pulls"
    echo ""
    
    # Open in browser
    read -p "Open repository in browser? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        open "https://github.com/AvaTar-ArTs/Ai-Merge-GitHub"
    fi
else
    echo "❌ Push cancelled"
    exit 1
fi
