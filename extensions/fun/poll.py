import lightbulb
import hikari
import datetime

plugin = lightbulb.Plugin('poll', 'starts a poll')

bot = lightbulb.BotApp

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass



@plugin.command
@lightbulb.option('message', 'The poll\'s message', type=str, required=True)
@lightbulb.command('poll', 'Starts a poll')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def poll(ctx):
    message = ctx.options.message
    author = hikari.Message.author
    embed_options = (
    hikari.Embed(
      title="New Poll",
      description=f"{message}",
      timestamp=datetime.datetime.now().astimezone()
    )
  )
    rp = await ctx.respond(embed=embed_options)
    msg = await rp.message()
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")


def load(bot):
    bot.add_plugin(plugin)
