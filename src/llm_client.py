import json
from openai import OpenAI
from .config import OPENAI_MODEL,OPENAI_MAX_TOKENS
client=OpenAI()
def call_llm_json(system_prompt,user_prompt,extra_input=None,temperature=0.2):
    full=f'System:\n{system_prompt}\n\nUser:\n{user_prompt}\n'
    if extra_input:
        full+='\nAdditional data:\n'+''.join(json.dumps(e,indent=2)+'\n' for e in extra_input)
    resp=client.responses.create(model=OPENAI_MODEL,input=full,max_output_tokens=OPENAI_MAX_TOKENS,temperature=temperature)
    text=resp.output[0].content[0].text
    s=text.find('{'); e=text.rfind('}')
    if s==-1 or e==-1: raise RuntimeError(text)
    return json.loads(text[s:e+1])
