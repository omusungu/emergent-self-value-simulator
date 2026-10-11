import math
import unittest

from src.cognition.social_cognition import evaluate


class SocialCognitionTests(unittest.TestCase):
    def test_valid_state(self):
        state = evaluate("stimulus-1", 0.7, 0.8)

        self.assertEqual(state.module_id, "social_cognition")
        self.assertEqual(state.stimulus_id, "stimulus-1")
        self.assertEqual(state.social_relevance, 0.7)
        self.assertEqual(state.perceived_acceptance, 0.8)

    def test_boundary_values(self):
        state = evaluate("stimulus-2", 0.0, 1.0)

        self.assertEqual(state.social_relevance, 0.0)
        self.assertEqual(state.perceived_acceptance, 1.0)

    def test_rejects_empty_stimulus_id(self):
        with self.assertRaises(ValueError):
            evaluate(" ", 0.5, 0.5)

    def test_rejects_invalid_social_relevance(self):
        for value in (-0.1, 1.1, math.nan, math.inf, -math.inf, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    evaluate("stimulus-3", value, 0.5)

    def test_rejects_invalid_perceived_acceptance(self):
        for value in (-0.1, 1.1, math.nan, math.inf, -math.inf, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    evaluate("stimulus-4", 0.5, value)


if __name__ == "__main__":
    unittest.main()
