
f = open('a.php','w')
from urllib.request import urlopen
import urllib3.request
from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import sys
keyword = 'Iphone 12 64 gb'
urlA = 'https://www.amazon.in/New-Apple-iPhone-12-64GB/dp/B08L5VJYV7/?tag=webtrendingams-21&ascsubtag=||1653903837|34241|553|detail-box-vary2-56990|372703097'
urlF = 'https://www.flipkart.com/apple-iphone-12-green-128-gb/p/itm4e0a120f7d9c4?pid=MOBFWBYZQXUEHF48&lid=LSTMOBFWBYZQXUEHF481T4EBB&marketplace=FLIPKART&q=iphone+12&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&fm=organic&iid=8ac0d540-90e7-4874-ac71-04976cef8dac.MOBFWBYZQXUEHF48.SEARCH&ppt=hp&ppn=homepage&ssid=6ymtgus4hs0000001653900517468&qH=7b7504afcaf2e1ea'
urlR = 'https://www.reliancedigital.in/apple-iphone-12-64-gb-black/p/491901528'
prices = {}
a=f'Showing results for : {keyword} in different sites\n'
b="\n"+a+"\n"
fp4=b.replace('\n','<br />')
print(fp4)
def scrape(url):
    if url == urlF:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemF = soup.find_all('div', class_='_4rR01T')
            costF = soup.find_all('div', class_='_30jeq3 _16Jk6d')
            #print(itemF[0].text + " " + costF[0].text)
            costF = costF[0].text[1:]
            prices["Flipkart"] = costF
            fp = "\nData is Retrieved Successfully!!\n"
            fp1 = fp.replace('\n','<br /> ')
            print(fp1)
            print(costF)
            fn = "\n"
            fp2 = '<a href="' +urlF+'" class="hero-btn">link</a></button>'
            print (fp2)
            
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

        except Exception as e:
            fp3="\ndata from Flipkart is not found\n"
            fp4=fp3.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

    elif url == urlA:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemA = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
            costA = soup.find_all('span', class_='store_prc')
            #print(itemA[0].text + " " + costA[0].text)
            costA = costA[0].text[1:]
            prices["Amazon"] = costA
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            print(costA)
            fp2 = '<a href="' +urlA+'" class="hero-btn">link</a></button>'
            print (fp2)

            
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)

        except Exception as e:
            fp="\ndata from Amazon is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)

    elif url == urlR:
        try:
            res = requests.get(url).content
            soup = BeautifulSoup(res, 'html.parser')
            itemH = soup.find_all('a', class_='name')
            costR = soup.find_all('span', class_='pdp__offerPrice')
            #print(itemH[0].text + " " + costH[0].text)
            costR = costR[0].text[1:]
            prices["Reliance Digital"] = costR
            fp="\nData is Retrieved Successfully!!\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            print(costR)
            fp2 = '<a href="' +urlR+'" class="hero-btn">link</a>'
            print (fp2)
            
            fp="\n========================================================\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
        except Exception as e:
            fp="\ndata from Reliance Digital is not found\n"
            fp4=fp.replace('\n','<br />')
            print(fp4)
            fp="\n========================================================\n"
            fp1=fp.replace('\n','<br />')
            print(fp1)
def priceComparision():
    a=f'Showing results for : {keyword} in different sites'
    b="\n"+a+"\n"
    fp4=b.replace('\n','<br />')
    print(fp4)
    
    for item in prices.items():
      a=item[0],":",item[1]
      fp="\n"+item[0]+":"+item[1]+"\n"
      fp4=fp.replace('\n','<br />')
      print(fp4)
        
if __name__ == '__main__':
    print('\nFlipkart.com\n')
    flip=scrape(urlF)
    print('Amazon.in\n')
    ama=scrape(urlA)
    print('Reliance Digital.in\n')
    hap=scrape(urlR)
    b=priceComparision()
message = f"""<html>
<head></head>
<body><p></br>Flipkart : {prices["Flipkart"]}</br></p><a href={ama}>Link</a></body>
</html>"""
f.write(message)
f.close()


