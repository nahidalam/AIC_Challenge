


# url shortner

# Enter your code here. Read input from STDIN. Print output to STDOUT

import random
import string

contents = []
domain = 'http://sprng.brd/'
# contains the short code for each url to make sure we are not creating different short code for same url
hashMap = {}

while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for url in contents:
    if url in hashMap:
        shortcode = hashMap[url]
        print(domain+shortcode)
    else:
        shortcode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        hashMap[url] = shortcode
        print(domain+shortcode)
