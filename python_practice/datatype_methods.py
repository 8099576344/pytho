"""To Practise data types methods"""
# dir help

import logging

# create logger
logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
fh = logging.FileHandler("python_training.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug(dir("python"))
logger.debug(dir(str))

logger.debug(help(str.isalnum))


logger.debug("welcome to python".capitalize())
logger.debug("python".istitle())
logger.debug("python".islower())
logger.debug("The converted message %s","welcome to python".title())

logger.debug("python".isalpha())

user_input = "teja"
logger.debug("the user input: %s", user_input.isdecimal())

logger.debug("123".isdecimal())

logger.debug(user_input.isalnum())

logger.debug("python".isspace())
logger.debug("\n".isspace())
logger.debug("\t".isspace())
logger.debug("tt".isspace())

up_var = "python".lower()
low_var = up_var.lower()
logger.debug(up_var.isupper())
logger.debug(low_var.islower())


logger.debug("python".swapcase())
logger.debug("Python".swapcase())

logger.debug("python".endswith("hon"))
logger.debug("python".startswith("p"))
logger.debug(user_input.isalnum())

# logger.debug(dir("java"))







