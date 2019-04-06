from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌")
url = base + quote
#print(url)

res = req.urlopen(url)
savePath = "C:\\synergy\\inflearnpython\\section2\\imagedown2\\"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath)) #절대경로를 가져와 파일을 생성한다.
except OSError as e:
    if e.errno != errno.EEXIST: # 이미 존재
        print("폴더 만들기 실패!")
        raise #에러 강제 발생

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("ul.slides")[0]

for i, e in enumerate(img_list, 1):
    #print(img_list["src"])
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.png')
    req.urlretrieve(e.select_one("div.block_media > a > img")['src'],fullFileName)

print("다운로드 완료!")
#\37 69 > div > ul > li:nth-child(2) > div > div.block_media > a > img
