import unittest

from src.cognition.semantic_memory import evaluate


class SemanticMemoryTests(unittest.TestCase):
    def test_valid_activation(self):
        state = evaluate("stimulus-001", 0.75)
        self.assertEqual(state.module_id, "semantic_memory")
        self.assertEqual(state.stimulus_id, "stimulus-001")
        self.assertEqual(state.activation, 0.75)

    def test_boundary_activations(self):
        self.assertEqual(evaluate("s", 0.0).activation, 0.0)
        self.assertEqual(evaluate("s", 1.0).activation, 1.0)

    def test_rejects_out_of_range_activation(self):
        for value in (-0.1, 1.1):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    evaluate("s", value)

    def test_rejects_non_finite_activation(self):
        for value in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    evaluate("s", value)

    def test_rejects_boolean_activation(self):
        with self.assertRaises(ValueError):
            evaluate("s", True)

    def test_rejects_empty_stimulus_id(self):
        for stimulus_id in ("", "   "):
            with self.subTest(stimulus_id=stimulus_id):
                with self.assertRaises(ValueError):
                    evaluate(stimulus_id, 0.5)


if __name__ == "__main__":
    unittest.main()
