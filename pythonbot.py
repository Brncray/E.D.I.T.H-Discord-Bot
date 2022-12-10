import lightbulb 
import hikari


bot = lightbulb.BotApp(
    token='TOKEN HERE', 
    default_enabled_guilds=(1046571281228775464)
)




#@bot.listen(hikari.GuildMessageCreateEvent)
#async def print_message(event):
#    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started.')

# simple pong slash command
#@bot.command
#@lightbulb.command('ping', 'Says pong')
#@lightbulb.implements(lightbulb.SlashCommand)
#async def ping(ctx):
#    await ctx.respond('Pong')
###############################################

# A grouped command
#@bot.command
#@lightbulb.command('group', 'This is a group')
#@lightbulb.implements(lightbulb.SlashCommandGroup)
#async def my_group(ctx):
#    pass
######################################################


# a subcommand
#@my_group.child
#@lightbulb.command('subcommand', 'subcommand test')
#@lightbulb.implements(lightbulb.SlashSubCommand)
#async def subcommand(ctx):
#    await ctx.respond('Subcommand test')
######################################################


#addition calculator 

##############################################################

# goes to the directory of extensions and then loads the files in the folder. 
bot.load_extensions_from('./extensions')
bot.load_extensions_from('./extensions/math')
bot.load_extensions_from('./extensions/moderation')
bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="nothing",
        url="https://www.twitch.tv/brncray_",
        type=hikari.ActivityType.STREAMING,
    ),
)
