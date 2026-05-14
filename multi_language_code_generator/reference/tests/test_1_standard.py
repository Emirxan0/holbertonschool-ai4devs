import unittest
import json
from log_analyzer import RecommendationEngine

class TestRecommendation(unittest.TestCase):
    def test_dense_history(self):
        user_db = {
            "user_A": ["prod_1", "prod_2", "prod_3"],
            "user_B": ["prod_1", "prod_2", "prod_4"],
        }
        metadata = [
            {"id": "prod_1", "stock": 5},
            {"id": "prod_2", "stock": 12},
            {"id": "prod_3", "stock": 1},
            {"id": "prod_4", "stock": 8}
        ]
        
        engine = RecommendationEngine(user_db, metadata)
        res = json.loads(engine.get_recommendations("user_A"))
        
        self.assertEqual(res["recommendations"][0]["product_id"], "prod_4")
