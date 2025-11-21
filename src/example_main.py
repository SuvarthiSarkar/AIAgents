from .models import Job,NodeState,SystemState
from .agents import LatencyAgent,EnergyAgent,ReliabilityAgent,CostAgent
from .coordinator import Coordinator
def build_state():
    return SystemState([
      NodeState('edge-1',True,8,16,0,0.5,0.4,0,10,120,0.01,0.02),
      NodeState('edge-2',True,4,8,0,0.8,0.7,0,8,90,0.008,0.05),
      NodeState('cloud-1',False,32,64,4,0.3,0.3,0.2,45,400,0.03,0.01)])
def main():
    job=Job('job-123','AR_STREAM',50,1.5,2.0,0)
    st=build_state()
    agents=[LatencyAgent(),EnergyAgent(),ReliabilityAgent(),CostAgent()]
    scores=[a.score_nodes(job,st) for a in agents]
    dec=Coordinator().aggregate(scores)
    print('Chosen:',dec.chosen_node_id)
if __name__=='__main__': main()
