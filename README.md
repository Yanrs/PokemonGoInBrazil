# Pokémon Go in Canada

[![Build Status](https://travis-ci.org/Coteh/PokemonGoInCanada.svg?branch=master)](https://travis-ci.org/Coteh/PokemonGoInCanada)

Out of my frustration over Pokemon Go not released in Canada yet, I whipped up this small terminal app in Python that will tell you if it's out in Canada yet or not.

It does this by making a HTML request to the iTunes page for the game and checking the content attributes on meta tags.
If there's a content attribute that says "Pokémon Go on the App Store", then that means there's a page on the region's iTunes store for the game.
