# 🚀 GitHub Actions 自动签到部署指南

## 快速部署步骤

### 第一步：准备 GitHub 仓库

1. **访问你的仓库**
   - 打开 https://github.com/eleium
   - 创建一个新的仓库，例如：`fishc-auto-sign`
   - 或者使用现有仓库

2. **上传文件到仓库**
   
   方法一：使用 Git 命令行（推荐）
   ```bash
   # 克隆你的仓库
   git clone https://github.com/eleium/fishc-auto-sign.git
   
   # 进入目录
   cd fishc-auto-sign
   
   # 将所有文件复制到仓库目录
   # 复制以下文件：
   # - auto_sign_github.py
   # - requirements.txt
   # - README_SIGN.md
   
   # 添加文件
   git add .
   
   # 提交
   git commit -m "Add FishC auto sign script"
   
   # 推送到 GitHub
   git push origin main
   ```

   方法二：通过 GitHub 网页上传
   - 在仓库页面点击 "Add file" → "Upload files"
   - 拖拽以下文件到上传区域：
     - `auto_sign_github.py`
     - `requirements.txt`
     - `.github/workflows/sign.yml`（需要先创建 .github/workflows 文件夹）
   - 点击 "Commit changes"

### 第二步：配置账号密码（Secrets）

⚠️ **重要**：这是最关键的一步！

1. **进入 Settings 页面**
   - 在你的 GitHub 仓库页面，点击右上角的 **Settings** 标签

2. **找到 Secrets 设置**
   - 左侧菜单选择：**Secrets and variables** → **Actions**
   - 点击 **New repository secrets** 按钮

3. **添加两个 Secrets**
   
   添加第一个 Secret（用户名）：
   - Name: `FISHC_USERNAME`
   - Value: 你的鱼 C 论坛用户名
   - 点击 **Add secret**
   
   添加第二个 Secret（密码）：
   - Name: `FISHC_PASSWORD`
   - Value: 你的鱼 C 论坛密码
   - 点击 **Add secret**

4. **确认添加成功**
   - 你应该能看到两个 Secrets：`FISHC_USERNAME` 和 `FISHC_PASSWORD`
   - ⚠️ 注意：出于安全考虑，你只能看到名称，看不到具体值

### 第三步：启用 GitHub Actions

1. **进入 Actions 页面**
   - 点击仓库顶部的 **Actions** 标签

2. **启用 Actions**
   - 如果是第一次使用，可能需要点击 **"I understand my workflows, go ahead and enable them"**

3. **查看工作流**
   - 你应该能看到名为 "FishC Daily Sign" 的工作流
   - 默认情况下，它会在每天 UTC 0:00（北京时间 8:00）自动运行

### 第四步：测试运行

1. **手动触发一次运行**
   - 在 Actions 页面，点击 "FishC Daily Sign" 工作流
   - 点击右侧的 **Run workflow** 按钮
   - 选择分支（通常是 main/master）
   - 点击 **Run workflow**

2. **查看运行结果**
   - 等待大约 1-2 分钟
   - 刷新页面，你应该能看到一个绿色的勾选✓（表示成功）或红色的叉号✗（表示失败）
   - 点击运行记录，查看详细日志

3. **检查签到结果**
   - 展开日志，查看是否有 "签到成功" 的字样
   - 如果失败，查看错误信息进行调试

### 第五步：验证签到

1. **访问鱼 C 论坛**
   - 打开 https://fishc.com.cn/plugin.php?id=k_misign:sign
   - 登录你的账号
   - 查看签到状态

2. **查看日志**
   - 如果签到了但没看到奖励，可能是重复签到
   - 程序会自动检测是否已签到

## 🔧 故障排查

### 常见问题 1：登录失败
```
✗ 登录失败，请检查用户名和密码
```

**解决方法**：
- 检查 Secrets 中的用户名和密码是否正确
- 确保没有多余的空格
- 如果修改了密码，记得更新 Secret

