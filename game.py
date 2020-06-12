import discord
import random
import secrets

from discord.ext import commands

print('start')
bot = commands.Bot(command_prefix='x_x:')
client = discord.Client()

BOT_KEY = ''  # put your bot secret here or use other methods

game_started = False
word = ''
category = ''
guessed = set([' ', '(', ')', "'"])
guessed_answers = set()
wrong_guesses = 0

CATEGORIES = ['Fruits', 'Minecraft_Blocks', 'Minecraft_Items']
ALIASES = {'FRUITS': 'Fruits',
           'FRUIT': 'Fruits',
           'MINECRAFT_BLOCKS': 'Minecraft_Blocks',
           'MINECRAFT_BLOCK': 'Minecraft_Blocks',
           'M_BLOCKS': 'Minecraft_Blocks',
           'M_BLOCK': 'Minecraft_Blocks',
           'MINECRAFT_ITEMS': 'Minecraft_Items',
           'MINECRAFT_ITEM': 'Minecraft_Items',
           'M_ITEMS': 'Minecraft_Items',
           'M_ITEM': 'Minecraft_Items', }
ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
             'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def random_word():
    global word, category
    with open('categories/' + category + '.txt', 'r') as cat_file:
        items = [i.strip() for i in cat_file.readlines()]
        random.seed(secrets.randbelow(18446744073709551616))
        word = random.choice(items)
        word = word.upper()


