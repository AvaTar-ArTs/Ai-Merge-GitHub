#!/usr/bin/env python3
"""
Multi-Modal Usage Example for AI Merge System
"""

from multi_modal_ai_merge_system import MultiModalAIMergeSystem, MultiModalAIAgent, ModalityType, MultiModalContent
from pathlib import Path

def main():
    print("🚀 Multi-Modal AI Merge System - Usage Example")
    print("=" * 50)
    
    # Initialize the multi-modal system
    mm_ai_merge = MultiModalAIMergeSystem()
    
    # Register a multi-modal agent
    agent = MultiModalAIAgent(
        id="gemini-001",
        name="Gemini",
        capabilities=["research", "creativity", "multimodal"],
        confidence=0.88,
        specialty="research and multimodal processing",
        supported_modalities=[ModalityType.TEXT, ModalityType.IMAGE, ModalityType.AUDIO],
        response_time_ms=1000
    )
    mm_ai_merge.register_agent(agent)
    
    print(f"✅ Registered: {agent.name} ({agent.specialty})")
    print(f"   Modalities: {[m.value for m in agent.supported_modalities]}")
    
    # Submit a text contribution
    text_hash = mm_ai_merge.submit_text_contribution(
        "gemini-001", 
        "Authentication systems should consider user experience aspects like password reset flows, account recovery, and accessibility requirements.",
        {"aspect": "ux"}
    )
    
    print(f"✅ Text contribution submitted: {text_hash[:8]}...")
    
    # Create dummy files for image, audio, and video contributions
    dummy_image_path = Path("dummy_diagram.png")
    dummy_audio_path = Path("dummy_explanation.mp3")
    dummy_video_path = Path("dummy_demo.mp4")
    
    # Create dummy files
    dummy_image_path.touch()
    dummy_audio_path.touch()
    dummy_video_path.touch()
    
    # Submit an image contribution
    image_hash = mm_ai_merge.submit_image_contribution(
        "gemini-001",
        dummy_image_path,
        {"type": "architecture_diagram"}
    )
    
    print(f"✅ Image contribution submitted: {image_hash[:8]}...")
    
    # Submit an audio contribution
    audio_hash = mm_ai_merge.submit_audio_contribution(
        "gemini-001",
        dummy_audio_path,
        {"type": "explanation"}
    )
    
    print(f"✅ Audio contribution submitted: {audio_hash[:8]}...")
    
    # Submit a video contribution
    video_hash = mm_ai_merge.submit_video_contribution(
        "gemini-001",
        dummy_video_path,
        {"type": "demo"}
    )
    
    print(f"✅ Video contribution submitted: {video_hash[:8]}...")
    
    # Merge contributions using cross-modal synthesis
    result = mm_ai_merge.merge_all_contributions(
        "cross_modal_synthesis",
        "Implementing user authentication system"
    )
    
    print(f"\n🎯 Multi-Modal Merge Result:")
    print(f"   Strategy: {result.strategy}")
    print(f"   Output modality: {result.output_modality.value}")
    print(f"   Confidence: {result.confidence_score:.2f}")
    print(f"   Contributing agents: {', '.join(result.contributing_agents)}")
    print(f"   Merged content preview:\n{result.merged_content.text[:300] if result.merged_content.text else 'No text content'}{'...' if result.merged_content.text and len(result.merged_content.text) > 300 else ''}")
    
    # Clean up dummy files
    try:
        dummy_image_path.unlink()
        dummy_audio_path.unlink()
        dummy_video_path.unlink()
    except:
        pass  # Ignore cleanup errors
    
    print(f"\n✅ Multi-modal usage example completed!")

if __name__ == "__main__":
    main()