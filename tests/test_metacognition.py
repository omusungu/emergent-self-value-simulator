import unittest

from src.cognition.metacognition import evaluate


class MetacognitionTests(unittest.TestCase):
    def test_valid_state(self):
        state = evaluate("stimulus-001", 0.8, 0.2)
        self.assertEqual(state.module_id, "metacognition")
        self.assertEqual(state.stimulus_id, "stimulus-001")
        self.assertEqual(state.confidence, 0.8)
        self.assertEqual(state.uncertainty, 0.2)

    def test_boundary_values(self):
        state = evaluate("stimulus-001", 0.0, 0.0)
        self.assertEqual(state.confidence, 0.0)
        self.assertEqual(state.uncertainty, 0.0)

        state = evaluate("stimulus-002", 1.0, 1.0)
        self.assertEqual(state.confidence, 1.0)
        self.assertEqual(state.uncertainty, 1.0)

    def test_rejects_empty_stimulus_id(self):
        with self.assertRaises(ValueError):
            evaluate("   ", 0.5, 0.5)

    def test_rejects_invalid_confidence(self):
        for value in (-0.1, 1.1, float("nan"), float("inf"), float("-inf"), True):
            with self.subTest(confidence=value):
                with self.assertRaises(ValueError):
                    evaluate("stimulus-001", value, 0.5)

    def test_rejects_invalid_uncertainty(self):
        for value in (-0.1, 1.1, float("nan"), float("inf"), float("-inf"), True):
            with self.subTest(uncertainty=value):
                with self.assertRaises(ValueError):
                    evaluate("stimulus-001", 0.5, value)


if __name__ == "__main__":
    unittest.main()
