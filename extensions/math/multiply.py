import lightbulb
import hikari

plugin = lightbulb.Plugin('multiply', 'Multiplication')


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass





@plugin.command
@lightbulb.option(
    'num2',
    'Number 2',
    type=int
)
@lightbulb.option(
    'num1',
    'Number 1',
    type=int
)
@lightbulb.command('multiplication', 'Multiplies stuff')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(ctx.options.num1 * ctx.options.num2)











def load(bot):
    bot.add_plugin(plugin)