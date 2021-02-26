import discord
from discord.ext import commands
import json
import requests

client = commands.Bot(command_prefix="!")


@client.event
async def on_message(message: discord.Message):
    for attachment in message.attachments:
        img_url = attachment.url
        print(img_url)
        await message.delete(delay=20)
        r = requests.get("http://api.foxtools.ru/v2/QR?cp=UTF-8&lang=EN&mode=Decode&url={}&formatting=1".format(img_url))
        json_data = json.loads(r.text)
        data = json_data.get('response')
        value = data['value']
        await message.channel.send("Твой код: **{}**".format(value))

@client.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


token = os.environ.get('BOT_TOKEN')
# token = ""
client.run(str(token))



