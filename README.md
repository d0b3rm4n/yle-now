# YLE-Now

`yle-now.py` is a script which interacts with the YLE API to fetch the current
playing song.

## Usage
        usage: yle-now.py [-h] -a YLE-APP-ID -k YLE-APP-KEY [-s YLE-RADIO-STATION]
                          [-V]

        optional arguments:
          -h, --help            show this help message and exit
          -a YLE-APP-ID, --appid YLE-APP-ID
                                Yle API application ID
          -k YLE-APP-KEY, --apikey YLE-APP-KEY
                                Yle API key
          -s YLE-RADIO-STATION, --station YLE-RADIO-STATION
                                Yle Radio Station, choices: yle-radio-1, yle-puhe,
                                yle-mondo, ylex, yle-x3m, yle-radio-vega, radio-vega-
                                huvudstadsregionen, radio-vega-vastnyland, radio-vega-
                                aboland, radio-vega-osterbotten, radio-vega-ostnyland,
                                yle-radio-suomi, yle-radio-suomi-lappeenranta, yle-
                                radio-suomi-mikkeli, yle-radio-suomi-kajaani, yle-
                                radio-suomi-kotka, yle-radio-suomi-lahti, yle-radio-
                                suomi-rovaniemi, yle-radio-suomi-oulu, yle-radio-
                                suomi-pohjanmaa, yle-radio-suomi-joensuu, yle-radio-
                                suomi-hameenlinna, yle-radio-suomi-kokkola, yle-radio-
                                suomi-jyvaskyla, yle-radio-suomi-kemi, yle-radio-
                                suomi-kuopio, yle-radio-suomi-pori, yle-radio-suomi-
                                tampere, yle-radio-suomi-turku, yle-radio-suomi-
                                helsinki, yle-sami-radio, elavan-arkiston-nettiradio
          -V, --verbose         increase output verbosity (use up to 2 times)

## API Key
An API key from Yle is needed, you can get one for free from their [developer
area](https://developer.yle.fi)
