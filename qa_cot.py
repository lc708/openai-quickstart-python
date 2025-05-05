import os, openai, sys
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#测试CoT
SYSTEM = "You are a helpful agent."
COT_INSTRUCTION = "Let's think step by step. First derive the reasoning, then provide the final answer after the words 'Answer:'."
question = " ".join(sys.argv[1:]) or "What is an AI agent?"
messages=[
    {"role":"system","content": SYSTEM},
    {"role":"user","content": f"{question}\n\n{COT_INSTRUCTION}"}
]
resp = openai.chat.completions.create(
        model="gpt-4.1-nano", 
        messages=messages,
        temperature=0.2
#        messages=[{"role":"user","content":question}]
)
print(resp.choices[0].message.content)

usage = resp.usage               # prompt_tokens, completion_tokens, total_tokens
cost  = usage.prompt_tokens * 0.0000001 + usage.completion_tokens * 0.0000004  # gpt-4.1-nano 输入 $0.1 / 1M tokens，输出$0.4 / 1M tokens
print(f"Total tokens: {usage.total_tokens}")
print(f"Approx cost : ${cost:.4f}")