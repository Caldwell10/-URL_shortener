#Creating a URL shortener

import random
import string

#dicionary
url_mapping= {}

def shorten_url(long_url):
   # Generate a short URL using random characters
   short_url =''.join(random.choices(string.ascii_letters + string.digits, k=6))

   #store mapping between long url and short url
   url_mapping[long_url]=short_url
   return short_url

def retrieve_url(long_url):
    # Return the original long URL based on the short URL
    return url_mapping.get(long_url)

if __name__ == '__main__':
    original_url = input('Enter the URL to shorten: ')
    short_url = shorten_url(original_url)
    print(F'Shortened URL: {short_url}')
    print(F'Original URL: {original_url}')






