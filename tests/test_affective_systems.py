import unittest

from src.cognition.affective_systems import evaluate


class AffectiveSystemsTests(unittest.TestCase):
    def test_valid_state(self):
        state = evaluate("stimulus-001", 0.75, -0.4)
        self.assertEqual(state.module_id, "affective_systems")
        self.assertEqual(state.stimulus_id, "stimulus-001")
        self.assertEqual(state.activation, 0.75)
        self.assertEqual(state.valence, -0.4)

    def test_boundary_values(self):
        state = evaluate("stimulus-001", 0.0, -1.0)
        self.assertEqual(state.activation, 0.0)
        self.assertEqual(state.valence, -1.0)

        state = evaluate("stimulus-002", 1.0, 1.0)
        self.assertEqual(state.activation, 1.0)
        self.assertEqual(state.valence, 1.0)

    def test_rejects_empty_stimulus_id(self):
        with self.assertRaises(ValueError):
            evaluate("   ", 0.5, 0.0)

    def test_rejects_invalid_activation(self):
        for value in (-0.1, 1.1, float("nan"), float("inf"), float("-inf"), True):
            with self.subTest(activation=value):
                with self.assertRaises(ValueError):
                    evaluate("stimulus-001", value, 0.0)

    def test_rejects_invalid_valence(self):
        for value in (-1.1, 1.1, float("nan"), float("inf"), float("-inf"), True):
            with self.subTest(valence=value):
                with self.assertRaises(ValueError):
                    evaluate("stimulus-001", 0.5, value)


if __name__ == "__main__":
    unittest.main()
