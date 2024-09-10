def determine(card, settings, xp_column):
    xp = int(card[xp_column])

    if card['edition'] == 4 or card['tier'] >= 4:
        bcx = xp
    else:
        if card['edition'] == 0 or (card['edition'] == 2 and card['card_detail_id'] < 100):
            if card['gold']:
                xp_property = "gold_xp"
            else:
                xp_property = "alpha_xp"
        else:
            if card['gold']:
                xp_property = "beta_gold_xp"
            else:
                xp_property = "beta_xp"

        bcx_xp = settings[xp_property][card['rarity'] - 1]
        bcx = max(xp / bcx_xp if card['gold'] else (xp + bcx_xp) / bcx_xp, 1)

        if card['edition'] == 0:
            bcx -= 1

    return int(bcx)

# Alternative method used previously not sure what is better
#
#
# rarity = card['rarity']
# edition = int(card['edition'])
# xp = int(card[xp_column])
#
# if edition == 0:
#     if card['gold']:
#         bcx = xp / settings['gold_xp'][rarity - 1]
#     else:
#         bcx = xp / settings['alpha_xp'][rarity - 1] + 1
# elif edition == 2 and int(card['card_detail_id']) > 223:  # all promo cards alpha/beta
#     bcx = xp
# elif (edition < 3) or ((edition == 3) and (int(card['card_detail_id']) <= 223)):
#     if card['gold']:
#         bcx = xp / settings['beta_gold_xp'][rarity - 1]
#     else:
#         bcx = xp / settings['beta_xp'][rarity - 1] + 1
# else:
#     bcx = xp
###
