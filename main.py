### Bubble sort #####
# pass1
# 9,8,7,6,5,4,3
# 8,9,7,6,5,4,3
# 8,7,9.6.5.4.3
# 8,7,6,9,5,4,3
# 8,7,6,5,9,4,3
# 8,7,6,5,4,9,3
# 8,7,6,5,4,3,9
# after full loop highest no. is bubbled to last

# #pass2
# 7,8,6,5,4,3,    9
# 7,6,8,5,4,3,    9
#######

lst = [9,8,7,6,5,4,3]

def swap_list_ele(lst,i,j):
    lst[i], lst[j] = lst[j], lst[i]

# swap_list_ele(lst,0,1)
# print(lst)

## bubblesort does not return it sort the same list
def bubblesort(lst):
    leave = 1
    while leave <= len(lst):
        for i in range(len(lst)-leave):
            if lst[i] > lst[i+1]:
                swap_list_ele(lst, i, i+1)

        leave += 1

if __name__ == '__main__':
    bubblesort(lst)
    print(lst)

