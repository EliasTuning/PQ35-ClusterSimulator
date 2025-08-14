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