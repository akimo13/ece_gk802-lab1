# importing requests library
import requests
#importing time Python module to convert seconds to a human readable date
import time

# Asking URL from user
url = input("Please enter a valid URL: ")

# Checking if URL starts with https or http, if not it adds https:// 
if not url.startswith("https://") or url.startswith("http://"):
    url = "https://" + url

# Making a URL request and getting a response object
response = requests.request('GET', url)

# Printing HTTP response headers
print("\nHere are the HTTP response headers:\n")
for header in response.headers:                                         # Getting HTTP headers from response object
    if header.lower() != "set-cookie" and header.lower() != "server":   # excluding Cookies and Server, using lower() because HTTP headers are case-insensitive
        value = response.headers.get(header)
        print(f"{header}: {value}")

# Printing information for software server
software = response.headers.get('Server')
if software:
    print(f"\nThe software used by the server is: {software}")

# Printing information for cookies
print("\nHere are the cookies used by the webpage:\n")
for cookie in response.cookies:
        expiration_time = time.localtime(cookie.expires)                        # Converting seconds timestamp to a Python time tuple
        expiration_date = time.strftime("%Y-%m-%d %H:%M:%S", expiration_time)   # Converting Python time tuple to a readable string
        print(f"{cookie.name}, expiring at {expiration_date}")