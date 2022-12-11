import lightbulb 
import hikari
import asyncio


bot = lightbulb.BotApp(
    token='TOKEN HERE', 
    default_enabled_guilds=(1046571281228775464)
)




rest = hikari.RESTApp()

TOKEN = "TOKEN ALSO GOES HERE"
GUILD_ID = hikari.UNDEFINED

async def main():
    async with rest.acquire(TOKEN, hikari.TokenType.BOT) as client:
        application = await client.fetch_application()

        await client.set_application_commands(application.id, (), guild=GUILD_ID)

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

asyncio.run(main())
