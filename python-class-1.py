import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class UserInfo:
    #생성자
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("--------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("--------------")

    def __del__(self):
        print("delete!")

user1 = UserInfo("kim","010-2323-4141")
user2 = UserInfo("park","010-5543-5353")

print(id(user1))
print(id(user2))

#user1.set_info("kim", "010-334-2424")
#user2.set_info("park", "010-234-4424")

user1.print_info()
user2.print_info()
