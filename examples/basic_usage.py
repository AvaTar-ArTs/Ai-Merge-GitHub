#!/usr/bin/env python3
"""
Basic AI-Merge Usage Example

This example demonstrates the core functionality of AI-Merge:
registering agents, submitting contributions, and merging with different strategies.
"""

from ai_merge_system import AIMergeSystem, AIAgent, MergeStrategy

def main():
    # Initialize the AI-Merge system
    print("🚀 Initializing AI-Merge System...\n")
    ai_merge = AIMergeSystem()
    
    # Register multiple AI agents
    print("📝 Registering AI agents...")
    
    claude = AIAgent(
        id="claude-001",
        name="Claude",
        capabilities=["analysis", "reasoning", "security"],
        confidence=0.92,
        specialty="complex reasoning and security analysis",
        response_time_ms=1200
    )
    
    gpt4 = AIAgent(
        id="gpt4-001",
        name="GPT-4",
        capabilities=["coding", "analysis", "creativity"],
        confidence=0.90,
        specialty="code generation and creative solutions",
        response_time_ms=1500
    )
    
    gemini = AIAgent(
        id="gemini-001",
        name="Gemini",
        capabilities=["research", "multimodal", "reasoning"],
        confidence=0.88,
        specialty="research and multimodal processing",
        response_time_ms=1000
    )
    
    ai_merge.register_agent(claude)
    ai_merge.register_agent(gpt4)
    ai_merge.register_agent(gemini)
    
    print(f"✅ Registered {len(ai_merge.agents)} agents\n")
    
    # Submit contributions from each agent
    print("💬 Submitting contributions...\n")
    
    ai_merge.submit_contribution(
        "claude-001",
        "Security analysis: Implement OAuth 2.0 with JWT tokens. "
        "Use httpOnly cookies for token storage to prevent XSS attacks. "
        "Add CSRF protection with double-submit cookie pattern.",
        {"aspect": "security", "priority": "high"}
    )
    
    ai_merge.submit_contribution(
        "gpt4-001",
        "Implementation approach: Create AuthController with /login, /logout, and /refresh endpoints. "
        "Use bcrypt for password hashing. Implement rate limiting with Redis. "
        "Add comprehensive error handling and logging.",
        {"aspect": "implementation", "priority": "high"}
    )
    
    ai_merge.submit_contribution(
        "gemini-001",
        "Research findings: According to OWASP guidelines, authentication systems should include: "
        "password strength requirements, account lockout after failed attempts, "
        "secure session management, and optional 2FA. Consider using established libraries like Passport.js.",
        {"aspect": "research", "priority": "medium"}
    )
    
    print(f"✅ Submitted {len(ai_merge.contributions)} contributions\n")
    
    # Demonstrate different merge strategies
    print("=" * 70)
    print("🎯 STRATEGY 1: SYNTHESIS")
    print("Combines all elements into a unified solution")
    print("=" * 70)
    
    result = ai_merge.merge_all_contributions(
        MergeStrategy.SYNTHESIS,
        "Design and implement a secure authentication system"
    )
    
    print(f"\n📊 Confidence: {result.confidence_score:.2f}")
    print(f"👥 Contributing agents: {', '.join(result.contributing_agents)}")
    print(f"\n📄 Merged Content:\n{result.merged_content}\n")
    
    # Clear contributions for next example
    ai_merge.contributions.clear()
    
    # New contributions for consensus example
    print("\n" + "=" * 70)
    print("🎯 STRATEGY 2: CONSENSUS")
    print("Finds common agreement points")
    print("=" * 70 + "\n")
    
    ai_merge.submit_contribution("claude-001", "Best practice: Always hash passwords with bcrypt or Argon2")
    ai_merge.submit_contribution("gpt4-001", "Security recommendation: Use bcrypt for password hashing with cost factor 12")
    ai_merge.submit_contribution("gemini-001", "Industry standard: Password hashing should use bcrypt or Argon2")
    
    result = ai_merge.merge_all_contributions(
        MergeStrategy.CONSENSUS,
        "What are the agreed-upon password security practices?"
    )
    
    print(f"📊 Confidence: {result.confidence_score:.2f}")
    print(f"\n📄 Consensus:\n{result.merged_content}\n")
    
    # Clear and demonstrate complementary
    ai_merge.contributions.clear()
    
    print("=" * 70)
    print("🎯 STRATEGY 3: COMPLEMENTARY")
    print("Combines different specialized aspects")
    print("=" * 70 + "\n")
    
    ai_merge.submit_contribution("claude-001", "Security layer: OAuth 2.0, JWT, CSRF protection")
    ai_merge.submit_contribution("gpt4-001", "API endpoints: /auth/login, /auth/logout, /auth/refresh, /auth/verify")
    ai_merge.submit_contribution("gemini-001", "Testing strategy: Unit tests for auth logic, integration tests for endpoints, security audit")
    
    result = ai_merge.merge_all_contributions(
        MergeStrategy.COMPLEMENTARY,
        "Complete authentication system design"
    )
    
    print(f"📊 Confidence: {result.confidence_score:.2f}")
    print(f"\n📄 Complementary aspects:\n{result.merged_content}\n")
    
    # Demonstrate validation
    print("=" * 70)
    print("🔍 VALIDATION RESULTS")
    print("=" * 70 + "\n")
    
    if result.validation_results:
        print("✅ Completeness:", "PASS" if result.validation_results.get("completeness") else "FAIL")
        print("✅ Coherence:", "PASS" if result.validation_results.get("coherence") else "FAIL")
        print("✅ Relevance:", "PASS" if result.validation_results.get("relevance") else "FAIL")
        print("✅ Consistency:", "PASS" if result.validation_results.get("consistency") else "FAIL")
    
    print("\n🎉 AI-Merge demonstration complete!")

if __name__ == "__main__":
    main()
