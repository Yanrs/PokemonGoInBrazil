import urllib.request
import sys
from html.parser import HTMLParser

eh = 'é'
entryToFind = "Pok" + eh + "mon GO on the App Store"

class PokemonHTMLParser(HTMLParser):
    def __init__(self):
        self.foundGo = False
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if (self.foundGo == False and tag == "meta"):
            for i in range(0,len(attrs)):
                if (attrs[i][0] == "content"):
                    encoded = attrs[i][1].encode(sys.stdout.encoding)
                    if (encoded.decode('utf-8') == entryToFind):
                        # we found it, leave the loop
                        self.foundGo = True
                        break
    def didFindGo(self):
        return self.foundGo


def checkForPokemonGo(region):
    content = urllib.request.urlopen("https://itunes.apple.com/" + region + "/app/pokemon-go/id1094591345?mt=8")
    resultStr = content.read().decode(sys.stdout.encoding) # read the results, which returns as a bytes object, then convert to string object using terminal's encoding
    htmlParser = PokemonHTMLParser()
    htmlParser.feed(resultStr)
    return htmlParser.didFindGo()

def isPokemonGoInCanada():
    if (checkForPokemonGo("ca")):
        print("Pokemon Go is now in Canada!")
    else:
        print("Pokemon Go is not in Canada yet")

isPokemonGoInCanada()
