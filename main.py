# This is a sample Python script.

# Press Alt+Umschalt+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class MessageGenerator:
	def __init__(self, dbc_path: str = 'vw_pq.dbc'):
		import cantools
		self._cantools = cantools
		self._db = cantools.database.load_file(dbc_path)

	def get_message(self, name: str):
		return self._db.get_message_by_name(name)

	def generate_Lenkhilfe1(self):
		return self.get_message('Lenkhilfe_1')

	def generate_BSGKombi(self):
		return self.get_message('BSG_Kombi')

	def generate_Motor5(self):
		return self.get_message('Motor_5')

	def generate_Motor1(self):
		return self.get_message('Motor_1')

	def generate_Bremse2(self):
		return self.get_message('Bremse_2')

	def generate_Bremse1(self):
		return self.get_message('Bremse_1')

	def generate_Airbag1(self):
		return self.get_message('Airbag_1')

	def generate_Getriebe2(self):
		return self.get_message('Getriebe_2')

	def generate_Motor2(self):
		return self.get_message('Motor_2')


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
		print(message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
