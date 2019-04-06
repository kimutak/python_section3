from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://www.daum.net/"

res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

#print(soup)
recommand = soup.select("div.rank_cont > span.txt_issue> a[tabindex='-1']")
#print(recommand)

for i,e in enumerate(recommand,1):
    print(i,e.string , e.attrs["href"])
