# AI Merge System - Getting Started Guide

## Overview
This guide will help you set up and start using the AI Merge System, which creates a collaborative environment where multiple AI inputs are intelligently synthesized into cohesive, high-quality outputs.

## Prerequisites
- Python 3.8+
- No additional dependencies required (uses only Python standard library)

## Installation

### 1. Clone or Download the System
The system is contained in a single directory with no external dependencies.

### 2. Verify Dependencies
The system uses only Python standard library components, so no additional packages are required.

### 3. Run the Demo
Test the system functionality:
```bash
python3 ai_merge_system.py
```

## Basic Usage

### 1. Import and Initialize the System
```python
from ai_merge_system import AIMergeSystem, AIAgent, MergeStrategy

# Initialize the system
ai_merge = AIMergeSystem()
```

### 2. Register AI Agents
Register the AI agents you want to participate in the merge process:

```python
# Register Claude
claude_agent = AIAgent(
    id="claude-001",
    name="Claude",
    capabilities=["analysis", "reasoning", "documentation"],
    confidence=0.9,
    specialty="complex reasoning",
    response_time_ms=1200
)
ai_merge.register_agent(claude_agent)

# Register other agents as needed
cursor_agent = AIAgent(
    id="cursor-001",
    name="Cursor",
    capabilities=["coding", "debugging"],
    confidence=0.85,
    specialty="code generation",
    response_time_ms=800
)
ai_merge.register_agent(cursor_agent)
```

### 3. Submit Contributions
Collect contributions from your AI agents:

```python
# Submit a contribution from Claude
claude_hash = ai_merge.submit_contribution(
    "claude-001",
    "For implementing user authentication, we should consider security best practices...",
    {"aspect": "security"}
)

# Submit a contribution from Cursor
cursor_hash = ai_merge.submit_contribution(
    "cursor-001", 
    "Here's a basic structure for an authentication controller...",
    {"aspect": "implementation"}
)
```

### 4. Merge Contributions
Combine the contributions using one of the merge strategies:

```python
# Use synthesis strategy to create a unified solution
result = ai_merge.merge_all_contributions(
    MergeStrategy.SYNTHESIS,
    "Implementing user authentication system"
)

print(f"Merged content: {result.merged_content}")
print(f"Confidence score: {result.confidence_score}")
print(f"Contributing agents: {result.contributing_agents}")
```

## Understanding Merge Strategies

The system offers four different approaches to merging contributions:

### 1. Synthesis (MergeStrategy.SYNTHESIS)
- **Purpose**: Combine elements from all contributions into a new, unified solution
- **Best for**: Creating comprehensive solutions from diverse inputs
- **Example**: Combining security considerations, implementation details, and UX factors into a complete system design

### 2. Consensus (MergeStrategy.CONSENSUS)
- **Purpose**: Find common agreement points among contributions
- **Best for**: Validating common approaches or identifying agreed-upon best practices
- **Example**: Finding common security practices agreed upon by multiple AIs

### 3. Complementary (MergeStrategy.COMPLEMENTARY)
- **Purpose**: Combine different aspects from various contributions
- **Best for**: Bringing together different perspectives or specialized knowledge
- **Example**: Combining security (from Claude), implementation (from Cursor), and UX (from another agent) aspects

### 4. Competitive Evaluation (MergeStrategy.COMPETITIVE_EVAL)
- **Purpose**: Evaluate contributions and select the best one
- **Best for**: When you need to choose among competing approaches
- **Example**: Selecting the most efficient implementation approach from multiple proposals

## Advanced Usage

### Merging Specific Contributions
You can merge only specific contributions by their hash:

```python
# Merge only specific contributions
subset_result = ai_merge.merge_subset(
    [claude_hash, cursor_hash],  # Only these contributions
    MergeStrategy.SYNTHESIS,
    "Authentication implementation"
)
```

### Getting Agent Contributions
Retrieve all contributions from a specific agent:

```python
claude_contributions = ai_merge.get_contributions_by_agent("claude-001")
for contrib in claude_contributions:
    print(f"Claude said: {contrib.content}")
```

### Clearing Contributions
Clear all contributions to start a new merge session:

```python
ai_merge.clear_contributions()
```

## Example Workflow

Here's a complete example of using the AI Merge System for a complex task:

```python
from ai_merge_system import AIMergeSystem, AIAgent, MergeStrategy

# Initialize the system
ai_merge = AIMergeSystem()

# Register your AI agents
agents = [
    AIAgent("claude-001", "Claude", ["analysis", "security"], 0.9, "security", 1200),
    AIAgent("cursor-001", "Cursor", ["coding", "implementation"], 0.85, "implementation", 800),
    AIAgent("gemini-001", "Gemini", ["research", "ux"], 0.88, "ux_research", 1000)
]

for agent in agents:
    ai_merge.register_agent(agent)

# Collect contributions for a task
ai_merge.submit_contribution("claude-001", "Security considerations for the API...")
ai_merge.submit_contribution("cursor-001", "Implementation approach for the API...")
ai_merge.submit_contribution("gemini-001", "User experience requirements for the API...")

# Merge using synthesis strategy
result = ai_merge.merge_all_contributions(
    MergeStrategy.SYNTHESIS,
    "Designing a secure and user-friendly API"
)

print(f"Synthesized approach: {result.merged_content}")
print(f"Confidence: {result.confidence_score}")
```

## Event Logging
The system automatically logs all activities to `ai_merge_events.jsonl`, which can be used for analysis and debugging.

## Troubleshooting

### Common Issues
1. **Agent not registered**: Make sure to register agents before submitting contributions
2. **Low confidence scores**: This may indicate disagreement among AIs or insufficient contributions
3. **Empty results**: Ensure contributions have been submitted before merging

### Getting Help
- Review the API documentation in `API.md`
- Check the event logs for detailed execution information
- Examine the demo script for working examples

## Next Steps

1. Start with simple tasks to familiarize yourself with the merge strategies
2. Experiment with different combinations of agents
3. Monitor the event logs to understand system behavior
4. Gradually increase complexity as you become comfortable

The AI Merge System enhances your AI collaboration workflows by providing intelligent synthesis of multiple AI inputs while maintaining systematic discipline.