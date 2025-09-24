#!/bin/bash

# Simple data processing script

echo "Setting up project, make directories"
mkdir -p src data output 

echo "create files using \"here-documents\""
# Create files using "here-documents"

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

chmod +x setup_project.sh