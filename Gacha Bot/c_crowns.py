import setup
import server_differences
import datetime
import open_close_stuff as ocs


@setup.slash.slash(description=f"Hol dir deine täglichen Kjell Kronen ab", guild_ids=setup.guild_ids)
async def daily(ctx):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den daily Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    # darf der Nutzer Kronen abholen?
    with open(f"Datenbank/{ctx.channel.guild.id}/banned.txt", mode="r", encoding="utf-8") as banned_users_load:
        banned_users = []
        for user in banned_users_load.readlines():
            banned_users.append(user)

    if message_author in banned_users:
        return

    daily_time = ocs.open_time(ctx)
    users_crowns = ocs.open_crowns(ctx)
    streak = ocs.open_streak(ctx)

    today = datetime.date.today()
    tdelta = datetime.timedelta(days=1)
    yeday = today - tdelta

    # Hat er jemals schon abgeholt und hat er heute schon abgeholt
    if message_author not in daily_time:
        daily_time[message_author] = "0"
        users_crowns[message_author] = 300
        streak[message_author] = 0

    if daily_time[message_author] == str(today):
        await ctx.send(f"**{ctx.author.name}**, du hast deine {server_differences.kk} heute schon abgeholt!")
        return

    user_earnings = 65

    # Falls das Datum nicht gestern und damit die Streak unterbrochen ist
    if not daily_time[message_author] == str(yeday):
        streak[message_author] = 1
        users_crowns[message_author] += user_earnings

    # Falls das Datum gestern ist und die streak damit läuft
    else:
        streak[message_author] += 1

        rewards = ("65 " * 4) + ("70 " * 4) + ("75 " * 4) + ("80 " * 4) + ("85 " * 4) + ("90 " * 4) + ("95 " * 4)
        reward_list = rewards.split(" ")
        try:
            user_earnings = reward_list[streak[message_author]]
        except IndexError:
            user_earnings = 95
        users_crowns[message_author] += int(user_earnings)

    daily_time[message_author] = str(today)

    ocs.close_crowns(ctx, users_crowns)
    ocs.close_time(ctx, daily_time)
    ocs.close_streak(ctx, streak)

    await ctx.send(
        f"Glückwunsch **{ctx.author.name}**, du hast deine täglichen **{user_earnings}** {server_differences.kk} "
        f"eingefordert! Deine Streak beträgt nun **{streak[message_author]}** :fire:!")


@setup.slash.slash(description="Lass dir angeben wie viel Kjell Kronen du hast", guild_ids=setup.guild_ids)
async def kk(ctx):

    setup.check_channel(ctx)
    print(f"{ctx.author.name} hat den kk Befehl ausgeführt")
    message_author = ctx.author.mention.replace("!", "")

    users_crowns = ocs.open_crowns(ctx)

    if message_author not in users_crowns:
        await ctx.send(f"**{ctx.author.name}**, du hast noch keine {server_differences.kk}!")

    else:
        await ctx.send(f"**{ctx.author.name}** hat **{users_crowns[message_author]}** {server_differences.kk}")
