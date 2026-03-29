import google.generativeai as genai
import pandas as pd
import time
import os
import streamlit as st
from kaggle_sync import sync_latest_data

# 1. 官方 SDK 配置 (跳过 OpenAI 转换层，直接穿透)
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc"
genai.configure(api_key=API_KEY)

def run_low_pressure_audit():
    with st.status("🚀 正在启动深层推演协议...", expanded=True) as status:
        
        # 强制冷却 70 秒，确保免费额度不被爆破
        st.write("📡 正在连接反重力冷却链路 (强制等待 70 秒)...")
        time.sleep(70) 

        try:
            # 2. 数据获取
            st.write("🔍 正在同步最新数据补给...")
            remote_path = sync_latest_data()
            
            if remote_path and os.path.exists(remote_path):
                target_path = remote_path
                st.write("✅ 远程补给：已锁定 Kaggle 实时数据")
            else:
                target_path = "lottery_history.csv" 
                st.write("⚠️ 链路波动：使用本地备份数据")

            # 3. 数据处理
            st.write("📊 正在执行数据审计与特征提取...")
            df = pd.read_csv(target_path).tail(15)
            data_info = df.to_string()

            # 4. AI 核心推演 (使用官方生成方法)
            st.write("🤖 正在调用 Gemini-1.5-Flash 官方链路...")
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"你是一名资深数据审计专家。基于以下历史趋势：\n{data_info}\n请给出 2026033 期的穿透预测建议。"
            
            response = model.generate_content(prompt)
            result = response.text
            
            # 5. 结果持久化
            with open("latest_predictions.csv", "w", encoding="utf-8") as f:
                f.write(f"period,numbers\n2026033,\"{result.strip()}\"\n")
            
            status.update(label="✅ 推演任务圆满完成！", state="complete", expanded=False)
            
            st.balloons()
            st.success("官方链路推演成功！")
            st.markdown(f"### 🎯 033 期穿透推演结果：\n\n```text\n{result}\n```")

        except Exception as e:
            status.update(label="❌ 链路发生致命错误", state="error")
            st.error(f"详细反馈: {str(e)}")

# 6. UI 构建
if __name__ == "__main__":
    st.set_page_config(page_title="臻算天机", page_icon="🔮")
    st.title("🔮 臻算天机 - 极简推演中心")
    
    if not os.path.exists("lottery_history.csv"):
        st.warning("🚨 警告：本地备份文件缺失！")
    else:
        st.info("系统就绪：官方链路接入点已重置。")
    
    if st.button("🔥 立即执行 033 期推演"):
        run_low_pressure_audit()
