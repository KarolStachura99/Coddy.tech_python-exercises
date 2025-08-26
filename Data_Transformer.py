def transform_dataset(data):
    # Inicjalizujemy dwa puste słowniki do przechowywania wyników.
    # 'qualified_students' będzie przechowywał ID studenta i jego średnią ocen.
    # 'subject_summary' będzie zliczał, ilu kwalifikujących się studentów bierze dany przedmiot.
    qualified_students = {}
    subject_summary = {}
    
    # Rozpoczynamy główną pętlę, która przechodzi przez każdy rekord (słownik) w liście `data`.
    # Zmienna `student_data` będzie kolejno przyjmować dane każdego studenta.
    for student_data in data:
        
        # Używamy funkcji `all()` z wyrażeniem generatorowym, aby sprawdzić,
        # czy WSZYSTKIE oceny danego studenta są większe od 70.
        # Jeśli warunek jest spełniony, student jest "kwalifikujący się".
        if all(grade > 70 for grade in student_data['grades']):
            
            # --- Sekcja 1: Obliczanie i zapisywanie średniej ocen ---
            
            # Sumujemy wszystkie oceny i dzielimy przez ich liczbę, aby uzyskać średnią.
            # Używamy `round()` do zaokrąglenia wyniku do dwóch miejsc po przecinku.
            average_grade = sum(student_data['grades']) / len(student_data['grades'])
            
            # Bezpośrednio dodajemy parę klucz-wartość do słownika `qualified_students`.
            # Kluczem jest unikalne ID studenta, a wartością jego średnia ocena.
            # Nie używamy `.get()`, ponieważ klucz z ID studenta jest unikalny i dodajemy go po raz pierwszy.
            qualified_students[student_data['student_id']] = round(average_grade, 2)
            
            # --- Sekcja 2: Zliczanie przedmiotów ---
            
            # Rozpoczynamy wewnętrzną pętlę, która przechodzi przez każdy przedmiot
            # w liście `subjects` dla bieżącego, zakwalifikowanego studenta.
            for subject in student_data['subjects']:
                
                # Używamy metody `.get()` do bezpiecznego zliczania wystąpień przedmiotów.
                # `subject_summary.get(subject, 0)`:
                # - Jeśli przedmiot (`subject`) jest już w słowniku, pobiera jego bieżącą wartość.
                # - Jeśli to pierwszy raz, gdy widzimy ten przedmiot, domyślnie przyjmuje wartość 0.
                # Następnie dodajemy 1 do tej wartości, aby zaktualizować licznik.
                subject_summary[subject] = subject_summary.get(subject, 0) + 1
                
    # Po zakończeniu pętli głównej, funkcja zwraca słownik zawierający oba wyniki:
    # `qualified_students` i `subject_summary`.
    return {
        "qualified_students": qualified_students,
        "subject_summary": subject_summary
    }
