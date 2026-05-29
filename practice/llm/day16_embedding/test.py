from zhipuai import ZhipuAI

# 1. 直接把你的真实 key 粘贴在这里（注意前后不要有空格，保留引号）
# 长得大概像这样: "123456789abcdef.abcdefghijklmn"
REAL_API_KEY = "e77dd6af64794dff9a96595a6b23a368.CQLNX13x5w2J0DVwY"

def main():
    print("开始纯净版底层测试...")
    
    # 2. 实例化最底层的智谱客户端
    client = ZhipuAI(api_key=REAL_API_KEY)
    
    try:
        # 3. 发送 Embedding 请求
        response = client.embeddings.create(
            model="embedding-3", 
            input="Agent为什么需要Tool Calling?"
        )
        
        # 4. 解析结果
        vector = response.data[0].embedding
        print(f"✅ 成功！底层通道完全畅通！")
        print(f"📊 向量维度大小: {len(vector)}")
        print(f"🔢 向量前 5 个数字预览: {vector[:5]}")
        
    except Exception as e:
        print(f"❌ 依然失败，错误信息：{e}")

if __name__ == "__main__":
    main()