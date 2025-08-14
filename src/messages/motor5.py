from .base_message import BaseMessage


class Motor5(BaseMessage):
    """Motor_5 message generator."""
    
    def generate(self):
        """Generate Motor_5 message."""
        message = self.get_message('Motor_5')
        data = message.encode({
            # 'Multiplex_Info_norm__Verbrauch': 0,
            'Multiplex_Info_Motortyp': 20,
            # 'Multiplex_Info_Drehzahl_MD_Max': 0,
            # 'Multiplex_Info_Max_Drehmoment': 0,
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
        return self.generate_can_message(message.frame_id, data)
