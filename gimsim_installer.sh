# Update pip
python -m pip install --upgrade pip

# Install PyInstaller
python -m pip install PyInstaller

# Generate executable file
pyinstaller --noconsole --onefile gimsim.py