import os
import webbrowser

from jinja2 import Environment, FileSystemLoader

import comic_scraper

# file_loader: webbrowser.open_new_tabfile_loader = FileSystemLoader("templates")
file_loader = FileSystemLoader("templates")

env = Environment(loader=file_loader)

template_filename = "w3css.html"
template = env.get_template(template_filename)

if __name__ == "__main__":
    # comics = scrape_comicskingdom() + scrape_gocomics()
    # comics = comic_scraper.scrape_gocomics() + comic_scraper.scrape_comicskingdom()
    comics = comic_scraper.scrape_comicskingdom() + comic_scraper.scrape_gocomics()
    # comics = comic_scraper.scrape_gocomics()
    # comics = comic_scraper.scrape_comicskingdom()
    comic_strip_html = template.render(comics=comics)
    path = os.path.abspath("temp.html")
    url = "file://" + path

    with open(path, "w") as f:
        f.write(comic_strip_html)
    webbrowser.open(url, new=2)