@bot.command(name='play', help='Starts a hangman game, if not already started')
async def play(play_context, cat=''):
    print('play cmd issued')
    global game_started, word, category, wrong_guesses, guessed, CATEGORIES, ALIASES
    if not game_started:
        if cat in CATEGORIES:
            game_started = True
            category = cat
            print(f'game starting, category {cat} chosen')
            await play_context.send('Starting game! Welcome to HANGMAN!\n' +
                                    'The game ends when the man is hanged or ' +
                                    'when you guessed all alphabets correctly.\n' +
                                    'You can also send "!quit" or "!stop" to quit the game.\n' +
                                    'To guess a letter, send "!guess ", followed by the alphabet you want to guess.' +
                                    '\nFor example, to guess the alphabet Y, send "!guess Y".\n' +
                                    'Those underlined are the ones you have guessed and ' +
                                    'those with bold are correct guesses.')
            random_word()
            print(f'word to guess is {word}')
            await play_context.send(f'**Category:  {category}**',
                                    file=discord.File('img/' + str(wrong_guesses) + '.png'))
            await play_context.send('**' +
                                    '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                    '**\n\n')
        elif cat.upper() in ALIASES:
            game_started = True
            category = ALIASES[cat.upper()]
            print(f'game starting, category {category} chosen')
            await play_context.send('Starting game! Welcome to HANGMAN!\n' +
                                    'The game ends when the man is hanged or ' +
                                    'when you guessed all alphabets correctly.\n' +
                                    'You can also send "!quit" or "!stop" to quit the game.\n' +
                                    'To guess a letter, send "!guess ", followed by the alphabet you want to guess.' +
                                    '\nFor example, to guess the alphabet Y, send "!guess Y".\n' +
                                    'Those underlined are the ones you have guessed and ' +
                                    'those with bold are correct guesses.')
            random_word()
            print(f'word to guess is {word}')
            await play_context.send(f'**Category:  {category}**',
                                    file=discord.File('img/' + str(wrong_guesses) + '.png'))
            await play_context.send('**' +
                                    '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                    '**\n\n')
        else:
            print('no category specified or category not available')
            await play_context.send('Welcome to HANGMAN!\n' +
                                    'To start a game, send "!start {category}" or "!play {category}.\n\n' +
                                    'Categories available:\n' + '\n'.join(CATEGORIES) + '\n' +
                                    'For example, to start a game with category fruits, send "!play Fruits".')
    else:
        print('game failed to start: game in progress.')
        await play_context.send('Game in progress already! Use "!quit" or "!stop" to quit the game.')


@bot.command(name='start', help='Starts a hangman game, if not already started')
async def start(start_context, cat=''):
    print('start cmd issued')
    global game_started, word, category, wrong_guesses, guessed, CATEGORIES, ALIASES
    if not game_started:
        if cat in CATEGORIES:
            game_started = True
            category = cat
            print(f'game starting, category {category} chosen')
            await start_context.send('Starting game! Welcome to HANGMAN!\n' +
                                     'The game ends when the man is hanged or ' +
                                     'when you guessed all alphabets correctly.\n' +
                                     'You can also send "!quit" or "!stop" to quit the game.\n' +
                                     'To guess a letter, send "!guess ", followed by the alphabet you want to guess.' +
                                     '\nFor example, to guess the alphabet Y, send "!guess Y".\n' +
                                     'Those underlined are the ones you have guessed and ' +
                                     'those with bold are correct guesses.')
            random_word()
            print(f'word to guess is {word}')
            await start_context.send(f'**Category:  {category}**',
                                     file=discord.File('img/' + str(wrong_guesses) + '.png'))
            await start_context.send('**' +
                                     '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                     '**\n\n')
        elif cat.upper() in ALIASES:
            game_started = True
            category = ALIASES[cat.upper()]
            print(f'game starting, category {category} chosen')
            await start_context.send('Starting game! Welcome to HANGMAN!\n' +
                                     'The game ends when the man is hanged or ' +
                                     'when you guessed all alphabets correctly.\n' +
                                     'You can also send "!quit" or "!stop" to quit the game.\n' +
                                     'To guess a letter, send "!guess ", followed by the alphabet you want to guess.' +
                                     '\nFor example, to guess the alphabet Y, send "!guess Y".\n' +
                                     'Those underlined are the ones you have guessed and ' +
                                     'those with bold are correct guesses. \n' +
                                     'You can also guess a whole word with "!guess". \n' +
                                     'For example, to guess "blue wire", send "!guess blue wire". \n' +
                                     'You can check what answers you have guessed using "!stats" or "status".')
            random_word()
            print(f'word to guess is {word}')
            await start_context.send(f'**Category:  {category}**',
                                     file=discord.File('img/' + str(wrong_guesses) + '.png'))
            await start_context.send('**' +
                                     '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                     '**\n\n')
        else:
            print('no category specified or category not available')
            await start_context.send('Welcome to HANGMAN!\n' +
                                     'To start a game, send "!start {category}" or "!play {category}.\n\n' +
                                     'Categories available:\n' + '\n'.join(CATEGORIES) + '\n' +
                                     'For example, to start a game with category fruits, send "!play Fruits".')
    else:
        print('game failed to start: game in progress.')
        await start_context.send('Game in progress already! Use "!quit" or "!stop" to quit the game.')


@bot.command(name='guess', help='Send a guess of a letter, or the whole answer.')
async def guess(context, *submission):
    print('guess cmd issued')
    global game_started, guessed, category, word, wrong_guesses, guessed_answers, ALPHABETS
    if game_started:
        checking = -1  # 2: check letter, 3: check words, else: don't check at all
        to_send = ''  # message to send after displaying hangman
        if len(submission) == 0:
            to_send = 'Guess cannot be blank!'
            print('empty guess issued')
        else:
            if len(submission) == 1:
                compare = submission[0]
                if len(compare) == 1:
                    checking = 2
                elif len(word.split()) == 1:  # if word is 1 word long, same as the guess
                    if len(word) != len(compare):  # if number of alphabets in the guess is not equals to answer
                        to_send = 'The number of characters in your guess does not match the answer.'
                        checking = -1
                    else:
                        checking = 3
                else:
                    to_send = 'The number of words you guessed does not match the answer. Try again.'
                    print(f'Number of words do not match. Guessed {compare}, which is 1 word long.')
            elif len(submission) != len(word.split()):
                to_send = 'The number of words you guessed does not match the answer. Try again.'
                print(f'No. of words not match. Guessed {" ".join(submission)}, which is {len(submission)} word long.')
            else:
                if len(word) != len(' '.join(submission)):
                    to_send = 'The number of characters in your guess does not match the answer. Try again.'
                    checking = -1
                else:
                    checking = 3

            if checking == 2:
                check = submission[0]
                if check.upper() not in ALPHABETS:
                    to_send = 'Guess should be an alphabet'
                    print('non-alphabet guess issued')
                else:
                    if check.upper() not in guessed:
                        guessed.add(check.upper())
                        if check.upper() in word:
                            to_send = f'Guessed {check.upper()} **correctly**!\n'
                        else:
                            wrong_guesses += 1
                            to_send = f'Guessed {check.upper()} **wrongly**!\n'
                    else:
                        to_send = f'Guessed {check.upper()} **previously**!\n'
            elif checking == 3:
                check = ' '.join(submission)
                if check.upper() == word:
                    to_send = f'Guessed {check.upper()} **correctly**!\n'
                    guessed = set(check.upper())
                elif check.upper() in guessed_answers:
                    to_send = f'Guessed {check.upper()} **previously**!\n'
                else:
                    wrong_guesses += 1
                    guessed_answers.add(check.upper())
                    to_send = f'Guessed {check.upper()} **wrongly**!\n'

        await context.send(f'Category:  {category}',
                           file=discord.File('img/' + str(wrong_guesses) + '.png'))
        await context.send('**' +
                           '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                           '**\n\n' +
                           '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                      else '__' + i + '__' if i.upper() in guessed
                                      else i for i in list(ALPHABETS)]) +
                           '\n\n' + to_send)
        print('='*25)
        print('  '.join([i if i.upper() in guessed else '_' for i in list(word)]))
        for i in sorted(guessed_answers):
            print(i)
        print(to_send)
        print('='*25)

        if wrong_guesses == 6:
            await context.send(f'**Category:  {category}**', file=discord.File('img/7.png'))
            await context.send('**' +
                               '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                               '**\n\n' +
                               '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                          else '__' + i + '__' if i.upper() in guessed
                                          else i for i in list(ALPHABETS)]) +
                               '\n\n' +
                               'Answer is  ' + '  '.join(['**' + i + '**' for i in list(word)]) +
                               '!  You lost! 😫 😭\n\n' +
                               '**Play a new game by sending "!play {category}" or "!start {category}"**')
            game_started = False
            guessed = set([' ', '(', ')', "'"])
            wrong_guesses = 0
            print('Game end! 6 tries up. Answer is  ' + '  '.join([i for i in list(word)]) + '!')
            word = ''
        else:
            word_set = set(word)
            if word_set.issubset(guessed):
                await context.send(f'**Category:  {category}**', file=discord.File('img/8.png'))
                await context.send('**' +
                                   '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                   '**\n\n' +
                                   '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                              else '__' + i + '__' if i.upper() in guessed
                                   else i for i in list(ALPHABETS)]) +
                                   '\n\n' +
                                   '\nAnswer is  ' + '  '.join(['**' + i + '**' for i in list(word)]) + '!\n' +
                                   'Congratulations on guessing correctly and winning!  🎉\n\n' +
                                   '**Play a new game by sending "!play {category}" or "!start {category}"**')
                game_started = False
                guessed = set([' ', '(', ')', "'"])
                wrong_guesses = 0
                print('Game end! WON! Answer is  ' + '  '.join([i for i in list(word)]) + '!')
                word = ''
    else:
        await context.send('No game running! Send "!play {category}" or "!start {category}" to start a game!')
        print(f'Guessed {" ".join(submission).upper()}, but the game is not running')


