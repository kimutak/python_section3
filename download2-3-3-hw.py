import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

AP1I = "https://ssl.pstatic.net/tveta/libs/1226/1226284/2bfe79b7a2b7b2db5d8f_20190326202308410.jpg"
API2 = "https://ssl.pstatic.net/tveta/libs/1229/1229310/0ffc922810a5ba8f82d7_20190318155927695.jpg"
values = {
    'csxCd' : '1001'
}
print("before", values)
params = urlencode(values)
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode("utf-8")
print("출력", reqData)
