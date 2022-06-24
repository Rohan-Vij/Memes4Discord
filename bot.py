# importing the image class from image.py
from image import image

# Library used to manage the bot
from discord.ext import commands

# Purely for image --> Discord processing
import discord

# Import os to delete the image once downloaded
import os

# For downloading the avatar images
import requests

# Token
token = "YOUR_TOKEN"

# Declaring bot (command_prefix doesn't really matter)
bot = commands.Bot(command_prefix="!", self_bot=True)

# Creating object with Bernie Sanders/Sokka image template
sokka = image("pls.jpg")  

@bot.event
async def on_ready():
    print(bot.user)

@bot.event
async def on_message(ctx):
    # If the message starts with a command 
    # Add more if-statements when more commands are added
    if ctx.content.startswith('.sanders'):
        # Remomving prefix
        msg = ctx.content.replace(".sanders", "").strip()
        
        # If nothing else is after the prefix (just ".sokkafy")
        if len(msg) == 0:
            await ctx.channel.send("Make sure to enter a valid string after `.sokkafy`! For example, `.sokkafy please stop`")
            return
        # If the text goes out of the permitted space in the image 
        elif len(msg) > 27:
            await ctx.channel.send("Make sure that your string is under 28 characters!")
            return

        # Getting the avatar url of the message sender
        url = str(ctx.author.avatar_url).replace("1024", "256")
        print(url)

        # Using the name
        filename = url.split('/')[-1].split("?")[0].replace("webp", "jpg")

        # Downloading image
        img_data = requests.get(url).content
        with open(f'pfps/{filename}.jpg', 'wb') as handler:
            handler.write(img_data)
        handler.close()        

        # Resetting the sokka object by redefining it
        sokka = image("pls.jpg")  
        # Settings the self.txt variable to the value of the message
        sokka.set_txt(msg)
        # Pasting profile picture
        sokka.paste(filename)
        # Writing to the image
        sokka.write()
        # Saving to /downloaded
        name = sokka.save()

        # Getting file to send from /downloaded directory
        to_send = discord.File(f"downloaded/{name}.jpg")

        # Sending image
        await ctx.channel.send(file=to_send) 

        # Deleteing image from /downloaded
        os.remove(f"downloaded/{name}.jpg")

        # Deleting pfp image from /pfps
        os.remove(f"pfps/{filename}.jpg")

# Running bot
bot.run(token, bot=False)  
