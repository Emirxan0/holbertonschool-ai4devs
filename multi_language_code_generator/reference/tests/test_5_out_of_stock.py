import unittest
import json
from log_analyzer import RecommendationEngine

class TestOutOfStock(unittest.TestCase):
    def test_out_of_stock(self):
        user_db = {
            "user_A": ["prod_1"],
            "user_B": ["prod_1", "prod_2"]
        }
        metadata = [
            {"id": "prod_1", "stock": 5},
            {"id": "prod_2", "stock": 0}
        ]
        engine = RecommendationEngine(user_db, metadata)
        res = json.loads(engine.get_recommendations("user_A"))
        self.assertEqual(res["recommendations"], [])
