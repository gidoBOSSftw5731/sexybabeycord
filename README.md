# Sexybabeycord (A Sexybabeycord Production)

[![CI/CD](https://github.com/vaughnw128/sexybabeycord/actions/workflows/main.yml/badge.svg)](https://github.com/vaughnw128/sexybabeycord/actions/workflows/main.yml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

This is the newest iteration/amalgam of the many discord bots I've made over the years.
I plan on adding new bots and re-implementing old bots in this new and improved system!
The bot itself is a collection of multiple pieces, each with vastly
different functionalities. There certainly will be more to come as our
server never has enough bots (lie).

What the hell is Sexybabeycord?: Sexybabeycord is the current iteration of the Discord server that I share
with my close friends (we accidentally nuked the last one with homemade spambots). It's more of a
chaotic groupchat than a high-functioning Discord 'community,' as we all have Administrator
permissions, and we don't particularly care for rules. I love making bots for our server, and my
friends seem to as well.

## Usage

Sexybabeycord uses poetry to manage dependencies, and as such, should be easy to manage. In order to run on your own system, the Python virtual environment needs to be set up.


Clone the repository:
```
git clone https://github.com/vaughnw128/sexybabeycord
cd sexybabeycord/
```


Install and initialize the python environment:
```
brew install pyenv
pyenv install 3.10.6
pyenv local 3.10.6
```


Installing dependencies with poetry:
```
poetry self add poetry-dotenv-plugin
poetry install
```

Additional dependencies are required, such as ffmpeg, and libmagickwand-dev.

Then, it's necessary to create a `.env` file to match the one in `bot/resources/templates/env_template` in the root directory of the project. The tenor token is required to grab certain gifs posted from tenor, and can be obtained for free by following the [Google Cloud Tenor Quickstart Guide](https://developers.google.com/tenor/guides/quickstart)
```
DISCORD_TOKEN=1234
TENOR_TOKEN=1234
```


The bot can then be tested by running pytest
```
poetry run -m pytest
```


Finally, once tests pass, the bot can be run
```
poetry run -m bot
```

## Components

The current components (cogs) of the bot are as follows:
- Astropix: Scrapes and sends the NASA picture of the day every day at noon.
- Distort: Grabs images from messages then uses liquid rescaling to distort and resend them.
- fixlink: Takes any link to twitter, instagram, or tiktok, and fixes it with either the 'vx' or 'dd' prefix for proper embed formatting.
- fate: Uses twscrape to grab @JamesCageWhite's tweets and send them in our #fate channel. Love that guy.
- gabonganized: Gabonganizes all face pics sent. This adds a gabonga where someone's face is supposed to be.
- caption: Adds captions to images when you reply with the 'caption' keyword.
- Mood Matrix: Allows users to select a coordinate from a drop down and then puts their profile photo on a mood matrix.
- Ytdl: Downloads youtube videos and clips with a command or menu button.
- Peanut gallery: Whenever someone sends a youtube link, a random comment from the video is automatically sent to chat



<sub><sup>Made with love and care by Vaughn Woerpel</sub></sup>
