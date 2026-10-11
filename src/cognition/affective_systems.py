from dataclasses import dataclass
import math


@dataclass(frozen=True)
class AffectiveSystemsState:
    module_id: str
    stimulus_id: str
    activation: float
    valence: float


def evaluate(
    stimulus_id: str,
    activation: float,
    valence: float,
) -> AffectiveSystemsState:
    if not isinstance(stimulus_id, str) or not stimulus_id.strip():
        raise ValueError("stimulus_id must be a non-empty string")

    if isinstance(activation, bool) or not isinstance(
        activation, (int, float)
    ):
        raise ValueError("activation must be a finite number")

    activation = float(activation)

    if not math.isfinite(activation) or not 0.0 <= activation <= 1.0:
        raise ValueError("activation must be finite and in [0.0, 1.0]")

    if isinstance(valence, bool) or not isinstance(valence, (int, float)):
        raise ValueError("valence must be a finite number")

    valence = float(valence)

    if not math.isfinite(valence) or not -1.0 <= valence <= 1.0:
        raise ValueError("valence must be finite and in [-1.0, 1.0]")

    return AffectiveSystemsState(
        module_id="affective_systems",
        stimulus_id=stimulus_id,
        activation=activation,
        valence=valence,
    )
