# Edition and Rarity mappings


edition_mapping = {
    0: 'Alpha',
    1: 'Beta',
    2: 'Promo',
    3: 'Reward',
    4: 'Untamed',
    5: 'Dice',
    6: 'Gladius',
    7: 'Chaos',
    8: 'Rift',
    10: 'Soulbound',
    12: 'Rebellion',
    13: 'Soulbound Rebellion'
}

rarity_mapping = {
    1: 'Common',
    2: 'Rare',
    3: 'Epic',
    4: 'Legendary'
}

rarity_to_level = {
    'Common': '10',
    'Rare': '8',
    'Epic': '6',
    'Legendary': '4'
}

rarity_colors = {
    'Common': 'gray',
    'Rare': 'blue',
    'Epic': 'purple',
    'Legendary': 'orange'
}

rarity_order = [
    'Common',
    'Rare',
    'Epic',
    'Legendary'
]

edition_order = [edition_mapping[num] for num in sorted(edition_mapping)]
