"""1 Link - 10 qrcode"""
# import qrcode
# x = qrcode.make("https://www.w3schools.com/python/trypython.asp")
# a=1
# for a in range (1,10):
#     x.save(f'{a}.png')
"""100 link - 100 qr code"""
import qrcode
import re

Links = [
    "https://example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.reddit.com",
    "https://www.medium.com",
    "https://www.nytimes.com",
    "https://www.bbc.com",
    "https://www.cnn.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.amazon.com",
    "https://www.netflix.com",
    "https://www.spotify.com",
    "https://www.linkedin.com",
    "https://www.instagram.com",
    "https://www.twitter.com",
    "https://www.facebook.com",
    "https://www.tesla.com",
    "https://www.nasa.gov",
    "https://www.adobe.com",
    "https://www.quora.com",
    "https://www.wordpress.com",
    "https://www.blogger.com",
    "https://www.dropbox.com",
    "https://www.tumblr.com",
    "https://www.pinterest.com",
    "https://www.paypal.com",
    "https://www.shopify.com",
    "https://www.ebay.com",
    "https://www.walmart.com",
    "https://www.twitch.tv",
    "https://www.soundcloud.com",
    "https://www.khanacademy.org",
    "https://www.coursera.org",
    "https://www.udemy.com",
    "https://www.edx.org",
    "https://www.codecademy.com",
    "https://www.freecodecamp.org",
    "https://www.hackerrank.com",
    "https://www.leetcode.com",
    "https://www.producthunt.com",
    "https://www.ycombinator.com",
    "https://www.venturebeat.com",
    "https://www.forbes.com",
    "https://www.businessinsider.com",
    "https://www.bloomberg.com",
    "https://www.wsj.com",
    "https://www.theverge.com",
    "https://www.engadget.com",
    "https://www.arstechnica.com",
    "https://www.techcrunch.com",
    "https://www.wired.com",
    "https://www.cnet.com",
    "https://www.android.com",
    "https://www.xda-developers.com",
    "https://www.tomshardware.com",
    "https://www.linux.org",
    "https://www.debian.org",
    "https://www.ubuntu.com",
    "https://www.redhat.com",
    "https://www.oracle.com",
    "https://www.ibm.com",
    "https://www.intel.com",
    "https://www.nvidia.com",
    "https://www.amd.com",
    "https://www.raspberrypi.org",
    "https://www.arduino.cc",
    "https://www.autodesk.com",
    "https://www.canva.com",
    "https://www.behance.net",
    "https://www.dribbble.com",
    "https://www.figma.com",
    "https://www.invisionapp.com",
    "https://www.getbootstrap.com",
    "https://www.tailwindcss.com",
    "https://www.fontawesome.com",
    "https://www.jquery.com",
    "https://www.typescriptlang.org",
    "https://www.nodejs.org",
    "https://www.reactjs.org",
    "https://www.vuejs.org",
    "https://www.angular.io",
    "https://www.djangoproject.com",
    "https://www.flask.palletsprojects.com",
    "https://www.fastapi.tiangolo.com",
    "https://www.tensorflow.org",
    "https://www.pytorch.org",
    "https://www.scikit-learn.org",
    "https://www.matplotlib.org",
    "https://www.pandas.pydata.org",
    "https://www.postman.com",
    "https://www.mongodb.com",
    "https://www.mysql.com",
    "https://www.postgresql.org",
    "https://www.sqlite.org",
    "https://www.cloudflare.com",
    "https://www.openai.com"
]

# Remove duplicates while preserving order
Links = list(dict.fromkeys(Links))

# Generate QR codes
for i, l in enumerate(Links, start=1):
    x = qrcode.make(l)
    
    # Sanitize filename for safety
    safe_filename = re.sub(r'\W+', '_', l)  # Replace non-alphanumeric characters with "_"
    
    x.save(f'qrcode_{i}_{safe_filename}.png')

print("QR codes generated successfully!")