@bot.command(name='status', help='Checks status of game.')
async def status(context):
    print('status cmd issued')
    global game_started, category, wrong_guesses, word, guessed, guessed_answers, ALPHABETS
    if game_started:
        await context.send(f'Category chosen: {category}\n' +
                           'Word so far: **' +
                           '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                           '**\n' + 'Words status: ' +
                           '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                      else '__' + i + '__' if i.upper() in guessed
                                      else i for i in list(ALPHABETS)]) + '\n' +
                           f'Wrong guesses: {wrong_guesses}/6\n' +
                           'Guessed answers: \n' +
                           '\n'.join(sorted(guessed_answers)) +
                           '='*15 + 'END OF STATUS' + '='*15)
    else:
        await context.send('No game running. Send "!play {category}" or "!start {category}" to play.')


@bot.command(name='stats', help='Checks status of game.')
async def stats(context):
    print('stats cmd issued')
    global game_started, category, wrong_guesses, word, guessed, guessed_answers, ALPHABETS
    if game_started:
        await context.send(f'Category chosen: {category}\n' +
                           'Word so far: **' +
                           '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                           '**\n' + 'Words status: ' +
                           '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                      else '__' + i + '__' if i.upper() in guessed
                           else i for i in list(ALPHABETS)]) + '\n' +
                           f'Wrong guesses: {wrong_guesses}/6\n' +
                           'Guessed answers: \n' +
                           '\n'.join(sorted(guessed_answers)) +
                           '='*15 + 'END OF STATUS' + '='*15)
    else:
        await context.send('No game running. Send "!play {category}" or "!start {category}" to play.')


@bot.command(name='stop', help='Quits a hangman game, if running.')
async def stop(stop_context):
    print('stop cmd issued')
    global game_started, guessed, wrong_guesses, word
    if not game_started:
        print('no game to quit')
        await stop_context.send('No game in progress to quit.')
    else:
        game_started = False
        print('game quit.')
        word = ''
        guessed = set([' ', '(', ')', "'"])
        wrong_guesses = 0
        await stop_context.send('Game quit! Type "!play {category}" or "!start {category}" to play a round of HANGMAN.')


@bot.command(name='quit', help='Quits a hangman game, if running.')
async def quit_game(quit_context):
    print('quit cmd issued')
    global game_started, guessed, wrong_guesses, word
    if not game_started:
        print('no game to quit')
        await quit_context.send('No game in progress to quit.')
    else:
        game_started = False
        print('game quit.')
        word = ''
        guessed = set([' ', '(', ')', "'"])
        wrong_guesses = 0
        await quit_context.send('Game quit! Type "!play {category}" or "!start {category}" to play a round of HANGMAN.')


bot.run(BOT_KEY)
