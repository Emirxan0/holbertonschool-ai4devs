import unittest
import json
from log_analyzer import RecommendationEngine

class TestPerfectMatch(unittest.TestCase):
    def test_perfect_match(self):
        user_db = {
            "user_A": ["prod_1", "prod_2"],
            "user_B": ["prod_1", "prod_2", "prod_3"]
        }
        metadata = [
            {"id": "prod_1", "stock": 5},
            {"id": "prod_2", "stock": 5},
            {"id": "prod_3", "stock": 5}
        ]
        engine = RecommendationEngine(user_db, metadata)
        res = json.loads(engine.get_recommendations("user_A"))
        self.assertEqual(res["recommendations"][0]["score"], 1.0)
