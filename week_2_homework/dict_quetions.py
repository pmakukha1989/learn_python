questions_to_ask_dict = {
     "hru?": "good",
     "what?": "code",
     "why?" : "cause",
     }


def ask_user (questions_dict):
    while True:
        print ('ask:')
        user_input = input()
        if user_input != 'exit' :
                print (questions_dict.get(user_input,'one more time'))
        else: 
                user_input == 'exit'
                print ('bb')
                break
            

ask_user (questions_to_ask_dict)






