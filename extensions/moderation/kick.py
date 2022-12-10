import lightbulb
import hikari

plugin = lightbulb.Plugin('kick', 'Kicks a member')


@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass





@plugin.command
@lightbulb.add_cooldown(8, 2, lightbulb.UserBucket)
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.KICK_MEMBERS)
)
@lightbulb.option('reason', 'reason for kicking member', type = str,required = True)
@lightbulb.option('member', 'member to be kicked',type = hikari.Member, required = True)
@lightbulb.command('kick', 'kick members')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def kick(ctx):
    member = ctx.options.member
    reasoN = ctx.options.reason

    await hikari.User.send(self=member, content=hikari.Embed(title=f"You were kicked from {ctx.get_guild().name}.", description=f'You were kicked for reason: {reasoN}', color="#FF0000"))
    await member.kick()
    await ctx.respond(
        
        hikari.Embed
        (
            title=f"{member} has been kicked.",
            description=f"Reason: {reasoN}"
        ),
        flags=hikari.MessageFlag.EPHEMERAL
    )
    









def load(bot):
    bot.add_plugin(plugin)