### 常见问题 2：找不到 formhash
```
✗ 无法获取表单验证令牌
```

**解决方法**：
- 鱼 C 论坛的页面结构可能已更新
- 需要检查网页源代码，调整 `extract_formhash()` 函数
- 或者网站可能需要 JavaScript 才能完成签到

### 常见问题 3：网络超时
```
requests.exceptions.Timeout
```

**解决方法**：
- GitHub Actions 的网络问题，通常重试即可
- 可以在代码中添加重试机制

### 常见问题 4：工作流不运行

**检查项**：
- Actions 是否已启用？
- 是否在 Settings → Actions → General 中允许了 Actions？
- 是否达到了 GitHub Actions 的使用限制？

## 📊 查看运行历史

1. **访问 Actions 标签页**
   - 所有运行记录都会在这里显示
   - 绿色✓ = 成功
   - 红色✗ = 失败
   - 黄色● = 运行中

2. **查看日志详情**
   - 点击任意一次运行
   - 点击 "Run sign script" 步骤
   - 展开日志查看详细输出

3. **下载日志（可选）**
   - 每次运行的日志可以保存为 artifact
   - 保留 7 天供查看

## ⏰ 修改运行时间

如果想修改每天签到的时间，编辑 `.github/workflows/sign.yml`：

```yaml
on:
  schedule:
    # 修改这里的 cron 表达式
    # 格式：分 时 日 月 星期（UTC 时间）
    
    # 北京时间 8:00（UTC 0:00）
    - cron: '0 0 * * *'
    
    # 北京时间 9:00（UTC 1:00）
    - cron: '0 1 * * *'
    
    # 北京时间 18:00（UTC 10:00）
    - cron: '0 10 * * *'
```

### Cron 表达式计算器

推荐使用：https://crontab.guru/

示例：
- 每天早上 6:00：`0 22 * * *`（前一天 UTC 22:00）
- 每天晚上 20:00：`0 12 * * *`（UTC 12:00）

## 🔐 安全提示

1. **保护账号信息**
   - ✅ Secrets 是加密存储的
   - ✅ 只有你能看到设置的值
   - ❌ 不要将密码硬编码在代码中
   - ❌ 不要提交 cookies.json 到仓库

2. **.gitignore 配置**
   
   建议创建 `.gitignore` 文件：
   ```
   # Python
   __pycache__/
   *.py[cod]
   *$py.class
   *.so
   
   # 敏感文件
   cookies.json
   .env
   *.log
   
   # IDE
   .vscode/
   .idea/
   ```

## 📈 进阶功能

### 添加通知功能

可以在签到成功后发送邮件或 Telegram 通知：

```python
# 在 auto_sign_github.py 中添加
def send_notification(title, message):
    """发送通知（示例：使用 ServerChan）"""
    import requests
    
    # 微信推送（需要先注册获取 SCKEY）
    sckey = os.getenv('SERVERCHAN_SCKEY')
    if sckey:
        url = f"https://sctapi.ftqq.com/{sckey}.send"
        data = {'title': title, 'desp': message}
        requests.post(url, data=data)
```

### 多平台签到

可以扩展程序支持多个论坛同时签到。

## 💡 小贴士

1. **首次运行建议手动触发**，确保配置正确
2. **定期检查运行日志**，确保正常工作
3. **如果鱼 C 论坛改版**，可能需要调整代码
4. **GitHub Actions 免费额度**：每月 2000 分钟，这个脚本每次运行约 1 分钟，完全够用

## 🎯 总结

完成以上步骤后，你就拥有了一个：
- ✅ 完全免费的自动签到系统
- ✅ 不需要本地电脑开机
- ✅ 每天自动运行
- ✅ 可以随时随地查看日志
- ✅ 安全可靠的云端解决方案

如果遇到任何问题，请查看 GitHub Actions 的日志，那是最好的调试信息来源！

---

**祝你使用愉快！🎉**
