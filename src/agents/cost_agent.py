from ..llm_client import call_llm_json
from ..models import AgentScores
from .base import BaseAgent
class CostAgent(BaseAgent):
    def __init__(self): super().__init__('cost')
    def score_nodes(self,job,system):
        sys='Cost scores 0-1. Return JSON.'
        nodes=[{'node_id':n.node_id,'price':n.price_per_cpu_hour,'cpu':n.cpu_util} for n in system.nodes]
        usr=f'Job:{job}\nNodes:{nodes}'
        res=call_llm_json(sys,usr)
        return AgentScores(self.name,res.get('scores',{}))
