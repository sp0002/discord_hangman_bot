import discord
import random
import secrets

from discord.ext import commands

print('start')
bot = commands.Bot(command_prefix='!')
client = discord.Client()

game_started = False
word = ''
category = ''
guessed = set(' ')
wrong_guesses = 0

BOT_KEY = ''  # add your bot key or sth
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
    global game_started, word, category, wrong_guesses, guessed
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
    global game_started, word, category, wrong_guesses, guessed
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
                                     'those with bold are correct guesses.')
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


@bot.command(name='guess', help='Send a guess of a letter.')
async def guess(context, letter=''):
    print('guess cmd issued')
    global game_started, guessed, category, word, wrong_guesses
    if game_started:
        if letter == '':
            await context.send('Guess cannot be blank!')
            print('empty guess issued')
        elif letter.upper() not in ALPHABETS:
            await context.send('Guess should be a single alphabet!')
            print('non-single alphabet guess issued')
        else:
            if letter.upper() not in guessed:
                guessed.add(letter.upper())
                if letter.upper() in word:
                    await context.send(f'Category:  {category}',
                                       file=discord.File('img/' + str(wrong_guesses) + '.png'))
                    await context.send('**' +
                                       '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                       '**\n\n' +
                                       '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                                  else '__' + i + '__' if i.upper() in guessed
                                                  else i for i in list(ALPHABETS)]) +
                                       '\n\n' +
                                       f'Guessed {letter.upper()} **correctly**!\n')
                    print('  '.join([i if i.upper() in guessed else '_' for i in list(word)]))
                    print(f'Guessed {letter.upper()} correctly.')
                else:
                    wrong_guesses += 1
                    await context.send(f'Category:  {category}',
                                       file=discord.File('img/' + str(wrong_guesses) + '.png'))
                    await context.send('**' +
                                       '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                       '**\n\n' +
                                       '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                                  else '__' + i + '__' if i.upper() in guessed
                                                  else i for i in list(ALPHABETS)]) +
                                       '\n\n' +
                                       f'Guessed {letter.upper()} **wrongly**!\n')
                    print('  '.join([i if i.upper() in guessed else '_' for i in list(word)]))
                    print(f'Guessed {letter.upper()}, but is wrong.')
            else:
                await context.send(f'Category:  {category}', file=discord.File('img/' + str(wrong_guesses) + '.png'))
                await context.send('**' +
                                   '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                                   '**\n\n' +
                                   '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                              else '__' + i + '__' if i.upper() in guessed
                                              else i for i in list(ALPHABETS)]) +
                                   '\n\n' +
                                   f'Guessed {letter.upper()} already!')
                print('  '.join([i if i.upper() in guessed else '_' for i in list(word)]))
                print(f'Guessed {letter.upper()}, but already guessed.')
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
                guessed = set(' ')
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
                    guessed = set(' ')
                    wrong_guesses = 0
                    print('Game end! WON! Answer is  ' + '  '.join([i for i in list(word)]) + '!')
                    word = ''
    else:
        await context.send('No game running! Send "!play {category}" or "!start {category}" to start a game!')
        print(f'Guessed {letter.upper()}, but the game is not running')


@bot.command(name='status', help='Checks status of game.')
async def status(context):
    print('status cmd issued')
    global category, wrong_guesses, word, guessed
    if game_started:
        await context.send(f'Category chosen: {category}\n' +
                           'Word so far: **' +
                           '  '.join([i if i.upper() in guessed else '\\_' for i in list(word)]) +
                           '**\n' + 'Words status: ' +
                           '  '.join(['**__' + i + '__**' if i.upper() in guessed and i.upper() in word
                                      else '__' + i + '__' if i.upper() in guessed
                           else i for i in list(ALPHABETS)]) +
                           '\n' +
                           f'Wrong guesses: {wrong_guesses}/6\n')
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
        guessed = set(' ')
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
        guessed = set(' ')
        wrong_guesses = 0
        await quit_context.send('Game quit! Type "!play {category}" or "!start {category}" to play a round of HANGMAN.')


bot.run(BOT_KEY)
