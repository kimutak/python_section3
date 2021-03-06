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

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("강아지")
url = base + quote
#print(url)

res = req.urlopen(url)
savePath = "C:\\synergy\\inflearnpython\\section2\\imagedown\\"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath)) #절대경로를 가져와 파일을 생성한다.
except OSError as e:
    if e.errno != errno.EEXIST: # 이미 존재
        print("폴더 만들기 실패!")
        raise #에러 강제 발생

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area._item > a.thumb._thumb > img")

for i, img_list in enumerate(img_list, 1):
    #print(img_list["src"])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    req.urlretrieve(img_list['data-source'],fullFileName)

print("다운로드 완료!")
#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > span.img_border
