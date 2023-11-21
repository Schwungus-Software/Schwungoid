# Schwungoid

A Discord bot for all things Schwungus.

## Deployment

You have two options actually:

1. Deploying on your server (or even your PC) directly.
2. Running the bot inside a Docker container.

### Direct

TL;DR: for a "direct" deployment, run:

```bash
echo 'DISCORD_TOKEN=<your-bot-token>' > .env
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m schwungoid
```

**TODO**: explain what the commands do.

### Docker

I suppose you already know what you're doing if you're going to deploy with Docker. Using Portainer perhaps?

But if you're less knowledgeable and just want to run an instance of the bot, you should try:

```bash
sudo docker build -t schwungoid . # build once and for all
sudo docker run --rm --env 'DISCORD_TOKEN=<your-bot-token>' schwungoid # re-run each time to redeploy
```
