# This is a sample Python script.

# Press Alt+Umschalt+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pprint import pprint

from src.message_generator import MessageGenerator



def main():
	generator = MessageGenerator()
	generators = [
		generator.generate_Lenkhilfe1,
		generator.generate_BSGKombi,
		generator.generate_Motor5,
		generator.generate_Motor1,
		generator.generate_Bremse2,
		generator.generate_Bremse1,
		generator.generate_Airbag1,
		generator.generate_Getriebe2,
		generator.generate_Motor2,
	]
	for create_message in generators:
		message = create_message()
		print(message.name,message.signals)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
