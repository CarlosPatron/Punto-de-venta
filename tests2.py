import ast

strList = '[[1, 1], [2, 1]]'

def convert(string):
    string = ast.literal_eval(string)
    print(string)

convert(string=strList)