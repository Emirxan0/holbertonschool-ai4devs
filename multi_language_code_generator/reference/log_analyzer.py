import json

class RecommendationEngine:
    def __init__(self, user_db: dict, product_metadata: list):
        self.user_db = user_db
        self.product_metadata = {p["id"]: p for p in product_metadata}

    def _calculate_similarity(self, user_history_1: list, user_history_2: list) -> float:
        set1, set2 = set(user_history_1), set(user_history_2)
        if not set1 or not set2:
            return 0.0
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        return len(intersection) / len(union)

    def get_recommendations(self, target_user_id: str, top_n: int = 5) -> str:
        if not self.product_metadata:
            return json.dumps({"recommendations": [], "status": "No products available"})

        if not target_user_id or not isinstance(target_user_id, str):
            return json.dumps({"error": "Invalid User ID format"})

        if target_user_id not in self.user_db or not self.user_db[target_user_id]:
            trending = [pid for pid, p in self.product_metadata.items() if p.get("stock", 0) > 0][:top_n]
            return json.dumps({
                "recommendations": [{"product_id": pid, "score": 0.5} for pid in trending],
                "status": "Cold start fallback triggered"
            })

        target_history = set(self.user_db[target_user_id])
        candidate_scores = {}

        for other_user, other_history in self.user_db.items():
            if other_user == target_user_id:
                continue
            
            sim = self._calculate_similarity(list(target_history), other_history)
            if sim <= 0:
                continue

            for prod_id in other_history:
                if prod_id not in target_history:
                    if self.product_metadata.get(prod_id, {}).get("stock", 0) <= 0:
                        continue
                    candidate_scores[prod_id] = candidate_scores.get(prod_id, 0) + sim

        sorted_candidates = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
        
        recommendations = []
        for pid, score in sorted_candidates:
            normalized_score = min(round(score, 2), 1.0)
            recommendations.append({"product_id": pid, "score": normalized_score})

        return json.dumps({"recommendations": recommendations, "status": "success"})
