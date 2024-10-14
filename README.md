# English to Welsh Language Translation App

This repository contains a **Streamlit** web application that performs language translation from **English to Welsh**. The app uses a **pretrained model from Helsinki**, fine-tuned using **PEFT (Parameter-Efficient Fine-Tuning)** for better accuracy and performance.

## Features

- **Streamlit-based Web Interface**: Provides a simple and intuitive web-based user interface for translating text from English to Welsh.
- **Helsinki Pretrained Model**: Leverages the pretrained `Helsinki-NLP/opus-mt-en-cy` model, fine-tuned using PEFT for optimized results.
- **Real-time Translation**: Translate sentences or paragraphs from English to Welsh in real-time.
- **User-friendly Design**: Easy to use interface, with an option to input and translate multiple sentences at once.

## Installation

To run the app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/translation_webapp_cy-en.git
   cd translation_webapp_cy-en

2. **Create a virtual environment (Optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate 

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py




# Model Information
The translation model used in this application is based on the Helsinki-NLP/opus-mt-en-cy model, which is trained for English to Welsh translation. To further enhance the model's performance for this specific task, PEFT (Parameter-Efficient Fine-Tuning) was applied.

**Model**: Helsinki-NLP/opus-mt-en-cy
**Fine-tuning**: Performed using PEFT for better translation quality in this specific language pair.

# Usage
1. Start the app using streamlit run app.py.
2. Input the text you wish to translate from English to Welsh in the provided text area.
3. Click "Translate" to view the translated text.
4. Enjoy!
5. 
# Dependencies
**Streamlit**: Web framework for creating interactive web apps.
**Transformers**: Library by Hugging Face for using the translation model.
**PEFT**: Used for fine-tuning the pretrained model.

# Example
**Input**: "How are you?"
**Output**: "Sut ydych chi?"

# Fine-tuning with PEFT
This app uses PEFT to fine-tune the base model to enhance its performance in specific translation scenarios. For more details on PEFT and how it was applied, you can check the documentation or the model training notebook.

# Future Work
1. Support for additional language pairs.
2. Integration with other pretrained models.
3. Improving translation accuracy with more fine-tuning data.

# Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.
