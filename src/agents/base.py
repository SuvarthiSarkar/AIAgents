from abc import ABC,abstractmethod
from ..models import Job,SystemState,AgentScores
class BaseAgent(ABC):
    def __init__(self,name): self.name=name
    @abstractmethod
    def score_nodes(self,job:Job,system_state:SystemState)->AgentScores:...
