from .base_message import BaseMessage


class Motor2(BaseMessage):
    """Motor_2 message generator."""
    
    def generate(self):
        """Generate Motor_2 message."""
        message = self.get_message('Motor_2')
        data = message.encode({
            # 'Multiplex_Info_Motorcode__4_x_': 0,
            'Multiplex_Info_Getriebecode': 10,
            # 'Multiplex_Info_Max_Moment__Norm': 0,
            # 'Multiplex_Info_CAN_Stand': 0,
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
        return self.generate_can_message(message.frame_id, data)
