score = raw_input("Enter Score: ")
try:
    score = float(score)
except:
    score = -1
if (score <= 1.0) and (score >= 0.0):   
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = 'Error'
print grade