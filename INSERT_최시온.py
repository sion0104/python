import os

def insertion_ASC(lst):
    for j in range(1, len(lst)):
        i = 1

        array_num = 0
        name_list2 = list(lst[j])
        name_list1 = list(lst[i-1])
    
        while name_list2[array_num] >= name_list1[array_num]:
            array_num = 0
            while (array_num+1) != len(name_list2) and (array_num+1) != len(name_list1) and name_list2[array_num] == name_list1[array_num]:
                array_num += 1
                
            if name_list2[array_num] > name_list1[array_num]:
                i += 1
            
            if len(name_list2) == (array_num+1):
                break
            
            name_list1 = list(lst[i-1])
            
        temp = lst[j]
        
        for k in range(0, j-(i-1)):
    
            lst[j-k] = lst[j-k-1]

        lst[i-1] = temp

    print(*lst, sep=', ')

def insertion_DESC(lst):
    for j in range(1, len(lst)):
        i = 1

        array_num = 0
        name_list2 = list(lst[j])
        name_list1 = list(lst[i-1])
    
        while name_list2[array_num] <= name_list1[array_num]:
            array_num = 0
            while (array_num+1) != len(name_list2) and (array_num+1) != len(name_list1) and name_list2[array_num] == name_list1[array_num]:
                array_num += 1
                
            if name_list2[array_num] < name_list1[array_num]:
                i += 1
            
            if len(name_list2) == (array_num+1):
                break
            
            name_list1 = list(lst[i-1])
            
        temp = lst[j]
        
        for k in range(0, j-(i-1)):
    
            lst[j-k] = lst[j-k-1]

        lst[i-1] = temp

    print(*lst, sep=', ')
    
animal_name = ["elephant","giraffe","hippo","otter","seal","meerkat","whale","hedgehog","tiger","lion","heyne","buffalo","zebra","rhinoceros","squirrel"]

print("INSERTION SORT")

print("○" + "-" * 150)

print("[Input String] : ", end = "")
print(*animal_name, sep = ', ')

print("[IAcending order] : ", end = "")
insertion_ASC(animal_name)

print("[Descending order] : ", end = "")
insertion_DESC(animal_name)

print("○" + "-" * 150)

os.system('pause')
