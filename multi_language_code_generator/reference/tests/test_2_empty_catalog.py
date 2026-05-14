import unittest
import json
from log_analyzer import RecommendationEngine

class TestEmptyCatalog(unittest.TestCase):
    def test_empty_catalog(self):
        engine = RecommendationEngine({}, [])
        res = json.loads(engine.get_recommendations("user_A"))
        self.assertEqual(res["recommendations"], [])
        self.assertEqual(res["status"], "No products available")
