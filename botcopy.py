import discord
import os
from discord.ext import commands

TOKEN = "NzI3NzY3NzkxMjQ3MDMyMzUw.Xwvq2g.0mm9MyOfBZq4FewO_r0lGuZwPEs"

bot = commands.AutoShardedBot(command_prefix="-")
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="suggest")
async def _suggest(ctx, *, suggestion=None):
    if suggestion is None:
        embed= discord.Embed(title="Invalid Arguments", 
                            description=f"Usage:{ctx.prefix}suggest <suggestion>", 
                            color=0xff0000, 
                            timestamp=ctx.message.created_at)
        await ctx.send(embed=embed)
        return
    channel = ctx.guild.get_channel(729176150542254100)
    if not channel:
        await ctx.send("This channel does not exist in this server!")
        return
    embed = discord.Embed(title= "Suggestion", 
                    description=suggestion,
                    color=0x00fffff,
                    timestamp=ctx.message.created_at)
    embed.set_footer(text=f"From: {ctx.author}", icon_url=ctx.author.avatar_url)
    msg = await channel.send(embed=embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")

@bot.command(name="help")
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        color=0x00fffff
    )

    embed.set_author(name='Help')
    embed.add_field(name='Suggestion Command', value='suggest <suggestion>', inline=False)
    embed.add_field(name='Help Command', value='help (DMs you this embed)', inline=False)
    embed.add_field(name='Author Of CMA Bot:', value='@🇨🇦ConmanAgar🇨🇦#2504', inline=False)
    await author.send(embed=embed)

@bot.command(name="quit")
@commands.has_permissions(administrator=True)
async def close(ctx):
    await bot.close()
    print("Bot Closed")

bot.run(TOKEN)