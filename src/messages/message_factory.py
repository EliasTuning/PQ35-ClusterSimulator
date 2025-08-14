from .lenkhilfe1 import Lenkhilfe1
from .bsg_kombi import BSGKombi
from .motor5 import Motor5
from .motor1 import Motor1
from .bremse2 import Bremse2
from .bremse1 import Bremse1
from .airbag1 import Airbag1
from .getriebe2 import Getriebe2
from .motor2 import Motor2


class MessageFactory:
    """Factory class for creating message generators."""
    
    def __init__(self, dbc_path: str = 'vw_pq.dbc'):
        self.dbc_path = dbc_path
        self._message_instances = {}
    
    def get_message_instance(self, message_name: str):
        """Get or create a message instance for the given message name."""
        if message_name not in self._message_instances:
            self._message_instances[message_name] = self._create_message_instance(message_name)
        return self._message_instances[message_name]
    
    def _create_message_instance(self, message_name: str):
        """Create a new message instance based on the message name."""
        message_classes = {
            'Lenkhilfe_1': Lenkhilfe1,
            'BSG_Kombi': BSGKombi,
            'Motor_5': Motor5,
            'Motor_1': Motor1,
            'Bremse_2': Bremse2,
            'Bremse_1': Bremse1,
            'Airbag_1': Airbag1,
            'Getriebe_2': Getriebe2,
            'Motor_2': Motor2,
        }
        
        if message_name not in message_classes:
            raise ValueError(f"Unknown message name: {message_name}")
        
        return message_classes[message_name](self.dbc_path)

    def getMessages(self):
        """Return a dictionary mapping message names to their generate functions.
        This maintains compatibility with the old MessageGenerator interface."""
        message_names = [
            #"Lenkhilfe_1",
            # "BSG_Kombi",  # Commented out as in original
            "Motor_5",
            #"Motor_1",
            #"Bremse_2",
            #"Bremse_1",
            #"Airbag_1",
            #"Getriebe_2",
            #"Motor_2",
        ]

        generators = {}
        for name in message_names:
            instance = self.get_message_instance(name)
            generators[name] = instance.generate

        return generators
