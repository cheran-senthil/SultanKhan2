import chaturanga
import berserk

Chessboard = chaturanga.Chessboard()

session = berserk.TokenSession('token')
lichess = berserk.Client(session)

for challenge in lichess.bots.stream_incoming_events():
    game_id = challenge['challenge']['id']
    lichess.bots.accept_challenge(game_id)
    flag = False

    for game_state in lichess.bots.stream_game_state(game_id):
        if not flag:
            flag = True
            is_black = game_state['black']['id'] == 'sultankhan2'
            bot_color = {True: 'b', False: 'w'}[is_black]

            if bot_color == 'w':
                bot_move = chaturanga.bot(Chessboard)[0]
                Chessboard.move(bot_move)
                lichess.bots.make_move(game_id, bot_move)

            continue

        last_move = game_state['moves'].split(' ')[-1]
        Chessboard.move(last_move)

        if bot_color == Chessboard.active_color:
            bot_move = chaturanga.bot(Chessboard)[0]
            Chessboard.move(bot_move)
            lichess.bots.make_move(game_id, bot_move)

    break
