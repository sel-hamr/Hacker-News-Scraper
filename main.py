import requests
from bs4 import BeautifulSoup
import pprint

def scripting_data_hn(url):
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    votes = soup.select(".subtext")
    links = soup.select(".titleline > a")
    return votes, links

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda n: n["votes"], reverse=True)

def filter_data_hacker_new(votes, links, minimum_point):
    hn_list = []

    for index, item in enumerate(links):
        title = item.getText()
        link = item.get("href", None)
        vote = votes[index].select(".score")
        if len(vote):
            point = int(vote[0].getText().replace(" points", ""))
            if point >= minimum_point:
                hn_list.append({"title": title, "link": link, "votes": point})
    return sort_stories_by_votes(hn_list)

def main():
    list_votes = []
    list_links = []
    count = 1
    number_of_item = int(input("Enter the number of articles you want to see: "))
    point = int(input("Enter the minimum number of votes you want to see: "))

    while True:
        votes, links = scripting_data_hn(f"https://news.ycombinator.com/?p={count}")
        list_votes.extend(votes)
        list_links.extend(links)

        count += 1
        if len(list_votes) > number_of_item:
            break
    pprint.pprint(filter_data_hacker_new(list_votes, list_links, point))

if __name__ == "__main__":
    main()
