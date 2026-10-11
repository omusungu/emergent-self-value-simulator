# Affective Systems Module Contract

## Status
DRAFT — not implemented or validated.

## Responsibility
Represent the modeled affective response to a stimulus.

## Input
- stimulus_id: non-empty string
- activation: finite number in [0.0, 1.0]
- valence: finite number in [-1.0, 1.0]

## Output
- module_id: affective_systems
- stimulus_id: identifier for the current stimulus
- activation: validated value in [0.0, 1.0]
- valence: validated value in [-1.0, 1.0]

## Invariants
- Invalid inputs must be rejected.
- Activation represents response intensity, not positivity.
- Valence represents modeled negative-to-positive direction.
- The module must not calculate self-worth or self-trust.
- The module must not directly control other modules.
- System-level integration is outside this module's responsibility.
