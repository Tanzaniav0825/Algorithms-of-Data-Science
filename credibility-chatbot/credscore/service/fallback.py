def fallback_score(req):
 s_prior=0.6 if req.citations else 0.5
 c_simple=0.5+min(0.4,0.002*len(req.answer))
 p=0.5*s_prior+0.5*c_simple
 return {"score":p,"label":"high" if p>0.8 else "medium" if p>0.6 else "low","confidence_interval":[max(0.0,p-0.15),min(1.0,p+0.15)]}
