dict1 = {'foo':'bar', 'fizz':'buzz'}

dict2 = {'fizz':'fizzbuz', 'test':'flasky'}

dict1 |= dict2

print(dict1)

dict1['invalid']