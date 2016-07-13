import sys
import unittest
from unittest.mock import patch, Mock
import urllib.request
import urllib.error
import http.client
import main

real_urlopen = urllib.request.urlopen
real_checkForPokemonGo = main.checkForPokemonGo

class TestingPokemonGoMethods(unittest.TestCase):

    def test_pokemonHTMLParser(self):
        parser = main.PokemonHTMLParser()
        parser.feed("<html><meta content=\"Pokémon GO on the App Store\"></meta></html>")
        self.assertEqual(parser.didFindGo(), True)

    def test_pokemonHTMLParser_noContent(self):
        parser = main.PokemonHTMLParser()
        parser.feed("<html></html>")
        self.assertEqual(parser.didFindGo(), False)

    def test_pokemonHTMLParser_noPokemonGo(self):
        parser = main.PokemonHTMLParser()
        parser.feed("<html><meta content=\"Not Pokemon Go\"></meta></html>")
        self.assertEqual(parser.didFindGo(), False)

    @patch("urllib.request.urlopen")
    def test_checkForPokemonGo(self, urlopen_mock):
        urlopen_mock.return_value = Mock(spec=http.client.HTTPResponse)
        urlopen_mock.return_value.read.return_value = "<html><meta content=\"Pokémon GO on the App Store\"></meta></html>".encode(sys.stdout.encoding)
        self.assertEqual(main.checkForPokemonGo("us"), True) # those bastards!

    @patch("urllib.request.urlopen")
    def test_checkForPokemonGoErrorHandling(self, urlopen_mock):
        urlopen_mock.side_effect = urllib.error.URLError("Error retrieving webpage")
        with self.assertRaises(main.PokemonGoError):
            main.checkForPokemonGo("us")

    @patch("main.checkForPokemonGo")
    def test_PokemonGoCanadaCall(self, checkForPokemonGo_mock):
        main.isPokemonGoInCanada()
        main.checkForPokemonGo.assert_called_once_with("ca")

if __name__ == "__main__":
    unittest.main()
