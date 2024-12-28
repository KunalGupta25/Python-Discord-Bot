# Discord Bot

A simple Discord bot that can send memes, jokes, and handle basic moderation commands.

## Features

- Get random memes
- Get random jokes
- Message purging (moderation)
- Help command
- Greeting command

## Setup

1. Clone the repository
```
git clone https://github.com/your-username/discord-bot.git
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Create a .env file with your Discord bot token
```
BOT_TOKEN=your_discord_bot_token
```
4. Run the bot
```
python old_bot.py
```

## Usage

- !meme: Get a random meme
- !joke: Get a random joke
- !purge [number]: Delete specified number of messages (Requires Manage Messages permission)
- !help: Show this help message
- !hello: Say hello to the bot

API:
- https://meme-api.com/gimme
- https://official-joke-api.appspot.com/random_joke

