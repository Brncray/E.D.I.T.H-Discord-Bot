import lightbulb
import hikari

plugin = lightbulb.Plugin('ban', 'Bans a member')


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass






@plugin.command
@lightbulb.add_cooldown(8, 2, lightbulb.UserBucket)
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.BAN_MEMBERS)
)
@lightbulb.option('reason', 'reason for banning member', type = str,required = True)
@lightbulb.option('member', 'member to be banned',type = hikari.Member, required = True)
@lightbulb.command('ban', 'ban members')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def ban(ctx):
    member = ctx.options.member
    reasoN = ctx.options.reason
    await hikari.User.send(self=member, content=hikari.Embed(title=f"You were banned from {ctx.get_guild().name}.", description=f'You were banned for reason: {reasoN}', color="#FF0000"))
    await member.ban(reason=reasoN)
    await ctx.respond(
        hikari.Embed
        (
        title=f'{member} has been banned',
        description=f'Reason: {reasoN}',   
        color="#FF0000" 
        ),
        flags=hikari.MessageFlag.EPHEMERAL
    )
    #await ctx.respond(f'Successfully banned. `{member}` because `{reasoN}`')









def load(bot):
    bot.add_plugin(plugin)