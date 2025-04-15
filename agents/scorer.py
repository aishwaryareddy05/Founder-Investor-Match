
from typing import Dict, List

def score_matches(state: Dict) -> Dict:
    matches = state["raw_matches"]

    # Extract similarities for normalization
    similarities = [m["similarity"] for m in matches]
    max_sim = max(similarities) if similarities else 1.0

    # Convert to percentage scores
    scored = []
    for m in matches:
        score = round((m["similarity"] / max_sim) * 100, 2)

        # Parse the profile string to extract more info (if structured with |)
        profile_parts = m["profile"].split(" | ")
        profile_text = (
            f"Name: {m['name']}\n"
            f"Score: {score}%\n"
        )
        if len(profile_parts) >= 6:
            profile_text += (
                f"Investment Range: ${profile_parts[1]} - ${profile_parts[2]}\n"
                f"Sectors: {profile_parts[3]}\n"
                f"Stages: {profile_parts[4]}\n"
                f"Description: {profile_parts[5]}\n"
            )
        profile_text += "-" * 60

        scored.append({
            "name": m["name"],
            "score": score,
            "profile": profile_text
        })

    return {"query": state["query"], "matches": scored}

