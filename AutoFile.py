import requests
from bs4 import BeautifulSoup

level = "Bronze3"
level_site = "https://solved.ac/problems/level/3"

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(level_site,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

pages = soup.select(".Paginationstyles__PaginationWrapper-sc-dc43mb-2 > a")

for x in range(1,int(pages[-1].get_text())+1):
    next_site = level_site+"?page="+str(x)
    trs = soup.select(".sticky-table-table > .sticky-table-row > .sticky-table-cell > span > .ProblemInline__ProblemStyle-sc-1w7zwvy-0 > span")

    for span in trs:
        name = span.get_text()
        fileName = "BaekJoon/" + level + "/Num" + name + ".py"
        f = open(fileName, 'w')
        f.write("#https://www.acmicpc.net/problem/" + name)
        f.close()






