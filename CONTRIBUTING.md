# Contributing to AI-Merge

Thank you for your interest in contributing to AI-Merge! This document provides guidelines for contributions.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/ai-merge.git`
3. Create a branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Run tests: `python -m pytest tests/`
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/avatararts/ai-merge.git
cd ai-merge

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints for all function signatures
- Write docstrings for all public functions and classes
- Keep lines under 100 characters
- Use meaningful variable names

## Testing

- Write tests for all new features
- Maintain test coverage above 80%
- Run `pytest tests/` before committing
- Include both unit and integration tests

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include tests for new features
- Update documentation as needed
- Ensure all tests pass
- Follow the code style guidelines

## Reporting Bugs

- Use the GitHub issue tracker
- Include a clear description
- Provide steps to reproduce
- Include error messages and stack traces
- Mention your Python version and OS

## Feature Requests

- Open an issue with the "enhancement" label
- Describe the feature and its use case
- Explain why it would be useful
- Be open to discussion and feedback

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community

## Questions?

Open an issue or reach out to the maintainers.

Thank you for contributing to AI-Merge!
