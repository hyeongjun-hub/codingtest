import copy

a = [1,[2,4,5],3]
c = a[:]
# slice한 a를 대입 - nested(중첩된)list는 적용되지 않는다
b = copy.copy(a)
# shallow copy - 모든 타입의 변수를 복사가능, nested(x)
d = copy.deepcopy(a)
# deep copy - 모든 타입의 변수를 복사가능, nested(o)
print(a)
print(b)
a[1][0] = -99
print(a)
print(b)
print(d)