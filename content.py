import openai
import getinput
from parameters import load_prompts
from language import languageEnter

# 定义聊天函数
def chat():
    # 加载语言参数
    language=languageEnter()
    
    # 加载模型的其他参数，例如预设的对话，最大token数，temperature等
    parameters = load_prompts()
    
    # 初始化对话历史列表
    conversation_history = []
    
    # 加载预设的用户对话
    while True:
        if parameters['talk'][0] not in [0]:
             # 将预设的用户对话添加到对话历史
             conversation_history.append({"role": "user", "content": parameters['talk'][0]})
             break
        else:
             print(f"{language[16]}")
             parameters = load_prompts()
    
    # 加载预设的AI对话
    for i in range(4):
        if parameters['talk'][2*i+1] not in [0]:
            # 将预设的AI对话和接下来的用户对话添加到对话历史
            conversation_history.append({"role": "assistant", "content": parameters['talk'][2*i+1]})
            if parameters['talk'][i*2+2] not in [0]:
                conversation_history.append({"role": "user", "content": parameters['talk'][i*2+2]})
                
    # 输出AI模型的信息
    print(f"AI({parameters['model'][0]}):\nHi！({parameters['parameter'][0]})")

    # 进入主循环
    while True:
        # 获取用户的输入
        print("User：")
        user_input = getinput.get_user_input()
        
        # 将用户的输入添加到对话历史
        conversation_history.append({"role": "user", "content": user_input})
        
        # 使用OpenAI API获取AI的回复
        response = openai.ChatCompletion.create(
                model=parameters['model'][0],
                messages=conversation_history,
                max_tokens=parameters['max_tokens'][0],
                temperature=parameters['temperature'][0],
            )    
            
        # 从回复中提取AI的文本
        ai_reply = response['choices'][0]['message']['content']

        # 输出AI的回复和token使用情况
        print(f"AI ({parameters['model'][0]}):\n {ai_reply}" )
        print(f'{response["usage"]["prompt_tokens"]} prompt tokens counted by the OpenAI API.')
        
        # 将AI的回复添加到对话历史
        conversation_history.append({"role": "assistant", "content": ai_reply})


