def name(url):
    name = url.partition("www.")[2]
    # print(name)
    if ".org" in name:
        name = name.partition(".org")[0]
    elif ".com" in name:
        name = name.partition(".com")[0]
    elif ".in" in name:
        name = name.partition(".in")[0]
    return name
    
    # print(name)
