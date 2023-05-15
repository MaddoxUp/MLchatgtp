import openai
import getinput
from parameters import load_prompts


def chat():
    parameters = load_prompts()
    conversation_history = []
    while True:
        if parameters['talk'][0] not in [0]:
             conversation_history.append({"role": "user", "content": parameters['talk'][0]})
             break
        else:
             print("预设错误请重新设置")
             parameters = load_prompts()
    for i in range(4):
        if parameters['talk'][2*i+1] not in [0]:
            conversation_history.append({"role": "assistant", "content": parameters['talk'][2*i+1]})
            if parameters['talk'][i*2+2] not in [0]:
                conversation_history.append({"role": "user", "content": parameters['talk'][i*2+2]})


    print(f"AI({parameters['model'][0]}):\nHi！({parameters['parameter'][0]})")

    while True:
        print("User：")
        user_input = getinput.get_user_input()
        conversation_history.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
                model=parameters['model'][0],
                messages=conversation_history,
                max_tokens=parameters['max_tokens'][0],
                temperature=parameters['temperature'][0],
            )    
            
        ai_reply = response['choices'][0]['message']['content']

        print(f"AI ({parameters['model'][0]}):\n {ai_reply}" )
        print(f'{response["usage"]["prompt_tokens"]} prompt tokens counted by the OpenAI API.')
        conversation_history.append({"role": "assistant", "content": ai_reply})


