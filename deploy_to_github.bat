@echo off
chcp 65001 >nul
echo ========================================
echo GitHub 推送助手
echo ========================================
echo.

REM 检查是否安装了 Git
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [错误] 未检测到 Git，请先安装 Git
    echo 下载地址：https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [提示] 请确保你已经：
echo 1. 在 GitHub 创建了仓库
echo 2. 复制了仓库的 HTTPS 地址
echo.

set /p REPO_URL="请输入你的 GitHub 仓库 HTTPS 地址（例如：https://github.com/eleium/fishc-auto-sign.git）: "

if "%REPO_URL%"=="" (
    echo [错误] 仓库地址不能为空
    pause
    exit /b 1
)

echo.
echo ========================================
echo 开始部署...
echo ========================================
echo.

REM 初始化 Git 仓库（如果还没有）
if not exist ".git" (
    echo [1/6] 初始化 Git 仓库...
    git init
) else (
    echo [1/6] Git 仓库已存在
)

REM 添加远程仓库
echo [2/6] 配置远程仓库...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

REM 创建 .gitignore
echo [3/6] 创建 .gitignore...
(
echo __pycache__/
echo *.py[cod]
echo *$py.class
echo *.so
echo cookies.json
echo .env
echo *.log
echo .vscode/
echo .idea/
) > .gitignore

REM 添加所有文件
echo [4/6] 添加文件到暂存区...
git add .

REM 提交
echo [5/6] 提交更改...
git commit -m "Add FishC auto sign script with GitHub Actions"

REM 推送
echo [6/6] 推送到 GitHub...
echo.
echo ⚠️ 如果是私有仓库或首次推送，可能需要输入 GitHub 账号密码或使用 Token
echo.

REM 尝试推送到 main 分支
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo ✓ 推送成功！
    echo ========================================
    echo.
    echo 下一步操作：
    echo 1. 访问 https://github.com/eleium
    echo 2. 进入你的仓库
    echo 3. 点击 Settings → Secrets and variables → Actions
    echo 4. 添加两个 Repository secrets:
    echo    - FISHC_USERNAME: 你的鱼 C 论坛用户名
    echo    - FISHC_PASSWORD: 你的鱼 C 论坛密码
    echo 5. 点击 Actions 标签，启用工作流
    echo 6. 手动运行一次测试
    echo.
    echo 详细教程请查看：GitHub 部署教程.md
    echo.
) else (
    echo.
    echo ========================================
    echo ✗ 推送失败
    echo ========================================
    echo.
    echo 可能的原因：
    echo 1. 网络连接问题
    echo 2. 需要 GitHub Token（推荐使用 Token）
    echo 3. 仓库不存在或没有权限
    echo 4. Git 配置问题
    echo.
    echo 建议：使用 GitHub Personal Access Token
    echo 创建方法：https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    echo.
)

pause
