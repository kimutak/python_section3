from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser") #파이썬에서 .html형식의 파일을 파싱할 수 있도록 지원하는 모듈

links = soup.find_all("a") # html의 a태그형식을 모두 받는다
a = soup.find_all("a", string="daum")# daum의 태그들을 가져온다.
print('a', a)
b = soup.find_all("a", limit=3) #a태그 개수 제한
print('b', b)
c = soup.find_all(string=["naver", "google"])
print('c', type(c))

for a in links:
    #print('a', type(a), a)
    href = a.attrs['href']  #attrs = 속성 ex)href속성값을 받는다
    txt = a.string
    #print('txt >> ', txt, 'href >> ',href)
