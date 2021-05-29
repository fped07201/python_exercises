import random

def removeListDuplicatesLoop(in_list):
    ret_list = []
    [ret_list.append(n) for n in in_list if n not in ret_list]
    return ret_list


def removeListDuplicatesSet(in_list):
    return list(set(in_list))

input_list = [random.randint(0,100) for n in range(random.randint(10,100))]
print("Random generated input list: ",input_list)
print("Input list length: ", len(input_list))
print("\r\n")

out_list = removeListDuplicatesLoop(input_list)
print("New list removing duplicates(loop function): ", out_list)
print("Output list length: ", len(out_list))
print("\r\n")

out_list = removeListDuplicatesSet(input_list)
print("New list removing duplicates(set function): ", out_list)
print("Output list length: ", len(out_list))
