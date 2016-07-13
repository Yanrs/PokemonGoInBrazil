# Pokémon Go in Brazil

[![Build Status](https://travis-ci.org/Yanrs/PokemonGoInBrazil.svg?branch=master)](https://travis-ci.org/Yanrs/PokemonGoInBrazil)

Out of my frustration over Pokemon Go not released in Brazil yet, I whipped up this small terminal app in Python 3 that will tell you if it's out in Brazil yet or not.

It does this by making a HTML request to the region's iTunes page for the game (an app has the same ID for all regions) and checking the content attributes on meta tags.
If there's a content attribute that contains the substring "Pokémon GO", then that means there's a page on the region's iTunes store for the game.

# Pokémon Go no Brasil

[![Build Status](https://travis-ci.org/Yanrs/PokemonGoInBrazil.svg?branch=master)](https://travis-ci.org/Yanrs/PokemonGoInBrazil)

Com a minha frustração sobre o Pokemon Go ainda não ter lançado no Brasil, eu criei este pequeno aplicativo de terminal em Python 3 que lhe dirá se está disponivel no Brasil ou não .

Ele faz isso através de uma solicitação HTML para a página do iTunes da região do jogo ( o aplicativo tem o mesmo ID para todas as regiões ) e verificar os atributos de conteúdo nas suas meta tags.
Se há um atributo de conteúdo que contém a substring "Pokémon GO" , então isso significa que há uma página na loja iTunes da região para o jogo.
