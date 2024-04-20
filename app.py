import tkinter as tk
from tkinter import messagebox, ttk
import requests
import re
import pyperclip

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def generate_summary(input_text, length):
    output = query({
        "inputs": input_text,
        "min_length": length,
        "max_length": length + 20,  
    })
    if 'error' in output:
        return "Error occurred. Please try again."
    else:
        summary_text = output[0]['summary_text']
        # Trim summary if it exceeds the requested length
        summary_words = summary_text.split()
        if len(summary_words) > length:
            summary_text = ' '.join(summary_words[:length])
        return summary_text

def summarize():
    input_text = text_input.get("1.0", "end-1c")
    length = length_scale.get()
    initial_word_count = len(re.findall(r'\w+', input_text))
    if input_text.strip():
        summary = generate_summary(input_text, length)
        final_word_count = len(re.findall(r'\w+', summary))
        initial_word_count_label.config(text=f"Initial Word Count: {initial_word_count}")
        final_word_count_label.config(text=f"Final Word Count: {final_word_count}")
        summary_text.delete("1.0", "end")
        summary_text.insert("1.0", summary)
    else:
        messagebox.showwarning("Warning", "Please enter some text to summarize.")

def copy_text():
    text_to_copy = summary_text.get("1.0", "end-1c")
    pyperclip.copy(text_to_copy)

root = tk.Tk()
root.title("Texty")

# Add padding to the root window
root.configure(padx=20, pady=20)

# Create a title label
title_label = tk.Label(root, text="Texty", font=("Helvetica", 24))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Enter text to summarize:")
label.grid(row=0, column=0, pady=(0, 5))

text_input = tk.Text(frame, height=10, width=50)
text_input.grid(row=1, column=0, pady=(0, 5))

length_frame = tk.Frame(frame)
length_frame.grid(row=2, column=0, pady=(0, 5))

length_label = tk.Label(length_frame, text="Choose summarization length:")
length_label.pack()

length_scale = tk.Scale(length_frame, from_=20, to=70, orient="horizontal", length=200)
length_scale.set(45)  # Initial value
length_scale.pack()

summarize_button = tk.Button(frame, text="Summarize", command=summarize)
summarize_button.grid(row=3, column=0, pady=(0, 5))

summary_label = tk.Label(frame, text="Summary:")
summary_label.grid(row=4, column=0, pady=(0, 5))

summary_text = tk.Text(frame, height=10, width=50)
summary_text.grid(row=5, column=0, pady=(0, 5))

copy_button = tk.Button(frame, text="Copy Text", command=copy_text)
copy_button.grid(row=6, column=0, pady=(0, 5))

initial_word_count_label = tk.Label(frame, text="Initial Word Count: 0")
initial_word_count_label.grid(row=7, column=0, pady=(0, 5))

final_word_count_label = tk.Label(frame, text="Final Word Count: 0")
final_word_count_label.grid(row=8, column=0, pady=(0, 5))

root.mainloop()
