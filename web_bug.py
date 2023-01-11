import requests,bs4
def web_text(url,label):
    head = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    }
    response = requests.get(url,headers = head)
    response.encoding = "UTF-8"
    soup = bs4.BeautifulSoup(response.text, "lxml")
    data = soup.find_all(name = label)
    return data
def web_file(file_url,name):
    head = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    }
    file = requests.get(file_url, headers=head).content
    with open(name,"wb") as f:
        f.write(file)
