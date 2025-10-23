from fastapi.testclient import TestClient
from credscore.service.app import app
def test_score_endpoint_contract():
 c=TestClient(app); r=c.post("/v1/credibility/score", json={"query":"Q","answer":"A","citations":[{"url":"https://example.com"}],"timeout_ms":500}); assert r.status_code==200; body=r.json(); assert 'score' in body and 'label' in body and 'latency_ms' in body
