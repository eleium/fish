import requests
import os
from datetime import datetime
import re

class FishCSign:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://fishc.com.cn"
        self.sign_url = "https://fishc.com.cn/plugin.php?id=k_misign:sign"
        
        # 从环境变量获取账号信息（GitHub Actions 使用）
        self.username = os.getenv('FISHC_USERNAME')
        self.password = os.getenv('FISHC_PASSWORD')
    
    def log(self, message):
        """记录日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
    
    def login(self):
        """登录鱼 C 论坛"""
        if not self.username or not self.password:
            self.log("错误：未找到账号信息，请检查环境变量是否设置")
            return False
            
        self.log(f"尝试登录：{self.username}")
        
        # 鱼 C 论坛的登录接口
        login_url = f"{self.base_url}/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        
        login_data = {
            'fastloginfield': 'username',
            'username': self.username,
            'password': self.password,
            'quickforward': 'yes',
            'handlekey': 'ls'
        }
        
        try:
            response = self.session.post(login_url, data=login_data)
            
            if '欢迎您回来' in response.text or '退出' in response.text:
                self.log("✓ 登录成功！")
                return True
            else:
                self.log("✗ 登录失败，请检查用户名和密码")
                return False
        except Exception as e:
            self.log(f"✗ 登录异常：{e}")
            return False
    
    def sign_in(self):
        """执行签到"""
        self.log("开始执行签到...")
        
        try:
            # 访问签到页面
            response = self.session.get(self.sign_url)
            
            # 检查是否已登录
            if 'plugin.php?id=k_misign:sign' in response.url:
                # 已经在签到页面，说明已登录
                pass
            
            # 检查是否已经签到
            if '已签' in response.text or '今日已签到' in response.text:
                self.log("✓ 今天已经签到过了")
                return True
            
            # 提取 formhash
            formhash = self.extract_formhash(response.text)
            if not formhash:
                self.log("✗ 无法获取表单验证令牌")
                return False
            
            # 执行签到
            sign_action_url = f"{self.base_url}/plugin.php?id=k_misign:sign&operation=qiandao"
            
            sign_data = {
                'operation': 'qiandao',
                'formhash': formhash
            }
            
            response = self.session.post(sign_action_url, data=sign_data)
            
            if '签到成功' in response.text or '奖励' in response.text or '恭喜您' in response.text:
                self.log("✓ 签到成功！")
                return True
            elif '已经签到' in response.text or '今日已签' in response.text:
                self.log("✓ 今天已经签到过了")
                return True
            else:
                self.log("? 签到结果未知")
                self.log(f"响应内容预览：{response.text[:200]}")
                return False
                
        except Exception as e:
            self.log(f"✗ 签到异常：{e}")
            return False
    
    def extract_formhash(self, html):
        """从 HTML 中提取 formhash"""
        match = re.search(r'name="formhash" value="([^"]+)"', html)
        if match:
            return match.group(1)
        return ""
    
    def run(self):
        """运行签到流程"""
        self.log("=" * 50)
        self.log("🤖 鱼 C 论坛自动签到程序")
        self.log("=" * 50)
        
        # 登录
        if not self.login():
            self.log("登录失败，程序终止")
            return False
        
        # 签到
        success = self.sign_in()
        
        if success:
            self.log("\n✓ 签到流程完成！")
        else:
            self.log("\n✗ 签到失败")
        
        self.log("=" * 50)
        return success


def main():
    """主函数"""
    sign_bot = FishCSign()
    sign_bot.run()


if __name__ == "__main__":
    main()

# Updated: 2026-03-28 12:30:43

