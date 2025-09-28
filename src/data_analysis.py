#TODO: Analysis of data

import os 
import csv 

# Load student data from a CSV file
def load_students(filename):
    """Read CSV and return list of student data"""
    students = []
    with open(filename, 'r') as f:
        lines = f.readlines()[1:]  # skip header
        for line in lines:
            name, age, grade, subject = line.strip().split(',')
            students.append({
                'name': name,
                'age': int(age),
                'grade': int(grade),
                'subject': subject
            })
    return students

#calculate the average grades of students 
def calculate_average_grade(students):
    grades = [s['grade'] for s in students]    
    return sum(grades) / len(grades)

#count students in math subject 
def count_math_students(students):
    count = 0
    for student in students:
        # Make sure 'subject' exists and normalize case/strip spaces
        if 'subject' in student and student['subject'].strip().lower() == 'math':
            count += 1
    return count

#generate report
def generate_report(students):
    total_students = len(students)
    avg_grade = calculate_average_grade(students)
    math_count = count_math_students(students)

    report = (
        f"Total Students: {total_students}\n"
        f"Average Grade: {avg_grade:.1f}\n"
        f"Number of Math Students: {math_count}\n"
    )
    return report

def save_report(report, filename):
    # Make sure output directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(report)

def main():
    students = load_students('data/students.csv')

    if not students:
        print("No student data to analyze")
        return
    
    report = generate_report(students)
    save_report(report, 'output/analysis_report.txt')
    print("Basic analysis complete. Report saved to output/analysis_report.txt")

if __name__ == "__main__":
    main()