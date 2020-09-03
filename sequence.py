#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, __
n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1=1
n2=2
n3=3
counter=1
while counter <=n:
    print(n1)
    new_num = n1+n2+n3
    n1=n2
    n2=n3
    n3=new_num
    counter += 1

    
