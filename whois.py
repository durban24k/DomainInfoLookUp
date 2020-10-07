import whois

def iplookup():
     result=whois.whois('google.com')
     print(result)

if __name__ == '__main__':
     iplookup()