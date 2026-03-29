# --- 臻算天机：极简抗压版推演脚本 (全链路打通最终版) ---
import openai
import pandas as pd
import time
import os
import streamlit as st
from kaggle_sync import sync_latest_data

# 1. API 基础配置
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc"
client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def run_low_pressure_audit():
    with st.status("🚀 正在启动深层推演协议...", expanded=True) as status:
        
        # 为了规避免费版 API 的 429 错误，必须保留这 70 秒冷却
        st.write("📡 正在连接反重力冷却链路 (强制等待 70 秒)...")
        time.sleep(70) 

        try:
            # 2. 数据获取逻辑
            st.write("🔍 正在从 Kaggle 获取实时数据补给...")
            remote_path = sync_latest_data()
            
            if remote_path and os.path.exists(remote_path):
                target_path = remote_path
                st.write("✅ 远程补给：已锁定 Kaggle 实时数据")
            else:
                target_path = "lottery_history.csv" 
                st.write("⚠️ 链路波动：切换至本地备份数据模式")

            # 3. 数据预处理
            st.write("📊 正在执行数据审计与特征提取...")
            df = pd.read_csv(target_path).tail(10)
            data_info = df.to_string()

            # 4. AI 推演 (使用额度更宽松的 Flash 模型)
            st.write("🤖 正在调用 Gemini 执行穿透推演...")
            response = client.chat.completions.create(
                model="gemini-1.5-flash",
                messages=[
                    {"role": "system", "content": "You are a data auditor."},
                    {"role": "user", "content": f"Data:\n{data_info}\nPredict for period 2026033."}
                ],
                temperature=0.1 
            )
            
            result = response.choices[0].message.content
            
            # 5. 结果写入 (修复了之前版本中导致报错的写入语法)
            with open("latest_predictions.csv", "w", encoding="utf-8") as f:
                f.write(f"period,numbers\n2026033,\"{result.strip()}\"\n")
            
            status.update(label="✅ 推演任务圆满完成！", state="complete", expanded=False)
            
            st.balloons()
            st.markdown(f"### 🎯 033 期穿透推演结果：\n\n```text\n{result}\n```")

        except Exception as e:
            status.update(label="❌ 链路发生致命错误", state="error")
            st.error(f"详细反馈: {e}")

# 6. Streamlit 界面构建
if __name__ == "__main__":
    st.set_page_config(page_title="臻算天机", page_icon="🔮")
    st.title("🔮 臻算天机 - 极简推演中心")
    
    # 检测本地备份文件是否存在 (解决截图 11 中的 FileNotFoundError)
    if not os.path.exists("lottery_history.csv"):
        st.warning("🚨 警告：仓库中缺失 lottery_history.csv 备份文件！请确保已上传该文件。")
    else:
        st.info("系统已就绪，Kaggle 链路与本地备份已双重连接。")
    
    if st.button("🔥 立即开始执行 033 期推演"):
        run_low_pressure_audit()
