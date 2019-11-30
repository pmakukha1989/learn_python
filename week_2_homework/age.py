print(
    "введите возрат пользователя"
)
age = input()

def occupation (years):
   
    try:   
        years = float (years)
        
        if years >0 and years <7:
            to_return = 'детский сад'
        elif years >=7 and years <17:
            to_return = 'школа'
        elif years >=17 and years <=22:
            to_return = 'ВУЗ'
        elif years >22 and years < 99:
            to_return = 'работать'
        else :
            to_return = 'error'
        return to_return
    except TypeError:
        return 'TypeError'
    except ValueError:
        return 'ValueError'


to_print= occupation(age)
print (to_print)