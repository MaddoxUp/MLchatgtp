import openai
import os
from language import languageEnter

def load_config():
    language=languageEnter()
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
        print(f"{language[1]}")
        print(e)
        set_config_manually(config_path)

def set_config_manually(config_path):
    language=languageEnter()
    openai.api_key = input(f"{language[2]}")
    
    proxy = input(f"{language[3]}")
    if proxy:
        openai.proxy = proxy
    with open(config_path, 'w') as f:
        f.write(f"api_key={openai.api_key}\n")
        if proxy:
            f.write(f"proxy={proxy}\n")
    print(f"{language[4]}")

load_config()