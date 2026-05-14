import unittest
import json
from log_analyzer import RecommendationEngine

class TestNoSimilarity(unittest.TestCase):
    def test_no_similarity(self):
        user_db = {
            "user_A": ["prod_1"],
            "user_B": ["prod_2"]
        }
        metadata = [
            {"id": "prod_1", "stock": 5},
            {"id": "prod_2", "stock": 5}
        ]
        engine = RecommendationEngine(user_db, metadata)
        res = json.loads(engine.get_recommendations("user_A"))
        self.assertEqual(res["recommendations"], [])
