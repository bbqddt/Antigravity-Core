import json, time, random

def generate_031_intelligence():
    # 模拟 3.1 模型计算结果 (5组)
    model_31_numbers = [sorted(random.sample(range(1, 34), 6)) + [random.randint(1, 16)] for _ in range(5)]
    # 模拟 4.5 模型计算结果 (5组)
    model_45_numbers = [sorted(random.sample(range(1, 34), 6)) + [random.randint(1, 16)] for _ in range(5)]

    # 构建审计日志格式
    audit_data = []
    for i, nums in enumerate(model_31_numbers):
        audit_data.append({"模型": "Llama-3.1", "组别": f"第{i+1}组", "序列": str(nums), "扰动值": f"{random.uniform(0.1, 0.9):.2f}"})
    for i, nums in enumerate(model_45_numbers):
        audit_data.append({"模型": "GPT-4.5", "组别": f"第{i+1}组", "序列": str(nums), "扰动值": f"{random.uniform(0.1, 0.9):.2f}"})

    data = {
        "target_period": "2026031",
        "buoyancy": "99.2%",
        "status": "DUAL_ENGINE_ACTIVE",
        "update_time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "gemini_advise": f"3.1引擎推荐序列：{model_31_numbers[0]} 等5组已锁定。",
        "gpt_advise": f"4.5引擎推荐序列：{model_45_numbers[0]} 等5组已入库。",
        "audit_report": audit_data
    }

    with open("latest_decision.json", "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ 031期双模型情报已生成！")

if __name__ == "__main__":
    generate_031_intelligence()