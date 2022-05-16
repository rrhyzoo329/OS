import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text

soup=BeautifulSoup(html,'html.parser')
links = soup.select(".news_tit") # 결과 리스트로 출력
for link in links:
    title = link.text #태그 안에 텍스트 요소를 가져온다
    url = link.attrs['href'] #텍스트 안 href 속성값을 가져온다
    print(title,url)