import discord
import os
import random

goon_choices = ["Keep on Gooning!", "Goon Mode: Activated!", "Stay Goon-tastic!", "Goon Vibes Only!", "Goon On, Friend!", "Goofy Gooning Ahead!", "Goon Patrol, Assemble!", "Gooning All the Way!", "Goon Dreams Await!", "Goon Squad, Unite!", "May the Goon Be with You!", "Live, Laugh, Goon!"]
def get_image():
    folder = r"C:\Users\nandy\Desktop\Brother Pictures s25"
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

client = MyClient(intents=intents)
key = ''
client.run(key)
print(random.choice(images))