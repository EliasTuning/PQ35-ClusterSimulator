from .base_message import BaseMessage


class Bremse1(BaseMessage):
    """Bremse_1 message generator."""
    
    def generate(self):
        """Generate Bremse_1 message."""
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
        return self.generate_can_message(message.frame_id, data)
