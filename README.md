# Logo Converter

Converts a JPG or PNG to a 96x96 pixel round PNG logo file with a transparent background.

## Prerequisites

Before you can use this project, ensure you have Python installed on your system.

### Installing Python

If you don't already have Python installed, follow the steps below:

1. **Check if Python is installed**:

   ```bash
   python3 --version
   ```

   If you see a version number (e.g., `Python 3.x.x`), Python is already installed.

2. **Installing Python on macOS/Linux**:

   - Open a terminal and install Python using a package manager:

     ```bash
     # For macOS
     brew install python

     # For Ubuntu/Linux
     sudo apt-get update
     sudo apt-get install python3
     ```

## Install

Follow these steps to set up the virtual environment and install the necessary dependencies:

```bash
python3 -m venv venv          # Create a virtual environment
source venv/bin/activate      # Activate the virtual environment
pip3 install -r requirements.txt  # Install required Python packages
python3 logo_convert.py       # Run the logo converter script
```

## Usage

After running the `logo_convert.py` script, it will process all `.jpg` and `.png` files in the current directory and convert them to 96x96 pixel round PNG logos with a transparent background. The output files will have `_circular` appended to their filenames.
