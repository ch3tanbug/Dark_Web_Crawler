import time
import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup
from art import text2art

print(text2art("DARKWEB    CRAWLER ",font="doom").center(200))

# Set the number of links to crawl
num_links_to_crawl = 100

# Set the user agent to use for the request
user_agent = "HotJava/1.1.2 FCS"

# Set the headers for the request
headers = {'User-Agent': user_agent}

# Initialize the controller for the Tor network
with Controller.from_port(port=9051) as controller:
    # Set the controller password
    controller.authenticate(password='newpassword')

    # Set the starting URL
    url = ['http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/', 'http://k6m3fagp4w4wspmdt23fldnwrmknse74gmxosswvaxf3ciasficpenad.onion/'] #Websites url to crawl

    # Initialize the visited set and the link queue
    visited = set()
    queue = url.copy()

    # Get the list of keywords to search for
    keywords = input('Enter a list of keywords to search for, separated by commas: ').split(',')

    # Crawl the links
    while queue:
        # Get the next link in the queue
        link = queue.pop(0)

        # Skip the link if it has already been visited
        if link in visited:
            continue

        # Set the new IP address
        controller.signal(Signal.NEWNYM)

        # Send the request to the URL
        session = requests.session()
        session.proxies = {}
        session.proxies['http'] = 'socks5h://localhost:9050'
        session.proxies['https'] = 'socks5h://localhost:9050'
        # response = requests.get(link, headers=headers)
        response=session.get(link,headers=headers)

        # Parse the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links on the page
        links = soup.find_all('a')

        # Add any links that contain the keywords to the queue
        for a in links:
            href = a.get('href')
            if any(keyword in href for keyword in keywords):
                queue.append(href)
        
        # searching for keywords in main website as well
        page_text=soup.get_text()
        if any(keyword in page_text for keyword in keywords):
            print(f"Found keyword(s) in main content: {keywords}")
            print(soup.title.string, link)

        # Add the link to the visited set
        visited.add(link)

        # Check if the number of visited links has reached the limit
        if len(visited) >= num_links_to_crawl:
            break

# Print the visited links
print('Visited links:')
for link in visited:
    print(link)