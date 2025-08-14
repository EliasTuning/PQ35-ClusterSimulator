from .base_message import BaseMessage


class Bremse2(BaseMessage):
    """Bremse_2 message generator."""
    
    def generate(self):
        """Generate Bremse_2 message."""
        message = self.get_message('Bremse_2')
        data = message.encode({
            # 'Timer': 0,
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
        return self.generate_can_message(message.frame_id, data)
