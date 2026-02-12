#!/usr/bin/env python3
"""
Basic Usage Example for AI Merge System
"""

from ai_merge_system import AIMergeSystem, AIAgent, MergeStrategy

def main():
    print("🚀 AI Merge System - Basic Usage Example")
    print("=" * 45)
    
    # Initialize the system
    ai_merge = AIMergeSystem()
    
    # Register an agent
    agent = AIAgent(
        id="claude-001",
        name="Claude",
        capabilities=["analysis", "reasoning", "documentation"],
        confidence=0.9,
        specialty="complex reasoning",
        response_time_ms=1200
    )
    ai_merge.register_agent(agent)
    
    print(f"✅ Registered: {agent.name} ({agent.specialty})")
    
    # Submit a contribution
    hash_id = ai_merge.submit_contribution(
        "claude-001", 
        "For implementing user authentication, we should consider security best practices including password hashing, secure session management, and protection against common attacks like CSRF and XSS.",
        {"aspect": "security"}
    )
    
    print(f"✅ Contribution submitted: {hash_id[:8]}...")
    
    # Submit another contribution
    hash_id2 = ai_merge.submit_contribution(
        "claude-001", 
        "From a technical perspective, we should use industry-standard libraries for JWT handling and consider rate limiting to prevent brute force attacks.",
        {"aspect": "technical"}
    )
    
    print(f"✅ Contribution submitted: {hash_id2[:8]}...")
    
    # Merge contributions using synthesis strategy
    result = ai_merge.merge_all_contributions(
        MergeStrategy.SYNTHESIS,
        "Implementing user authentication system"
    )
    
    print(f"\n🎯 Merge Result:")
    print(f"   Strategy: {result.strategy.value}")
    print(f"   Confidence: {result.confidence_score:.2f}")
    print(f"   Contributing agents: {', '.join(result.contributing_agents)}")
    print(f"   Merged content preview:\n{result.merged_content[:300]}{'...' if len(result.merged_content) > 300 else ''}")
    
    print(f"\n✅ Basic usage example completed!")

if __name__ == "__main__":
    main()