# 9. Define a function which takes lengths of three sides of a triangle as arguments and
# display the perimeter or triangle. Define and apply a decorator which checks for the
# validity of the triangle on the basis of lengths of the side. This makes the perimeter to
# be displayed when the triangle can exist with the given lengths of the sides.

# valid traingle= sum of it's two side is greater than third side
def decorator_perimeterTriangle(perimeterT):
    def checktriangle(a,b,c):
        if(a+b>c or b+c>a or c+a>b):
            return perimeterT(a,b,c)
        else:
            print("Invalid Triangle")    
    return checktriangle   

@decorator_perimeterTriangle
def perimeterTriangle(a,b,c):
    return a+b+c

x=perimeterTriangle(int(input("Enter length of three sides of a triangle: ")),int(input()),int(input()))
if(x!=None):
    print(x)
else:
     pass
