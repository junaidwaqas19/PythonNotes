def get_circle_info(radius):
    pi =3.14
    area = pi * radius **2
    circumference = 2* pi *radius
    return area,circumference,pi
# simultaneous assignments
a,c,p=get_circle_info(5.0)

print(a,c,p)

