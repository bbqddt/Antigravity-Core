import google.generativeai as genai
import pandas as pd
import time
import os
import streamlit as st
from kaggle_sync import sync_latest_data

# 1. 官方 SDK 穿透配置
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc"
genai.configure(api_key=API_KEY)

def run_low_pressure_audit():
    with st.status("🚀 正在启动深层推演协议...", expanded=True) as status:
        
        st.write("📡 正在连接反重力冷却链路 (强制等待 70 秒)...")
        time.sleep(70) 

        try:
            # 2. 数据获取逻辑
            st.write("🔍 正在同步最新数据补给...")
            remote_path = sync_latest_data()
            target_path = remote_path if remote_path and os.path.exists(remote_path) else "lottery_history.csv"

            # 3. 数据处理
            st.write("📊 正在执行数据审计与特征提取...")
            df = pd.read_csv(target_path).tail(15)
            data_info = df.to_string()

            # 4. AI 核心推演 (换成最基础的 gemini-pro 以确保兼容性)
            st.write("🤖 正在调用 Gemini 稳定版链路...")
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"基于以下历史数据：\n{data_info}\n请给出 2026033 期的穿透推演。"
            
            response = model.generate_content(prompt)
            result = response.text
            
            # 5. 结果持久化
            with open("latest_predictions.csv", "w", encoding="utf-8") as f:
                f.write(f"period,numbers\n2026033,\"{result.strip()}\"\n")
            
            status.update(label="✅ 推演任务圆满完成！", state="complete", expanded=False)
            st.balloons()
            st.success("官方链路推演成功！")
            st.markdown(f"### 🎯 033 期穿透结果：\n\n```text\n{result}\n```")

        except Exception as e:
            status.update(label="❌ 链路发生致命错误", state="error")
            st.error(f"详细反馈: {str(e)}")

if __name__ == "__main__":
    st.set_page_config(page_title="臻算天机", page_icon="🔮")
    st.title("🔮 臻算天机 - 极简推演中心")
    
    if st.button("🔥 立即执行 033 期推演"):
        run_low_pressure_audit()
