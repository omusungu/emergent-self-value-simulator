from dataclasses import dataclass
import math


@dataclass(frozen=True)
class SocialCognitionState:
    module_id: str
    stimulus_id: str
    social_relevance: float
    perceived_acceptance: float


def evaluate(
    stimulus_id: str,
    social_relevance: float,
    perceived_acceptance: float,
) -> SocialCognitionState:
    if not isinstance(stimulus_id, str) or not stimulus_id.strip():
        raise ValueError("stimulus_id must be a non-empty string")

    if isinstance(social_relevance, bool) or not isinstance(
        social_relevance, (int, float)
    ):
        raise ValueError("social_relevance must be a finite number")

    social_relevance = float(social_relevance)

    if (
        not math.isfinite(social_relevance)
        or not 0.0 <= social_relevance <= 1.0
    ):
        raise ValueError(
            "social_relevance must be finite and in [0.0, 1.0]"
        )

    if isinstance(perceived_acceptance, bool) or not isinstance(
        perceived_acceptance, (int, float)
    ):
        raise ValueError("perceived_acceptance must be a finite number")

    perceived_acceptance = float(perceived_acceptance)

    if (
        not math.isfinite(perceived_acceptance)
        or not 0.0 <= perceived_acceptance <= 1.0
    ):
        raise ValueError(
            "perceived_acceptance must be finite and in [0.0, 1.0]"
        )

    return SocialCognitionState(
        module_id="social_cognition",
        stimulus_id=stimulus_id,
        social_relevance=social_relevance,
        perceived_acceptance=perceived_acceptance,
    )
