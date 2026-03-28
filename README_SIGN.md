# 鱼 C 论坛自动签到程序

## 功能说明
这是一个自动签到程序，可以每天自动访问 https://fishc.com.cn/plugin.php?id=k_misign:sign 进行签到。

## 安装依赖

首先需要安装必要的 Python 库：

```bash
pip install requests schedule
```

## 使用方法

### 首次运行
1. 打开命令行或 PowerShell
2. 导航到脚本所在目录
3. 运行程序：
```bash
python auto_sign.py
```
4. 输入你的鱼 C 论坛用户名和密码
5. 登录成功后会自动保存 Cookie

### 后续运行
直接运行即可，程序会自动使用保存的 Cookie：
```bash
python auto_sign.py
```

## 设置定时任务（Windows）

### 方法一：使用任务计划程序（推荐）

1. 按 `Win + R`，输入 `taskschd.msc`，回车打开"任务计划程序"
2. 点击右侧的"创建基本任务"
3. 输入任务名称：`鱼 C 论坛签到`
4. 触发器选择"每天"
5. 设置每天执行的时间（比如早上 8:00）
6. 操作选择"启动程序"
7. 程序/脚本填写：
   ```
   python.exe
   ```
8. 添加参数填写完整路径：
   ```
   "D:\python_learning\fish\auto_sign.py"
   ```
9. 起始于填写：
   ```
   D:\python_learning\fish
   ```
10. 完成设置

### 方法二：使用批处理文件

创建一个批处理文件 `run_sign.bat`：

```batch
@echo off
cd /d "D:\python_learning\fish"
python auto_sign.py
pause
```

然后在任务计划程序中调用这个批处理文件。

## 注意事项

1. **Cookie 有效期**：Cookie 可能会过期，如果签到失败需要重新运行程序登录
2. **账号安全**：请妥善保管 `cookies.json` 文件，不要分享给他人
3. **网络问题**：确保运行时机能正常访问 fishc.com.cn
4. **关机问题**：此方案需要在开机状态下运行，如果要实现关机时也能运行，建议使用云端部署

## 日志查看

程序会在 `sign_log.txt` 文件中记录每次签到的详细信息，可以通过查看日志了解签到状态。

## 高级用法

可以修改代码中的签到时间、添加推送通知等功能。
