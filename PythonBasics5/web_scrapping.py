import requests
from bs4 import BeautifulSoup

# response = requests.get('https://randomuser.me/api')    

# data = response.json()  

# source ./venv/bin/activate

# url = 'https://www.youtube.com/watch?v=ywZevdHW5bQ'

# my_soup = soup(requests.get(url).text, 'lxml')

# print(my_soup.select_one('meta[itemprop="interactionCount"][content]')['content'])  

def scrape_info(url):
    r = requests.get(url)
      
    s = BeautifulSoup(r.text, "html.parser") 

    title = s.find("meta", itemprop="name")['content']
      
    views = s.find("meta", itemprop="interactionCount")['content']
    # print(s.find_all('meta'))
    # print(views)

    data = {'title':title, 'views':views}
      
    return data
  
# main function
if __name__ == "__main__": 
      
    url ="https://www.youtube.com/watch?v=rfscVS0vtbw&t=8636s"
      
    data = scrape_info(url)
      
    print(data)