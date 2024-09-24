class Function():
    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __str__(self):
        return f"Function(name='{self.name}', body='{self.body}'"
