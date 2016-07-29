import math
print("Input the coordinates of the first TOP")
x1=float(input("x1= "))
y1=float(input("y1= "))
print("Input the coordinates of the second TOP")
x2=float(input("x2= "))
y2=float(input("y2= "))
print("Input the coordinates of the third TOP")
x3=float(input("x3= "))
y3=float(input("y3= "))
a=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
b=math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3));
c=math.sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1));

if((a+b>c) & (c+b>a) & (a+c>b)):
	print("Input the coordinates of the POINT")
	x0=float(input("x0= "))
	y0=float(input("y0= "))
else:
	print("Input the right coordinates of the triangle")
	raise SystemExit


vec1 = (x1-x0)*(x2-x0) + (y1-y0)*(y2-y0)
vec2 = (x2-x0)*(x3-x0) + (y2-y0)*(y3-y0)
vec3 = (x1-x0)*(x3-x0) + (y1-y0)*(y3-y0)

len1 = math.sqrt((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1))
len2 = math.sqrt((x0-x2)*(x0-x2) + (y0-y2)*(y0-y2))
len3 = math.sqrt((x0-x3)*(x0-x3) + (y0-y3)*(y0-y3))

alpha1 = math.acos(vec1/(len1*len2))
alpha2 = math.acos(vec2/(len2*len3))
alpha3 = math.acos(vec3/(len3*len1))
sum = alpha1+alpha2+alpha3

if(sum == 2*math.pi):
    print("The dot is inside")
else:
    print("The dot is outside")
