'''CREATED BY MUHAMMAD HANAN ASGHAR
DATA SCIENTIST 
PYTHONIST
'''
import requests
from bs4 import BeautifulSoup
def Wallpapers():
    search = str(input("Enter : "))
    def WallpapersPlay(search):
        values = []
        values2 = []
        values3 = []
        html_data = requests.get(f"https://wallpaperplay.com/search?term={str(search)}")
        html = html_data.content
        soup = BeautifulSoup(html,'html.parser')
        anchors_class = soup.find_all("a",class_="fluid")
        for i in anchors_class:
            value = i.attrs.get("href")
            values.append(value)
            if len(values) == 1:
                html_page_data = requests.get(values[0]).content
        for i in range(len(values)):
            soup = BeautifulSoup(requests.get(values[i]).content,"html.parser")
            values2.append(soup)
        for i in values2:
            divs = i.find_all("div",class_="flexbox_item")
            for j in divs:
                value = "https://wallpaperplay.com"+str(j.attrs.get("data-fullimg"))
                if value == "https://wallpaperplay.comNone":
                    pass
                else:
                    values3.append(value)
        return values3
    def WallpapersFlare(search):
        html_data = requests.get(f"https://www.wallpaperflare.com/search?wallpaper={str(search)}")
        html = html_data.content
        soup = BeautifulSoup(html,"html.parser")
        anchors_images = soup.find_all("img",class_="lazy")
        values = []
        for i in anchors_images:
            value = i.attrs.get("data-src")
            values.append(value)
        return values
    def WallpaperCave(search):
        values = []
        values2 = []
        values3 = []
        html_data = requests.get(f"https://wallpapercave.com/search?q={search}")
        html = html_data.content
        soup = BeautifulSoup(html,"html.parser")
        divs = soup.find_all("div",class_="albumphoto")
        for i in divs:
            value = "https://wallpapercave.com/"+i.attrs.get("href")
            values.append(value)
        for i in values:
            value2 = BeautifulSoup(requests.get(i).content,"html.parser")
            values2.append(value2)
        for i in range(len(values2)):
            value = values2[i].find_all("a",class_="addtofavorite")
            for j in value:
                value = "https://wallpapercave.com"+j.attrs.get("src")
                values3.append(value)
        return values3
    def WallpaperAccess(search):
        values = []
        values2 = []
        values3 = []
        html_data = requests.get(f"https://free4kwallpapers.com/search?q={str(search)}")
        html = html_data.content
        soup = BeautifulSoup(html,"html.parser")
        divs = soup.find_all("div",class_="block")
        for i in divs:
            value = i.find("a")
            if value == None:
                pass
            else:
                value = value.attrs.get("href")
                value2 = "https://free4kwallpapers.com"+value
                values.append(value2)
        for i in values:
            soup2 = BeautifulSoup(requests.get(i).content,"html.parser")
            values2.append(soup2)
        for i in values2:
            figures = i.find_all("a")
            for j in figures:
                a = [i for i in j.attrs.get("href")]
                up = [i for i in "uploads"]
                if a[:7] == up:
                    value = "https://free4kwallpapers.com/"+j.attrs.get("href")
                    values3.append(value)
        return values3
    def Zedge(search):
        html_data = requests.get(f"https://www.zedge.net/find/wallpapers/{search}")
        html = html_data.content
        soup = BeautifulSoup(html,"html.parser")
        anchors = soup.find_all("a",class_="igLGYr")
        values = []
        for i in anchors:
            value = "https://www.zedge.net"+i.attrs.get("href")
            values.append(value)
        values2 = []
        for i in values:
            soup2 = BeautifulSoup(requests.get(i).content,"html.parser")
            values2.append(soup2)
        values3 = []
        link = ""
        for i in range(len(values2)):
            a = values2[i].find_all("script")
            a = a[0]
            b = a.string[355:]
            c = [i for i in b]
            c.pop()
            c.pop()
            link = "".join(c)
            values3.append(link)
        values4 = []
        for i in range(len(values3)):
            value = values3[i].find("=")
            value2 = values3[i][value+1:]
            value3 = "https://fsa.zobj.net/crop.php?r="+value2
            values4.append(value3)
        return values4
    def WallpaperHungama(search):
        a = str(search)
        newval = ""
        if " " in a:
            list_search = [i for i in a]
            for i in range(len(list_search)):
                if " " == list_search[i]:
                    list_search[i] = "+"
            newval = "".join(list_search)
        html_data = requests.get(f"https://www.bollywoodhungama.com/?s={newval}&type=image")
        html = html_data.content
        soup = BeautifulSoup(html,"html5lib")
        values = []
        for i in soup.find_all("figure"):
            values.append(i)
        values2 = []
        for i in values:
            value = i.find("a").attrs.get("href")
            if "celeb-photos" in value:
                values2.append(value)
            else:
                pass
        values3 = []
        for i in values2:
            soup = BeautifulSoup(requests.get(i).content,"html5lib")
            values3.append(soup)
        values4 = []
        for i in values3:
            value = i.find_all("li",class_="hash")
            values4.append(value)
        values5 = []
        for i in values4:
            for j in i:
                values5.append(j)
        values6 = []
        for i in values5:
            value = i.find("img").attrs.get("src")
            values6.append(value)
        return values6
    a = WallpapersPlay(search) + WallpapersFlare(search) + WallpaperCave(search) + WallpaperHungama(search) + WallpaperAccess(search) + Zedge(search)
    with open("wallpapers.txt","w",encoding="utf-8") as file:
        for i in a:
            file.write(f"{i}\n")
    return a
wall = Wallpapers()
