from .base_message import BaseMessage


class Lenkhilfe1(BaseMessage):
    """Lenkhilfe_1 message generator."""
    
    def generate(self):
        """Generate Lenkhilfe_1 message."""
        message = self.get_message('Lenkhilfe_1')
        data = message.encode({
            'Lastinformation': 0,
            'Fehlerstatus_Lastinformation': 0,
            'Fehlerlampe_Lenkhilfe': 0,
            'Frei_Lenkhilfe_1_2': 0,
            'Fehlerspeichereintrag__Lenkhilf': 1,
        })
        return self.generate_can_message(message.frame_id, data)
