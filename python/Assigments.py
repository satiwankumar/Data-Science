# # #queestion
# # #
# # # def donuts(count):
# # #   if(count >= 10):
# # #     return  "many"
# # #   return "number of donuts count " + str(count)
# # #
# # # print(donuts(5))
# # #
# #
# #
# # question2
# #
# # def both_ends(s):
# #   # +++your code here+++
# #   if(len(s)<2):
# #     return  " "
# #   else:
# #     str1=s[:2]
# #     str2=s[-2:]
# #   return print(str1+str2)
# #
# # both_ends("pardeep")
# #
#
# #question3
# # # s= "satiwan"
# # # print()
# # #
# # # def fix_start(s):
# # #     for i in s:
# # #         if(i==s[0:1] ):
# # #            k= s.replace(i,"*")
# # #         return k
# # #
# # # print(fix_start("babble"))
# # #
# # # #
# # question4
# #
# # def mix_up(a, b):
# #   str1 = a[0:2]+b[2:]
# #   str2 = b[0:2]+a[2:]
# #   return str1 + ' ' +str2
# #
# # # #
# # # print(mix_up("Satiwan","kumar"))
# #
# #
# #
# # #question 5
# # def verbing(s):
# #   # +++your code here+++
# #   if(s[-3:]!="ing" and len(s)>=3):
# #      s=s.replace(s[-3:],"ing")
# #   elif(s[-3:]=="ing"):
# #      s=s.replace(s[-3:],"ly")
# #   return s
# # print(verbing("hail"))
#
# #question 6
# #
# # def not_bad(s):#
# #     # +++your code here+++
# #   a= s.find("not")
# #   b=s.find("bad")
# #   if(a!=-1 and b!=-1 and b>a):
# #       print(s[0:a] + "good")
# #   else:
# #       print(s)
# #   return  print(a)
# #
# # not_bad("This dinner is not that bad!")
# #
# # question 7
# #
# # words = ["alia","kamran","paredeep","damad"]
# # def match_ends(words):
# #     count =0
# #     for i in words:
# #         if(i[-1:] == i[0:1] and len(i)>2):
# #             count +=1
# #     return count
# # print(match_ends(words))
# #
# # question 8
# # otherlist = []
# # word=['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
# # def front_x(words):
# #     for i in words:
# #         if i[0] == 'x':
# #            otherlist.append(i)
# #     for i in otherlist:
# #         if i in words:
# #             words.remove(i)
# #     words.sort()
# #
# #     return print(otherlist +words)
# #
# #
# #
# #
# # front_x(word)
# #
# #
# #
# # question 9 //error
# # tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# # last = 0
# # def sort_last(tuples):
# #     for i in tuples:
# #         last = i[-1]
# #     sorted(tuples, key=last)
# #     return print(tuples)
# #
# # sort_last(tuples)
# #
# # question 10
# #
# #
# #
# #
#
#
# dict  = {
# }
# id=0
# while(id!=-1):
#     id = int(input("Enter your id in integer"))
#
#     if(id==-1):
#         print("Thank you for using this program")
#     else:
#         name = input("Enter your name")
#         dict[id] = name
#         print(dict)
#

# names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
# names2 = names1
# names3 = names1[:]
# names2[0] = 'Alice'
# names3[1] = 'Bob'
# sum = 0
# for ls in (names1, names2, names3):
#     if ls[0] == 'Alice':
#          sum += 1
#     if ls[1] == 'Bob':
#           sum += 10
# print(sum)
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# # print(len(list1 + list2))
# print([j for i in range(2,8) for j in range(i*2, 50, i)])

# c = ['satiw','kumar']
# result = map(tuple,c)
# print(list(result))



