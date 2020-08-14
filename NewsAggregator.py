#!/usr/bin/env python3

# Parse RSS feeds of the given websites to return latest posts.
# The script will print out basic details of a post in a formatted
# output and limit the results to 10 entries.

import feedparser
from itertools import islice

Wired = feedparser.parse("https://www.wired.com/feed/rss")
TechCrunch = feedparser.parse("http://feeds.feedburner.com/TechCrunch/")
ComputerWorld = feedparser.parse("https://www.computerworld.com/news/index.rss")
TechRadar = feedparser.parse("https://www.techradar.com/rss")
Motherboard = feedparser.parse("https://www.vice.com/en_us/rss/section/tech")

limit = 10


def site(siteName, siteTitle):
    print(siteTitle + "\n")
    for post in islice((siteName.entries), limit):
        print(
            "------Date-------"
            + "\n"
            + post.published
            + "\n"
            + "------Title-------"
            + "\n"
            + post.title
            + "\n"
            + "------Link-------"
            + "\n"
            + post.link
            + "\n"
        )


site(Wired, "Wired")
site(TechCrunch, "TechCrunch")
site(ComputerWorld, "Computer World")
site(TechRadar, "TechRadar")
site(Motherboard, "Vice Motherboard")
