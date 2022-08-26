import requests
from bs4 import BeautifulSoup

# using hackers news website to parse data (they are legal)
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

#finding all the html tag <a> for heading reference
web_tag = soup.find_all(name = "a", class_= "titlelink")
web_text=[]
web_link=[]
for article_tag in web_tag:
  web_text.append(article_tag.getText())
  web_link.append(article_tag.get("href"))

#finging all the html tag <span> to get votes
web_votes =[int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_="score")]

#highest votes are considered and generated appropriate data though indexing from generated array
largest_votes = max(web_votes)
largest_index = web_votes.index(largest_votes)
sms_text = web_text[largest_index]
sms_link = web_link[largest_index]


