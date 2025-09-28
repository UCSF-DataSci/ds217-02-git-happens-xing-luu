

import os 
import csv
import sys

def load_data(filename):
    """Generic loader that checks file extension."""
    if filename.lower().endswith(".csv"):
        return load_csv(filename)
    else:
        raise ValueError

def load_csv(csv_file):
    students = []
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            # normalize headers
            reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]

            for row in reader:
                # get values safely and strip spaces
                students.append({
                    'name': row.get('name', '').strip(),
                    'age': int(row.get('age', 0)),
                    'grade': int(row.get('grade', 0)),
                    'subject': row.get('subject', '').strip().lower()
                })

    except FileNotFoundError:
        print(f"Error: File {csv_file} not found")
    except Exception as e:
        print(f"Error loading data: {e}")

    return students


def analyze_data(students):
    """Return a dictionary with multiple statistics."""
    if not students:
        return {}

    grades = [s["grade"] for s in students]
    subjects = [s["subject"].lower() for s in students]

    analysis = {
        "total_students": len(students),
        "average_grade": sum(grades) / len(grades),
        "highest_grade": max(grades),
        "lowest_grade": min(grades),
        "subject_counts": {},
        "grade_distribution": analyze_grade_distribution(grades)
    }

    # Count students by subject
    for subj in subjects:
        analysis["subject_counts"][subj] = analysis["subject_counts"].get(subj, 0) + 1

    return analysis

#Analyze grade distribution

def analyze_grade_distribution(grades):
    """Analyze the distribution of grades."""
    if not grades:
        return {}

    # Count grades by ranges
    distribution = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }

    for grade in grades:
        if grade >= 90:
            distribution['A (90-100)'] += 1
        elif grade >= 80:
            distribution['B (80-89)'] += 1
        elif grade >= 70:
            distribution['C (70-79)'] += 1
        elif grade >= 60:
            distribution['D (60-69)'] += 1
        else:
            distribution['F (0-59)'] += 1

    return distribution


# Save basic results using imported function
def save_results(results, filename):
    """Save detailed analysis results to a file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(f"Total Students: {results.get('total_students',0)}\n")
        f.write(f"Average Grade: {results.get('average_grade',0):.1f}\n")
        f.write(f"Highest Grade: {results.get('highest_grade',0)}\n")
        f.write(f"Lowest Grade: {results.get('lowest_grade',0)}\n\n")

        f.write("Students by Subject:\n")
        for subj, count in results.get("subject_counts", {}).items():
            f.write(f"  {subj.title()}: {count}\n")
        f.write("\nGrade Distribution:\n")

        dist = results.get("grade_distribution", {})
        total_students = results.get("total_students", 0)
        for grade_range, count in dist.items():
            percent = (count / total_students * 100) if total_students > 0 else 0
            f.write(f"  {grade_range}: {count} ({percent:.1f}%)\n")

# --- Main function ---
def main():
    if len(sys.argv) < 2:
        print("Usage: python src/data_analysis_functions.py students.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "output/module_analysis.txt"

    students = load_data(input_file)
    results = analyze_data(students)
    save_results(results, output_file)

    print("Analysis complete. Report saved to", output_file)

# Run main if script executed directly
if __name__ == "__main__":
    main()