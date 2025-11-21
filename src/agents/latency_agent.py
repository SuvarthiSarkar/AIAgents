from ..llm_client import call_llm_json
from ..models import AgentScores
from .base import BaseAgent
class LatencyAgent(BaseAgent):
    def __init__(self): super().__init__('latency')
    def score_nodes(self,job,system):
        sys='You score latency 0-1. Return JSON {"scores":{}}.'
        nodes=[{'node_id':n.node_id,'lat':n.est_net_latency_ms,'cpu':n.cpu_util} for n in system.nodes]
        usr=f'Job:{job}\nNodes:{nodes}'
        res=call_llm_json(sys,usr)
        return AgentScores(self.name,res.get('scores',{}))
