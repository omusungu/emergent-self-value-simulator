from dataclasses import dataclass
import math


@dataclass(frozen=True)
class SemanticMemoryState:
    module_id: str
    stimulus_id: str
    activation: float


def evaluate(stimulus_id: str, activation: float) -> SemanticMemoryState:
    if not isinstance(stimulus_id, str) or not stimulus_id.strip():
        raise ValueError("stimulus_id must be a non-empty string")

    if isinstance(activation, bool) or not isinstance(
        activation, (int, float)
    ):
        raise ValueError("activation must be a finite number")

    activation = float(activation)

    if not math.isfinite(activation) or not 0.0 <= activation <= 1.0:
        raise ValueError("activation must be finite and in [0.0, 1.0]")

    return SemanticMemoryState(
        module_id="semantic_memory",
        stimulus_id=stimulus_id,
        activation=activation,
    )
