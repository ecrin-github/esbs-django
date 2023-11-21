class CreateUserDto:
    email: str
    sub: str
    name: str
    family_name: str

    def __init__(self, sub, name, family_name, email):
        self.email = email
        self.name = name
        self.sub = sub
        self.family_name = family_name
