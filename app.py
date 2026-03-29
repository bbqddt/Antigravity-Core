import google.generativeai as genai
import pandas as pd
import time
import os
import streamlit as st
from kaggle_sync import sync_latest_data

# 1. 配置官方旧版 SDK (确保环境兼容性)
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc"
genai.configure(api_key=API_KEY)

def run_low_pressure_audit():
    with st.status("🚀 正在启动 033 期稳定版推演...", expanded=True) as status:
        
        # 核心：强制等待 70 秒以规避免费层级频率限制 (429 错误)
        st.write("📡 正在连接冷却链路 (强制等待 70 秒)...")
        time.sleep(70) 

        try:
            # 2. 获取数据补给
            st.write("🔍 正在同步数据补给...")
            try:
                remote_path = sync_latest_data()
            except Exception:
                remote_path = None
            
            # 优先使用实时同步数据，若同步失败则回退至本地文件
            target_path = remote_path if remote_path and os.path.exists(remote_path) else "lottery_history.csv"
            
            if not os.path.exists(target_path):
                raise FileNotFoundError(f"找不到数据源: {target_path}")

            # 3. 数据处理
            st.write("📊 正在执行数据审计...")
            df = pd.read_csv(target_path).tail(15)
            data_info = df.to_string()

            # 4. AI 核心推演 (改用 gemini-pro 彻底解决 404 问题)
            st.write("🤖 正在调用 Gemini 稳定版链路...")
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"你是一名资深审计专家。基于以下历史数据：\n{data_info}\n请给出 2026033 期的穿透推演。"
            
            response = model.generate_content(prompt)
            result = response.text
            
            # 5. 结果持久化与展示
            with open("latest_predictions.csv", "w", encoding="utf-8") as f:
                f.write(f"period,numbers\n2026033,\"{result.strip()}\"\n")
            
            status.update(label="✅ 推演任务圆满完成！", state="complete", expanded=False)
            st.balloons()
            st.success("推演成功！")
            st.markdown(f"### 🎯 033 期推演结果：\n\n```text\n{result}\n```")

        except Exception as e:
            status.update(label="❌ 链路发生致命错误", state="error")
            st.error(f"详细反馈: {str(e)}")

# 6. Streamlit 界面构建
if __name__ == "__main__":
    st.set_page_config(page_title="臻算天机", page_icon="🔮")
    st.title("🔮 臻算天机 - 033 期稳定版")
    
    # 环境检查
    if not os.path.exists("lottery_history.csv"):
        st.error("🚨 警告：仓库缺失本地备份文件 lottery_history.csv！")
    else:
        st.info("系统就绪：已锁定本地备份数据链路。")
    
    if st.button("🔥 立即执行 033 期推演"):
        run_low_pressure_audit()
