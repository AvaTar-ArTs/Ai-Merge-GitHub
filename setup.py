#!/usr/bin/env python3
"""
AI-Merge: Collaborative Intelligence Platform
Setup configuration for pip installation
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="ai-merge",
    version="0.1.0",
    author="Steven (AvaTar-ArTs)",
    author_email="me@avatararts.org",
    description="Revolutionary collaborative intelligence platform for synthesizing multi-AI outputs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/avatararts/ai-merge",
    packages=find_packages(exclude=["tests", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - uses only standard library
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-merge=ai_merge_system:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/avatararts/ai-merge/issues",
        "Source": "https://github.com/avatararts/ai-merge",
        "Documentation": "https://github.com/avatararts/ai-merge/blob/main/docs",
    },
)
