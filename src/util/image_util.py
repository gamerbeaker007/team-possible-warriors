from src.statics_enums import rarity_to_level, edition_img_mapping

image_base_url = "https://images.hive.blog/125x0/https://d36mxiodymuqjm.cloudfront.net/cards_by_level/"


def generate_image_url(name, rarity_name, edition, gold):
    card_name = name.replace(' ', '%20')  # Replace spaces with %20
    level = rarity_to_level[rarity_name]
    edition_img_name = edition_img_mapping.get(edition)
    if gold:
        img_url = f"{image_base_url}{edition_img_name}/{card_name}_lv{level}_gold.png"
    else:
        img_url = f"{image_base_url}{edition_img_name}/{card_name}_lv{level}.png"

    return f'<img src="{img_url}" width="60">'
