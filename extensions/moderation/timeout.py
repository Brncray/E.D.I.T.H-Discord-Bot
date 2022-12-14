import lightbulb
import hikari
import datetime

plugin = lightbulb.Plugin('mute', 'mutes a member')



@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    pass



@plugin.command
@lightbulb.add_checks(
    lightbulb.has_guild_permissions(hikari.Permissions.MODERATE_MEMBERS),
    lightbulb.bot_has_guild_permissions(hikari.Permissions.MODERATE_MEMBERS)
)
@lightbulb.option('minutes', 'amount minutes to timeout user.', type=int, required=True)
@lightbulb.option('hours', 'amount hours to timeout user.', type=int, required=True)
@lightbulb.option('days', 'amount days to timeout user.', type=int, required=True)
@lightbulb.option('reason', 'reason for muting member', type = str, required=True)
@lightbulb.option('member', 'member being muted', type=hikari.Member, required=True)
@lightbulb.command('timeout', 'mutes members')
@lightbulb.implements(lightbulb.PrefixCommand, lightbulb.SlashCommand)
async def timeout(ctx):
    member = ctx.options.member
    reasoN = ctx.options.reason
    datetimE = datetime.timedelta(seconds=10)
    await ctx.respond(
    
    hikari.Embed
    (
         title=f"{member} has been timed out.",
         description=f"Reason: {reasoN}"
        ),
        flags=hikari.MessageFlag.EPHEMERAL
    )
    await hikari.Member.edit(reason=reasoN, communication_disabled_until=datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=ctx.options.days, hours=ctx.options.hours, minutes=ctx.options.minutes), self=ctx.options.member)
    await hikari.User.send(self=member, content=hikari.Embed(title=f"You were timed out from {ctx.get_guild().name}.", description=f'You were timed out for reason: {reasoN}', color="#FF0000"))






def load(bot):
    bot.add_plugin(plugin)
