a=()
print(a)
print(type(a))

a1=("sumit",45,True,89.98,{"key1":"value1","key2":"value2"},(1,2,3),[4,5,6])
print(a1)
print(type(a1))

b ={}
print(b)
print(type(b))

a2={
    "name":"sumit",
    "age":45,
    "is_student":True,
    "marks":89.98,
    "details":{"key1":"value1","key2":"value2"},
    "tuple_data":(1,2,3),
    "list_data":[4,5,6]
}
print(a2)
print(type(a2))

c=[]
print(c)
print(type(c))

c1=["sumit",45,True,89.98,{"key1":"value1","key2":"value2"},(1,2,3),[4,5,6],{7,0,9}]
print(c1)
print(c1[7])
print(type(c1))

d=set()
print(d)
print(type(d))

d1={"sumit",45,True,89.98,(1,2,3)}
# a1=("sumit",45,True,89.98,{"key1":"value1","key2":"value2"},(1,2,3),[4,5,6]) we cannot insert list and dict inside of a set because list is mutable
print(d1)
print(type(d1))

