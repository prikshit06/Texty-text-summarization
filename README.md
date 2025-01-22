# Texty: Summarization Tool

## Overview
**Texty** is a desktop application for text summarization. Built with **Python** and **Tkinter**, this tool leverages **Hugging Face's BART-Large-CNN model** to generate concise summaries of user-provided text. Users can specify the desired summary length, visualize word counts, and copy the summarized text with ease.

---

## Features
- **Customizable Summary Length**: Users can set a preferred summary length (20-70 words).
- **Word Count Tracking**: Displays initial and final word counts for better text analysis.
- **Text Copying**: One-click functionality to copy the summary to the clipboard.
- **Interactive GUI**: User-friendly interface for easy text input and summary generation.

---

## How It Works
1. The user inputs text to be summarized in the text box.
2. Select the desired summary length using the slider.
3. Click the **"Summarize"** button to generate the summary.
4. View the summary in the output box, along with the word count.
5. Copy the summary text using the **"Copy Text"** button.

---

## Installation
### Prerequisites
- Python 3.7+
- Internet connection (to access the Hugging Face API)

### Clone the Repository
```bash
git clone https://github.com/yourusername/Texty.git
cd Texty
```

### Install Required Libraries
```bash
pip install requests pyperclip
```

---

## Usage
Run the following command to start the application:
```bash
python texty.py
```

---

## API Integration
The app uses the **Hugging Face Inference API** with the BART-Large-CNN model for summarization. The API requires an authentication token, which can be obtained by creating an account on Hugging Face and generating an API token.

### Setting Up the API Token
Replace the placeholder in the script with your Hugging Face API token:
```python
headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
```

---

## Screenshots
1. **Input Text:**
   ![Input](path/to/input_screenshot.png)
2. **Generated Summary:**
   ![Summary](path/to/summary_screenshot.png)

---

## Roadmap
- Add support for additional summarization models.
- Enable offline summarization using pre-trained models.
- Implement advanced text cleaning options.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **Hugging Face**: For providing the BART-Large-CNN model and inference API.
- **Tkinter**: For the graphical user interface.

---

## Author
- Your Name - [GitHub Profile](https://github.com/yourusername)

---

