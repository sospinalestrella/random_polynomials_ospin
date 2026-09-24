#Samuel OSPINAL
#Random polynomials

import random



def get_coeff(maxi):
    abel = []
    for i in range(maxi, -1 ,-1):
        abel.append(i)

    return abel
        
def is_empty(alist):
    if len(alist) == 0:
        return True
    else:
        return False


#degrees is a list of degrees
#alist is a list of coefficients


def get_pol(degree = 10, alist = get_coeff(4)):
    b = len(alist) - 1
    x = 'x'
    pol = ''
    degree_list = []
    for i in range(degree, -1 ,-1):
        degree_list.append(i)

        
    while is_empty(degree_list) == False :
        pol = pol + f"{alist[0]}" + x + f"**{degree_list[0]}" + '+'
        alist.pop(0)
        degree_list.pop(0)
        if is_empty(alist) == True:
            alist = get_coeff(b)        
        

    pol = pol.rstrip('+')
    return pol




def evaluate(value, pol):
    pol = pol.replace('x', f"*({value})")

    return eval(pol)




def get_bundle(amount):
    abel = list(range(0,10))
    bundle = []
    for i in range(0,amount):
        asample = random.sample(abel,k=2)
        pol = get_pol(degree = asample[0], alist = get_coeff(asample[1]))
        #print(pol)
        bundle.append(pol)
    
    return bundle



def union_of_bundles(amount_of_bundles, sample_size):
    cain = []
    for i in range(0,amount_of_bundles):
        #print(f"TRIAL {i+1}")
        abundle = get_bundle(amount = sample_size)
        cain.append(abundle)

    final = []
    
    for i in range(0,amount_of_bundles):
        for j in range(0,sample_size):
            print(cain[i][j])
            final.append(cain[i][j])
    return final
 

def antipodes(union):
    b = len(union)
    length = []
    for i in range(0,b):
        length.append(len(union[i]))
        if len(union[i]) == max(length):
            longest = max(length)
            ind_longest = i

        if len(union[i]) == min(length):
            shortest = min(length)
            ind_shortest = i


    return print(f"The longest polynomial is:\n{union[ind_longest]}\nIts index is {ind_longest}\nThe shortest polynomial is:{union[ind_shortest]}\nIts index is {ind_shortest}")
        
        
    
    
#union = union_of_bundles(10,5)
#antipodes(union)

union = union_of_bundles(20,4) 
antipodes(union)
