import urllib.request
from bs4 import BeautifulSoup

def calculate_1():
    company=["aartidrugs","icicibank","ashokleyland","sunteckrealty","menonbearings","relaxofootwears","knrconstructions","aartiindustries","britanniaindustries","asianpaints","relianceindustries","bhartiairtel","bajajauto","axisbank"]
    all_sites=open("sites.txt",'r',encoding='ascii')

    rate=[]

    count =0
    for i in all_sites:
        sites=i
        count += 1


    all_sites=open("sites.txt",'r',encoding='ascii')
    for i in range(count):
        sites=all_sites.readline()
        page=urllib.request.urlopen(sites)
        soup=BeautifulSoup(page,features="html.parser")
        #print(soup.prettify())
        data=soup.find("div",{"id":"b_changetext"})
        string_data=str(data)
        start=string_data.find("<strong>")
        start +=8
        end=string_data.find("</strong>")
        string_data=string_data[start:end]
        #print(string_data)
        rate.append(string_data)

    #print(rate)
    rate=[float(i) for i in rate]

    predict=[]
    size=len(rate)

    for i in range(size):
        if(rate[i]>=0):
            predict.append("sell")
        else:
            predict.append("buy")

    print("company \t\t predicition")
    for i in range(0,len(company)):
        print(company[i]+"\t\t"+predict[i])
