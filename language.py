import os
import json

# 检查并初始化语言配置文件
def languagelogcheek():
 # 如果tran_.json文件不存在
 if not os.path.exists("tran_.json"):

    # 语言配置，包括中文和英文两种语言
    lag={"1.中文":["选择语言","无法读取配置文件，错误如下:","请输入你的 OpenAI API 密钥:","请输入你的代理地址（可选）: ","配置已保存到 MLchatgpt_key.txt 文件中.","语言模型","预设选项","其他参数（可选）","退出","跳过选择","请选择模型","输入有误，默认选择1","请选择语言模型","请选择需要修改参数:","请输入修改后的值","预设错误请重新设置"],
         "2.English":["selet language","Failed to read the configuration file, error message as follows:", "Please enter your OpenAI API key:", "Please enter your proxy address (optional):", "Configuration saved to the MLchatgpt_key.txt file.","Language Model", "Default Options", "Other Parameters (optional)", "Exit", "Skip Selection", "Please select a model", "Invalid input, default selection 1", "Please select a language model", "Please select the parameter to modify:", "Please enter the modified value.","Invalid preset. Please reset it."],
         "i":["1.中文","2.English"],
         "mem":[0]
         }
    # 将语言配置写入tran_.json文件中
    with open("tran_.json", "w") as f:
        json.dump(lag, f, ensure_ascii=False, indent=4)        


# 读取并返回当前语言配置
def languageEnter():
    os.path.exists('tran_.json')
    with open('tran_.json', 'r') as f:
         lag = json.load(f)        
    # 返回当前语言的配置
    return lag[lag['i'][lag['mem'][0]]]


# 提供用户选择语言的界面
def languagechoise():
    test=languageEnter()
    os.path.exists('tran_.json')
    with open('tran_.json', 'r') as f:
         lag = json.load(f)
    # 打印语言选项，并提示用户选择
    print(f"{lag['i']}\n{test[0]}:")  


    # 获取用户的输入
    choise=int(input())
    # 更新语言选项
    lag["mem"][0] = choise-1 
    # 判断输入是否在有效范围内
    if  lag["mem"][0] in [0,1]:
        # 将更新后的语言选项保存到文件中
        with open("tran_.json", "w") as f:
             json.dump(lag, f, ensure_ascii=False, indent=4)
        # 返回更新后的语言配置
        languageEnter()      






