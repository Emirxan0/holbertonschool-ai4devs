import unittest
import json
from log_analyzer import RecommendationEngine

class TestTopNLimit(unittest.TestCase):
    def test_top_n_limit(self):
        user_db = {
            "user_A": ["prod_1"],
            "user_B": ["prod_1", "prod_2", "prod_3", "prod_4"]
        }
        metadata = [
            {"id": "prod_1", "stock": 5},
            {"id": "prod_2", "stock": 5},
            {"id": "prod_3", "stock": 5},
            {"id": "prod_4", "stock": 5}
        ]
        engine = RecommendationEngine(user_db, metadata)
        res = json.loads(engine.get_recommendations("user_A", top_n=2))
        self.assertEqual(len(res["recommendations"]), 2)

