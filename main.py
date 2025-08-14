# This is a sample Python script.

# Press Alt+Umschalt+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+Umschalt+B to toggle the breakpoint.
    import cantools
    from pprint import pprint
    db = cantools.database.load_file('vw_pq.dbc')
    pprint(db.messages)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
