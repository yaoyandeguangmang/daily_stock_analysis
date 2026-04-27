import os
from openai import OpenAI

API_KEY = os.getenv("API_KEY")
STOCK_LIST = os.getenv("STOCK_LIST", "600519").split(",")
MODEL = "gpt-3.5-turbo"  # 换成低消费费模型，稳定不限制

client = OpenAI(
    api_key=API_KEY,
    base_url="https://aihubmix.com/v1"
)

# 只分析第一个股票，减少调用次数
stock_code = STOCK_LIST[0]
print(f"正在分析 {stock_code}...")
prompt = f"请对股票 {stock_code} 做一个简短的市场分析"

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"\n{stock_code} 分析结果：")
    print(response.choices[0].message.content)
except Exception as e:
    print("❌ 调用失败：", e)
