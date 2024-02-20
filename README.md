<h1 align="center">EmbedFix - A Discord bot for fixing Twitter and Instagram link embeds</h1>

## About

EmbedFix connects to your Discord server and simply replies to any Twitter or Instagram
link with a link to fxtwitter or ddinstagram, sites which have implemented proper embeds
within Discord.

## Adding the bot to your server

[Click here to add the bot to your server](https://discord.com/api/oauth2/authorize?client_id=1176694987732287588&permissions=8&scope=bot) (requires admin privileges)

## Setup

To set up a local instance of EmbedFix, simply clone the repo and then follow below steps.

1. Add token to environment
   `export DISCORD_BOT_TOKEN={INSERT_DISCORD_BOT_TOKEN}`
2. Install the requirements
   `poetry install`
3. Run the bot
   `poetry run python3 main.py`

You can use this to test any updates you make to the bot, use your own bot token from the
Discord Developer Portal and add the local bot to your server for testing. Once you've
made your changes you can create a pull request to add your code to the base bot for use
everywhere the bot is added. If you have any issues with this, please reach out to me at
daledave on Discord and I can help you out.

## Contributing

Any any all contributions are welcome, feel free to create a feature request, bug report,
or even a pull request of your own code to improve the bot.

## Running your own version

If you want, you can create a fork and host your version yourself, please simply keep
the link to the original repository.
