# Opis: Ten plik definiuje klasę User,
# która zarządza hasłem użytkownika w bezpieczny sposób,
# używając prywatnego atrybutu (__).
# Klasa pozwala na weryfikację i zmianę hasła.

class User:
    def __init__(self, password):
        # Store the password as a private attribute using double underscore (__)
        # This makes it harder to access from outside the class
        self.__password = password
    
    def check_password(self, input_password):
        # Return True if input_password matches the stored private password
        # Return False otherwise
        return self.__password == input_password
    
    def change_password(self, old_password, new_password):
        # Check if old_password is correct using the check_password method
        if self.check_password(old_password):
            # If old_password is correct, update the private password to new_password and return True
            self.__password = new_password
            return True
        # If old_password is incorrect, return False without changing the password
        return False
