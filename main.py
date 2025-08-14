# This is a sample Python script.

# Press Alt+Umschalt+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def get_message(name:str):
    import cantools
    from pprint import pprint
    db = cantools.database.load_file('vw_pq.dbc')
    pprint(db.messages)
    message = db.get_message_by_name(name)
    print(message)
    return message


def generate_Lenkhilfe1():
    return get_message('Lenkhilfe_1')


def generate_BSGKombi():
    return get_message('BSG_Kombi')


def generate_Motor5():
    return get_message('Motor_5')


def generate_Motor1():
    return get_message('Motor_1')


def generate_Bremse2():
    return get_message('Bremse_2')


def generate_Bremse1():
    return get_message('Bremse_1')


def generate_Airbag1():
    return get_message('Airbag_1')


def generate_Getriebe2():
    return get_message('Getriebe_2')


def generate_Motor2():
    return get_message('Motor_2')

def generate_Lights():
    #0x531
    #LightsGHTS_ID
    pass

def main():





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
