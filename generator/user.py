import jsonpickle
import random
import string
import os.path
import getopt
import sys
from models.user import User


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_phone():
    symbols = '+7' + ''.join(random.choice(string.digits) for i in range(10))
    return symbols


def random_mail():
    symbols = ''.join(random.choice(string.ascii_letters) for i in range(5)) + '@email.com'
    return symbols


test_data = [
    User(fname=random_string("fname", 10), mname=random_string("mname", 15), lname=random_string("lname", 15),
         nickname=random_string("nickname", 10), company=random_string("company", 10), address=random_string("address", 10),
         home_phone=random_phone(), mobile=random_phone(), work_phone=random_phone(), fax=random_string("fax", 5),
         email1=random_mail(), email2=random_mail(), email3=random_mail(), note=random_string("note", 10),
         second_phone=random_phone())
    for i in range(2)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
