import sys
import os
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self): # self = 객체 자기 자신
        print("function2 called!")

f = SelfTest()
#print(dir(f))

print(id(f))
f.function2() # 자기 자신을 instance로 넘긴다
print(SelfTest.function1()) # 즉시 호출
