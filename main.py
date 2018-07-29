import chaturanga
import berserk

token = 'token'
bot_id = 'sultankhan2'

session = berserk.TokenSession(token)
lichess = berserk.Client(session)

for event in lichess.bots.stream_incoming_events():
    if event['type'] == 'challenge':
        challenge = event['challenge']
        if (challenge['variant']['key'] == 'standard') and (challenge['rated'] == False):
            Chessboard = chaturanga.Chessboard()
            game_id = challenge['id']
            lichess.bots.accept_challenge(game_id)

            for game_state in lichess.bots.stream_game_state(game_id):
                if game_state['type'] == 'gameFull':
                    is_white = game_state['black']['id'] != bot_id

                    if is_white:
                        bot_move = chaturanga.bot(Chessboard)[0]
                        Chessboard.move(bot_move)
                        lichess.bots.make_move(game_id, bot_move)

                if game_state['type'] == 'gameState':
                    moves = game_state['moves'].split(' ')
                    if len(moves) % 2 != is_white:
                        Chessboard.move(moves[-1])
                        bot_move = chaturanga.bot(Chessboard)[0]
                        Chessboard.move(bot_move)
                        lichess.bots.make_move(game_id, bot_move)
