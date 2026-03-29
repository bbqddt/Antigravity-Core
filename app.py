import google.generativeai as genai
import pandas as pd
import streamlit as st
import time
import os

# 1. 基础配置：锁定最兼容的官方旧版路径
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc"
genai.configure(api_key=API_KEY)

def run_stable_audit():
    with st.status("🔮 正在启动 033 期稳定版推演协议...", expanded=True) as status:
        
        # 强制冷却 70 秒，这是绕过免费层级 429 报错的唯一物理手段
        st.write("📡 正在激活反重力冷却链路 (等待 70s)...")
        time.sleep(70) 

        try:
            # 2. 锁定本地备份数据源 (避开 Kaggle 403 错误)
            target_file = "lottery_history.csv"
            if not os.path.exists(target_file):
                st.error("🚨 致命错误：本地缺失 lottery_history.csv！请手动上传该文件。")
                return

            st.write("📊 正在审计本地历史特征...")
            df = pd.read_csv(target_file).tail(15)
            data_context = df.to_string()

            # 3. AI 推演：强制使用 gemini-pro 规避 404
            st.write("🤖 正在调用 Gemini 稳定版链路 (gemini-pro)...")
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"作为资深审计专家，请基于以下数据趋势推演 2026033 期结果：\n{data_context}"
            
            response = model.generate_content(prompt)
            result = response.text

            # 4. 结果展示
            status.update(label="✅ 033 期推演圆满成功！", state="complete", expanded=False)
            st.balloons()
            st.success("推演链路已穿透！")
            st.markdown(f"### 🎯 033 期核心推演结果：\n\n```text\n{result}\n```")

        except Exception as e:
            status.update(label="❌ 链路发生严重干扰", state="error")
            st.error(f"详细反馈: {str(e)}")

# UI 界面构建
if __name__ == "__main__":
    st.set_page_config(page_title="臻算天机", page_icon="🔮")
    st.title("🔮 臻算天机 - 稳定版通道")
    
    st.info("当前模式：本地数据直连 + Gemini-Pro 稳定链路")
    
    if st.button("🔥 立即执行 033 期穿透推演"):
        run_stable_audit()
