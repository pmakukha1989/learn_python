print ('input str_1')
input_str_1 = input ()
print ('intup str_2')
input_str_2 = input ()

def compare_str (str_1, str_2):
    if type(str_1) == str and type(str_2) ==str :
        if str_1 == str_2:
            return '1'
        elif len (str_1) > len(str_2):
            return '2'
        elif str_1 != str_2 and str_2 =='learn':
            return '3'

    else:
         return '0' 

print (compare_str(input_str_1, input_str_2))