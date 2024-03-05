def seriesResistance(numbers):
    sum = 0

    for i in numbers:
        sum = i + sum

    return sum

nums = [1,5,6,3]
numb = [10,30,45,15,5]
j = [ 16,3.5, 6]
k = [0.5, 0.5]

print(seriesResistance(nums))
print(seriesResistance(numb))
print(seriesResistance(j))
print(seriesResistance(k))
