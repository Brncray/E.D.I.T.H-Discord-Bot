import lightbulb 
import hikari


bot = lightbulb.BotApp(
    token='TOKEN HERE', 
)




#@bot.listen(hikari.GuildMessageCreateEvent)
#async def print_message(event):
#    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started.')







#purge command



@bot.command
@lightbulb.option('messages', 'how many messages to delete', type=int, required=True)
@lightbulb.command('purge', 'mass delete messages')
@lightbulb.implements(lightbulb.SlashCommand)
async def purge(ctx):
  if ctx.options.messages > 50:
    await ctx.respond(
        hikari.Embed
        (
            title="Error",
            color="#FF0000",
            description="You cannot delete more than 50 messages at a time."
        )
    
    )
    return

    
  await bot.rest.delete_messages(ctx.channel_id, await bot.rest.fetch_messages(ctx.channel_id).limit(ctx.options.messages))






# goes to the directory of extensions and then loads the files in the folder. 
bot.load_extensions_from('./extensions')
bot.load_extensions_from('./extensions/math')
bot.load_extensions_from('./extensions/moderation')
bot.load_extensions_from('./extensions/fun')

bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="nothing",
        url="https://www.twitch.tv/brncray_",
        type=hikari.ActivityType.STREAMING,
    ),
)
