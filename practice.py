
# !!! Identifying the Differences in Lists

# list_1 = [1, 3, 5, 7, 8]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# solution_1 = list(set(list_2) - set(list_1))
# solution_2 = list(set(list_1) ^ set(list_2))
# solution_3 = list(set(list_1).symmetric_difference(set(list_2)))

# print(f"Solution 1: {solution_1}")
# print(f"Solution 2: {solution_2}")
# print(f"Solution 3: {solution_3}")

##################################################################################################

# def some_function(*args, **kwargs):
#     print(f"Args: {args}")
#     print(f"Kwargs: {kwargs}")


# some_function(1, 2, 3,  a=4, b=5, c=6)


######################################################################################################



###############################################################################################3


# def split_string(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string

#     return wrapper


# def upper_string(function):
#     def upper():
#         func = function()
#         upper_str = func.upper()
#         return upper_str
    
#     return upper


# @split_string
# @upper_string
# def say_hi():
#     return 'hello there'
# print(say_hi())

############################################################################################

# class ExceptionProxy(Exception):
#     def __init__(self, msg, function):      
#         self.msg = msg
#         self.function = function

# def transform_exceptions(func_ls):
#     data = []
#     for func in func_ls:
#         try:
#             func()
#             data.append(ExceptionProxy("ok!", func))
#         except Exception as e:
#             data.append(ExceptionProxy(str(e), func))

#     return data


# def f():
#     1/0

# def g():
#     pass

# tr_ls = transform_exceptions([f, g])

# for tr in tr_ls:
#     print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)

#######################################################################################

# txt = "xxxxxxxxbananaxxxxxxxxx"
# x = txt.strip()
# print(x)

# x = input("enter a number")
# print(x.strip())


# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")   # delete specific character
# print(x)

# txt = "bananab"
# x = txt.strip("b")
# print(x)

##########################################################################################

# def factoriel(n):
#     if n < 1:
#         return "is not acceptable"
#     if n == 1:
#         return 1
#     else:
#         return n * factoriel(n-1)

# print(factoriel(6))

############################################################################################

# def fibo(n):
#     fibonacci = [1, 1]
#     count = 0

#     while count < n - 2:
#         sum = 0
#         for i in fibonacci[-2:]:
#             sum += i
#         fibonacci.append(sum)
#         count += 1
#     return fibonacci

# print(fibo(10))

#################################################################################################

# string = "Hello welcome to python toturial"

# splitted_string = string.split()

# new_array = [word[::-1] for word in splitted_string]

# for word in new_array:
#     print(word, end=" ")

# print()

################################################################################################

# def reverse_keyvalue(dic: dict):
#     reverse_dic = {v: k for k, v in dic.items()}
#     return reverse_dic

# print(reverse_keyvalue({'A': 20, 'B': 30}))

#################################################################################################

# import collections

# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

# duplicates = []
# for item, count in collections.Counter(sample_list).items():
#     if count > 1:
#         duplicates.append(item)
# print(duplicates)

###############################################################################################
# d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# l1 = ['A', 'C', 'F']

# def specific_items(sample_dict: dict, specific_list: list):
#     new_dict = {v: k for v, k in sample_dict.items() if v in specific_list}

#     return new_dict

# print(specific_items(d1, l1))

############################################################################################

# a = int(input('enter an integer number:'))
# print(str(a//31) + ' month' + '\n' + str(a%31) + ' day')

############################################################################

# import numpy as np
# arr = np.array([i for i in range(0, 36)])

# # array in range(36)
# print(arr, end='\n\n')

# newarr = arr.reshape(6, 6)

# # 6*6 array
# print(newarr, end='\n\n')

# # reverse array 
# print(arr[::-1], end='\n\n')

# newarr3 = arr[::-1].reshape(6, 6)
# # reverse each index of array
# print(newarr3, end='\n\n')

# newarr2 = np.array_split(arr, 6)
# for a in newarr2:
#     print(a, end=' ')

###########################################################################################

# import numpy 

# iranFootball = numpy.array([1978, numpy.nan, 1998, "2006", 2014.0, 2018, 2022, numpy.nan])

# iranFootball = [int(float(x)) for x in iranFootball if x != 'nan']

# print(iranFootball)

# # last element of array
# print(iranFootball[-1])