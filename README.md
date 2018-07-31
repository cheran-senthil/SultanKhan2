# SultanKhan2

[SultanKhan2](http://www.chessgames.com/perl/chessgame?gid=1135510) is a Lichess integration of my Chess Engine [Chaturanga](https://github.com/Cheran-Senthil/Chaturanga)

## Sample Game

https://lichess.org/uRuE8p1k5axh

![SultanKhan2 vs Stockfish level 4](https://i.imgur.com/pnl1uyp.png)

## Usage

- Create a lichess bot account, by following the steps [here](https://lichess.org/api#tag/Chess-Bot).
- Create an API access token with "Play bot moves" permission.
- In `main.py`:
    - change `token` to your Lichess access API token
    - change `bot_id` to your bot's Lichess id
- Run `main.py` with `python main.py`
