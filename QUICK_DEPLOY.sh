#!/bin/bash
# Quick Deploy Script for AI-Merge-GitHub
# Handles multiple GitHub account authentication scenarios

set -e

echo "🚀 AI-Merge GitHub Quick Deploy"
echo "================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

cd ~/iterm2/Ai-Merge-GitHub

echo "📋 Current Repository Status:"
echo "   Local Config: $(git config user.name) <$(git config user.email)>"
echo "   Remote: $(git remote get-url origin)"
echo ""

echo "🔐 Choose Authentication Method:"
echo ""
echo "1️⃣  Create NEW token for AvaTar-ArTs (RECOMMENDED)"
echo "2️⃣  Use EXISTING AvaTar-ArTs token (I have one)"
echo "3️⃣  Use ichoake token (switch account)"
echo "4️⃣  Use GPTJunkie token (switch account)"
echo ""
read -p "Choose (1-4): " choice

case $choice in
    1)
        echo ""
        echo "${YELLOW}📝 Creating New Token for AvaTar-ArTs${NC}"
        echo ""
        echo "Opening GitHub token creation page..."
        open "https://github.com/settings/tokens/new?scopes=repo,workflow&description=AI-Merge-GitHub-Deployment"
        echo ""
        echo "⚠️  Make sure you're logged in as: ${GREEN}AvaTar-ArTs${NC}"
        echo "   (If not, open in Incognito/Private window)"
        echo ""
        echo "Token Settings:"
        echo "   • Name: AI-Merge-GitHub Deployment"
        echo "   • Scopes: ✅ repo, ✅ workflow"
        echo "   • Expiration: No expiration"
        echo ""
        read -p "Paste your new token here: " TOKEN
        
        # Add to consolidated github.env (if not already there)
        if ! grep -q "GITHUB_TOKEN_AVATARARTS=" ~/.env.d/github.env 2>/dev/null; then
            echo "" >> ~/.env.d/github.env
            echo "# AvaTar-ArTs token added: $(date +%Y-%m-%d)" >> ~/.env.d/github.env
            echo "GITHUB_TOKEN_AVATARARTS=$TOKEN" >> ~/.env.d/github.env
            echo "GITHUB_PERSONAL_ACCESS_TOKEN_AVATARARTS=$TOKEN" >> ~/.env.d/github.env
            echo "${GREEN}✅ Token added to ~/.env.d/github.env${NC}"
        else
            # Update existing token
            sed -i.bak "s|GITHUB_TOKEN_AVATARARTS=.*|GITHUB_TOKEN_AVATARARTS=$TOKEN|" ~/.env.d/github.env
            sed -i.bak "s|GITHUB_PERSONAL_ACCESS_TOKEN_AVATARARTS=.*|GITHUB_PERSONAL_ACCESS_TOKEN_AVATARARTS=$TOKEN|" ~/.env.d/github.env
            echo "${GREEN}✅ Token updated in ~/.env.d/github.env${NC}"
        fi
        ;;
        
    2)
        echo ""
        read -p "Enter your existing AvaTar-ArTs token: " TOKEN
        ;;
        
    3)
        echo ""
        echo "${YELLOW}Switching to ichoake account${NC}"
        # Load from consolidated github.env
        source ~/.env.d/github.env
        TOKEN=$GITHUB_TOKEN_ICHOAKE
        
        # Update remote URL
        git remote set-url origin https://github.com/ichoake/Ai-Merge-GitHub.git
        git config user.name "ichoake"
        git config user.email "sjchaplinski@gmail.com"
        
        echo "${GREEN}✅ Configured for ichoake${NC}"
        echo "   Remote changed to: https://github.com/ichoake/Ai-Merge-GitHub.git"
        ;;
        
    4)
        echo ""
        echo "${YELLOW}Switching to GPTJunkie account${NC}"
        # Load from consolidated github.env
        source ~/.env.d/github.env
        TOKEN=$GITHUB_TOKEN_GPTJUNKIE
        
        # Update remote URL
        git remote set-url origin https://github.com/GPTJunkie/Ai-Merge-GitHub.git
        git config user.name "GPTJunkie"
        git config user.email "info@gptjunkie.com"
        
        echo "${GREEN}✅ Configured for GPTJunkie${NC}"
        echo "   Remote changed to: https://github.com/GPTJunkie/Ai-Merge-GitHub.git"
        ;;
        
    *)
        echo "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

echo ""
echo "🔄 Attempting to push to GitHub..."
echo ""

# Update remote URL with token
CURRENT_URL=$(git remote get-url origin)
REPO_PATH=$(echo $CURRENT_URL | sed 's|https://github.com/||')

# Set remote with token
git remote set-url origin "https://${TOKEN}@github.com/${REPO_PATH}"

# Push
if git push -u origin main --force-with-lease; then
    echo ""
    echo "${GREEN}✅ Successfully pushed to GitHub!${NC}"
    echo ""
    echo "🌐 Repository URL: https://github.com/${REPO_PATH}"
    echo ""
    echo "Next steps:"
    echo "1. Visit your repository"
    echo "2. Configure GitHub Actions secrets if needed"
    echo "3. Create first release tag for PyPI"
    echo ""
else
    echo ""
    echo "${RED}❌ Push failed${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "1. Verify token has 'repo' scope"
    echo "2. Check repository exists: https://github.com/${REPO_PATH}"
    echo "3. Confirm you have write access"
    echo ""
fi

# Clean up - remove token from remote URL for security
git remote set-url origin "${CURRENT_URL}"
