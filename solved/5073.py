a,b,c = map(int,input().split())
while a!=0 and b!=0 and c!=0:
    if a<b+c and b<a+c and c<a+b:
        if a==b and b==c:
            print("Equilateral")
        else:
            if a==b or b==c or a==c:
                print("Isosceles")
            else:
                print("Scalene")
    else:
        print("Invalid")

    a,b,c = map(int,input().split())