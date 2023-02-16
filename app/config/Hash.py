from werkzeug.security import check_password_hash, generate_password_hash

class Hash:

    def __init__(self):
        pass

    def check_password_hash(self, password, hash):
        return check_password_hash(hash, password)

    def generate_password_hash(self, password):
        return generate_password_hash(password)