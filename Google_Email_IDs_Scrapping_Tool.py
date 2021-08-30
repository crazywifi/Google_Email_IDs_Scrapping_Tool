#Python3
import requests
from bs4 import BeautifulSoup
import re
import time
from random import randint

regex = r"([a-zA-Z0-9_.+-])+(@gmail.com)"
i = 51
data = []
while (i<60):
        f = open("emaillist.txt","a")
        #Google Dork used here: [intext:"gmail.com" site:linkedin.com], for changing the page like in Google we chaged the page number, I used "i" variable for that.
        page = requests.get("https://www.google.com/search?q=intext:%22gmail.com%22+site:linkedin.com&sxsrf=ALeKk01cBkyaitS1ypoG5y5oPKU3SKPz4w:1617967532812&ei=rDlwYPGGMf-d4-EPvMu4wAU&start="+str(i)+"&sa=N&ved=2ahUKEwjxjLTghvHvAhX_zjgGH")
        soup = BeautifulSoup(page.content, 'html.parser')
        page_body = soup.body
        text = str(page_body)
        matches = re.finditer(regex, text, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
                emails = ("{match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
                if emails not in data:
                        data.append(emails)
                        filteremail =  (emails)
                        print (filteremail)
                        f.write(filteremail)
                        f.write("\n")
                else:
                        print ("[-]"+emails+" exist in database....")

        i = i+1
        f.close()
        randomtime = (randint(60,120))
        print ("Sleep for "+str(randomtime)+" sec...")
        time.sleep(randomtime)
