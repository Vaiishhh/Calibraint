def get_grade(s1, s2, s3):
    avg_score = (s1 + s2 + s3) / 3
    if 90 <= avg_score <= 100:
        return 'A'
    elif 80 <= avg_score < 90:
        return 'B'
    elif 70 <= avg_score < 80:
        return 'C'
    elif 60 <= avg_score < 70:
        return 'D'
    else:
        return 'F'


s1 = 85
s2 =  92
s3 = 78
grade = get_grade(s1,s2,s3)
print(f"The average grade for scores {s1}, {s2}, {s3} is {grade}")