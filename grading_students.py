def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        elif grades[i] % 5 != 0:
            for j in range(grades[i],grades[i]+3):
                if j % 5 == 0 and j - grades[i] < 3:
                    grades[i] = j
                    break
    return grades
            
