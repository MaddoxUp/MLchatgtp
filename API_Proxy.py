import openai
import os

def load_config():
    home_dir = os.path.expanduser("~")
    config_path = os.path.join(home_dir, 'MLchatgpt_key.txt')
    try:
        with open(config_path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith('api_key'):
                openai.api_key = line.split('=')[1].strip()
            elif line.startswith('proxy'):
                openai.proxy = line.split('=')[1].strip()
        if not openai.api_key:
            set_config_manually(config_path)
    except Exception as e:
        print("无法读取配置文件，错误如下：")
        print(e)
        set_config_manually(config_path)

def set_config_manually(config_path):
    openai.api_key = input("请输入你的 OpenAI API 密钥: ")
    proxy = input("请输入你的代理地址（可选）: ")
    if proxy:
        openai.proxy = proxy
    with open(config_path, 'w') as f:
        f.write(f"api_key={openai.api_key}\n")
        if proxy:
            f.write(f"proxy={proxy}\n")
    print(f"配置已保存到 MLchatgpt_key.txt文件中。")

load_config()