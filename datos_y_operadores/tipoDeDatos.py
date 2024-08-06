"""
                    type of data
    
      numeric   dictionary  boolean   set   sequence type
        |                                         |         
    int - float                               str - tuple  
        |                                         |
     complex number                              list
"""
x = 1
y = 1.1
z = 'str'
a = 'str long'
e = -1
i = (x,y)
o = [x,y]
u = {'num':x,'num2':y}
b = True

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(e))
print(type(i))
print(type(o))
print(type(u))
print(type(b))