def swap (lst):
    if len(lst) > 1:
     lst[0], lst[1] = lst[1], lst[0]
     return lst

lst=[4,0,1,-2]
res= swap(lst)
print(res)
