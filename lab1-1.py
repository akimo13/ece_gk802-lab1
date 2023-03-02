# HCI202, Design of Web Applications, 1st Lab Exercise
# 1103932, Karatsoulas Dimitrios

# importing libraries
import requests
import re
import time                                                                        # Importing time Python module to convert seconds to a human readable date

 # While loop enables program to keep asking for a valid URL until it gets one
while True:
    # Prompting for a valid URL
    url = input("Please enter a valid URL: ")
    if not url.startswith("http"):                                                  # Adding "https://" if it's not in front of the url
        url = "https://" + url

    valid_url_pattern = re.compile(
        r'^(?:http)s?://'                                                           # Checking for http:// or https://
        r'(?:www\.)?'                                                               # Checking for "www."
        r'\w+\.[a-zA-Z]{2,}(?:\.\w+)*'                                              # Checking for domain names and top-level domain
    )
    
    # Validation for URL, if not asking for a valid one 
    if not re.match(valid_url_pattern, url):
        print("Please try to input a valid URL.")
        continue

    # Making a URL request and getting a response object   
    response = requests.get(url)

    # Printing HTTP response headers
    print("\nHere are the HTTP response headers:\n")
    for header in response.headers:                                                 # Getting HTTP headers from response object
        if header.lower() != "set-cookie" and header.lower() != "server":           # excluding Cookies and Server, using lower() because HTTP headers are case-insensitive
            value = response.headers.get(header)
            print(f"{header}: {value}")

    # Printing information for software server
    software = response.headers.get('Server')                                       # Getting Server information from response object
    if software:
        print(f"\nThe server software used by {url} is: {software}")

    # Printing information for cookies
    print("\nHere are the cookies used by the webpage:\n")
    if response.cookies:                                                            # Checking if there are cookies   
        for cookie in response.cookies:                                             # Getting Cookies information from response object
            expiration_time = time.localtime(cookie.expires)                        # Converting seconds timestamp to a Python time tuple
            expiration_date = time.strftime("%Y-%m-%d %H:%M:%S", expiration_time)   # Converting Python time tuple to a readable string
            print(f"{cookie.name}, expiring at {expiration_date}")
    else:
        print(f"{url} has no cookies\n")        
