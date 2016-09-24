# Python Website Image Scraper

Downloads images from specified websites and saves them into "images" folder

## How To Use
* Run 'python3 downloadImages.py \<website\>' from a command line.
* Either enter a URL like twitter.com or http://twitter.com, both work.

## Bugs
* Some websites save images locally, so the src in img tag looks like this: /to/image/file, I need to add a fix for this. For now, this program just skips over them.
