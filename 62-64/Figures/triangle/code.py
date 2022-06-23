a_=7
b_=2
c_=8
__all__=["triangle_perimeter","triangle_area"]
def triangle_perimeter(a=a_, b=b_, c=c_):
    P=a+b+c
    return P
def triangle_area(a=a_, b=b_, c=c_):
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**(1/2)
    return S