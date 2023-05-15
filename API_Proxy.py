import openai
def load_config():
    try:
        with open('config.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith('api_key'):
                openai.api_key = line.split('=')[1].strip()
            elif line.startswith('proxy'):
                openai.proxy = line.split('=')[1].strip()
        if not openai.api_key:
            set_config_manually()
    except Exception as e:
        print("无法读取配置文件，错误如下：")
        print(e)
        set_config_manually()

def set_config_manually():
    openai.api_key = input("请输入你的 OpenAI API 密钥: ")
    proxy = input("请输入你的代理地址（可选）: ")
    if proxy:
        openai.proxy = proxy
    with open('config.txt', 'w') as f:
        f.write(f"api_key={openai.api_key}\n")
        if proxy:
            f.write(f"proxy={proxy}\n")
    print("配置已保存到 config.txt 文件中。")

load_config()