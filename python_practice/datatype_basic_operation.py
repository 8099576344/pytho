""" To practice basic operation"""
# ================== Numbers =============== #
a = 2
salary = 120034.24

streaming_bit_octal = 0o12
streaming_bit_hex = 0x12
print(a)
print(salary)
print(streaming_bit_octal)
print(streaming_bit_hex)

# # ============= Strings ============== #
message = 'Hello world'
message2 = "Hello world"

print(message)
print(message2)
print(message == message2)

# Multi-line string
message3 = """Hello
            this is multi-line string.
            used for Documenting functions, modules, classes
            methods"""

print(message3)
#
message4 = "Hello this is single line string , " \
           "and it should not more than 120 " \
           "characters in same line"

print(message4)

message5 = "Hello this is single line string , \nand it should not more than 120 \n" \
           "characters in same line"

print(message5)
#
# # ==================== List & Tuple ================== #
list1 = [1, 20.2, "Python", [1, 3, 4]]

tuple1 = (1, 20.2, "Python", [1, 3, 4])

print(list1)
print(tuple1)
print(type(list1))
print(type(tuple1))
del list1[1:2]
print(list1)
#
# Use ',' if single data in tuple
a = (1)
print(a)  # 1
print(type(a))  # <class 'int'>
a = (1,)
print(a)  # (1,)
print(type(a))   # <class 'tuple'>

# # =============== Dict & Set & Frozenset =============== #
employee_id_data = {"xyz": 1,
                    "mn": 2,
                    "ll": 5,
                    "mn": 12
                    }

print(employee_id_data)
print(type(employee_id_data))
print(employee_id_data["xyz"])  # 1
print(employee_id_data["mn"])  # 12

employee_id_data["naresh"] = 1234
print(employee_id_data)
employee_id_data["naresh"] = 2435
print(employee_id_data)
del employee_id_data["xyz"]
print(employee_id_data)



unique_emplyee_set = {1, 2, 3, 1, 12 , 3}  # { 1, 2 ,3 , 12 }

print(unique_emplyee_set)
print(type(unique_emplyee_set))

set_with_empty = {}
print(type(set_with_empty))    # <class 'dict'>

employee_data = frozenset(unique_emplyee_set)
print(employee_data)
print(type(employee_data))

# ===================== Basic operations ============ #

print(4/2)    # 2.0
print(4/2.0)  # 2.0

print(4//2)   # 2
print(2/3)
print(2//3)
print(9/4)
print(9//4.0)


print(2**3)


# sequential data type
# [ start[0]: end[len(object): step[1] ]
# [:] or [::]
#  p y t h o n
#  0 1 2 3 4 5
name = "python"
print(name[0])  # p
print(name[:])  # python
print(name[1:5])  # ytho
print(name[::])  # python

# Repetition
print("*==="*12)
print("*==="*12)


list_lan = ["python", "java", "ruby", "scala", "R"]
list_lan[2] = "Ruby"
print(list_lan)

del list_lan[1:2]
print(list_lan)
del list_lan[:]
print(list_lan)