# Menedżer haseł

Ten projekt zawiera prostą klasę w języku Python do zarządzania hasłami użytkowników. Głównym celem jest zademonstrowanie podstawowych zasad **programowania obiektowego**, takich jak hermetyzacja (użycie prywatnego atrybutu `__password`) oraz modularność (podział kodu na dwa oddzielne pliki).

### Struktura projektu

* `user.py`: Definiuje klasę `User` z metodami do sprawdzania i zmiany hasła. Hasło jest przechowywane jako atrybut prywatny, co zwiększa bezpieczeństwo.
* `driver.py`: Plik testowy, który tworzy instancję klasy `User` i uruchamia różne przypadki testowe w celu weryfikacji poprawności działania wszystkich metod.

### Jak uruchomić

Aby uruchomić program, przejdź do folderu `password_manager` w terminalu i wykonaj następujące polecenie:

python driver.py


Następnie, w konsoli wpisz nazwę przypadku testowego, który chcesz uruchomić, i naciśnij `Enter`.

### Dostępne przypadki testowe

* `constructor_test`
* `correct_password_test`
* `incorrect_password_test`
* `change_password_test`
* `change_password_wrong_old_test`
* `comprehensive_test`
