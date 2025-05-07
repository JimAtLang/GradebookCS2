def average_grade(gradelist, index):
    headers = gradelist[0]
    row = gradelist[index]
    numerator = 0
    denominator = 0
    name = row[0]
    for i,grade in enumerate(row):
        if i == 0:
            continue
        assignment_name = headers[i]
        if "HW" in assignment_name:
            numerator += grade
            denominator += 1
        elif "Project" in assignment_name:
            numerator += 3*grade
            denominator += 3
        elif "Quiz" in assignment_name:
            numerator += 2*grade
            denominator += 2
        elif "Test" in assignment_name:
            numerator += 4*grade
            denominator += 4
        elif "Final" in assignment_name:
            numerator += 6*grade
            denominator += 6
    grade = numerator/denominator
    return (name, grade)
