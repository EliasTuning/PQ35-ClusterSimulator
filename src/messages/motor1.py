from .base_message import BaseMessage


class Motor1(BaseMessage):
    """Motor_1 message generator."""
    
    def generate(self):
        """Generate Motor_1 message."""
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
        return self.generate_can_message(message.frame_id, data)
