#!/usr/bin/env python3
"""Multi-AI Code Review Example"""

from ai_merge_system import AIMergeSystem, AIAgent, MergeStrategy

def main():
    ai_merge = AIMergeSystem()
    
    # Register code review specialists
    agents = [
        ("claude", "Claude", "security and architecture"),
        ("gpt4", "GPT-4", "code quality and performance"),
        ("gemini", "Gemini", "best practices and patterns")
    ]
    
    for agent_id, name, specialty in agents:
        ai_merge.register_agent(
            AIAgent(agent_id, name, ["code-review"], 0.9, specialty, 1000)
        )
    
    # Submit code reviews
    ai_merge.submit_contribution(
        "claude",
        "SECURITY: SQL injection vulnerability on line 42. Use parameterized queries."
    )
    ai_merge.submit_contribution(
        "gpt4",
        "PERFORMANCE: N+1 query issue. Use join or batch loading."
    )
    ai_merge.submit_contribution(
        "gemini",
        "BEST PRACTICE: Missing error handling for network failures."
    )
    
    # Find consensus on critical issues
    result = ai_merge.merge_all_contributions(
        MergeStrategy.CONSENSUS,
        "Code review for PR #123"
    )
    
    print(f"🔍 Code Review Results (Confidence: {result.confidence_score:.2f})")
    print(f"\n{result.merged_content}")

if __name__ == "__main__":
    main()
