# Cognitive Integration Contract

## Status
DRAFT — implemented and tested; contract not approved or frozen.

## Responsibility
Aggregate the four specialized module states for one stimulus
without changing their individual responsibilities or state values.

## Required inputs
- One SemanticMemoryState.
- One AffectiveSystemsState.
- One MetacognitionState.
- One SocialCognitionState.

## Initial output
- stimulus_id: the shared stimulus identifier.
- semantic_memory: the original semantic memory state.
- affective_systems: the original affective systems state.
- metacognition: the original metacognition state.
- social_cognition: the original social cognition state.

## Invariants
- Exactly one state from each required module must be supplied.
- Each state must have the expected module identity.
- All four states must have the same stimulus_id.
- Invalid or inconsistent inputs must be rejected.
- Input states must not be mutated.
- The aggregate must not calculate Self-Value or Self-Trust.
- This increment does not implement the Global Workspace,
  Predictive Feedback, or Inter-module Connections.
- Aggregation does not establish scientific or psychological validity.

## Implementation boundary
- The integration function validates each argument's expected state class.
- It validates each state's expected module identity.
- It validates that all four states share the same stimulus_id.
- It relies on the module evaluation functions for module-specific value validation.
- Directly constructed state instances may bypass module evaluation validation.
- Passing tests establish tested software behavior, not scientific or psychological validity.

## Validation plan
- Test a valid set of four states.
- Test mismatched stimulus identifiers.
- Test missing, duplicated, or incorrectly typed module states.
- Test incorrect module identities.
- Verify that original states remain unchanged.
