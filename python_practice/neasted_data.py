""" To practise netsted data type"""

# I want to collect list of student information in whichever the order they registered , it's not fixed
# list of dict
# Adding marks for math, science, language to each student
# I need to get each subject mark by it's subject name, How you can modify the existing data type?
import logging

# """ To Practise Type casting operation"""
import logging

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler("python_training.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)
#
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)
class_information = [
    {"name":"xyz",
     "dob":"13/07/2017"},
    {"name":"yz",
     "dob":"12/05/2017"}
]

# for var in iterable_object/Collection:

for student in class_information:
    logger.debug("student:%s"%student)

# count = 0
# for student in class_information:
#     if student["name"] == "yz":
#         class_information[count]["db"] = "13/06/2017"
#
#     count +=1

logger.debug(class_information)
class_information[1]['dob'] = "13/06/2017"

student2 = class_information[1]
logger.debug(type(student2))
logger.debug(student2['name'],student2['dob'])
logger.debug(class_information)

class_information[0]["marks"] = [60, 70, 80]
class_information[1]["marks"] = [70,80, 100]

logger.debug(class_information)

# class_information[0]["marks"]["math']  #

class_information[0]["marks"] = {
    "math":60,
    "science":70,
    "language":80
}

class_information[1]["marks"] = {
    "math":70,
    "science":80,
    "language":90
}

logger.debug(class_information)

class_information[0]["marks"]["science"]=80
logger.debug(class_information)

