# Emergent Self-Value Simulator

An experimental Python project exploring how specialized cognitive modules can be combined into a unified simulated state.

## Project purpose

The project models interactions among four specialized modules:

1. **Semantic Memory** — represents modeled memory activation.
2. **Affective Systems** — represents modeled affective activation and valence.
3. **Metacognition** — represents modeled confidence and uncertainty.
4. **Social Cognition** — represents modeled social relevance and perceived acceptance.

The long-term aim is to explore how these modules might contribute to modeled Self-Value and Self-Trust. These outputs are proposed goals, not currently implemented or scientifically validated measurements.

## Current implementation

- Four specialized cognitive modules with input validation.
- An aggregation-only integration layer that combines one state from each module for the same stimulus.
- Validation of expected state types, module identities, and matching stimulus identifiers.
- Immutable state objects and automated unit tests.

The integration layer preserves the supplied module states. It does not calculate Self-Value or Self-Trust.

## Not yet implemented

- Global Workspace
- Predictive Feedback
- Inter-module Connections
- Self-Value and Self-Trust calculations
- Interactive user interface

The cognitive integration contract is a draft and has not been approved or frozen.

## Run the tests

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

The current test suite contains 28 tests.

## Scientific and interpretive limitations

This project is an experimental software simulation, not a validated psychological model or diagnostic tool. Its internal values are modeled variables and should not be interpreted as objective measurements of a person's psychological state.

Passing software tests demonstrates tested software behavior, not scientific validity.

## Development approach

The project prioritizes small, testable Python components, explicit module responsibilities, inspectable integration rules, and clear separation between implemented behavior and future design goals.
