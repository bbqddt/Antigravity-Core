import openai
import pandas as pd
import time
import os
import streamlit as st
from kaggle_sync import sync_latest_data

# 1. 核心配置：适配 Google OpenAI 转换协议
# 注意：API 地址必须包含 v1beta 才能正确调用 Flash 模型
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc"
client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def run_low_pressure_audit():
    with st.status("🚀 正在启动深层推演协议...", expanded=True) as status:
        
        # 强制冷却 70 秒以规避 429 额度限制
        st.write("📡 正在连接反重力冷却链路 (强制等待 70 秒)...")
        time.sleep(70) 

        try:
            # 2. 数据补给获取
            st.write("🔍 正在同步最新数据补给...")
            remote_path = sync_latest_data()
            
            # 优先使用实时同步数据，若失败则回退至本地文件
            if remote_path and os.path.exists(remote_path):
                target_path = remote_path
                st.write("✅ 远程补给：已锁定 Kaggle 实时数据")
            else:
                target_path = "lottery_history.csv" 
                st.write("⚠️ 链路波动：切换至本地备份数据模式")

            # 3. 数据特征提取
            st.write("📊 正在执行数据审计与特征提取...")
            df = pd.read_csv(target_path).tail(15)
            data_info = df.to_string()

            # 4. AI 穿透推演
            st.write("🤖 正在调用 Gemini-1.5-Flash 执行核心推演...")
            # 修正 404：模型名称需为简洁形式
            response = client.chat.completions.create(
                model="gemini-1.5-flash",
                messages=[
                    {"role": "system", "content": "You are a specialized data auditor."},
                    {"role": "user", "content": f"Analyze trends:\n{data_info}\nOutput numbers for period 2026033."}
                ],
                temperature=0.1 
            )
            
            result = response.choices[0].message.content
            
            # 5. 结果持久化
            with open("latest_predictions.csv", "w", encoding="utf-8") as f:
                f.write(f"period,numbers\n2026033,\"{result.strip()}\"\n")
            
            status.update(label="✅ 推演任务圆满完成！", state="complete", expanded=False)
            
            st.balloons()
            st.success("推演成功，033 期数据已生成！")
            st.markdown(f"### 🎯 033 期穿透推演结果：\n\n```text\n{result}\n```")

        except Exception as e:
            status.update(label="❌ 链路发生致命错误", state="error")
            st.error(f"详细反馈: {str(e)}")

# 6. UI 构建
if __name__ == "__main__":
    st.set_page_config(page_title="臻算天机", page_icon="🔮")
    st.title("🔮 臻算天机 - 极简推演中心")
    
    # 状态实时检查
    if not os.path.exists("lottery_history.csv"):
        st.warning("🚨 警告：仓库缺失 lottery_history.csv 备份文件，请确认已上传！")
    else:
        st.info("系统就绪：Kaggle 链路与本地备份双重连接已建立。")
    
    if st.button("🔥 立即执行 033 期推演"):
        run_low_pressure_audit()
