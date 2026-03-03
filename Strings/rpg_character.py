
full_dot = '●'
empty_dot = '○'

def create_character(char_name, strength, intelligence, charisma):
    if(not isinstance(char_name, str)):
        return 'The character name should be a string'
    elif(char_name == ''):
        return 'The character should have a name'
    elif(len(char_name) > 10):
        return 'The character name is too long'
    elif(' ' in char_name):
        return 'The character name should not contain spaces'

    if(not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int)):
        return 'All stats should be integers'
    elif(strength < 1 or intelligence < 1 or charisma < 1):
        return 'All stats should be no less than 1'
    elif(strength > 4 or intelligence > 4 or charisma > 4):
        return 'All stats should be no more than 4'
    elif(strength + intelligence + charisma != 7):
        return 'The character should start with 7 points'
    
    rpg_char = char_name + '\n'
    
    str_value = 'STR '
    for i in range(0, 10):
        if(i < strength):
            str_value += full_dot
        else:
            str_value += empty_dot

    int_value = 'INT '
    for i in range(0, 10):
        if(i < intelligence):
            int_value += full_dot
        else:
            int_value += empty_dot
    
    cha_value = 'CHA '
    for i in range(0, 10):
        if(i < charisma):
            cha_value += full_dot
        else:
            cha_value += empty_dot

    return rpg_char + str_value + '\n' + int_value + '\n' + cha_value

print(create_character('ren g', 5, 2, 1))