
# Assignment 02 Submission: Git Workflow, CLI Automation, and Python Data Processing

## Project Overview
This project demonstrates integration of Git workflows, command-line interface (CLI) automation, and Python data processing. It consists of two main components:

1. **CLI Project Scaffold Script**  
   Automates the creation of a project structure, including directories, files, and sample data.

2. **Python Data Processing**  
   Reads CSV data, performs basic statistical analysis, and outputs results to a report file.

---

## Part 2: CLI Project Scaffold Script

**Objective**: Automate project setup using a shell script.

**Script**: `setup_project.sh`

**Functionality**:
- Creates directory structure:
```After running script, the following files and directories exist:
├── src/
│   ├── data_analysis.py
│   └── data_analysis_functions.py
├── data/
│   └── students.csv
├── output/
├── .gitignore
└── requirements.txt
```

## Features
- **Project Scaffold**: Automated project setup with `setup_project.sh`
- **Data Processing**: Python scripts for student grade analysis
- **Git Workflow**: Feature branch development and merging

## Usage
1. Run `./setup_project.sh` to create project structure
2. Execute `python src/data_analysis.py` for basic analysis
3. Run `python src/data_analysis_functions.py` for advanced analysis

## Git Workflow
| Branch | Purpose | Status |
|--------|---------|--------|
| main | Production code | Active |
| feature/project-scaffold | CLI automation | Merged |
| feature/data-processing | Python analysis | Merged |
```

## Git Workflow

**Objective**: Implement Python scripts that process data and output results to files.

Python Scripts Overview
data_analysis.py (Basic)
load_students(filename) – Reads CSV file into a list of student records
calculate_average_grade(students) – Calculates average grade
count_math_students(students) – Counts students in Math
generate_report() – Formats the report
save_report(report, filename) – Writes report to file
main() – Orchestrates the workflow


data_analysis_functions.py (Advanced)
load_data(filename) – Generic loader
load_csv(filename) – Reads CSV file
analyze_data(students) – Returns statistics dictionary
analyze_grade_distribution(grades) – Counts grades by ranges
save_results(results, filename) – Writes detailed report
main() – Runs the complete analysis



I'm not really sure how to writeup a markdown and what is expected. This is my best attempt! 

