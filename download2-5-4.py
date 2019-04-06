from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# id값은 유일한 것, class는 여러 개
html = """
<html><body>
<div id="main"> 
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html,"html.parser")
h1 = soup.select("div#main > h1")
print('h1', h1)
list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>>", li.string)
#print('h1',h1.string) type이 list이므로 string으로 접근할 수 없다. 따라서 for문을 돌려줘야한다.
#for z in h1:
#   print('h1',h1.string)  // 이러한 경우 select_one을 사용.
