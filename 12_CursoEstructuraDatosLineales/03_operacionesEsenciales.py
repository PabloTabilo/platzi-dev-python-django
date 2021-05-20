fruits=[]
fruits.append("Kiwi")
fruits.append("Berry")
fruits.append("Melon")
#print(fruits)
fruits.sort()
#print(fruits)
fruits.pop()
fruits.insert(0,"Apple")
fruits.insert(1,"Strawberry")
#print(fruits)
fruits.pop(1)
fruits.remove("Apple")
#print(fruits)

def pyramid_sum(l,u,m=0):
    b=" "*m
    print(b,l,u)
    if l>u:
        print(b,0)
        return 0
    else:
        res = l + pyramid_sum(l+1,u,m+4)
        print(b,res)
        return res
pyramid_sum(1, 4)