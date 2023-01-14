#Approach1
"""
def print_odd_desc(*a):
    x = []
    for n1 in a:
        if n1%2==1:
            x.append(n1)
             x.sort()    
        x.reverse()       ## descending order
    print(x)
print_odd_desc(1,2,33,5,7,6)
print_odd_desc(1,2,33,6,7,8,9,51,12,99)
"""

#Approach2
def print_odd_desc(*a):
    x = []
    for n1 in a:
        if n1%2!=0:
            x.append(n1)
        x.sort()    
        x.reverse()       ## descending order
    print(x)
print_odd_desc(1,2,33,5,7,6)
print_odd_desc(1,2,33,6,7,8,9,51,12,99)
