from .config import AGENT_WEIGHTS,EPS
from .models import Decision

class Coordinator:
    def __init__(self,agent_weights=None): self.agent_weights=agent_weights or AGENT_WEIGHTS
    def _norm(self,s):
        vals=list(s.values()); vmin=min(vals); vmax=max(vals)
        return {k:0.5 for k in s} if abs(vmax-vmin)<EPS else {k:(v-vmin)/(vmax-vmin) for k,v in s.items()}
    def aggregate(self,alist):
        nodes=set().union(*[set(a.scores) for a in alist])
        norm={a.agent_name:self._norm(a.scores) for a in alist}
        comb={nid:0 for nid in nodes}
        for an,ns in norm.items():
            w=self.agent_weights.get(an,0)
            for nid in nodes: comb[nid]+=w*ns.get(nid,0)
        chosen=max(comb,key=comb.get)
        return Decision(chosen,comb,{a.agent_name:a.scores for a in alist})
