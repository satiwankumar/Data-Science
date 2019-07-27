#
# #
# # print("DAy one Challenge")
# # def get_table(num):
# #     for i in range(1, 11):
# #         result = num * i
# #         print(str(num) + "*" + str(i) + " = " + str(result))
# #
# #
# #
# #
# #
# #
# # num = int(input("Enter your number  to get the table"))
# # get_table(num)
# #Question 2
# # #Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# # between 2000 and 3200 (both included).
# # The numbers obtained should be printed in a comma-separated sequence on a single line.
# #
# # list = []
# # for i in range(2000,3201):
# #     if((i%7==0) and  (i%5 !=0)):
# #        list.append(str(i))
# #
# #
# # print(','.join(list))
#
# #Question 2
# # Write a program which can compute the factorial of a given numbers.
# # The results should be printed in a comma-separated sequence on a single line.
# # Suppose the following input is supplied to the program:
#
# # def fact(x):
# #     if x == 0:
# #         return 1
# #     else:
# #         return x * fact(x-1)
# # print(fact(8))
# #Question 3
# # #With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n
# # (both included). and then the program should print the dictionary.
# # Suppose the following input is supplied to the program:
# # 8
# # Then, the output should be:
# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# # dic = {}
# # def get_integral(n):
# #     for i in range(1,n+1):
# #         dic.update([(i,i*i)])
# #     return dic
# #
# #
# # print(get_integral(5))
#
# #Question 4
# # Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# # Suppose the following input is supplied to the program:
# # 34,67,55,33,12,98
# # Then, the output should be:
# # ['34', '67', '55', '33', '12', '98']
# # ('34', '67', '55', '33', '12', '98')
#
# # values = input("Enter your values")
# # l=values.split(',')
# # t=tuple(l)
# # print(l)
# # print(t)
#
# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu =cpu
#         self.ram =ram
#
#
#     def config(self):
#         print("I5, 16 gb machine")
#
# comp=computer()





