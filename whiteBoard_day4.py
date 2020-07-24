#

#create a list of even numbers form a list

def even_num(numbers):
    evens=[]
    for num in numbers:
        if num %2 == 0:
            evens.append(num)
        else:
            break
    return evens

numbers= [1,2,3,4,5,6,7]

print(even_num(evens))
