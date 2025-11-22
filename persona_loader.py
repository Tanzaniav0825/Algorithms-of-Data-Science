from typing import List, Dict, Any

# In-code persona database to avoid file path issues in deployment.
PERSONAS: List[Dict[str, Any]] = [
    {
        "id": "tech_savvy_power_user",
        "name": "Jordan (Tech-Savvy PM)",
        "role": "Product Manager",
        "demographics": {
            "age_range": "30-40",
            "location": "Urban, US",
            "family_status": "Single"
        },
        "tech_skill_level": "advanced",
        "usage_context": "Uses the app daily at work to coordinate feature launches and share updates with the team.",
        "goals": [
            "Share content with the team as fast as possible",
            "Avoid friction in daily workflows",
            "Get quick visual confirmation that things were shared"
        ],
        "frustrations": [
            "Slow UI or extra clicks",
            "Unclear icons or labels",
            "Hidden privacy toggles"
        ],
        "behavior_style": {
            "tone": "direct, analytical",
            "risk_attitude": "low tolerance for downtime",
            "feedback_depth": "detailed and structured"
        },
        "channels": ["web", "mobile"],
        "scenario_tags": ["quick_share", "productivity", "team_collaboration"],
        "constraints": [
            "Needs clear audit trail of what was shared and when"
        ]
    },
    {
        "id": "busy_parent_casual",
        "name": "Riley (Busy Parent)",
        "role": "Caregiver",
        "demographics": {
            "age_range": "35-45",
            "location": "Suburban, US",
            "family_status": "Two kids under 10"
        },
        "tech_skill_level": "beginner",
        "usage_context": "Uses the app in short bursts on mobile in the evenings and weekends.",
        "goals": [
            "Quickly share photos and updates with family",
            "Avoid complicated settings",
            "Keep everything kid-safe"
        ],
        "frustrations": [
            "Long onboarding flows",
            "Too many notifications",
            "Tiny text and low contrast"
        ],
        "behavior_style": {
            "tone": "warm, practical",
            "risk_attitude": "cautious about kids' privacy",
            "feedback_depth": "medium depth, focused on convenience"
        },
        "channels": ["mobile"],
        "scenario_tags": ["onboarding_tooltip", "notifications", "family_sharing"],
        "constraints": [
            "Frequently interrupted while using the app",
            "Prefers one-tap actions"
        ]
    },
    {
        "id": "privacy_focused_professional",
        "name": "Sam (Privacy-Focused Lawyer)",
        "role": "Legal Counsel",
        "demographics": {
            "age_range": "40-50",
            "location": "Urban, EU",
            "family_status": "Married, no kids"
        },
        "tech_skill_level": "intermediate",
        "usage_context": "Uses the app to review documents and share sensitive content with clients.",
        "goals": [
            "Avoid accidental data leaks",
            "Understand exactly who can see shared content",
            "Ensure compliance with regulations"
        ],
        "frustrations": [
            "Ambiguous privacy labels",
            "Auto-sharing defaults",
            "Dark-pattern prompts"
        ],
        "behavior_style": {
            "tone": "formal, precise",
            "risk_attitude": "very risk-averse",
            "feedback_depth": "deep, focused on edge cases"
        },
        "channels": ["web"],
        "scenario_tags": ["quick_share", "permissions", "access_control"],
        "constraints": [
            "Must comply with strict confidentiality rules"
        ]
    },
    {
        "id": "accessibility_first_user",
        "name": "Avery (Accessibility Advocate)",
        "role": "UX Researcher",
        "demographics": {
            "age_range": "25-35",
            "location": "Urban, US",
            "family_status": "Single"
        },
        "tech_skill_level": "advanced",
        "usage_context": "Uses the app daily with assistive technologies such as screen readers and keyboard navigation.",
        "goals": [
            "Complete tasks without visual-only cues",
            "Access all features via keyboard and screen reader",
            "Promote inclusive design"
        ],
        "frustrations": [
            "Missing alt text",
            "Unlabeled buttons",
            "Poor contrast and tiny touch targets"
        ],
        "behavior_style": {
            "tone": "constructive, advocacy-oriented",
            "risk_attitude": "medium",
            "feedback_depth": "very detailed on accessibility impacts"
        },
        "channels": ["web"],
        "scenario_tags": ["onboarding_tooltip", "settings", "accessibility"],
        "constraints": [
            "Relies heavily on screen reader feedback",
            "Avoids mouse-only interactions"
        ]
    },
    {
        "id": "social_super_user",
        "name": "Mia (Social Power User)",
        "role": "Content Creator",
        "demographics": {
            "age_range": "18-28",
            "location": "Global, often traveling",
            "family_status": "Single"
        },
        "tech_skill_level": "advanced",
        "usage_context": "Uses the app multiple times a day to share content with followers and friends.",
        "goals": [
            "Maximize engagement on posts",
            "Easily cross-post to multiple platforms",
            "Get quick stats and reactions"
        ],
        "frustrations": [
            "Rate limits with no explanation",
            "Inconsistent share previews",
            "Delayed notifications"
        ],
        "behavior_style": {
            "tone": "casual, expressive",
            "risk_attitude": "willing to experiment",
            "feedback_depth": "high when it affects reach"
        },
        "channels": ["mobile", "web"],
        "scenario_tags": ["quick_share", "analytics", "notifications"],
        "constraints": [
            "Time-sensitive posting windows"
        ]
    },
    {
        "id": "low_bandwidth_user",
        "name": "Diego (Low Connectivity User)",
        "role": "Field Worker",
        "demographics": {
            "age_range": "25-40",
            "location": "Rural, South America",
            "family_status": "Married"
        },
        "tech_skill_level": "intermediate",
        "usage_context": "Uses the app in areas with poor connectivity, mostly on a low-end Android phone.",
        "goals": [
            "Share updates even with weak signal",
            "Avoid losing unsent content",
            "Use as little data as possible"
        ],
        "frustrations": [
            "Infinite spinners with no offline support",
            "Large image uploads failing silently",
            "Features that assume fast Wi-Fi"
        ],
        "behavior_style": {
            "tone": "pragmatic, concise",
            "risk_attitude": "cautious about wasting time",
            "feedback_depth": "medium, very context-specific"
        },
        "channels": ["mobile"],
        "scenario_tags": ["offline_mode", "quick_share"],
        "constraints": [
            "Limited data plan and battery",
            "Works in noisy environments"
        ]
    },
    {
        "id": "new_to_tech_senior",
        "name": "Evelyn (New Tech Senior)",
        "role": "Retired Teacher",
        "demographics": {
            "age_range": "65-75",
            "location": "Suburban, US",
            "family_status": "Widowed, many grandchildren"
        },
        "tech_skill_level": "beginner",
        "usage_context": "Uses the app mainly to keep in touch with family and receive photos.",
        "goals": [
            "Easily see photos and messages",
            "Avoid making mistakes when pressing buttons",
            "Feel confident using the app alone"
        ],
        "frustrations": [
            "Tiny fonts and complex menus",
            "Jargon or slang in labels",
            "Overwhelming first-time setup"
        ],
        "behavior_style": {
            "tone": "polite, hesitant",
            "risk_attitude": "very cautious",
            "feedback_depth": "short, focused on confusion points"
        },
        "channels": ["tablet"],
        "scenario_tags": ["onboarding_tooltip", "accessibility"],
        "constraints": [
            "Mild vision and dexterity limitations"
        ]
    },
    {
        "id": "security_engineer_paranoid",
        "name": "Noah (Security Engineer)",
        "role": "Security Engineer",
        "demographics": {
            "age_range": "30-40",
            "location": "Urban, US",
            "family_status": "In a relationship"
        },
        "tech_skill_level": "expert",
        "usage_context": "Uses the app to test integrations and occasionally for personal communication.",
        "goals": [
            "Understand exactly what happens to shared data",
            "Verify encryption and storage practices",
            "Avoid any unnecessary data collection"
        ],
        "frustrations": [
            "Opaque data policies",
            "In-app trackers and third-party scripts",
            "Features enabled without explicit consent"
        ],
        "behavior_style": {
            "tone": "skeptical, technical",
            "risk_attitude": "paranoid about security",
            "feedback_depth": "very deep on security behaviors"
        },
        "channels": ["web"],
        "scenario_tags": ["permissions", "quick_share", "settings"],
        "constraints": [
            "Blocks many trackers at browser level"
        ]
    }
]


def load_personas() -> List[Dict[str, Any]]:
    """Return the in-code persona database."""
    return PERSONAS

