import os
import kagglehub
import streamlit as st

def sync_latest_data():
    """
    使用 Kaggle API 自动同步最新的双色球历史数据
    """
    try:
        # 自动获取 Secrets
        os.environ["KAGGLE_USERNAME"] = st.secrets["KAGGLE_USERNAME"]
        os.environ["KAGGLE_API_TOKEN"] = st.secrets["KAGGLE_API_TOKEN"]

        dataset_handle = "fanyunqi/ssq-history-data"
        
        # 下载至云端缓存
        local_path = kagglehub.dataset_download(dataset_handle)
        
        files = [f for f in os.listdir(local_path) if f.endswith('.csv')]
        if not files:
            return None
        
        return os.path.join(local_path, files[0])

    except Exception as e:
        print(f"Kaggle Sync Error: {e}")
        return None
