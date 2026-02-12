# AI Merge Auto-Setup System - GitHub Version

## Overview
The AI Merge Auto-Setup System provides an automated way to configure and use the Multi-Modal AI Merge System. This version is designed for GitHub distribution without hardcoded paths.

## Key Features
- **Interactive Position Setup**: Prompts for AI positions with customizable capabilities
- **Auto-Configuration**: Automatically creates configuration files and directories
- **Easy Launch**: Simple scripts to run the system
- **Flexible Integration**: Works with various AI agents and modalities

## Installation

### Quick Install
Run the installation script to set up the system:

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-merge-system.git
cd ai-merge-system

# Run the setup
python3 setup.py
```

### Manual Install
If you prefer to run the setup manually:

```bash
# Navigate to the repository directory
cd ai-merge-system

# Run the auto-setup directly
python3 auto_setup.py
```

## Setup Process

The auto-setup will guide you through:

1. **Position Creation**: Enter names for your AI positions (e.g., "Code Reviewer", "Documentation Writer", "System Architect")
2. **Capabilities Configuration**: Define what each position can do
3. **Specialty Definition**: Specify the main focus area for each position
4. **Modality Support**: Select which data types each position supports (text, image, audio, video)

### Example Setup Session
```
Enter AI position name (or 'done' to finish): Code Assistant
Configuring Code Assistant:
Enter capabilities for Code Assistant (comma-separated, press Enter for defaults): coding, debugging, refactoring
Enter specialty for Code Assistant (press Enter for 'Code Assistant'): code generation
Supported modalities:
1. text
2. image
3. audio
4. video
5. multimodal
Enter supported modalities for Code Assistant (comma-separated numbers, press Enter for 'text'): 1
✅ Added position: Code Assistant

Enter AI position name (or 'done' to finish): done
```

## Usage

### Interactive Interface
After setup, use the simple interface to interact with the system:

```bash
cd ai_merge_auto
./run_ai_merge.sh
```

The interface provides options to:
- Submit text, image, audio, or video contributions
- Merge contributions using different strategies
- View current contributions
- Clear contributions

### Programmatic Usage
You can also use the system programmatically:

```python
from simple_interface import SimpleAIMergeInterface

# Initialize the interface
interface = SimpleAIMergeInterface()

# Submit a contribution
interface.submit_text_contribution("Code Assistant", "Here is some code...")

# Merge contributions
result = interface.merge_contributions("cross_modal_synthesis", "Context for merging")
```

### Configuration
The system creates a configuration file at `ai_merge_auto/config.json` that you can modify to adjust agent settings, capabilities, and modalities.

## Auto-Created Components

The system automatically creates:

- **Configuration Files**: JSON files for each AI position
- **Directory Structure**: Organized folders for agents, contributions, outputs, and logs
- **Launcher Scripts**: Easy-to-use scripts to start the system
- **Example Files**: Usage examples to get you started
- **Logging System**: Event logs for tracking system activity

## Integration Options

### CLI Interface
Use the command-line interface for scripting and automation:

```bash
cd ai_merge_auto
python3 cli_interface.py
```

### Direct API Access
Import and use the system directly in your Python projects:

```python
from ai_merge_system import MultiModalAIMergeSystem, MultiModalAIAgent, ModalityType

# Create and use the system directly
```

## Customization

### Adding New Agents
To add new agents after initial setup:
1. Edit `ai_merge_auto/config.json`
2. Add a new agent configuration
3. Or rerun the auto-setup to recreate the configuration

### Modifying Capabilities
Update agent capabilities by editing the configuration files in `ai_merge_auto/agents/`

## Troubleshooting

### Common Issues
- **Python Version**: Ensure you're using Python 3.8+
- **Permissions**: Make sure scripts have execute permissions
- **Paths**: Verify the system is installed in the correct location

### Resetting the System
To start fresh, remove the auto-setup directory and rerun the installer:
```bash
rm -rf ai_merge_auto
python3 setup.py
```

## Next Steps

1. **Run the installer**: `python3 setup.py`
2. **Configure your AI positions**: Follow the interactive prompts
3. **Start using the system**: `./run_ai_merge.sh`
4. **Experiment with different strategies**: Try cross-modal synthesis, modality-specific, and consensus approaches
5. **Integrate with your workflow**: Use the system programmatically in your projects

The AI Merge Auto-Setup System eliminates the need to manually code paths and configurations, providing an easy-to-use interface for multi-modal AI collaboration.