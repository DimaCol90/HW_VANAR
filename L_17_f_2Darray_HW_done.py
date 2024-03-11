from random import randint

def random2dArray(row,cols,edge1,edge2):
    matrix=[]

    for ri in range(row):
        row=[]
        for ci in range(cols):
            row.append(randint(edge1,edge2))

        matrix.append(row)
    return matrix

##################################



def print2dArray(matrix):
    print() 
    print(f"Matrix Size: {len(matrix)} rows x {len(matrix[0])} columns")
    print()
    for ri in range(len(matrix)):
        for ci in range(len(matrix[0])):
            print(f'{matrix[ri][ci]:5}', end="")
        print()


##################################
        
def average2dArray(matrix):
    s=0
    h=len(matrix)
    w=len(matrix[0])
    for ri in range(h):
        for ci in range(w):    
            s+=matrix[ri][ci]

    average=s/(h*w)
    return average

def findMinMax2dArray(matrix):
    min_val = matrix[0][0]
    max_val = matrix[0][0]

    for row in matrix:
        for val in row:
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
                
    return [min_val, max_val]


data=random2dArray(5,3,int(input("input lower limit: ")), int(input("input higher limit: ")))            
print2dArray(data)

a=average2dArray(data)
print ("average is: ",a)

min_max = findMinMax2dArray(data)
print("Minimum and Maximum values are:", min_max)
#hw3 - create another function that finds min and max, 
# and returns them grouped in a list and print them
 