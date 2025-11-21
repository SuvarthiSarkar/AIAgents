from dataclasses import dataclass
from typing import Dict, List, Any
@dataclass
class Job: job_id:str; job_type:str; sla_ms:int; cpu_demand:float; mem_demand_gb:float; gpu_demand:float=0.0; metadata:Dict[str,Any]=None
@dataclass
class NodeState: node_id:str; is_edge:bool; cpu_capacity:float; mem_capacity_gb:float; gpu_capacity:float; cpu_util:float; mem_util:float; gpu_util:float; est_net_latency_ms:float; est_power_watts:float; price_per_cpu_hour:float; failure_rate:float; extra:Dict[str,Any]=None
@dataclass
class SystemState: nodes:List[NodeState]
@dataclass
class AgentScores: agent_name:str; scores:Dict[str,float]
@dataclass
class Decision: chosen_node_id:str; per_node_score:Dict[str,float]; per_agent_scores:Dict[str,Dict[str,float]]
