questions_to_ask_dict = {
     "hru?": "good",
     "what?": "code",
     "why?" : "cause",
     }


def ask_user (questions_dict):
    for question in questions_dict:
        answer = ''
        while questions_dict [question] != answer:
            print (question)
            answer = input ()

ask_user (questions_to_ask_dict)






