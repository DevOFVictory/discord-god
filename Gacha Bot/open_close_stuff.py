import json
import yaml


def open_inv(ctx):
    with open(f"Datenbank/{ctx.channel.guild.id}/inv.txt", mode="r", encoding="utf-8") as inventory_load:
        inventories = json.load(inventory_load)
        return inventories


def open_bas(ctx):
    with open(f"Datenbank/{ctx.channel.guild.id}/basar.txt", mode="r", encoding="utf-8") as bas_load:
        the_basar = json.load(bas_load)
        return the_basar


def open_crowns(ctx):
    with open(f"Datenbank/{ctx.channel.guild.id}/kk.txt", mode="r", encoding="utf-8") as users_crowns_load:
        users_crowns = json.load(users_crowns_load)
        return users_crowns


def open_time(ctx):
    with open(f"Datenbank/{ctx.channel.guild.id}/dailytime.txt", encoding="utf-8") as daily_time_load:
        daily_time = json.load(daily_time_load)
        return daily_time


def open_streak(ctx):
    with open(f"Datenbank/{ctx.channel.guild.id}/streak.txt", mode="r") as streak_load:
        streak = json.load(streak_load)
        return streak


def open_dinos():
    with open("Gacha Bot/dinosaurs.yaml", mode="r", encoding="utf-8") as dino_file:
        dinos = yaml.safe_load(dino_file)
        return dinos


def close_inv(ctx, inventory):
    with open(f"Datenbank/{ctx.channel.guild.id}/inv.txt", mode="w", encoding="utf-8") as inventory_load:
        json.dump(inventory, inventory_load)


def close_crowns(ctx, users_crowns):
    with open(f"Datenbank/{ctx.channel.guild.id}/kk.txt", mode="w", encoding="utf-8") as users_crowns_load:
        json.dump(users_crowns, users_crowns_load)


def close_basar(ctx, the_basar):
    with open(f"Datenbank/{ctx.channel.guild.id}/basar.txt", mode="w", encoding="utf-8") as bas_load:
        json.dump(the_basar, bas_load)


def close_time(ctx, daily_time):
    with open(f"Datenbank/{ctx.channel.guild.id}/dailytime.txt", "w") as daily_time_load:
        json.dump(daily_time, daily_time_load)


def close_streak(ctx, streak):
    with open(f"Datenbank/{ctx.channel.guild.id}/streak.txt", mode="w") as streak_load:
        json.dump(streak, streak_load)
