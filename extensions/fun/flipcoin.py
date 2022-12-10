import lightbulb
import hikari
import datetime
import random

plugin = lightbulb.Plugin('flip', 'flip')

bot = lightbulb.BotApp

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass



@plugin.command
@lightbulb.command('coinflip', 'Flips a coin')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def poll(ctx):
    coin = random.randint(1,2)
    if coin == 1:
        result = "Heads"
    elif coin == 2:
        result = "Tails"
    await ctx.respond(
        hikari.Embed
        (
            title="Coin Flip",
            description=f"{result}"
        )
    )



def load(bot):
    bot.add_plugin(plugin)
