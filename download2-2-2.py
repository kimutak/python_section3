import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://imgnews.naver.net/image/002/2017/03/13/0002026985_001_20170313153101670.jpg"
htmlURL = "http://google.com"

savePath1 = "C:/synergy/inflearnpython/section2/test1.jpg"
savePath2 = "C:/synergy/inflearnpython/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)



print("다운로드 완료!")
