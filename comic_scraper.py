import time

import requests
from bs4 import BeautifulSoup as BS

import date_f

GOCOMICS_BASE_URL = "https://www.gocomics.com"
GCOMICSKINGDOM_BASE_URL = "https://www.comicskingdom.com"


# gocomics comic names

gocomic_name = (
    "pluggers",
    "calvinandhobbes",
    "gasolinealley",
    "9chickweedlane",
    "nonsequitur",
    "heathcliff",
    "dilbert-classics",
    "luann",
    "garfield",
    "forbetterorforworse",
    "redandrover",
    "heartofthecity",
    "peanuts",
    "baldo",
    "tankmcnamara",
    "shoe",
    "broomhilda",
    "the-born-loser",
    "drabble",
    "bc",
    # 'foxtrotclassics',
    # 'foxtrot',     # errors out, maybe in htlm pharse???
    "marmaduke",
    "roseisrose",
    "wizardofid",
    "andycapp",
    "muttandjeff"
)

# comicskingdom comic names

ckcomic_name = (
    "crock",
    # 'prince-valiant',
    "barney-google-and-snuffy-smith",
    "mother-goose-grimm",
    "hagar-the-horrible",
    "blondie",
    "beetle-bailey-1",
    "curtis",
    "phantom",
    "family-circus",
    "zits",
    "baby-blues",
    "hi-and-lois",
    "sally-forth",
    "Crankshaft",
    "lockhorns",
    "mallard-fillmore",
    "marvin",
    "funky-winkerbean"
)


def scrape_gocomics():
    comic_days_from_today = 0
    comic_date_str = date_f.comic_date(True, comic_days_from_today)

    comic_imgs = []
    for i in range(len(gocomic_name)):
        gcn = gocomic_name[i]
        url = GOCOMICS_BASE_URL + "/" + gcn
        comic_url = url + "/" + comic_date_str
        print()
        print(comic_url)
        try:
            comic_req_url = requests.get(comic_url)
            comic_req_url.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            # continue

        # get web page text in soup

        soup = BS(comic_req_url.text, "lxml")

        # image_url contains the comic strip description,
        #  date and the url src to the comic strip image

        image_url = soup.find("picture", class_="item-comic-image").img
        alt = image_url["alt"] + "| Go Comics"
        src = image_url["src"]
        # comic_imgs.append({'url': url, 'alt': alt, 'src': src})
        thiscomic = "GoComics"
        comic_imgs.append({"url": url, "alt": alt, "src": src, "frmcomic": thiscomic})

        # Allow time between url requests
        # time.sleep(comic_req_url.elapsed.total_seconds())

    return comic_imgs


def scrape_comicskingdom():
    comic_days_from_today = 0
    comic_date_str = date_f.comic_date(True, comic_days_from_today)
    comic_date_str = comic_date_str.replace("/", "-")

    comic_imgs = []

    for i in range(len(ckcomic_name)):
        gcn = ckcomic_name[i]
        url = GCOMICSKINGDOM_BASE_URL + "/" + gcn
        comic_url = url + "/" + comic_date_str
        print()
        print(comic_url)

        try:
            comic_req_url = requests.get(comic_url)
            comic_req_url.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)

        # get web page text in soup
        soup = BS(comic_req_url.text, "lxml")

        # Find and get the print image url in byprtsrc
        byprtsrc = soup.find("img", class_="buy-print-image")["src"]

        # Find and get the strip title in comic_title
        # comic_title_s = soup.find('title').text

        # Comic strip description and date
        strip_name = soup.find("slider-prints")["feature-name"]
        strip_date = soup.find("slider-prints")["date"]
        strip_description = (
            strip_name + "Comic Strip for " + strip_date + " | ComicsKingdom"
        )

        alt = strip_description
        src = byprtsrc
        thiscomic = "Kingdom"
        comic_imgs.append({"url": url, "alt": alt, "src": src, "frmcomic": thiscomic})
        # print(comic_imgs)

        # Allow time between url requests
        # time.sleep(comic_req_url.elapsed.total_seconds())

    return comic_imgs


if __name__ == "__main__":
    # comics = scrape_gocomics()
    comics = scrape_comicskingdom()
    # comics = scrape_gocomics() + scrape_comicskingdom()
    print(comics)
