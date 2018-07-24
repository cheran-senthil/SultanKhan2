import chaturanga
import berserk

token = 'token'
bot_id = 'sultankhan2'

session = berserk.TokenSession(token)
lichess = berserk.Client(session)

for event in lichess.bots.stream_incoming_events():
    if event['type'] == 'challenge':
        Chessboard = chaturanga.Chessboard()
        game_id = event['challenge']['id']
        lichess.bots.accept_challenge(game_id)

        for game_state in lichess.bots.stream_game_state(game_id):
            if game_state['type'] == 'gameFull':
                is_black = game_state['black']['id'] == bot_id
                bot_color = {True: 'b', False: 'w'}[is_black]

                if bot_color == 'w':
                    bot_move = chaturanga.bot(Chessboard)[0]
                    Chessboard.move(bot_move)
                    lichess.bots.make_move(game_id, bot_move)

            if game_state['type'] == 'gameState':
                last_move = game_state['moves'].split(' ')[-1]
                Chessboard.move(last_move)

                if bot_color == Chessboard.active_color:
                    bot_move = chaturanga.bot(Chessboard)[0]
                    Chessboard.move(bot_move)
                    lichess.bots.make_move(game_id, bot_move)
