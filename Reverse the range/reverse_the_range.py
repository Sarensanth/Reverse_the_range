def reverse_the_range(array,start,end):
    
    i=start
    j=end
    while i<j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1
    return array

array=list(map(int,input().split()))
start=int(input("Enter the starting point: "))
end=int(input("Enter the ending point: "))
print(reverse_the_range(array,start,end))