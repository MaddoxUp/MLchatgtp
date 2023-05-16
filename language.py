import os
import json
def languagelogcheek():
 if not os.path.exists("tran_.json"):

    lag={"1.中文":["选择语言","无法读取配置文件，错误如下:","请输入你的 OpenAI API 密钥:","请输入你的代理地址（可选）: ","配置已保存到 MLchatgpt_key.txt 文件中.","语言模型","预设选项","其他参数（可选）","退出","跳过选择","请选择模型","输入有误，默认选择1","请选择语言模型","请选择需要修改参数:","请输入修改后的值","预设错误请重新设置"],
         "2.English":["selet language","Failed to read the configuration file, error message as follows:", "Please enter your OpenAI API key:", "Please enter your proxy address (optional):", "Configuration saved to the MLchatgpt_key.txt file.","Language Model", "Default Options", "Other Parameters (optional)", "Exit", "Skip Selection", "Please select a model", "Invalid input, default selection 1", "Please select a language model", "Please select the parameter to modify:", "Please enter the modified value.","Invalid preset. Please reset it."],
         "i":["1.中文","2.English"],
         "mem":[0]
         }
    with open("tran_.json", "w") as f:
        json.dump(lag, f, ensure_ascii=False, indent=4)        


def languageEnter():
    os.path.exists('tran_.json')
    with open('tran_.json', 'r') as f:
         lag = json.load(f)        
    ENTER=lag[lag['i'][lag['mem'][0]]]
    print(ENTER)
    return ENTER


def languagechoise():
    test=languageEnter()
    os.path.exists('tran_.json')
    with open('tran_.json', 'r') as f:
         lag = json.load(f)
    print(f"{lag['i']}\n{test[0]}:")  

    #下面有问题 
    choise=int(input())
    lag["mem"][0] = choise-1 
    if  lag["mem"][0] in [0,1]:
        with open("tran_.json", "w") as f:
             json.dump(lag, f, ensure_ascii=False, indent=4)





languagechoise()