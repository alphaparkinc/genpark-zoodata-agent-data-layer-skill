from client import ZooDataAgentDataLayerClient
client = ZooDataAgentDataLayerClient()
result = client.fetch(data_query="AI", data_category="news")
print(f"Fetched {len(result['structured_records'])} records in {result['freshness_ms']}ms:")
for r in result["structured_records"]:
    print(f"  {r}")
