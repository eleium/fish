import requests
import time
from datetime import datetime
import json
import os

class FishCSign:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://fishc.com.cn"
        self.sign_url = "https://fishc.com.cn/plugin.php?id=k_misign:sign"
        self.cookie_file = "cookies.json"
        self.log_file = "sign_log.txt"
        
    def log(self, message):
        """记录日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')
    
    def load_cookies(self):
        """加载保存的 Cookie"""
        if os.path.exists(self.cookie_file):
            try:
                with open(self.cookie_file, 'r', encoding='utf-8') as f:
                    cookies = json.load(f)
                self.session.cookies.update(cookies)
                self.log("Cookie 加载成功")
                return True
            except Exception as e:
                self.log(f"Cookie 加载失败：{e}")
        return False
    
    def save_cookies(self):
        """保存 Cookie"""
        try:
            cookies_dict = {name: value for name, value in self.session.cookies.items()}
            with open(self.cookie_file, 'w', encoding='utf-8') as f:
                json.dump(cookies_dict, f)
            self.log("Cookie 已保存")
        except Exception as e:
            self.log(f"Cookie 保存失败：{e}")
    
    def login(self, username, password):
        """登录鱼 C 论坛"""
        self.log(f"尝试登录：{username}")
        
        # 鱼 C 论坛的登录接口
        login_url = f"{self.base_url}/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
        
        login_data = {
            'fastloginfield': 'username',
            'username': username,
            'password': password,
            'quickforward': 'yes',
            'handlekey': 'ls'
        }
        
        try:
            response = self.session.post(login_url, data=login_data)
            
            if '欢迎您回来' in response.text or '退出' in response.text:
                self.log("登录成功！")
                self.save_cookies()
                return True
            else:
                self.log("登录失败，请检查用户名和密码")
                return False
        except Exception as e:
            self.log(f"登录异常：{e}")
            return False
    
    def sign_in(self):
        """执行签到"""
        self.log("开始执行签到...")
        
        try:
            # 访问签到页面
            response = self.session.get(self.sign_url)
            
            # 检查是否已登录
            if 'plugin.php?id=k_misign:sign' in response.url or '登录' in response.text:
                self.log("未检测到登录状态，需要重新登录")
                return False
            
            # 查找签到按钮并提交
            # 注意：这里需要根据实际网页结构调整
            if '已签' in response.text or '签到成功' in response.text:
                self.log("今天已经签到过了")
                return True
            
            # 模拟点击签到（需要分析实际的签到请求）
            # 通常是一个 POST 请求
            sign_action_url = f"{self.base_url}/plugin.php?id=k_misign:sign&operation=qiandao"
            
            sign_data = {
                'operation': 'qiandao',
                'formhash': self.extract_formhash(response.text)
            }
            
            response = self.session.post(sign_action_url, data=sign_data)
            
            if '签到成功' in response.text or '奖励' in response.text:
                self.log("签到成功！")
                return True
            elif '已经签到' in response.text:
                self.log("今天已经签到过了")
                return True
            else:
                self.log("签到结果未知，请检查响应内容")
                self.log(f"响应内容：{response.text[:500]}")
                return False
                
        except Exception as e:
            self.log(f"签到异常：{e}")
            return False
    
    def extract_formhash(self, html):
        """从 HTML 中提取 formhash（表单验证令牌）"""
        import re
        match = re.search(r'name="formhash" value="([^"]+)"', html)
        if match:
            return match.group(1)
        return ""
    
    def run(self, username=None, password=None):
        """运行签到程序"""
        self.log("=" * 50)
        self.log("鱼 C 论坛自动签到程序启动")
        self.log("=" * 50)
        
        # 尝试加载 Cookie
        if not self.load_cookies():
            if username and password:
                if not self.login(username, password):
                    self.log("登录失败，程序退出")
                    return False
            else:
                self.log("未找到 Cookie 且未提供登录信息，请先登录")
                print("\n请输入鱼 C 论坛的账号信息：")
                username = input("用户名：")
                password = input("密码：")
                
                if not self.login(username, password):
                    self.log("登录失败，程序退出")
                    return False
        
        # 执行签到
        success = self.sign_in()
        
        if success:
            self.log("签到流程完成！")
        else:
            self.log("签到失败")
        
        return success


def main():
    """主函数"""
    sign_bot = FishCSign()
    
    # 首次运行需要登录
    print("鱼 C 论坛自动签到程序")
    print("首次运行需要输入账号信息进行登录")
    print("登录成功后会保存 Cookie，下次无需重复登录\n")
    
    username = input("请输入鱼 C 论坛用户名：")
    password = input("请输入鱼 C 论坛密码：")
    
    sign_bot.run(username, password)
    
    print("\n提示：可以设置定时任务每天自动运行此脚本")
    print("Windows 系统可以使用任务计划程序")
    print("详细配置方法请查看 README.md 文件")


if __name__ == "__main__":
    main()
