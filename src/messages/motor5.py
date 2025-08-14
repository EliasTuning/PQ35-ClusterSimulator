from .base_message import BaseMessage


class Motor5(BaseMessage):
    """Motor_5 message generator."""
    
    def __init__(self, dbc_path: str):
        super().__init__(dbc_path)
        # Counter to ensure every message is sent 4 times
        self.message_counter = 0
        # Counter to cycle through different message types
        self.multiplex_counter = 0
    
    def generate(self):
        """Generate Motor_5 message with multiplexing logic."""
        # Increment message counter
        self.message_counter += 1
        
        # Check if we need to change the multiplex type
        if self.message_counter > 3:
            self.message_counter = 0
            self.multiplex_counter += 1
            
            # Reset multiplex counter if it exceeds 3
            if self.multiplex_counter > 3:
                self.multiplex_counter = 0
        
        # Start with base message data
        message_data = {
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
        }

        message_data.update({
            'Multiplex_Code': self.multiplex_counter,
        })
        
        # Add multiplex-specific fields based on counter
        print(self.multiplex_counter)
        if self.multiplex_counter == 0:
            message_data.update({
                'Multiplex_Info_Max_Drehmoment': 0,  # m0 - Max torque
            })
        elif self.multiplex_counter == 1:
            message_data.update({
                'Multiplex_Info_Drehzahl_MD_Max': 0,  # m1 - Max engine speed
            })
        elif self.multiplex_counter == 2:
            message_data.update({
                'Multiplex_Info_Motortyp': 20,  # m2 - Engine type
            })
        elif self.multiplex_counter == 3:
            message_data.update({
                'Multiplex_Info_norm__Verbrauch': 0,  # m3 - Normalized consumption
            })

        message = self.get_message('Motor_5')
        data = message.encode(message_data)
        return self.generate_can_message(message.frame_id, data)
