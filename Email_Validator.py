def clean_email_list(emails):
    # 1. Usuwanie białych znaków (spacji, tabulacji itp.) z początku i końca oraz zamiana na małe litery
    cleaned_emails = map(lambda x: x.strip().lower(), emails)
    
    # 2. Funkcja sprawdzająca poprawność pojedynczego adresu email
    def is_valid_email(email):
        # Sprawdzenie, czy email zawiera dokładnie jeden znak '@'
        if email.count('@') != 1:
            return False
        
        # Podział adresu na część przed '@' (local) i po '@' (domain)
        local, domain = email.split('@')
        
        # Sprawdzenie, czy:
        # - część przed '@' (local) nie jest pusta,
        # - część po '@' (domain) nie jest pusta,
        # - w całym adresie nie ma spacji
        if not local or not domain or ' ' in email:
            return False
        
        # Jeśli wszystkie warunki są spełnione, email jest uznawany za poprawny
        return True
    
    # 3. Filtrowanie adresów – pozostawiamy tylko te, które spełniają warunki is_valid_email
    valid_emails = filter(is_valid_email, cleaned_emails)
    
    # 4. Zwracanie listy poprawnych adresów (map i filter zwracają obiekty iteratorów, więc konwertujemy na listę)
    return list(valid_emails)
