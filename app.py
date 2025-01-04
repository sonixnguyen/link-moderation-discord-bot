import discord
from discord.ext import commands
import re

# Bot intents and prefix
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Staff channel ID
STAFF_CHANNEL_ID = 11111  # Replace with your staff channel ID

WHITELISTED_USER_IDS = []  # Add user IDs to whitelist [ID1, ID2]
WHITELISTED_CHANNEL_IDS = []  # Add channel IDs to whitelist

LINK_REGEX = r"https://[\w.-]+\.[a-z]{2,}(?:/[\w.-]*)*(?:\?[\w=&]*)?(?:#[\w-]*)?"

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author.id in WHITELISTED_USER_IDS or message.channel.id in WHITELISTED_CHANNEL_IDS:
        return

    links = re.findall(LINK_REGEX, message.content)
    if links:
        for link in links:
            if "discord.com" in link:
                return

        await message.delete()
        await message.channel.send(
            f"{message.author.mention}, your message with the link is being moderated.", delete_after=5
        )

        staff_channel = bot.get_channel(STAFF_CHANNEL_ID)
        if staff_channel:
            embed = discord.Embed(
                title="Messages need moderation",
                description=message.content,
                color=discord.Color.orange()
            )
            embed.add_field(name="Sender", value=message.author.mention, inline=False)
            embed.add_field(name="Original channel", value=message.channel.mention, inline=False)
            if message.reference:
                embed.add_field(name="Reply to", value=message.reference.message_id, inline=False)

            msg = await staff_channel.send(embed=embed)
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.message.channel.id == STAFF_CHANNEL_ID:
        message = reaction.message
        if str(reaction.emoji) == "✅":
            embed = message.embeds[0] if message.embeds else None
            if embed:
                original_channel_id = int(embed.fields[1].value.strip('<#>'))
                original_channel = bot.get_channel(original_channel_id)
                if original_channel:
                    user_id = int(embed.fields[0].value.strip('<@!>'))
                    user = await bot.fetch_user(user_id)
                    user_avatar = user.avatar.url if user.avatar else None

                    approval_embed = discord.Embed(
                        description=embed.description,
                        color=discord.Color.green()
                    )
                    approval_embed.set_author(name=user.display_name, icon_url=user_avatar)

                    reply_message_id = None
                    for field in embed.fields:
                        if field.name == "Reply to":
                            reply_message_id = int(field.value)

                    if reply_message_id:
                        try:
                            original_message = await original_channel.fetch_message(reply_message_id)
                            await original_message.reply(embed=approval_embed)
                        except discord.NotFound:
                            await original_channel.send(embed=approval_embed)
                    else:
                        await original_channel.send(embed=approval_embed)

        elif str(reaction.emoji) == "❌":
            pass

bot.run("XXX")