# Opis: Ten plik służy do testowania klasy User z pliku user.py.
# Uruchamia różne przypadki testowe w zależności od danych wejściowych,
# aby zweryfikować poprawność działania weryfikacji i zmiany hasła.

# Import the User class from the user module
from user import User

# Get test case from input
test_case = input()

if test_case == "constructor_test":
    # Create a User object with initial password "secure123"
    user = User("secure123")
    print("User created successfully")
    print("Initial password set")

elif test_case == "correct_password_test":
    # Create a User object with initial password "secure123"
    user = User("secure123")
    # Test the check_password method with correct password
    # Print "Password check successful!" if it returns True
    # Print "Password check failed!" if it returns False
    result = user.check_password("secure123")
    if result:
        print("Password check successful!")
    else:
        print("Password check failed!")

elif test_case == "incorrect_password_test":
    # Create a User object with initial password "secure123"
    user = User("secure123")
    # Test the check_password method with incorrect password "wrong"
    # Print "Incorrect password rejected!" if it returns False
    # Print "Security issue: incorrect password accepted!" if it returns True
    result = user.check_password("wrong")
    if not result:
        print("Incorrect password rejected!")
    else:
        print("Security issue: incorrect password accepted!")

elif test_case == "change_password_test":
    # Create a User object with initial password "secure123"
    user = User("secure123")
    # Test changing password from "secure123" to "newpass456"
    # Print "Password changed successfully!" if it returns True
    # Print "Password change failed!" if it returns False
    result = user.change_password("secure123", "newpass456")
    if result:
        print("Password changed successfully!")
    else:
        print("Password change failed!")
    
    # Verify the new password works by checking "newpass456"
    # Print "New password works!" if it returns True
    # Print "New password doesn't work!" if it returns False
    if user.check_password("newpass456"):
        print("New password works!")
    else:
        print("New password doesn't work!")

elif test_case == "change_password_wrong_old_test":
    # Create a User object with initial password "secure123"
    user = User("secure123")
    # Try changing password with incorrect old password
    # Print "Security working: incorrect old password rejected!" if it returns False
    # Print "Security issue: password changed with wrong old password!" if it returns True
    result = user.change_password("wrong", "hackerpw")
    if not result:
        print("Security working: incorrect old password rejected!")
    else:
        print("Security issue: password changed with wrong old password!")

elif test_case == "comprehensive_test":
    # Create a User object with initial password "secure123"
    user = User("secure123")
    print("User created with initial password")
    
    # Test the check_password method with correct password
    if user.check_password("secure123"):
        print("Initial password verification successful")
    
    # Test the check_password method with incorrect password
    if not user.check_password("wrongpass"):
        print("Incorrect password properly rejected")
    
    # Test changing password from "secure123" to "newpass456"
    if user.change_password("secure123", "newpass456"):
        print("Password successfully changed")
    
    # Verify old password no longer works
    if not user.check_password("secure123"):
        print("Old password no longer works")
    
    # Verify the new password works
    if user.check_password("newpass456"):
        print("New password works correctly")
    
    # Try changing password with incorrect old password
    if not user.change_password("wrongold", "hackerpw"):
        print("Security maintained: wrong old password rejected")
    
    # Verify password is still secure after failed change attempt
    if user.check_password("newpass456"):
        print("Password remains secure after failed change attempt")

else:
    print("Unknown test case")
