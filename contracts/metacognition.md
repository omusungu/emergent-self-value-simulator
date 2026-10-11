# Metacognition Module Contract

## Status
IMPLEMENTED — 5 unit tests passing.
Formal contract validation and system integration remain pending.

## Responsibility
Represent the simulator's monitoring and evaluation of its own modeled processing state.

## Input
- stimulus_id: non-empty string
- confidence: finite number in [0.0, 1.0]
- uncertainty: finite number in [0.0, 1.0]

## Output
- module_id: metacognition
- stimulus_id: identifier for the current stimulus
- confidence: validated value in [0.0, 1.0]
- uncertainty: validated value in [0.0, 1.0]

## Invariants
- Invalid inputs must be rejected.
- Confidence represents modeled confidence, not objective correctness.
- Uncertainty represents modeled uncertainty, not a calibrated probability unless calibration is separately established.
- The module must not calculate self-worth or self-trust.
- The module must not directly control other modules.
- System-level integration is outside this module's responsibility.
