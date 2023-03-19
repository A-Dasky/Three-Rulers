import re

def get_ruler_dialog(who, which, NPC):
    king = NPC['king']
    cler = NPC['cleric']
    merc = NPC['merchant']


    if who == 'king':
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

        # Mid2
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

        # Mid1
        if cler['stat']:
            # Cleric is alive
            if cler['fight']:
                # You are fighting the Cleric
                if cler['allies']:
                    # The Cleric's allies are alive
                    mid1 = 'It is known that you and the Cleric are battling. Her magic can be challenging to overcome. Do not forget about her evil elementals. I fear the Cleric, for soldiers dare not strike down a cleric and her elementals control the harvest.'
                else:
                    # You have slayed the elementals but not cleric
                    mid1 = 'I hear you have slayed the Cleric\'s elementals. Order has been restored to nature and the harvest should return to normal. However, you must finish off the Cleric! They remain dangerous as long as they have power.'
            else:
                # You are not fighting the Cleric
                if cler['power']:
                    # You have not fought against the Cleric yet
                    mid1 = 'There is a deceitful Cleric that controls elementals. The elementals provide her control over the harvest, which she uses to benefit only herself. I fear the Cleric, for soldiers dare not strike down a cleric and her elementals control the harvest.'
                else:
                    # You have defeated the Cleric but have spared her
                    if cler['allies']:
                        # You have spared the elementals
                        mid1 = 'The people rejoice with news of your recent victory against the Cleric and her elementals. I encourage you to return and slay her and her elementals before they regain power.'
                    else:
                        mid1 = 'The bards sing great overtures of your victory over the Cleric.  Order has been restored to nature and the harvest should return to normal. However, I encourange you to return to the Cleric and finish her off before she regains power.'
        else:
            # Cleric is dead
            if cler['allies']:
                # You have spared the dragons
                mid1 = 'Your name is shouted throughout the streets with news of your victory against the Cleric and her elementals. Elementals cannot be tamed and I encourage you to return and slay them.'
            
            else:
                # The Cleric and Elementals are dead
                mid1 = 'I see you have slayed the Cleric and her elementals. I guess they were not as difficult as I imagined.'
 
        if king['power']:
            # You have not started fighting the king
            if merc['stat'] and cler['stat']:
                # Merchant and Cleric both alive
                end = "Go forth brave Knight and slay the Cleric and the Merchant."
            elif merc['stat']:
                # Cleric dead
                end = "Go forth brave Knight and slay the Merchant."
            elif cler['stat']:
                # Merchant dead
                end = "Go forth brave Knight and slay the Cleric."
            else:
                # Both dead
                end = "You are indeed powerful. You should lay down your arms and head to the Hall of Heroes."
        else:
            # You have defeated the king
            if merc['stat'] and cler['stat']:
                # Merchant and Cleric both alive
                end = "I beg you merciful Knight to show me mercy. Turn your wrath towards the Cleric and the Merchant."
            elif merc['stat']:
                # Cleric dead
                end = "I beg you merciful Knight to show me mercy. Turn your wrath towards the Merchant."
            elif cler['stat']:
                # Merchant dead
                end = "I beg you merciful Knight to show me mercy. Turn your wrath towards the Cleric."
            else:
                # Both dead
                end = "Merciful Knight, I beg you to lay down your arms and head to the Hall of Heroes where your bravery will live forever."

    if who == 'merchant':
        # Greeting
        if not merc['meet']:
            greeting = 'Are you a cunning knight looking to increase their fortune? I am but a common Merchant that needs your assistance.'
        elif merc['power']:
            # You have met, but have not fought
            greeting = 'Welcome back, wise Knight!'
        elif not merc['power']:
            # You have defeated the merchant and his allies (alive)
            if merc['allies']:
                greetings = 'Oh righteous and intelligent Knight!'
            else:
                # Kings allies are dead
                greetings = 'Oh powerful and intelligent Knight!'

        # Mid2
        if cler['stat']:
            # Cleric is alive
            if cler['fight']:
                # You are fighting the Cleric
                if cler['allies']:
                    # The Cleric's allies are alive
                    mid2 = 'I hear you and the Cleric are battling. You should have no trouble defeating her and her elementals. She never worried me, for my dragons are immune to elemental magic.'
                else:
                    # You have slayed the elementals but not Cleric
                    mid2 = 'I hear you have slayed the Cleric\'s elementals. They never bothered me, for my dragons could have easily defeated them. You should finish off the weak Cleric quickly.'
            else:
                # You are not fighting the Cleric
                if cler['power']:
                    # You have not fought against the Cleric yet
                    mid2 = 'There is a evil Cleric that controls elementals. The elementals allow her to control the harvest, which she keeps all for herself. He is of little bother to me, for my dragons can easily defeat her elementals.'
                else:
                    # You have defeated the Cleric but have spared him
                    if cler['allies']:
                        # You have spared the elementals
                        mid2 = 'I hear wonderful tales of your recent victory against the Cleric and her elementals dragons. It would be wise to return and slay her and her elementals.'
                    else:
                        mid2 = 'I hear wonderful tales of your recent victory against the Cleric and her elementals. I encourage you to send her to the same place you sent her elementals.'
        else:
            # Cleric is dead
            if cler['allies']:
                # You have spared the elementals
                mid2 = 'I hear wonderful tales of your recent victory against the Cleric and her elementals. Elementals must be destroyed to ensure a bountiful harvest next year. I encourage you to return and slay them.'
            
            else:
                # The Merchant and Dragons are dead
                mid2 = 'I see you have slayed the weak Cleric and her pathetic elementals. My dragons could have easily done this, but alas the task is no more.'

        # Mid1
        if king['stat']:
            # King is alive
            if king['fight']:
                # You are fighting the King
                if king['allies']:
                    # The King's allies are alive
                    mid1 = 'It is known that you and the King are battling. His strength can be difficult to overcome. Do not forget about his dishonorable soldiers. I fear the King, for soldiers would slay my dragons but the elementals cannot control my dragons.'
                else:
                    # You have slayed the elementals but not King
                    mid1 = 'I hear you have slayed the King\'s soldiers. Justice has been restored to the land. However, you must finish off the King! They remain dangerous as long as they have power.'
            else:
                # You are not fighting the King
                if king['power']:
                    # You have not fought against the King yet
                    mid1 = 'There is a wicked King that rules with fear along with his soldiers. The soldiers help the King maintain power through fear and intimidation. I fear the King, for soldiers would slay my dragons but the elementals cannot control my dragons.'
                else:
                    # You have defeated the King but have spared her
                    if king['allies']:
                        # You have spared the soldiers
                        mid1 = 'The people rejoice with news of your recent victory against the King and his soldiers. I encourage you to return and slay him and his soldiers before they regain power.'
                    else:
                        mid1 = 'The bards sing great overtures of your victory over the King.  Peace has been restored to the land and the people need not live in fear. However, I urge you to return to the King and finish him off before he regains power.'
        else:
            # King is dead
            if king['allies']:
                # You have spared the soldiers
                mid1 = 'Your name is shouted throughout the streets with news of your victory against the King and his soldiers. Eventually the soldiers will try to gain power. I encourage you to return and slay them.'
            
            else:
                # The Cleric and Elementals are dead
                mid1 = 'I see you have slayed the King and his soldiers. I guess they were not as difficult as I imagined.'
 
        if merc['power']:
            # You have not started fighting the king
            if king['stat'] and cler['stat']:
                # Merchant and Cleric both alive
                end = "Go forth wise Knight and slay the King and the Cleric."
            elif king['stat']:
                # Cleric dead
                end = "Go forth wise Knight and slay the King."
            elif cler['stat']:
                # Merchant dead
                end = "Go forth wise Knight and slay the Cleric."
            else:
                # Both dead
                end = "You are indeed cunning. You should lay down your arms and head to the Hall of Heroes."
        else:
            # You have defeated the king
            if king['stat'] and cler['stat']:
                # Merchant and Cleric both alive
                end = "I beg you heroic Knight to show me mercy. Turn your wrath towards the King and the Cleric."
            elif king['stat']:
                # Cleric dead
                end = "I beg you heroic Knight to show me mercy. Turn your wrath towards the King."
            elif cler['stat']:
                # Merchant dead
                end = "I beg you heroic Knight to show me mercy. Turn your wrath towards the Cleric."
            else:
                # Both dead
                end = "Heroic Knight, I beg you to lay down your arms and head to the Hall of Heroes where your bravery will live forever."

    if who == 'cleric':
        # Greeting
        if not cler['meet']:
            greeting = 'Are you a honorable and righteous knight? I am but a simple Cleric that needs your aid.'
        elif cler['power']:
            # You have met, but have not fought
            greeting = 'Welcome back, wise Knight!'
        elif not cler['power']:
            # You have defeated the merchant and her allies (alive)
            if cler['allies']:
                greetings = 'Oh merciful and divine Knight!'
            else:
                # Kings allies are dead
                greetings = 'Oh powerful and merciful Knight!'

        # Mid2
        if king['stat']:
            # King is alive
            if king['fight']:
                # You are fighting the King
                if king['allies']:
                    # The King's allies are alive
                    mid2 = 'I hear you and the King are battling. You should have no trouble defeating him and his soldiers. He never concerned me, for my elementals can use their magic on the soldiers.'
                else:
                    # You have slayed the soldiers but not King
                    mid2 = 'I hear you have slayed the King\'s soldiers. They never bothered me, for my elementals could have easily defeated them. You should finish off the powerless King quickly.'
            else:
                # You are not fighting the King
                if king['power']:
                    # You have not fought against the King yet
                    mid2 = 'There is a wretched King that rules with his soldiers. The soldiers allow him to use his power to punish unjustly the common person. However, He is of little bother to me, for my elementals can easily defeat his soldiers.'
                else:
                    # You have defeated the King but have spared him
                    if king['allies']:
                        # You have spared the soldiers
                        mid2 = 'I hear glorious news of your recent victory against the King and his soldiers. It\'s only right to return and slay him and his soldiers.'
                    else:
                        mid2 = 'I hear glorious news of your recent victory against the King and his soldiers. I encourage you complete your sacred journey and send him to the same plane as his soldiers.'
        else:
            # King is dead
            if king['allies']:
                # You have spared the elementals
                mid2 = 'The people sing in the streets with news of your recent triumphh over the King and his soldiers. However, the soldiers must be brought to justice for power corrupts. I encourage you to return and slay them.'
            
            else:
                # The Merchant and Dragons are dead
                mid2 = 'I see you have slayed the meager King and his weak soldiers. My elementals could have easily done this, but alas the task is no more.'

        # Mid1
        if merc['stat']:
            # Merchant is alive
            if merc['fight']:
                # You are fighting the Merchant
                if merc['allies']:
                    # The Merchant's allies are alive
                    mid1 = 'It is known that you and the Merchant are battling. His cunning and pose a challenge. Do not forget about his beastly dragons. I fear the Merchant, for dragons resist magic and would slay me and destroy my elementals.'
                else:
                    # You have slayed the elementals but not Merchant
                    mid1 = 'I hear you have slayed the Merchant\'s dragons. Tranquility has been restored to the land. However, you must finish off the Merchant! They remain dangerous as long as they have power.'
            else:
                # You are not fighting the Merchant
                if merc['power']:
                    # You have not fought against the Merchant yet
                    mid1 = 'There is a greedy Merchant that controls trade and money along with his dragons. The dragons help the Merchant maintain power by providing him immense riches. I fear the Merchant, for dragons resist magic and would slay me and destroy my elementals.'
                else:
                    # You have defeated the Merchant but have spared her
                    if merc['allies']:
                        # You have spared the soldiers
                        mid1 = 'The people sign high praises about your recent conquest over the Merchant and his dragons. I encourage you to return and slay him and his dragons before they regain power.'
                    else:
                        mid1 = 'Glory be to you, for great overtures are being told of your conquest over the Merchant.  Tranquility has been restored to the land and the people need not be controlled by greed. However, I urge you to return to the Merchant and strike him down before he regains power.'
        else:
            # Merchant is dead
            if merc['allies']:
                # You have spared the soldiers
                mid1 = 'Glorious ballads are sung throughout the streets with news of your victory against the Merchant and his dragons. However, the dragons are unholy beasts. I encourage you to return them to the depths where they came.'
            
            else:
                # The Merchant and Elementals are dead
                mid1 = 'I see you have slayed the Merchant and his dragons. I guess they were not as difficult as I imagined.'
 
        if cler['power']:
            # You have not started fighting the king
            if king['stat'] and merc['stat']:
                # Merchant and Cleric both alive
                end = "Go forth holy Knight and slay the Merchant and the King."
            elif king['stat']:
                # Cleric dead
                end = "Go forth holy Knight and slay the King."
            elif merc['stat']:
                # Merchant dead
                end = "Go forth holy Knight and slay the Merchant."
            else:
                # Both dead
                end = "You are indeed glorious. It is time that you lay down your arms and head to the Hall of Heroes."
        else:
            # You have defeated the king
            if king['stat'] and merc['stat']:
                # Merchant and King both alive
                end = "I beg you heroic Knight to show me mercy. Turn your wrath towards the Merchant and the King."
            elif king['stat']:
                # Merchant dead
                end = "I beg you heroic Knight to show me mercy. Turn your wrath towards the King."
            elif merc['stat']:
                # King dead
                end = "I beg you heroic Knight to show me mercy. Turn your wrath towards the Merchant."
            else:
                # Both dead
                end = "Divine Knight, the heavens beg for you to lay down your arms and head to the Hall of Heroes where your glory will live forever."

    if which == 'greeting':
        return greeting
    elif which == 'mid1':
        return mid1
    elif which == 'mid2':
        return mid2
    elif which == 'end':
        return end
    raise


