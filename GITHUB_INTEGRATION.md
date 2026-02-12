# GitHub Integration Guide for AI-Merge

This document explains how AI-Merge integrates with your development workflow on GitHub.

## 🚀 Quick Start

### Installation from GitHub

```bash
# Clone the repository
git clone https://github.com/AvaTar-ArTs/Ai-Merge-GitHub.git
cd Ai-Merge-GitHub

# Install (no dependencies required for core!)
python3 -m pip install -e .

# Run tests
pytest tests/ -v
```

See full guide in [GETTING_STARTED.md](GETTING_STARTED.md)

---

## 🔄 GitHub Actions CI/CD

**Automated Testing** (`.github/workflows/tests.yml`):
- Matrix: Python 3.8-3.12 × Ubuntu/macOS/Windows
- Coverage reports uploaded to Codecov
- Linting: Black, Flake8, MyPy

**Automated Releases** (`.github/workflows/release.yml`):
```bash
git tag v0.2.0 && git push origin v0.2.0
# GitHub Actions automatically builds and publishes to PyPI
```

---

## 🤝 Contributing

Quick workflow:
1. Fork on GitHub
2. `git checkout -b feature/your-feature`
3. Make changes + add tests
4. `pytest tests/ -v && black . --check`
5. Push and open PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## 🔐 Security

Report vulnerabilities to: **me@avatararts.org**

Features:
- Zero external dependencies
- Input validation
- Thread-safe operations
- Comprehensive audit logging

---

## 📦 Integration Examples

### git-ai Integration
```bash
git-ai checkpoint claude
git-ai blame ai_merge_system.py
```

### Claude Code Skill
```bash
/ai-merge synthesis "Build auth system"
```

---

**GitHub:** https://github.com/AvaTar-ArTs/Ai-Merge-GitHub
**Created:** February 11, 2026 by Steven (AvaTar-ArTs)
