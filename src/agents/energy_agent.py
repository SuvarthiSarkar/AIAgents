from ..llm_client import call_llm_json
from ..models import AgentScores
from .base import BaseAgent
class EnergyAgent(BaseAgent):
    def __init__(self): super().__init__('energy')
    def score_nodes(self,job,system):
        sys='Energy scores 0-1. Return JSON.'
        nodes=[{'node_id':n.node_id,'power':n.est_power_watts,'cpu':n.cpu_util} for n in system.nodes]
        usr=f'Job:{job}\nNodes:{nodes}'
        res=call_llm_json(sys,usr)
        return AgentScores(self.name,res.get('scores',{}))
