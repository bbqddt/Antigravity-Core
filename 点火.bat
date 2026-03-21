@echo off
chcp 65001 >nul
if not exist token.txt (echo ❌ 缺失 token.txt & pause & exit)

echo [1/3] 蜂群计算中...
python engine.py

echo [2/3] 同步 GitHub 阵地 (三路合围)...
if exist .git rd /s /q .git
git init >nul
git checkout -b main >nul
git remote add g1 https://github.com/bbqddt/Antigravity_027.git
git remote add g2 https://github.com/bbqddt/Antigravity-Core.git
git remote add g3 https://github.com/bbqddt/Antigravity-V7-Hub.git
git add .
git commit -m "V16: Swarm Hybrid Deployment" >nul
git push -f g1 main >nul 2>&1
git push -f g2 main >nul 2>&1
git push -f g3 main >nul 2>&1
echo ✅ GitHub 三路阵地已占领。

echo [3/3] 🚀 正在执行 HF 核心区 API 强攻...
python hf_push.py

echo.
echo ✅ 报告统帅：V16 混合点火结束！请刷新 HF 页面查看。
pause