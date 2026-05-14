import unittest
import json
from log_analyzer import RecommendationEngine

class TestColdStartNoStock(unittest.TestCase):
    def test_cold_start_no_stock(self):
        user_db = {"user_A": []}
        metadata = [{"id": "prod_1", "stock": 0}]
        engine = RecommendationEngine(user_db, metadata)
        res = json.loads(engine.get_recommendations("user_A"))
        self.assertEqual(res["recommendations"], [])
