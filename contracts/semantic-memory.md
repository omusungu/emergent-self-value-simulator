# Semantic Memory Module Contract

## Responsibility
Represent the semantic activation associated with
the current stimulus.

## Input
- stimulus_id: identifier for the current stimulus
- activation: numeric value in the range [0.0, 1.0]

## Output
- module_id: semantic_memory
- stimulus_id: identifier for the current stimulus
- activation: validated numeric value in [0.0, 1.0]

## Invariants
- Activation must be finite and within [0.0, 1.0].
- Invalid input must be rejected.
- The module must not calculate self-worth or self-trust.
- The module must not directly control other modules.
- Integration belongs to a separate interaction mechanism.

## Status
IMPLEMENTED — 6 unit tests passing.
Formal contract validation and system integration remain pending.
