url = 'https://www.hackerrank.com/domains/python'
required_split = (url. split("/")[2].split(".")[1:])
domain = ".".join(required_split)
print(domain)
