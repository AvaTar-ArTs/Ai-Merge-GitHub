#!/usr/bin/env python3
"""
AI Merge System - Auto Setup Script

This script sets up the AI Merge system with interactive configuration
for AI positions and capabilities.
"""

import json
import os
from pathlib import Path
import uuid
from typing import Dict, List


def create_setup():
    """Create the AI Merge system setup with interactive configuration."""
    print("🚀 AI Merge System - Auto Setup")
    print("=" * 40)
    print("Let's configure your AI positions for the system\n")
    
    # Create the main directory
    base_path = Path("ai_merge_auto")
    base_path.mkdir(exist_ok=True)
    
    # Create subdirectories
    (base_path / "agents").mkdir(exist_ok=True)
    (base_path / "contributions").mkdir(exist_ok=True)
    (base_path / "outputs").mkdir(exist_ok=True)
    (base_path / "logs").mkdir(exist_ok=True)
    (base_path / "temp").mkdir(exist_ok=True)
    
    print("📁 Created directory structure")
    
    # Collect AI positions interactively
    agents = []
    
    while True:
        position_name = input("Enter AI position name (or 'done' to finish): ").strip()
        if position_name.lower() == 'done':
            break
            
        if not position_name:
            print("⚠️  Position name cannot be empty. Try again.")
            continue
        
        print(f"\nConfiguring {position_name}:")
        
        # Prompt for capabilities
        capabilities_input = input(f"Enter capabilities for {position_name} (comma-separated, press Enter for defaults): ").strip()
        if capabilities_input:
            capabilities = [cap.strip() for cap in capabilities_input.split(',')]
        else:
            # Default capabilities based on position name
            if 'code' in position_name.lower() or 'cursor' in position_name.lower():
                capabilities = ["coding", "debugging", "implementation"]
            elif 'claude' in position_name.lower() or 'analysis' in position_name.lower():
                capabilities = ["analysis", "reasoning", "documentation"]
            elif 'gemini' in position_name.lower() or 'research' in position_name.lower():
                capabilities = ["research", "creativity", "multimodal"]
            elif 'qwen' in position_name.lower() or 'technical' in position_name.lower():
                capabilities = ["coding", "technical", "multilingual"]
            else:
                capabilities = ["general", "assistance", "problem_solving"]
        
        # Prompt for specialty
        specialty = input(f"Enter specialty for {position_name} (press Enter for '{position_name}'): ").strip()
        if not specialty:
            specialty = position_name
        
        # Prompt for supported modalities
        print("\nSupported modalities:")
        print("1. text")
        print("2. image") 
        print("3. audio")
        print("4. video")
        print("5. multimodal")
        
        modality_input = input(f"Enter supported modalities for {position_name} (comma-separated numbers, press Enter for 'text'): ").strip()
        if modality_input:
            modality_map = {"1": "text", "2": "image", "3": "audio", "4": "video", "5": "multimodal"}
            modality_numbers = [num.strip() for num in modality_input.split(',')]
            modalities = [modality_map.get(num, "text") for num in modality_numbers if num in modality_map]
            if not modalities:
                modalities = ["text"]
        else:
            modalities = ["text"]
        
        # Auto-generate confidence and response time
        import random
        confidence = round(random.uniform(0.75, 0.95), 2)
        response_time = random.randint(500, 1500)
        
        agent = {
            "id": f"{position_name.lower().replace(' ', '-')}-{str(uuid.uuid4())[:8]}",
            "name": position_name,
            "capabilities": capabilities,
            "confidence": confidence,
            "specialty": specialty,
            "supported_modalities": modalities,
            "response_time_ms": response_time
        }
        
        agents.append(agent)
        print(f"✅ Added position: {position_name}")
        print()
    
    if not agents:
        print("❌ No positions were created. Setup incomplete.")
        return False
    
    # Create agent configuration files
    for agent in agents:
        agent_file = base_path / "agents" / f"{agent['id']}.json"
        with open(agent_file, 'w') as f:
            json.dump(agent, f, indent=2)
        print(f"📄 Created agent config: {agent_file.name}")
    
    # Create main configuration
    config = {
        "system": {
            "name": "AI Merge Auto-Setup System",
            "version": "1.0",
            "base_path": str(base_path),
            "log_path": str(base_path / "logs" / "ai_merge_events.jsonl")
        },
        "agents": agents,
        "settings": {
            "default_strategy": "cross_modal_synthesis",
            "auto_merge_threshold": 3,
            "validation_enabled": True,
            "telemetry_enabled": True
        }
    }
    
    config_path = base_path / "config.json"
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"⚙️  Created main configuration: {config_path.name}")
    
    # Create a simple launcher script
    launcher_content = '''#!/usr/bin/env python3
"""
AI Merge System Launcher
Generated by AI Merge Auto-Setup
"""

import sys
import os
from pathlib import Path

# Add the AI Merge system to the path
sys.path.insert(0, str(Path(".")))

from ai_merge_system import AIMergeSystem

def main():
    print("🚀 AI Merge System - Auto-Launched")
    print("=" * 40)
    
    # Initialize with auto-generated config
    config_path = Path("ai_merge_auto/config.json")
    
    if not config_path.exists():
        print(f"❌ Config file not found: {config_path}")
        return
    
    # Load configuration
    import json
    with open(config_path, "r") as f:
        config = json.load(f)
    
    # Initialize the system
    ai_merge = AIMergeSystem()
    
    # Register agents from config
    from ai_merge_system import AIAgent, MergeStrategy
    
    for agent_config in config["agents"]:
        agent = AIAgent(
            id=agent_config["id"],
            name=agent_config["name"], 
            capabilities=agent_config["capabilities"],
            confidence=agent_config["confidence"],
            specialty=agent_config["specialty"],
            response_time_ms=agent_config["response_time_ms"]
        )
        ai_merge.register_agent(agent)
        print(f"✅ Registered: {agent_config['name']} ({agent_config['specialty']})")
    
    print(f"\n📋 Registered {len(config['agents'])} agents")
    print("\nReady to accept contributions and perform merges!")
    print("\nUse the system programmatically or via the API.")

if __name__ == "__main__":
    main()
'''
    
    launcher_path = base_path / "launch_ai_merge.py"
    with open(launcher_path, 'w') as f:
        f.write(launcher_content)
    
    # Make executable
    os.chmod(launcher_path, 0o755)
    
    print(f"🚀 Created launcher script: {launcher_path.name}")
    
    # Create a simple usage example
    example_content = '''#!/usr/bin/env python3
"""
Simple Usage Example for AI Merge System
"""

import sys
from pathlib import Path

# Add the system to path
sys.path.insert(0, str(Path(".")))

from ai_merge_system import AIMergeSystem, AIAgent, MergeStrategy

# Initialize the system
ai_merge = AIMergeSystem()

# The agents are automatically registered from config
# You can now submit contributions and merge them

# Example: Submit a text contribution
ai_merge.submit_contribution(
    "your-agent-id",  # Use ID from your config
    "This is a sample contribution",
    {"type": "example"}
)

# Example: Merge contributions
result = ai_merge.merge_all_contributions(
    MergeStrategy.SYNTHESIS, 
    "Sample context for merging"
)

print(f"Merged result: {result.merged_content[:100]}...")
'''
    
    example_path = base_path / "basic_usage_example.py"
    with open(example_path, 'w') as f:
        f.write(example_content)
    
    print(f"📝 Created example: {example_path.name}")
    
    print(f"\n🎉 AI Merge Auto-Setup Complete!")
    print(f"📁 System created at: {base_path}")
    print(f"📋 Positions created: {len(agents)}")
    print(f"⚙️  Configuration: {config_path.name}")
    print(f"🚀 Launcher: launch_ai_merge.py")
    print(f"📖 Examples: basic_usage_example.py")
    
    print("\n💡 Next steps:")
    print(f"  1. Review your configuration: {config_path}")
    print(f"  2. Launch the system: python {base_path}/launch_ai_merge.py")
    print(f"  3. Use the examples as starting points")
    
    return True


def main():
    """Main function to run the setup."""
    success = create_setup()
    if success:
        print("\n✅ AI Merge System setup completed successfully!")
        print("You can now use the system by navigating to the ai_merge_auto directory.")
    else:
        print("\n❌ AI Merge System setup failed.")


if __name__ == "__main__":
    main()