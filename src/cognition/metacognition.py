from dataclasses import dataclass
import math


@dataclass(frozen=True)
class MetacognitionState:
    module_id: str
    stimulus_id: str
    confidence: float
    uncertainty: float


def evaluate(
    stimulus_id: str,
    confidence: float,
    uncertainty: float,
) -> MetacognitionState:
    if not isinstance(stimulus_id, str) or not stimulus_id.strip():
        raise ValueError("stimulus_id must be a non-empty string")

    if isinstance(confidence, bool) or not isinstance(
        confidence, (int, float)
    ):
        raise ValueError("confidence must be a finite number")

    confidence = float(confidence)

    if not math.isfinite(confidence) or not 0.0 <= confidence <= 1.0:
        raise ValueError("confidence must be finite and in [0.0, 1.0]")

    if isinstance(uncertainty, bool) or not isinstance(
        uncertainty, (int, float)
    ):
        raise ValueError("uncertainty must be a finite number")

    uncertainty = float(uncertainty)

    if not math.isfinite(uncertainty) or not 0.0 <= uncertainty <= 1.0:
        raise ValueError("uncertainty must be finite and in [0.0, 1.0]")

    return MetacognitionState(
        module_id="metacognition",
        stimulus_id=stimulus_id,
        confidence=confidence,
        uncertainty=uncertainty,
    )
