import streamlit as st
import json, os, time

st.set_page_config(page_title="ANTIGRAVITY V18", layout="wide")
st.markdown("<style>.stApp{background:#000;color:#0f0;font-family:monospace;}</style>", unsafe_allow_html=True)

def get_safe_data():
    file_path = "latest_decision.json"
    if not os.path.exists(file_path):
        return {
            "target_period": "2026031",
            "last_open": "同步中",
            "gemini_advise": "量子引擎加载中...",
            "gpt_advise": "蜂群组建中...",
            "audit_report": [],
            "buoyancy": "99%",
            "status": "INITIALIZING",
            "update_time": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    try:
        with open(file_path, "r", encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"target_period": "RELOADING", "buoyancy": "0%", "status": "RELOADING", 
                "gemini_advise": "请刷新", "gpt_advise": "请刷新", "audit_report": []}

data = get_safe_data()

st.title(f"🌌 V18 蜂群指挥部 | 目标：{data['target_period']}")
c1, c2, c3 = st.columns(3)
c1.metric("🌀 实时浮力", data.get('buoyancy', '99%'))
c2.metric("🐝 蜂群模式", data.get('status', 'RUNNING'))
c3.metric("🕒 同步时刻", data.get('update_time', 'NEW'))

st.write("---")
st.success(f"Gemini-Agent: {data.get('gemini_advise', '计算中...')}")
st.warning(f"GPT-Agent: {data.get('gpt_advise', '审计中...')}")

st.write("---")
st.subheader("📊 铁面审计日志")
# 关键修正：确保即使为空也以 dataframe 形式展示，避免 AttributeError
if data.get('audit_report') and len(data['audit_report']) > 0:
    st.dataframe(data['audit_report'], use_container_width=True)
else:
    st.info("📡 031 期实时数据正在接入，请稍后刷新...")