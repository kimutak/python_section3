import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://imgnews.naver.net/image/002/2017/03/13/0002026985_001_20170313153101670.jpg"
htmlURL = "http://google.com"

savePath1 = "C:/synergy/inflearnpython/section2/test1.jpg"
savePath2 = "C:/synergy/inflearnpython/section2/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
