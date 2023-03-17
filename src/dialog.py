
def default_ruler_stat():
    """The default stat for all rulers

    The default stat for all rulers:
    stat - They are alive
    allies - Allies are alive
    meet - You have not met them
    fight - You have not fought them
    

    Returns
    -------
    dict
    """
    return {'stat': True,    # Alive or dead
            'allies': True,  # Are allies alive or dead
            'meet': False,    # Have you spoken to them before fighting
            'fight': False,   # Did choose to fight them / cannot talk during fight
            'power': True,    # Did you defeat them
           }

def get_ruler_dialog(which, NPC):
    king = NPC['king']
    cler = NPC['cleric']
    merc = NPC['merchant']

    out = '!GREETING! !MID1! !MID2! !END!'

    if which == 'king':
        # Greeting
        if not king['meet']:
            greeting = 'Are you a loyal knight looking to serve their King?'
        elif king['power']:
            # You have met, but have not fought
            greeting = 'Welcome back, loyal Knight!'
        elif not king['power']:
            # You have defeated the king and his allies (alive)
            if king['allies']:
                greetings = 'Oh honorable and merciful Knight!'
            else:
                # Kings allies are dead
                greetings = 'Oh powerful and merciful Knight!'

        if merc['stat']:
            # Merchant is alive
            if merc['fight']:
                # You are fighting the merchant
                if merc['allies']:
                    # The merchant's allies are alive
                    mid2 = 'I hear you and the Merchant are battling. You should have no trouble defeating him and his dragons. He never worried me, for my soldiers can easily defeat his dragons.'
                else:
                    # You have slayed the dragons but not merchant
                    mid2 = 'I hear you have slayed the Merchant\'s dragons. They never bothered me, for my soldiers could have easily defeated them. You should finish off the weak Merchant quickly.'
            else:
                # You are not fighting the merchant
                if merc['power']:
                    # You have not fought against the merchant yet
                    mid2 = 'There is a greedy Merchant that controls dragons. The dragons provide him with untold wealth, which he uses to benefit only himself. He is of little bother to me, for my soldiers can easily defeat his dragons.'
                else:
                    # You have defeated the merchant but have spared him
                    if merc['allies']:
                        # You have spared the dragons
                        mid2 = 'I hear wonderful tales of your recent victory against the Merchant and his dragons. I encourage you to return and slay him and his dragons.'
                    else:
                        mid2 = 'I hear wonderful tales of your recent victory against the Merchant and his dragons. I encourage you to give him the same fate as his dragons.'
        else:
            # Merchant is dead
            if merc['allies']:
                # You have spared the dragons
                    mid2 = 'I hear wonderful tales of your recent victory against the Merchant and his dragons. Dragons are wild beasts and I encourage you to return and slay them.'
            
            else:
                # The Merchant and Dragons are dead
                mid2 = 'I see you have slayed the weak Merchant and his puny dragons. My soldiers could have easily done this, but no matter the task is done.'
        
        if cler['stat']:
            # Cleric is alive
            if cler['fight']:
                # You are fighting the Cleric
                if cler['allies']:
                    # The Cleric's allies are alive
                    mid2 = 'It is known that you and the Cleric are battling. Her magic can be challenging to overcome. Do not forget about her evil elementals. I fear the Cleric, for soldiers dare not strike down a cleric and her elementals control the harvest.'
                else:
                    # You have slayed the elementals but not cleric
                    mid2 = 'I hear you have slayed the Cleric\'s elementals. Order has been restored to nature and the harvest should return to normal. However, you must finish off the Cleric! They remain dangerous as long as they have power.'
            else:
                # You are not fighting the Cleric
                if cler['power']:
                    # You have not fought against the Cleric yet
                    mid2 = 'There is a deceitful Cleric that controls elementals. The elementals provide her control over the harvest, which she uses to benefit only herself. I fear the Cleric, for soldiers dare not strike down a cleric and her elementals control the harvest.'
                else:
                    # You have defeated the Cleric but have spared her
                    if cler['allies']:
                        # You have spared the elementals
                        mid2 = 'The people rejoice with news of your recent victory against the Cleric and her elementals. I encourage you to return and slay her and her elementals before they regain power.'
                    else:
                        mid2 = 'The bards sing great overtures of your victory over the Cleric.  Order has been restored to nature and the harvest should return to normal. However, I encourange you to return to the Cleric and finish her off before she regains power.'
        else:
            # Cleric is dead
            if cler['allies']:
                # You have spared the dragons
                    mid2 = 'Your name is shouted throughout the streets with news of your victory against the Cleric and her elementals. Elementals cannot be tamed and I encourage you to return and slay them.'
            
            else:
                # The Cleric and Elementals are dead
                mid2 = 'I see you have slayed the Cleric and her elementals. I guess they were not as difficult as I imagined.'
 
        
        
        and cler['stat']:
            # Merchant and Cleric are alive
            if not merc['fight'] and not cler['fight'] and merc['power'] and cler['power']:
                # Not fighting either, both in power
                mid = "I ask you to find the Cleric and the Merchant and slay them and their forces. I fear the Cleric more than the Merchant, for her magic can enchant the soldiers loyal to me.  The Merchant is less of a concern because my soldiers can slay his dragons.  Go forth and slay the Cleric."
            elif not merc['fight'] and merc['power'] and cler['fight'] and cler['power']:
                # Fighting the cleric
                
                and cler['allies'] and cler['stat'] and cler['power']:
                # Not fighting Merc, fighting cleric (alive) and elementals (alive)
                mid = "I hear you are battling with the Cleric and her elementals. I wish you luck.  I fear her, for her magic can enchant the soldiers loyal to me. I beg you to finish your task and slay the Cleric and her elementals. Afterwards, seek out the Merchant and his dragons and do the same. Go forth Knight!"
            elif not merc['fight'] and cler['fight'] and cler['allies'] and cler['stat'] and not cler['power']:
                # You have not met the king, defeated cleric (alive) and elementals (alive), not fighting merchant (alive)
                mid = "I hear glorious ballads about your victory against the Cleric and her elementals, but I do not know why you spare them. Return at once while they are weak and slay them! Afterwards, seek out the Merchant and his dragons and do the same. Go forth Knight!"


NPC = {'king': RULERS,
       'merchant': RULERS,
       'cleric': RULERS,
       }