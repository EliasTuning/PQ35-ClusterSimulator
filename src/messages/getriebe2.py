from .base_message import BaseMessage


class Getriebe2(BaseMessage):
    """Getriebe_2 message generator."""
    
    def generate(self):
        """Generate Getriebe_2 message."""
        message = self.get_message('Getriebe_2')
        data = message.encode({
            'LFR_Adaption_Freigabeflag': 0,
            'Schubabschaltunterstuetzung': 0,
            'Ecomatic__4_1_': 0,
            'Zwischengasflag': 0,
            'Zahler_Getriebe_2': 9,
            'Leerlaufsolldrehzahl__Getriebe': 0,
            'Gradientenbegrenzung': 2540,
            'Synchronisations_Wunschdrehzahl': 0,
            'invertierte_Synchronisations_Wu': 6350,
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
        return self.generate_can_message(message.frame_id, data)
