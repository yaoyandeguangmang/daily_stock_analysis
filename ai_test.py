import os
from openai import OpenAI

# 读取配置
API_KEY = os.getenv("API_KEY")
STOCK_LIST = os.getenv("STOCK_LIST", "600519").split(",")
MODEL = "glm-5-free"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://aihubmix.com/v1"
)

for stock_code in STOCK_LIST:
    print(f"正在分析 {stock_code}...")
    prompt = f"请对股票 {stock_code} 做一个简短的市场分析"
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"\n{stock_code} 分析结果：")
    print(response.choices[0].message.content)
    print("-" * 50)
