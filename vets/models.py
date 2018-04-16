class Gravesite:
    name: str = ''
    address: str = ''
    state: str = ''
    contact: str = ''
    burial_space: str = ''

    def __init__(self, name: str, address: str, state: str, contact: str, burial_space: str):
        self.name = name
        self.address = address
        self.state = state
        self.contact = contact
        self.burial_space = burial_space
