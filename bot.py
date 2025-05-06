import discord
import os
import random
from dotenv import load_dotenv

# load .env into os.environ
load_dotenv()  

# now read them
TOKEN       = os.getenv("DISCORD_TOKEN")
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER")

if not TOKEN or not IMAGE_FOLDER:
    raise RuntimeError("Missing DISCORD_TOKEN or IMAGE_FOLDER in environment")

goon_choices = [
    "Keep on Gooning!", "Goon Mode: Activated!", "...",
]

def get_image():
    # read the folder path from env
    folder = IMAGE_FOLDER

    images = [
        os.path.join(folder, fn)
        for fn in os.listdir(folder)
        if fn.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ]
    if not images:
        raise FileNotFoundError(f"No images found in {folder!r}")
    return random.choice(images)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$jerk'):
            img_path = get_image()
            await message.channel.send(file=discord.File(img_path))
            await message.channel.send(random.choice(goon_choices))

intents = discord.Intents.default()
intents.message_content = True

# finally, run with the loaded token
client = MyClient(intents=intents)
client.run(TOKEN)
