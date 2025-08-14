class MessageGenerator:
	def __init__(self, dbc_path: str = 'vw_pq.dbc'):
		import cantools
		self._cantools = cantools
		self._db = cantools.database.load_file(dbc_path)

	def get_message(self, name: str):
		return self._db.get_message_by_name(name)

	def generate_Lenkhilfe1(self):
		message = self.get_message('Lenkhilfe_1')
		data = message.encode({
			'Lastinformation': 0,
			'Fehlerstatus_Lastinformation': 0,
			'Fehlerlampe_Lenkhilfe': 0,
			'Frei_Lenkhilfe_1_2': 0,
			'Fehlerspeichereintrag__Lenkhilf': 1,
		})
		return message

	def generate_BSGKombi(self):
		message = self.get_message('BSG_Kombi')
		data = message.encode({
			'Blinker_links_Kontrollampe': 0,
			'Blinker_rechts_Kontrollampe': 0,
			'Anhaenger_Kontrollampe': 0,
			'Warnblink_Mode': 0,
			'DWA_Akku': 0,
			'Rueckfahrlicht': 0,
			'Frei_BSG_Kombi_1_1': 0,
			'Lade_Kontrollampe': 0,
			'Fahrertuer_geoeffnet': 0,
			'Beifahrertuer_geoeffnet': 0,
			'Tuer_hinten_links_geoeffnet': 0,
			'Tuer_hinten_rechts_geoeffnet': 0,
			'Motorhaube_geoeffnet': 0,
			'Heckdeckel_geoeffnet': 0,
			'Frei_BSG_Kombi_1_2': 0,
			'Unterspannung': 1,
			'Klemme_58d__BSG_Kombi_': 0,
			'Fehlerstatus_Kl__58d': 0,
			'Klemme_58s__BSG_Kombi_': 0,
			'Fehlerstatus_Kl__58s': 0,
			'Fehlerlampe_Lenkhilfe__BSG_Komb': 0,
			'Fehlerlampe_Lenkhilfe_veraltet': 0,
			'Ruecksitzlehne_HL_verr__4_1': 0,
			'Ruecksitzlehne_HR_verr__4_1': 0,
			'Frei_BSG_Kombi_1_3': 0,
		})
		return message

	def generate_Motor5(self):
		message = self.get_message('Motor_5')
		data = message.encode({
			'Multiplex_Info_norm__Verbrauch': 0,
			'Multiplex_Info_Motortyp': 20,
			'Multiplex_Info_Drehzahl_MD_Max': 0,
			'Multiplex_Info_Max_Drehmoment': 0,
			'Multiplex_Code': 2,
			'Ladekontroll_Lampe': 0,
			'Vorgluehlampe__Motor_5_': 0,
			'E_Gas_Lampe': 0,
			'OBD_2_Lampe': 0,
			'CAT_Warnung': 0,
			'Klimakompressor_aus__Motor_5_': 0,
			'Kennfeldkuehlung': 0,
			'Klimakompressor_Leistungsreduzi': 0,
			'Kraftstoffverbrauchssignal': 24909,
			'Verbrauch_Ueberlauf': 1,
			'K_hlerluefteransteuerung': 9.600000000000001,
			'Klimadrucksignal__Motor_5_': 0.0,
			'Anlasser_Freigabe': 0,
			'Anlasser_Ausspuren': 1,
			'GRA_Hauptschalter': 1,
			'Doppelte_Momente': 0,
			'Motortext_Bits__4_1_': 0,
			'CHECKSUM': 38,
		})
		return message

	def generate_Motor1(self):
		message = self.get_message('Motor_1')
		data = message.encode({
			'Leergasinformation': 1,
			'Fahrpedalwert_ungenau__Motor_1_': 0,
			'Kickdownschalter': 0,
			'Kupplungsschalter': 1,
			'Time_Out_Bremsen_Botschaft': 0,
			'Fehlerstatus_Brems_Momenteneing': 0,
			'Fehlerstatus_Getriebe_Momentene': 1,
			'Momentenangaben_ungenau': 0,
			'inneres_Motor_Moment': 5.46,
			'Motordrehzahl': 0.0,
			'inneres_Motor_Moment_ohne_exter': 5.46,
			'Fahrpedalwert_oder_Drosselklapp': 0.0,
			'mechanisches_Motor_Verlustmomen': 10.530000000000001,
			'Fahrerwunschmoment': 5.46,
		})
		return message

	def generate_Bremse2(self):
		message = self.get_message('Bremse_2')
		data = message.encode({
			'Timer': 0,
			'Querbeschleunigung': 0.010000000000000009,
			'Querbeschl__TimerTic': 0,
			'mittlere_Raddrehzahl__Bremse_2': 0.0,
			'Zeitstempel': 0,
			'Wegimpulse_Vorderachse': 0,
			'Wegimpulszaehlerstatus': 0,
			'Fehlerspeichereintrag_Bremse': 0,
			'Warnlampe_DDS': 0,
			'Frei_Bremse_2_5': 0,
			'Fehlerstatus_Wegimpulse_4_1': 0,
			'Impulszahl': 45,
			'Frei_Bremse_2_2': 0,
			'gemessene_Querbeschleunigung': 1,
		})
		return message

	def generate_Bremse1(self):
		message = self.get_message('Bremse_1')
		data = message.encode({
			'ASR_Anforderung': 0,
			'MSR_Anforderung': 0,
			'ABS_Bremsung__4_1_': 0,
			'EDS_Eingriff': 0,
			'ESP_Eingriff': 0,
			'ASR_Schaltbeeinflussung': 0,
			'EBV_Eingriff': 0,
			'Lampe_ABS': 0,
			'Lampe_ASR___ESP': 0,
			'Bremskontroll_Lampe': 0,
			'Fahrer_bremst__Bremse_1___4_1_': 0,
			'Schlechtwegausblendung': 0,
			'Fehlerstatus_Schlechtwegausblen': 1,
			'ABS_in_Diagnose': 0,
			'Aktiver_Bremskraftverstaerker': 0,
			'Geschwindigkeit_neu__Bremse_1_': 0.0,
			'ASR_Eingriffsmoment_langsam': 99.06,
			'ASR_Eingriffsmoment_schnell': 99.06,
			'MSR_Eingriffsmoment': 0.0,
			'COUNTER': 0,
			'ASR_Steuerger_t': 0,
			'ESP_Passiv_getastet': 0,
			'ESP_Systemstatus_4_1': 0,
			'Geschwindigkeitsersatzwert': 0,
		})
		return message

	def generate_Airbag1(self):
		message = self.get_message('Airbag_1')
		data = message.encode({
			'Front_Crash': 0,
			'Heck_Crash': 0,
			'Seiten_Crash_Fahrer': 0,
			'Seiten_Crash_Beifahrer': 0,
			'Rollover': 0,
			'Crash_Intensitaet': 0,
			'Airbag_Lampe': 0,
			'Airbag_deaktiviert': 0,
			'Kindersitzerkennung': 0,
			'Airbag_Systemfehler': 0,
			'Gurtschalter_Fahrer': 0,
			'Gurtwarnung_Fahrer': 0,
			'Gurtschalter_Beifahrer': 0,
			'Gurtwarnung_Beifahrer': 1,
			'Airbag_in_Diagnose': 0,
			'Airbag_im_Stellgliedtest': 0,
			'Frei_Airbag_1_2': 0,
			'Fehlerspeichereintrag': 0,
			'COUNTER': 0,
			'CHECKSUM': 0,
		})
		return message

	def generate_Getriebe2(self):
		message = self.get_message('Getriebe_2')
		data = message.encode({
			'LFR_Adaption_Freigabeflag': 0,
			'Schubabschaltunterstuetzung': 0,
			'Ecomatic__4_1_': 0,
			'Zwischengasflag': 0,
			'Zahler_Getriebe_2': 9,
			'Leerlaufsolldrehzahl__Getriebe': 0,
			'Gradientenbegrenzung': 2550,
			'Synchronisations_Wunschdrehzahl': 0,
			'invertierte_Synchronisations_Wu': 6375,
			'Synchronisationszeit': 0,
			'Hochschaltlampe': 0,
			'Starter_wird_angesteuert': 1,
			'Gong': 0,
			'Unterdrueckung_von_Warnungen': 0,
			'Shift_Lock_Lampe': 0,
			'ECO_Anzeige__4_1_': 0,
			'Anforderung_Kriechadaption': 0,
			'Fehlerlampe_f_r_Kupplung_bei_VL': 0,
			'Ganganzeige_Kombi___Getriebe_Va': 0,
			'eingelegte_Fahrstufe': 0,
		})
		return message

	def generate_Motor2(self):
		message = self.get_message('Motor_2')
		data = message.encode({
			'Multiplex_Info_Motorcode__4_x_': 0,
			'Multiplex_Info_Getriebecode': 10,
			'Multiplex_Info_Max_Moment__Norm': 0,
			'Multiplex_Info_CAN_Stand': 0,
			'Multiplex_Code_Motor_2': 2,
			'Kuehlmitteltemperatur__Motor_2_': 87.0,
			'Bremslichtschalter': 0,
			'Bremstestschalter': 0,
			'Fehlerstatus_Kuhlmitteltempera': 0,
			'Ansteuerung_Klima__4_1_': 0,
			'Status_Normalbetrieb': 1,
			'OBD_2_freeze_frame': 1,
			'GRA_Status': 0,
			'Fahrzeuggeschwindigkeit': 0.0,
			'Soll_Geschwindigkeit_bei_GRA_Be': 103.68,
			'Leerlaufsolldrehzahl__Motor_2_': 700,
			'Begrenzungsmoment': 60.45,
			'Minimales_Motormoment_bei_Zuend': 3.5100000000000002,
		})
		return message