# a="Pakistan";
# substring="KIS"
# space = a+'\t'+substring
#
# #capitalize() capitalize
# print("Captalize()"+ a.capitalize());
#
# #Centre() make caentre
# print("Centre()"+a.center(20));
# print("centre() func with arguments"+a.center(20,'*'))
#
# #casefOld() to make casefold the string
# print(a.casefold())
# print(a.casefold())
#
# #count() to count substring in a string
# count = a.count(substring.casefold())
# print(count)
# count = a.count(substring.casefold(),2,15)
# print(count)
#
# #endswith()
# result = a.endswith("tan")
# print(result)
# result = a.endswith("tan",1,5)
# print(result)
#
#
# #epandtabsize
# print(space.expandtabs());#default size is 8
#
# #find() return -1 if not found else return first index of found string
# print(a.find('tan'));
#
# #.format function  formats the string
# abc = "our country name is {}".format(a);
# print(abc)
#
# # #index()
# # print(abc.index('sasdf'))
#
# #isalnum true if all characteristics are alphanumeric else return false;
# #isalnum();
#
# #is alpha() return true string is alphnumerric
# print(a.isalpha())
#
# #isDecimal return s true string is deciaml else returns false
# print(a.isdecimal())
#
# # #The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
# # B='4564';
# # print(a.isdigit());
# # print(B.isdigit());
# #
# # str="hello*3";
# # list=[]
# # abc= str.split()
# # for i in str:
# #     list.append(i);
# # print(list)
# #
# #
#
#
#
#
# class Man():
#     counter = 0;
#
#     def __init__(self, name, age, qualification):
#         self.name = name
#         self.age = age
#         self.qualification = qualification;
#         Man.counter+=1;
#     def sleeping(self, snooring="khahahah!"):
#         print("person need to sleep" + str(snooring));
#
#     def eating(self, eating="khahahah!"):
#         print("person need to eat" + str(eating));
#
#     def running(self, running="bhah"):
#         print("person need to run" + str(running));
#
# obj1= Man("satiwan",20,"BS");
# print(obj1.name)
# print(obj1.age)
# print(obj1.qualification);
# print(obj1.counter);
# print(obj1.sleeping());
# print(obj1.eating());
# print(obj1.running());
#
# class Baba(Man):
#     pass
#
# class person():
#     counter = 0;
#
#     def __init__(self, name, age, qualification):
#         self.name = name
#         self.age = age
#         self.qualification = qualification;
#         person.counter+=1;
#     def sleeping(self, snooring="khahahah!"):
#         print("person need to sleep" + str(snooring));
#
#     def eating(self, eating="khahahah!"):
#         print("person need to eat" + str(eating));
#
#     def running(self, running="bhah"):
#         print("person need to run" + str(running));
#
# class Man(person):
#     def work(self):
#         print("person work to earn money")
#
# class female(person):
#     def cooks(self):
#         print("female Cooks very well")
#
# obj1=Man("satiwan",22,"BSCS")
# print(obj1.name+" " +str(obj1.age),obj1.qualification)
# print(obj1.work())
# print(obj1.counter);
#
#
# obj2=female("sania",20,"BSCS")
# print(obj2.name+" " +str(obj2.age),obj2.qualification)
# print(obj2.cooks())
# print(obj2.counter);
#

#to make private any variable use __like self.__name=name;
from abc import  ABC,abstractmethod;
class Man(ABC):
    counter = 0;

    def __init__(self, name, age, qualification,gender,address):
        self.name = name
        self.age = age
        self.gender=gender
        self.__address=address
        self.__qualification = qualification
        Man.counter+=1
class female(Man):
    super().__setattr__("satiwan", 22, "BSCS", "sdfs", "sdfsdf");


class person():
    counter = 0;

    def __init__(self, name, age, qualification):
        self.name = name
        self.age = age
        self.qualification = qualification;
        person.counter+=1;
    def sleeping(self, snooring="khahahah!"):
        print("person need to sleep" + str(snooring));

    def eating(self, eating="khahahah!"):
        print("person need to eat" + str(eating));

    def running(self, running="bhah"):
        print("person need to run" + str(running));

class Man(person):
    def eating(self, eating="khahahah!"):
        print("CHILD us eating")


