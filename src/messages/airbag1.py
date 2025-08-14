from .base_message import BaseMessage


class Airbag1(BaseMessage):
    """Airbag_1 message generator."""
    
    def generate(self):
        """Generate Airbag_1 message."""
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
        return self.generate_can_message(message.frame_id, data)
