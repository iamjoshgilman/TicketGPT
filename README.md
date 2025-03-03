# Closeout Generator

A small Python project designed to help teams close out work orders with better, more detailed notes. This application uses a Tkinter-based GUI and leverages the OpenAI API to generate professional closeout descriptions from a given work order input.

## Features

- **Automated Note Generation:** Generates detailed work order closeouts based on a priming prompt and user-provided input.
- **Graphical User Interface:** Simple and intuitive interface built with Tkinter and themed with ttkthemes.
- **Customization:** Easily update the priming prompt and OpenAI settings to match your company’s requirements.
- **Standalone Application:** Can be packaged as a standalone executable using PyInstaller.

## Prerequisites

- **Python 3.6+** (tested with Python 3.8+)
- **OpenAI Python Package:** For API communication.
- **Tkinter:** Standard Python GUI library.
- **ttkthemes:** For enhanced GUI themes.
- **PyInstaller:** (Optional) For creating a standalone executable.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/closeout-generator.git
   cd closeout-generator
   ```

2. **Install Required Packages:**

   Use pip to install the dependencies:
   
   ```bash
   pip install openai ttkthemes
   ```

   _Note:_ Tkinter is typically included with your Python installation. If it is not installed, refer to your operating system’s installation guidelines.

3. **Configure Your OpenAI API Key:**

   In the source code (`WOCloseout.py`), replace the placeholder in the following line with your actual OpenAI API key:

   ```python
   openai.api_key = 'sk-***'
   ```

## Usage

1. **Run the Application:**

   Execute the script to launch the GUI:

   ```bash
   python WOCloseout.py
   ```

2. **Input Work Order Description:**

   Enter your work order description or notes in the text box.

3. **Generate Closeouts:**

   Click the **Generate** button to receive generated closeout notes based on the provided input.

4. **Clear Fields:**

   Use the **Clear** button to reset the input and output fields.

## Packaging with PyInstaller

If you want to create a standalone executable, you can use PyInstaller. From the project directory, run:

```bash
pyinstaller --onefile --noconsole --icon="pngegg.png" WOCloseout.py
```

This will generate a single executable file in the `dist` directory that you can share with your team.

## Code Overview

- **resource_path(relative_path):** Ensures resource paths are correct when running the script directly or from a packaged executable.
- **generate_closeouts(work_order_description):** Combines a priming prompt with the provided work order description and calls the OpenAI API to generate closeout notes.
- **generate_and_display_closeouts():** Retrieves input, calls the note generation function, and displays the generated notes in the GUI.
- **clear_entries():** Clears both the input and output text areas.
- **GUI Setup:** Uses Tkinter and ttkthemes to set up a simple, dark-themed interface with responsive resizing.
