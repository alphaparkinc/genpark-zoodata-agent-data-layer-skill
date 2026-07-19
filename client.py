import time, hashlib

class ZooDataAgentDataLayerClient:
    MOCK_DATA = {
        "market": [
            {"symbol": "AAPL", "price": 215.42, "change_pct": 1.2},
            {"symbol": "NVDA", "price": 142.87, "change_pct": -0.8},
            {"symbol": "MSFT", "price": 498.23, "change_pct": 0.5}
        ],
        "news": [
            {"headline": "AI spending reaches record $450B in H1 2026", "source": "Reuters"},
            {"headline": "OpenAI launches GPT-5 with 10M context window", "source": "TechCrunch"}
        ],
        "ecommerce": [
            {"product": "iPhone 17 Pro", "avg_price": 1199.00, "trend": "rising"},
            {"product": "Samsung S26 Ultra", "avg_price": 1099.00, "trend": "stable"}
        ]
    }

    def fetch(self, data_query: str, data_category: str) -> dict:
        t0 = time.time()
        records = self.MOCK_DATA.get(data_category.lower(), [])
        filtered = [r for r in records if any(
            data_query.lower() in str(v).lower() for v in r.values()
        )] or records
        freshness = int((time.time() - t0) * 1000)
        return {"structured_records": filtered, "freshness_ms": freshness}
