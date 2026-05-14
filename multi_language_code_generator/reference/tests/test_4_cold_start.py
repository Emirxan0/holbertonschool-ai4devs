import unittest
import json
from log_analyzer import RecommendationEngine

class TestColdStart(unittest.TestCase):
    def test_cold_start(self):
        user_db = {"user_A": ["prod_1"]}
        metadata = [
            {"id": "prod_1", "stock": 5},
            {"id": "prod_2", "stock": 10}
        ]
        engine = RecommendationEngine(user_db, metadata)
        res = json.loads(engine.get_recommendations("user_new"))
        self.assertEqual(res["status"], "Cold start fallback triggered")
        self.assertEqual(res["recommendations"][0]["product_id"], "prod_1")
