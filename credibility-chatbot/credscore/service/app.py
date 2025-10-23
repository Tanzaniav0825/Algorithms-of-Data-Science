from fastapi import FastAPI
from pydantic import BaseModel
from .fallback import fallback_score
from .metrics import METRICS
import time
app=FastAPI(title="Credibility Scoring Service",version="0.1.0")
class Citation(BaseModel):
 url:str; title:str|None=None; author:str|None=None; published_at:str|None=None
class ScoreRequest(BaseModel):
 query:str; answer:str; citations:list[Citation]=[]; return_explanations:bool=True; timeout_ms:int=1800
@app.get("/health")
async def health():
 return {"ok":True}
@app.post("/v1/credibility/score")
async def score(req:ScoreRequest):
 t0=time.perf_counter(); fb=fallback_score(req); METRICS.observe(latency_ms=int((time.perf_counter()-t0)*1000), ok=True)
 return {**fb, 'explanations':None, 'warnings':[], 'latency_ms':int((time.perf_counter()-t0)*1000)}
