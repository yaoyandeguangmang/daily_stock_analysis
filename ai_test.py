import os
from openai import OpenAI

# 配置免费模型客户端
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://aihubmix.com/v1"
)

# 免费模型名称，可替换为 gpt-4o-free / deepseek-r1-free 等
MODEL = "glm-5-free"

try:
    # 发送请求
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": "你好，请介绍一下自己"}]
    )
    print("✅ AI回复：")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ 错误：", e)
