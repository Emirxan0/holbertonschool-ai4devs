import unittest
import json
from log_analyzer import RecommendationEngine

class TestInvalidUser(unittest.TestCase):
    def test_invalid_user(self):
        engine = RecommendationEngine({}, [{"id": "prod_1", "stock": 5}])
        res = json.loads(engine.get_recommendations(None))
        self.assertIn("error", res)
        self.assertEqual(res["error"], "Invalid User ID format")
