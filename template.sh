# Script to automatically create project directories and files
mkdir -p src
mkdir -p research
mkdir -p static
mkdir -p templates

# Files
touch src/__init__.py
touch src/helper.py
touch src/prompt.py
touch .env
touch setup.py
touch app.py
touch research/trials.ipynb
touch requirements.txt
touch static/style.css
touch templates/chat.html
touch store_index.py

echo "Project directories and files created successfully!"