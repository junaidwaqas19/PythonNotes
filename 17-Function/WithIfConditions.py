def calculate_letter_grade(grade):
    if grade >=90:
        return 'A'
    elif grade <=80:
        return 'B'
    elif grade >=70:
       return 'C'
    else:
        return 'F'
    
print(calculate_letter_grade(75))