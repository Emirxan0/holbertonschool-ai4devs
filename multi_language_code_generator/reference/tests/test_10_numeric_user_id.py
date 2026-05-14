import unittest
import json
from log_analyzer import RecommendationEngine

class TestNumericUserId(unittest.TestCase):
    def test_numeric_user_id(self):
        engine = RecommendationEngine({}, [])
        res = json.loads(engine.get_recommendations(12345))
        self.assertEqual(res["error"], "Invalid User ID format")
