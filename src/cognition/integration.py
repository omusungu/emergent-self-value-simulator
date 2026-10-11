from dataclasses import dataclass

from src.cognition.semantic_memory import SemanticMemoryState
from src.cognition.affective_systems import AffectiveSystemsState
from src.cognition.metacognition import MetacognitionState
from src.cognition.social_cognition import SocialCognitionState


@dataclass(frozen=True)
class IntegratedCognitiveState:
    stimulus_id: str
    semantic_memory: SemanticMemoryState
    affective_systems: AffectiveSystemsState
    metacognition: MetacognitionState
    social_cognition: SocialCognitionState


def integrate(
    semantic_memory: SemanticMemoryState,
    affective_systems: AffectiveSystemsState,
    metacognition: MetacognitionState,
    social_cognition: SocialCognitionState,
) -> IntegratedCognitiveState:
    expected_states = (
        (semantic_memory, SemanticMemoryState, "semantic_memory"),
        (affective_systems, AffectiveSystemsState, "affective_systems"),
        (metacognition, MetacognitionState, "metacognition"),
        (social_cognition, SocialCognitionState, "social_cognition"),
    )

    for state, expected_type, expected_module_id in expected_states:
        if not isinstance(state, expected_type):
            raise TypeError(
                f"{expected_module_id} must be a {expected_type.__name__}"
            )
        if state.module_id != expected_module_id:
            raise ValueError(
                f"Expected module_id {expected_module_id!r}, "
                f"got {state.module_id!r}"
            )

    stimulus_ids = {
        semantic_memory.stimulus_id,
        affective_systems.stimulus_id,
        metacognition.stimulus_id,
        social_cognition.stimulus_id,
    }
    if len(stimulus_ids) != 1:
        raise ValueError("All module states must share the same stimulus_id")

    return IntegratedCognitiveState(
        stimulus_id=semantic_memory.stimulus_id,
        semantic_memory=semantic_memory,
        affective_systems=affective_systems,
        metacognition=metacognition,
        social_cognition=social_cognition,
    )
