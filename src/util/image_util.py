from src.statics_enums import rarity_to_level, edition_img_mapping

image_base_url = "https://images.hive.blog/125x0/https://d36mxiodymuqjm.cloudfront.net/cards_by_level/"


def generate_image_url(row):
    card_name = row['name'].replace(' ', '%20')  # Replace spaces with %20
    level = rarity_to_level[row['rarity_name']]
    edition = edition_img_mapping.get(row['edition'])
    if row['gold']:
        img_url = f"{image_base_url}{edition}/{card_name}_lv{level}_gold.png"
    else:
        img_url = f"{image_base_url}{edition}/{card_name}_lv{level}.png"

    return f'<img src="{img_url}" width="60">'
