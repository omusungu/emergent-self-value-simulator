import unittest
from dataclasses import FrozenInstanceError

from src.cognition.semantic_memory import evaluate as evaluate_semantic_memory
from src.cognition.affective_systems import evaluate as evaluate_affective_systems
from src.cognition.metacognition import evaluate as evaluate_metacognition
from src.cognition.social_cognition import evaluate as evaluate_social_cognition
from src.cognition.integration import integrate


class IntegrationTests(unittest.TestCase):
    def make_states(self, stimulus_id="stimulus-001"):
        return (
            evaluate_semantic_memory(stimulus_id, 0.7),
            evaluate_affective_systems(stimulus_id, 0.6, -0.2),
            evaluate_metacognition(stimulus_id, 0.8, 0.2),
            evaluate_social_cognition(stimulus_id, 0.5, 0.7),
        )

    def test_aggregates_four_matching_states(self):
        semantic, affective, metacognition, social = self.make_states()

        result = integrate(semantic, affective, metacognition, social)

        self.assertEqual(result.stimulus_id, "stimulus-001")
        self.assertIs(result.semantic_memory, semantic)
        self.assertIs(result.affective_systems, affective)
        self.assertIs(result.metacognition, metacognition)
        self.assertIs(result.social_cognition, social)

    def test_rejects_mismatched_stimulus_ids(self):
        semantic, affective, metacognition, _ = self.make_states()
        social = evaluate_social_cognition("different-stimulus", 0.5, 0.7)

        with self.assertRaises(ValueError):
            integrate(semantic, affective, metacognition, social)

    def test_rejects_incorrect_state_type(self):
        semantic, affective, metacognition, _ = self.make_states()

        with self.assertRaises(TypeError):
            integrate(semantic, affective, metacognition, object())

    def test_rejects_incorrect_module_identity(self):
        semantic, affective, metacognition, social = self.make_states()
        invalid_semantic = type(semantic)(
            module_id="wrong_module",
            stimulus_id=semantic.stimulus_id,
            activation=semantic.activation,
        )

        with self.assertRaises(ValueError):
            integrate(invalid_semantic, affective, metacognition, social)

    def test_rejects_duplicated_module_state(self):
        semantic, affective, metacognition, _ = self.make_states()

        with self.assertRaises((TypeError, ValueError)):
            integrate(semantic, affective, metacognition, semantic)

    def test_requires_all_four_arguments(self):
        semantic, affective, metacognition, _ = self.make_states()

        with self.assertRaises(TypeError):
            integrate(semantic, affective, metacognition)

    def test_input_states_remain_unchanged(self):
        semantic, affective, metacognition, social = self.make_states()
        original_activation = semantic.activation

        result = integrate(semantic, affective, metacognition, social)

        self.assertEqual(semantic.activation, original_activation)
        with self.assertRaises(FrozenInstanceError):
            semantic.activation = 0.1
        self.assertIs(result.semantic_memory, semantic)


if __name__ == "__main__":
    unittest.main()
