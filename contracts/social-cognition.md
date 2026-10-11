# Social Cognition Module Contract

## Status
IMPLEMENTED — 5 unit tests passing.
Formal contract validation and system integration remain pending.

## Responsibility
Represent modeled interpretations of social cues and interpersonal context.

## Input
- stimulus_id: non-empty string
- social_relevance: finite number in [0.0, 1.0]
- perceived_acceptance: finite number in [0.0, 1.0]

## Output
- module_id: social_cognition
- stimulus_id: identifier for the current stimulus
- social_relevance: validated value in [0.0, 1.0]
- perceived_acceptance: validated value in [0.0, 1.0]

## Invariants
- Invalid inputs must be rejected.
- Perceived acceptance represents the simulator's modeled interpretation, not verified opinions or intentions of other people.
- Social relevance represents modeled relevance, not objective social importance.
- The module must not calculate self-worth or self-trust.
- The module must not directly control other modules.
- System-level integration is outside this module's responsibility.
