from .base_message import BaseMessage


class BSGKombi(BaseMessage):
    """BSG_Kombi message generator."""
    
    def generate(self):
        """Generate BSG_Kombi message."""
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
        return self.generate_can_message(message.frame_id, data)
