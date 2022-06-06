#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(a):
    for x in range (len(a)):
        if a[x] > 0 :
            print("big")
        else:
            print(a[x])

    return a[x]

biggie_size([-1, 3, 5, -5])


# Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).

def count_positives(a):
    
    count=0
    for x in range(len(a)): 
        if a[x] > 0:
            count += 1
    a[len(a)-1] = count
    return a
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
def sum_total(a):
    count=0
    for x in range(len(a)):
        count+=a[x]
    return count
 
print(sum_total([1,2,3,4]))


#Average - Create a function that takes a list and returns the average of all the values.x

def average(a):
    count=0
    for x in range(len(a)):
        count+=a[x]
        avr=count/len(a)
    return avr
 
print(average([1,2,3,4]))


#Length - Create a function that takes a list and returns the length of the list.
def length(a):
    
    for x in range(len(a)):
        length=len(a)
        
    return length
 
print(length([1,2,3,4]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
def minimum(a):
    min = False
    if len(a) > 0:
        min = a[0]
        for x in range(len(a)):
            if a[x] < min:
                min = a[x]
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

#max
def maximum(a):
    max = False
    if len(a) > 0:
        max = a[0]
        for x in range(len(a)):
            if a[x] > max:
                max = a[x]
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

def ultimate_analysis(a):
    a_analysis = {}
    a_analysis['sumTotal'] = sum_total(a)
    a_analysis['average'] = average(a)
    a_analysis['minimum'] = minimum(a)
    a_analysis['maximum'] = maximum(a)
    a_analysis['length'] = length(a)
    return a_analysis
print(ultimate_analysis([37,2,1,-9]))

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def Reverse(lst):
    lst.reverse()
    return lst
     

print(Reverse([10, 11, 12, 13, 14, 15]))
    


    





    


