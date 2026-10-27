# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI


#创建了与Ai大模型交换的客户端对象(DEEPSEEK_API_KEY 环境变量的名字,值就是DeepSeek的 Api_key)
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

#与AI大模型进行交换()
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个AI助手,你的名字是小甜甜,请使用温柔的语气回答客户的问题"},
        {"role": "user", "content": "你是谁,你能帮我我做什么?"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)
#输出大模型返回的结果
print(response.choices[0].message.content)