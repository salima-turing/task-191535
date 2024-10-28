import unittest

# Your cross-selling logic function
from cross_selling_logic import suggest_cross_sell

class TestCrossSellingTactics(unittest.TestCase):

    def setUp(self):
        # Set up test data
        self.test_data = [
            # Example 1: Customer buys A, should be recommended B
            ([1, 2], [2]),
            # Example 2: Customer buys A and C, should be recommended B
            ([1, 3], [2]),
            # Example 3: Customer buys B, should not be recommended A
            ([2], []),
            # Add more test cases as needed
        ]

    def test_cross_selling_tactics(self):
        for purchase_history, expected_recommendations in self.test_data:
            with self.subTest(purchase_history=purchase_history):
                recommendations = suggest_cross_sell(purchase_history)
                self.assertEqual(recommendations, expected_recommendations,
                                 f"Recommendations {recommendations} do not match expected {expected_recommendations}")

if __name__ == '__main__':
    unittest.main()
