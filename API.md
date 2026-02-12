# AI Merge System - API Documentation

## Overview
The AI Merge System provides a revolutionary collaborative intelligence platform where multiple AI inputs are intelligently synthesized into cohesive, high-quality outputs that amplify human creativity and AI capabilities.

## Core Components

### 1. AIAgent
Represents an AI agent participating in the merge process.

#### Properties:
- `id`: Unique identifier for the agent
- `name`: Display name of the agent
- `capabilities`: List of capabilities (e.g., ["analysis", "coding", "research"])
- `confidence`: Agent's baseline confidence level (0.0-1.0)
- `specialty`: Primary area of expertise
- `response_time_ms`: Expected response time in milliseconds

### 2. Contribution
A contribution from an AI agent to be merged.

#### Properties:
- `agent_id`: ID of the contributing agent
- `content`: The actual contribution content
- `timestamp`: When the contribution was submitted
- `confidence`: Agent's confidence in this specific contribution
- `metadata`: Additional metadata about the contribution
- `hash`: Unique hash identifier for the contribution

### 3. MergeResult
Result of a merge operation.

#### Properties:
- `strategy`: The MergeStrategy used
- `merged_content`: The resulting merged content
- `contributing_agents`: List of agent IDs that contributed
- `confidence_score`: Overall confidence in the merge (0.0-1.0)
- `metadata`: Additional metadata about the merge
- `timestamp`: When the merge was completed
- `validation_results`: Results of validation for each contribution

### 4. MergeStrategy (Enum)
Different strategies for merging AI contributions.

#### Values:
- `SYNTHESIS`: Combine elements into a new solution
- `CONSENSUS`: Find agreement among AIs
- `COMPLEMENTARY`: Combine different aspects
- `COMPETITIVE_EVAL`: Evaluate and select the best

## Main Class: AIMergeSystem

### Constructor
```python
AIMergeSystem(log_path: Optional[Path] = None)
```
Initialize the AI Merge system with an optional custom log path.

### Methods

#### `register_agent(agent: AIAgent) -> None`
Register an AI agent with the system.

Parameters:
- `agent`: An AIAgent instance to register

#### `submit_contribution(agent_id: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> str`
Submit a contribution from an agent.

Parameters:
- `agent_id`: ID of the registered agent submitting
- `content`: The contribution content
- `metadata`: Optional metadata dictionary

Returns:
- Hash identifier for the contribution

#### `merge_all_contributions(strategy: MergeStrategy, context: str = "") -> MergeResult`
Merge all submitted contributions using the specified strategy.

Parameters:
- `strategy`: The merge strategy to use
- `context`: Context for the merge operation

Returns:
- MergeResult with the merged content and metadata

#### `merge_subset(contribution_hashes: List[str], strategy: MergeStrategy, context: str = "") -> MergeResult`
Merge a subset of contributions specified by their hashes.

Parameters:
- `contribution_hashes`: List of contribution hashes to merge
- `strategy`: The merge strategy to use
- `context`: Context for the merge operation

Returns:
- MergeResult with the merged content and metadata

#### `get_contributions_by_agent(agent_id: str) -> List[Contribution]`
Get all contributions from a specific agent.

Parameters:
- `agent_id`: ID of the agent

Returns:
- List of contributions from that agent

#### `clear_contributions() -> None`
Clear all contributions (preserving agent registrations).

## Usage Examples

### Basic Usage
```python
from ai_merge_system import AIMergeSystem, AIAgent, MergeStrategy

# Initialize the system
ai_merge = AIMergeSystem()

# Register an agent
agent = AIAgent(
    id="claude-001",
    name="Claude",
    capabilities=["analysis", "reasoning"],
    confidence=0.9,
    specialty="complex reasoning",
    response_time_ms=1200
)
ai_merge.register_agent(agent)

# Submit a contribution
hash_id = ai_merge.submit_contribution(
    "claude-001", 
    "This is my contribution to the task.",
    {"aspect": "analysis"}
)

# Merge all contributions using synthesis strategy
result = ai_merge.merge_all_contributions(MergeStrategy.SYNTHESIS, "Implement feature X")
print(f"Merged content: {result.merged_content}")
print(f"Confidence: {result.confidence_score}")
```

### Multiple Agents and Strategies
```python
# Register multiple agents
agents = [
    AIAgent("claude-001", "Claude", ["analysis"], 0.9, "reasoning", 1200),
    AIAgent("cursor-001", "Cursor", ["coding"], 0.85, "implementation", 800)
]

for agent in agents:
    ai_merge.register_agent(agent)

# Submit multiple contributions
ai_merge.submit_contribution("claude-001", "Security considerations...")
ai_merge.submit_contribution("cursor-001", "Implementation details...")

# Try different strategies
for strategy in [MergeStrategy.SYNTHESIS, MergeStrategy.CONSENSUS]:
    result = ai_merge.merge_all_contributions(strategy, "System design")
    print(f"{strategy.value}: {result.confidence_score}")
```

## Event Logging
The system logs events to `ai_merge_events.jsonl` in JSONL format with the following schema:

```json
{
  "event": "agent.registered|contribution.submitted|merge.completed|etc.",
  "ts_ms": 1739239200000,
  "source": "ai_merge_system",
  "data": { ... }
}
```

## Validation
The system includes built-in validation for contributions:
- Completeness check
- Coherence verification
- Relevance to context
- Internal consistency
- Quality scoring