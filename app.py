from genai import Client
import pandas as pd
import time
import os
import streamlit as st
from kaggle_sync import sync_latest_data

# 1. 初始化 Google 全新 GenAI 客户端
# 注意：新版 SDK 内部已自动处理 v1beta 逻辑
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc"
client = Client(api_key=API_KEY)

def run_low_pressure_audit():
    with st.status("🚀 正在启动 2.0 深层推演协议...", expanded=True) as status:
        st.write("📡 正在连接反重力冷却链路 (强制等待 70 秒)...")
        time.sleep(70) 

        try:
            # 2. 数据获取 (带异常捕获，防止 Kaggle 403 挂掉整个程序)
            st.write("🔍 正在同步最新数据补给...")
            try:
                remote_path = sync_latest_data()
            except Exception as kaggle_e:
                st.warning(f"Kaggle 链路异常: {kaggle_e}")
                remote_path = None
            
            target_path = remote_path if remote_path and os.path.exists(remote_path) else "lottery_history.csv"

            # 3. 数据处理
            st.write("📊 正在执行数据审计...")
            df = pd.read_csv(target_path).tail(15)
            data_info = df.to_string()

            # 4. AI 推演 (使用新版 SDK 语法)
            st.write("🤖 正在调用 Gemini 2.0 最新链路...")
            
            # 这里改用 gemini-2.0-flash-exp，通常是目前最稳定的测试入口
            response = client.models.generate_content(
                model='gemini-2.0-flash-exp', 
                contents=f"基于以下历史数据：\n{data_info}\n请给出 2026033 期的穿透推演。"
            )
            result = response.text
            
            # 5. 持久化结果
            with open("latest_predictions.csv", "w", encoding="utf-8") as f:
                f.write(f"period,numbers\n2026033,\"{result.strip()}\"\n")
            
            status.update(label="✅ 推演任务圆满完成！", state="complete", expanded=False)
            st.balloons()
            st.success("2.0 链路推演成功！")
            st.markdown(f"### 🎯 033 期推演结果：\n\n```text\n{result}\n```")

        except Exception as e:
            status.update(label="❌ 链路发生致命错误", state="error")
            st.error(f"详细反馈: {str(e)}")

# UI 界面
if __name__ == "__main__":
    st.set_page_config(page_title="臻算天机", page_icon="🔮")
    st.title("🔮 臻算天机 - 2.0 极简推演中心")
    
    # 诊断信息
    if not os.path.exists("lottery_history.csv"):
        st.error("🚨 致命错误：本地仓库缺少 lottery_history.csv 备份文件！请务必上传该文件！")
    
    if st.button("🔥 立即执行 033 期推演"):
        run_low_pressure_audit()
