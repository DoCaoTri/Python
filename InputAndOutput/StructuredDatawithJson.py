import json
print(json.dumps([1, 'simple', 'list']))

f = open("/home/tri/Exercise/Python/Python/InputAndOutput/testdoc.txt", "r+")

x = [1, 'simple', 'list', 10.5]

print(json.dump(x, f))
