from .base_message import BaseMessage


class Motor2(BaseMessage):
    """Motor_2 message generator."""
    
    def __init__(self,dbc_path: str):
        super().__init__(dbc_path)
        # Counter to ensure every message is sent 4 times
        self.message_counter = 0
        # Counter to cycle through different message types
        self.multiplex_counter = 0
    
    def generate(self):
        """Generate Motor_2 message with multiplexing logic."""
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
        }

        message_data.update({
            'Multiplex_Code_Motor_2': self.multiplex_counter,
        })
        # Add multiplex-specific fields based on counter
        print(self.multiplex_counter)
        if self.multiplex_counter == 0:
            message_data.update({
                'Multiplex_Info_CAN_Stand': 0,
            })
        elif self.multiplex_counter == 1:
            message_data.update({
                'Multiplex_Info_Motorcode__4_x_': 0,  # CANVERS value
            })
        elif self.multiplex_counter == 2:
            # CWGC_0_A[vkGeArt1] & 0x3f
            message_data.update({
                'Multiplex_Info_Getriebecode': 10,  # CWGC value
            })
        elif self.multiplex_counter == 3:
            message_data.update({
                'Multiplex_Info_Max_Moment__Norm': 0,  # FMOTC value
            })


        
        message = self.get_message('Motor_2')
        data = message.encode(message_data)
        return self.generate_can_message(message.frame_id, data)
