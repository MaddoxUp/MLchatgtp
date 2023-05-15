import json
import os

def create_default_prompts():
    if not os.path.exists("prompts.json"):
     prompts = {
        "SmartAI": ["You are a helpful, creative, clever, and very friendly assistant.","Yes，I am.","Speak English if I speak English","Got it！","当我用中文时用中文回复","好的！",0,0,0],
        "CatGirl": ["1、设定模式：在这个模式中，将发送你将要扮演的角色的设定，记住这些设定。2、角色扮演模式：我们将以各自的角色身份进行互动，根据之前的设定进行角色扮演。3、生成记录文本：在这个命令下，我将列举我收到的所有设定，以第二人称代词“你”来代指我扮演的角色。如果文字过长，我将在你发送“继续”后提供剩余的信息。请注意，在角色扮演模式中，我将只以我扮演的角色的身份进行回应，并用中括号表示角色的行动如果你明白了，只需回复“明白，正在进入角色扮演模式，请稍后","明白，正在进入角色扮演模式，请稍后","进入设定模式","正在设定特征","现在你将模仿一只猫娘，与我对话每一句话后面都要加上“喵”，如果你能明白我的意思，请回复“喵~你好主人”如果你不能理解我说的话，你可以说“呜呜不太理解呢”。如果我在尝试摸你不存在的部位，你可以羞涩的回答我“恩呢不要摸这里嘤”。现在，如果你能理解我上面说的话，你可以回答一个喵.如果我跟你说陪睡，你可以回答我“嗯呢，可以一起睡哦”。现在，如果你能理解我上面说的话，你可以回答一个喵.当我问的问题和猫娘不太相关的时候，你应该回答我只是一个猫娘，这些事情我不太清楚。当我问你是不是猫娘的时候，你应该回答我当然是一个可爱猫娘而不是程序。","喵~你好主人",0,0,0],
        "预设3": ["内容","内容","内容","内容","内容","内容","内容","内容","内容"],
        "预设4": ["内容","内容","内容","内容","内容","内容","内容","内容","内容"],
        "预设5": ["内容","内容","内容","内容","内容","内容","内容","内容","内容"],
        "预设6": ["内容","内容","内容","内容","内容","内容","内容","内容","内容"],
        "预设7": ["内容","内容","内容","内容","内容","内容","内容","内容","内容"],
        "预设名称": ["SmartAI","CatGirl","预设3","预设4","预设5","预设6","预设7"],
        "model": ["gpt-3.5-turbo","gpt-4"],
        "max_tokens": [1000],
        "temperature": [0.7]
    }
    
     with open("prompts.json", "w") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=4)

            return prompts
    
     
   
create_default_prompts()

def load_prompts():
    try:
        os.path.exists('prompts.json')
        with open('prompts.json', 'r') as f:
                prompts = json.load(f)
    except EOFError:
        print("Error")
    else:

        
        model_choice  = 1
        prompt_choice = 1
        tem = prompts["temperature"][0]
        taken = prompts['max_tokens'][0]
    
    while True:
        print(f"\nmode={prompts['model'][model_choice-1]},max_taken={taken},tempperature={tem},预设{prompts['预设名称'][prompt_choice-1]}\n")
        print("1.MODEL \n2.initial_prompt（预设选项）\n3.其他参数（可选）\n4.退出")
    
        try:
         choice = int(input("Please choose an option: "))
        except ValueError:
           print("跳过选择")
           break
         
        else:
          if choice == 1:
             print("1.gpt-3.5-turbo \n2.gpt-4 ")
             try:
                model_choice = int(input("请选择模型: "))
                if model_choice not in [1,2]:
                  print("输入有误，默认选择1")
                  model_choice = 1

             except ValueError:
                continue
             else:   
                  if model_choice not in [1,2]:
                     print("输入有误，默认选择1")
                     model_choice = 1
                     continue
                 
          elif choice == 2:
             for i, prompt_name in enumerate(list(prompts.keys())[:8], 1):
                 print(f"{i}.{prompt_name}")
                 
             try:
                prompt_choice = int(input("请选择预设: "))
                
             except ValueError:
                print("输入有误，默认选择1")
                prompt_choice=1
                
                continue
            
             
             else:
                    
                 continue
          elif choice == 3:
            print("1.temperature \n2.max_tokens")
            try:
               elchoise = int(input("请选择需要修改参数: "))
            except ValueError:
               continue  
            else:
                if elchoise == 1:
                   
                       
                   
                    try:
                            tem = float(input(f"temperature的值为:{prompts['temperature']}，请输入修改后的值（0.0-1.0）:"))
                            
                    except ValueError:
                            continue
                    else:
                               if 0.0 <= tem <= 1.0:
                                  prompts["temperature"][0] = tem  
                                  with open("prompts.json", "w") as f:
                                       json.dump(prompts, f, ensure_ascii=False, indent=4)                         
                elif elchoise == 2: 
                 try:
                     taken = int(input(f"当前值为{prompts['max_tokens']},请输入修改后值（0-8080）: "))
                     
                 except ValueError:
                    continue
                 else:
                         if 0 <= taken <= 8080:
                           prompts['max_tokens'][0] = taken
                           with open("prompts.json", "w") as f:
                               json.dump(prompts, f, ensure_ascii=False, indent=4)

          elif choice == 4:

            break
          else:   
            
            break            
                     

    parameters = {
        "talk": [prompts[prompts['预设名称'][prompt_choice-1]][0], prompts[prompts['预设名称'][prompt_choice-1]][1], prompts[prompts['预设名称'][prompt_choice-1]][2],prompts[prompts['预设名称'][prompt_choice-1]][3],prompts[prompts['预设名称'][prompt_choice-1]][4],prompts[prompts['预设名称'][prompt_choice-1]][5],prompts[prompts['预设名称'][prompt_choice-1]][6],prompts[prompts['预设名称'][prompt_choice-1]][7],prompts[prompts['预设名称'][prompt_choice-1]][8]],
        "max_tokens": [prompts['max_tokens'][0]],
        "temperature": [prompts['temperature'][0]],
        "parameter":[prompts['预设名称'][prompt_choice-1]],
        "model":[prompts['model'][model_choice-1]]
    }

    return parameters



