import discord
from discord import app_commands
from discord.ext import commands
import random
import json

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    bot_token = config['BOT_TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())
# Bot version and contributors
bot_version = "0.1.1 Beta"
contributors = [
    "A9qx",
    "TacticalSoupCan",
    # Add more contributors here
]
# Add or remove quotes in this list
quotes = [
            "no comment",
            "it's ok, we can buy a new one",
            "fronch fries",
            "typeerrrarace me right now",
            "andreas stop slapping that infant",
            "stop rizzing my mom",
            "kid named finger:",
            "how bad can i be? i'm just crashing the economy",
            "naked xbox",
            "usps is speedrunning my package through every single regional facility",
            "imagine not having a Verified Bank Account",
            "lol thats what makes this really funny because as you can see im actually really goated and ksaooifudsfusoifudsfusdoifusdfudsoiusfs fdsuf oisdufsdi fusdoiuf",
            "(Sending DDOS now)",
            "cheese",
            "CHCIKEN BREAST",
            "life sucks and then you die; get used to it",
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="status", description="Simple command to test if the bot is online or not.")
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Bot Status",
        description=f"I'm still here, {interaction.user.mention}; Ping is {bot.latency:.2f} ms.",
        color=discord.Color.green()  # You can customize the color of the embed
    )
    
    await interaction.response.send_message(embed=embed)
    
@bot.tree.command(name="dm", description="Send a direct message to a user")
async def dm(interaction: discord.Interaction, user: discord.User, *, message: str):
    # Send the message to the user
    await user.send(f"{message}  -{interaction.user.mention}")
    
    # Create and send an embed response
    embed = discord.Embed(
        title="Message Sent",
        description=f"I've sent a message to {user.mention}: `{message}`",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)
    
@bot.tree.command(name="quote", description="Get a random funny quote")
async def random_quote(interaction: discord.Interaction):
    random_quote = random.choice(quotes)
    
    embed = discord.Embed(
        title="Random Quote",
        description=f'"{random_quote}"',
        color=discord.Color.orange()
    )
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="version", description="Get bot version and contributors")
async def bot_info(interaction: discord.Interaction):
    contributor_list = "\n".join(contributors)
    
    embed = discord.Embed(
        title="Bot Information",
        description=f"**Version:** {bot_version}\n\n**Contributors:**\n{contributor_list}",
        color=discord.Color.blue()
    )
    
    await interaction.response.send_message(embed=embed)


bot.run(bot_token)