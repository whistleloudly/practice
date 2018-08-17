from urllib.request import urlopen

html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('UTF-8')
print(html)

import re
res = re.findall(r"<title>(.+?)</title>",html)
print("Page title is:",res[0])

