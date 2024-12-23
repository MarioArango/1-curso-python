#Las tuplas son inmutables
numbers = (1,2,3,4,5)
numbers2 = 1,2,3,4,5
print(id(numbers))
print(id(numbers2))
print(numbers == numbers2)
print(numbers is numbers2)
print(numbers[0])
