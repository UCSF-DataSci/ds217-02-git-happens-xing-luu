#!/bin/bash

chmod +x setup_project.sh

# Simple data processing script

# make the directories 
mkdir -p src data output 
echo "Created directories: src, data, output"

# make the files .gitignore, requirements.txt
touch .gitignore requirements.txt 
echo "Created files: .gitignore, requirements.txt"

# Create files using "here-documents", EOF starts a here document

cat > data/students.csv << 'EOF'
name,age,grade, subject 
1. Alice,20,5, science
2. Bob,19,6, math 
3. Charlie, 20, 4, history
4. Jamie, 21, 5, science
5. James, 22, 6, math
6. Henry, 23, 4, history
7. Yvonne, 21, 5, science
8. ulrich, 22, 6, math
EOF

cat data/students.csv

echo "Created data file: data/students.csv"

#Make the data_analysis.py file
cat > src/data_analysis.py << 'EOF'
# TODO: Analysis of data
EOF

#Make the data_analysis_functions.py file
cat > src/data_analysis_functions.py << 'EOF'
# TODO: Data analysis functions
EOF

echo "Project scaffold created successfully."