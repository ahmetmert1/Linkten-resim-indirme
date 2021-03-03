import urllib.request


with open('linkler.txt') as f:
    lines = f.readlines()
i=0
for link in lines:
    try:
        i = i + 1
        print("link = ", link)
        urllib.request.urlretrieve(link, "resimler/{0}.jpg".format(i))
    except:
        print("SIKINTILI LINK")