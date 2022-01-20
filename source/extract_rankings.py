import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd
url1 = 'https://www.universityreview.org/top-100-colleges/'
url2 = 'https://www.topuniversities.com/university-rankings/world-university-rankings/2022'
# logging.basicConfig(
#     format='%(asctime)s %(levelname)s:%(message)s',
#     level=logging.INFO)
def main():
    r = requests.get(url1)
    with open("../unirev_best_unis.html", "wb") as infile:
        infile.write(r.content)
    r2 = requests.get(url2)
    with open("../qs_best_unis.html", "wb") as infile2:
        infile2.write(r2.content)
    # OBSOLETE CODE TO EXTRACT TABLES
    # with open("../unirev_best_unis.html", "rb") as outfile: #Retrieve downloaded webpage
    #     content = outfile.read()

    # soup = BeautifulSoup(content, 'lxml')
    # print(soup)

    # #Extract columns
    # school_names =soup.find_all("td", {"class": "column-2"})
    # pba_rank = soup.find_all("td", {"class": "column-1"})
    # times_rank = soup.find_all("td", {"class": "column-3"})
    # usnews_rank = soup.find_all("td", {"class": "column-4"})
    # jt_rank = soup.find_all("td", {"class": "column-5"})
    # num_students = soup.find_all("td", {"class": "column-7"})
    # price  = soup.find_all("td", {"class": "column-8"})
    # school_names_str = [td.string for td in school_names]
    # pba_rank_int = [int(td.string) for td in pba_rank]
    # times_rank_int = [int(td.string) for td in times_rank]
    # usnews_int = [int(td.string) for td in usnews_rank]
    # jt_rank_int = [int(td.string) for td in jt_rank]
    # num_students_int = [int(td.string) for td in num_students]
    # price_int = [int(((td.string).replace(',',''))[1:]) for td in price]
    
    # d = {"University": school_names_str, "pba_rank": pba_rank_int, "times_rank": times_rank_int, "usnews_rank": usnews_int, "jt_rank": jt_rank_int, "num_students": num_students_int, "price": price_int}
    # df = pd.DataFrame(d)
    # df.to_csv("../unirev_data.csv")
    # tags = soup.find_all("div", attrs ={"class": "_qs-ranking-data-row"})
    # print(tags)
     
if __name__ == "__main__":
    main()
