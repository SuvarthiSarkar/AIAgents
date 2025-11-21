from ..llm_client import call_llm_json
from ..models import AgentScores
from .base import BaseAgent
class ReliabilityAgent(BaseAgent):
    def __init__(self): super().__init__('reliability')
    def score_nodes(self,job,system):
        sys='Reliability scores 0-1. Return JSON.'
        nodes=[{'node_id':n.node_id,'fail':n.failure_rate} for n in system.nodes]
        usr=f'Job:{job}\nNodes:{nodes}'
        res=call_llm_json(sys,usr)
        return AgentScores(self.name,res.get('scores',{}))
