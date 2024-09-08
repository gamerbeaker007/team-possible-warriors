def determine(card, settings, xp_column):
    rarity = card['rarity']
    edition = int(card['edition'])
    xp = int(card[xp_column])

    if edition == 0:
        if card['gold']:
            bcx = xp / settings['gold_xp'][rarity - 1]
        else:
            bcx = xp / settings['alpha_xp'][rarity - 1] + 1
    elif edition == 2 and int(card['card_detail_id']) > 223:  # all promo cards alpha/beta
        bcx = xp
    elif (edition < 3) or ((edition == 3) and (int(card['card_detail_id']) <= 223)):
        if card['gold']:
            bcx = xp / settings['beta_gold_xp'][rarity - 1]
        else:
            bcx = xp / settings['beta_xp'][rarity - 1] + 1
    else:
        bcx = xp

    return int(bcx)
