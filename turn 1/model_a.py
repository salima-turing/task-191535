import unittest
from collections import defaultdict

def cross_sell_recommender(customer_history, product_a, product_b, min_confidence=0.8):
	"""
	Simple cross-sell recommender based on customer history.
	Assumes history is a dict of customer IDs to lists of product IDs.
	"""

	bought_together = defaultdict(int)
	total_customers = len(customer_history)

	for customer, purchases in customer_history.items():
		if product_a in purchases:
			for purchase in purchases:
				if purchase == product_a:
					continue
				bought_together[purchase] += 1

	confidences = {
		p: bought_together[p] / total_customers for p in bought_together
	}

	if confidences.get(product_b, 0) >= min_confidence:
		return True
	return False

class TestCrossSellRecommender(unittest.TestCase):

	def setUp(self):
		self.customer_history = {
			1: ["Product_A", "Product_B", "Product_C"],
			2: ["Product_X", "Product_Y"],
			3: ["Product_A", "Product_Z"],
			4: ["Product_B", "Product_A", "Product_D"],
			5: ["Product_C"],
		}

	def test_cross_sell_recommendation_positive(self):
		product_a = "Product_A"
		product_b = "Product_B"
		min_confidence = 0.6
		result = cross_sell_recommender(self.customer_history, product_a, product_b, min_confidence)
		self.assertTrue(result, "Cross-sell recommendation should be positive")

	def test_cross_sell_recommendation_negative(self):
		product_a = "Product_X"
		product_b = "Product_Y"
		min_confidence = 0.6
		result = cross_sell_recommender(self.customer_history, product_a, product_b,min_confidence)
		self.assertFalse(result, "Cross-sell recommendation should be negative")

if __name__ == '__main__':
	unittest.main()
