import random

def bin_search(list, number):
    print("Bin search func: "+str(number))
    while(True):
        half_len = int(len(list)/2)
        if(number == list[half_len]):
            return True
        elif(half_len == 0):
            return False
        elif(number < list[half_len]):
            list = list[0:half_len]
        else:
            list = list[half_len:]
        
if __name__=="__main__":
    list =  sorted(random.sample(range(0,1000), random.randint(1,1000)))
    number = random.randint(0,1000)
    print("Random generated list:", list)
    ret_val = bin_search(list,number)
    if(ret_val): print("Number " + str(number) + " is present in list")
    else: print("Number " + str(number) + " is not present in list")

