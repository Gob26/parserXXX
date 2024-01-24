import requests
from bs4 import BeautifulSoup
from time import sleep
from  text import post


# Loop through blog pages (1-12)
for n in range(1, 2):
    sleep(21)  # Delay between each iteration

    # Form the URL of the blog page
    link = f'https://vegas-club.ru/blog/page/{n}'

    # Send a GET request to the specified URL and get the response as text
    response = requests.get(link).text

    # Create a BeautifulSoup object using the obtained HTML code and the lxml parser
    soup = BeautifulSoup(response, 'lxml')

    # Find <div> elements with class "blog-post clearfix"
    blocks = soup.find_all("div", class_="blog-post clearfix")

    # Create an empty list to store the URLs of blog articles
    blog_urls = []

    # Iterate through the found blocks and extract the URLs of the articles
    for block in blocks:
        blog_url = block.find("a").get("href")
        blog_urls.append(blog_url)



    # Iterate through the URLs of the blog articles
    for i, url in enumerate(blog_urls):
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')

        # Find <div> element with class "col-sm-8 col-md-8 blog-post"
        block = soup.find("div", class_="col-sm-8 col-md-8 blog-post")

        # Check if the block and URL are not None
        if block is not None:
            for p in block:
                # Extract text from each block, removing extra spaces and newlines
                block_text = p.get_text(strip=True)
                #print(block_text)
                post(block_text)
        else:
            print("Элемент не найден.")
        sleep(3)