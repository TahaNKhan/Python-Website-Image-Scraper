#! python3
# downloadImages.py - Downloads all images from a given website in the arguments.
import requests, os, bs4, sys
# get the URL from arguments
urls = sys.argv
# Check if the argument is a complete URL or not.
for url in urls:
    if not url[0:4] == 'http':
        # Add http:// if its not a complete URL
        url = 'http://'+url
    # Create a folder called images
    os.makedirs('images',exist_ok=True)

    website = requests.get(url)
    website.raise_for_status()
    soup = bs4.BeautifulSoup(website.text, "html.parser")
    # Find all image tags
    imgs = soup.findAll('img')

    for img in imgs:
        try:
            # Get image tags' src parameter
            imageurl = img.get('src')
            # If they aren't complete URLs, make them complete
            if not imageurl[0:4] == 'http':
                imageurl = 'http:'+imageurl
            # Make a get request for the image
            res = requests.get(imageurl)
            res.raise_for_status()
            # Create a file to download
            imageFile = open(os.path.join('images', os.path.basename(imageurl)), 'wb')
            # Start downloading item.
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            # close the file.
            imageFile.close()
        # If there's an exception, ignore it and continue.
        except Exception:
            continue
