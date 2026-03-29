# --- 统帅专用：极简抗压版推演脚本 (全链路打通最终版) ---
import openai
import pandas as pd
import time
import os
import streamlit as st
from kaggle_sync import sync_latest_data  # 确保仓库中有此文件

# 1. 配置区：适配 Gemini-1.5-Flash 与标准 API 路径
API_KEY = "AIzaSyBHD78cRYllItcLoLTzfkMlY-tHITyXsjc" 
client = openai.OpenAI(
    api_key=API_KEY,
    # 修正 404 错误：使用标准 v1 地址以匹配 Flash 模型
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/" 
)

def run_low_pressure_audit():
    # 使用状态组件提供实时反馈，避免黑屏错觉
    with st.status("🚀 正在启动深层推演协议...", expanded=True) as status:
        
        st.write("📡 正在连接反重力冷却链路（强制等待 70 秒）...")
        time.sleep(70) # 规避 429 频率限制的关键冷却

        try:
            # 2. 获取数据补给
            st.write("🔍 正在从 Kaggle 获取实时数据补给...")
            remote_path = sync_latest_data()
            
            if remote_path and os.path.exists(remote_path):
                target_path = remote_path
                st.write("✅ 远程补给：已锁定 Kaggle 实时数据")
            else:
                # 即使 Kaggle 失败，也会读取您上传的备份文件
                target_path = "lottery_history.csv" 
                st.write("⚠️ 链路波动：切换至本地备份数据模式")

            # 3. 读取数据
            st.write("📊 正在执行数据审计与特征提取...")
            df = pd.read_csv(target_path).tail(10)
            data_info = df.to_string()

            # 4. AI 推演：使用 Flash 模型规避额度限制
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
            
            # 5. 结果持久化 (已修复第 55 行的 f-string 语法错误)
            with open("latest_predictions.csv", "w", encoding="utf-8") as f:
                f.
