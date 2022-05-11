import discord as dc
import open_close_stuff as ocs


def create_dino_embed(dino_base_name, title):

    rarities = {
        "gewöhnlich": [0x777777, "Ein gewöhnlicher Dinosaurier!", ":white_circle:"],
        "ungewöhnlich": [0x359b15, "Ein ungewöhnlicher Dinosaurier!", ":green_circle:"],
        "selten": [0x1e72e6, "Ein seltener Dinosaurier!", ":blue_circle:"],
        "episch": [0x8227da, "Ein epischer Dinosaurier!", ":purple_circle:"],
        "legendär": [0xc0b838, "Ein legendärer Dinosaurier!", ":star:"],
        "sonderrang": [0xa13316, "Ein Objekt der ganz besonderen Art!", ":secret:"]
    }

    dinos = ocs.open_dinos()

    dino_features = dinos[dino_base_name]
    dino_name = dino_base_name + f" {rarities[dino_features[0]][2]}"

    embed = dc.Embed(title=title, colour=dc.Colour(rarities[dino_features[0]][0]),
                     description=rarities[dino_features[0]][1])
    embed.set_image(url=dino_features[1])
    embed.add_field(name=dino_name, value=dino_features[2])

    return [embed, dino_name]
