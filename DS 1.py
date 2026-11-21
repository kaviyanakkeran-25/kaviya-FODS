import numpy as np


student_scores = np.array([
    [85, 78, 92, 74],  
    [88, 82, 79, 85],  
    [90, 76, 88, 80],  
    [70, 85, 84, 90],  
] * 8)  


averages = np.mean(student_scores, axis=0)


subjects = ["Math", "Science", "English", "History"]
max_index = np.argmax(averages)


print("Average scores per subject:")
for subj, avg in zip(subjects, averages):
    print(f"{subj}: {avg:.2f}")

print("\nSubject with highest average:", subjects[max_index])
