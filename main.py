from random import randint 

def hit_roll( amount:int=1, dice_type:int=4, bonus:int=0) -> dict:
    # Function for rolling a specified number of dice with a given type and bonus.
    # Function returns dict with number of roll with value and sum of all roles with the key "SUM"
    result = dict()
    temp_sum = 0
    for rolling in range(1, amount + 1):
        temp_roll = randint( 1, dice_type) 
        result[rolling] = temp_roll
        temp_sum = temp_sum + temp_roll + bonus
    result["SUM"]  = temp_sum
    return result

def d20_roll(adv_modificator:str="no") -> dict:
    # Function for rolling a 20-sided die with optional advantage or disadvantage.
    if adv_modificator == "no":
        return randint( 1, 20)        
    elif adv_modificator == "adv":        
        return max(randint( 1, 20), randint( 1, 20))
    else:        
        return min(randint( 1, 20), randint( 1, 20))
    


hit_dice = input(f'You rolled a {d20_roll()}, type hit dice: ')
print(hit_roll(2, int(hit_dice)))
