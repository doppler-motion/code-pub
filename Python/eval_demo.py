import ast


dict_str = '{"a": 1, "b": 2}'

dict_1 = eval(dict_str)
dict_2 = ast.literal_eval(dict_str)

print("dict_1: ", dict_1)
print("dict_2: ", dict_2)
