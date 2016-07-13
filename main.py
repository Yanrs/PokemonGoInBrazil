# coding=utf-8
import urllib.request
import urllib.error
import sys
from html.parser import HTMLParser

eh = 'é'
entryToFind = "Pok" + eh + "mon GO"

class PokemonHTMLParser(HTMLParser):
    def __init__(self):
        self.foundGo = False
        self.html_parser_init_kwargs = { 'convert_charrefs' : True }
        HTMLParser.__init__(self, **self.html_parser_init_kwargs)
    def handle_starttag(self, tag, attrs):
        if (self.foundGo == False and tag == "meta"):
            for i in range(0,len(attrs)):
                if (attrs[i][0] == "content"):
                    encoded = attrs[i][1].encode(sys.stdout.encoding)
                    if (entryToFind in encoded.decode('utf-8')):
                        # we found it, leave the loop
                        self.foundGo = True
                        break
    def didFindGo(self):
        return self.foundGo

class PokemonGoError(Exception):
    pass

def checkForPokemonGo(region):
    try:
        content = urllib.request.urlopen("https://itunes.apple.com/" + region + "/app/pokemon-go/id1094591345?mt=8")
    except urllib.error.URLError as e:
        raise PokemonGoError("Error loading iTunes URL")
    resultStr = content.read().decode(sys.stdout.encoding) # read the results, which returns as a bytes object, then convert to string object using terminal's encoding
    htmlParser = PokemonHTMLParser()
    htmlParser.feed(resultStr)
    return htmlParser.didFindGo()

def isPokemonGoInCanada():
    try:
        if (checkForPokemonGo("ca")):
            print("Pokemon Go is now in Canada!")
        else:
            print("Pokemon Go is not in Canada yet")
    except PokemonGoError as e:
        print(e)

if __name__ == "__main__":
    isPokemonGoInCanada()
