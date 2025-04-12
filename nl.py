import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from tkinter import Tk, Text, Button, Label, Scrollbar, END, Entry, filedialog, messagebox

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract top keywords
def get_top_keywords(text, n=5):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token.lower() for token in words if token.isalpha() and token.lower() not in stop_words]
    token_frequency = Counter(filtered_tokens)
    top_keywords = token_frequency.most_common(n)
    return top_keywords

# Function to handle text extraction
def extract_keywords():
    text = input_text.get("1.0", END).strip()  # Get text from the input area
    if text:
        try:
            num_keywords = int(num_keywords_entry.get())  # Get the number of keywords to extract
            if num_keywords <= 0:
                raise ValueError
            keywords = get_top_keywords(text, num_keywords)
            result_text.delete("1.0", END)  # Clear previous results
            for word, freq in keywords:
                result_text.insert(END, f"{word}: {freq}\n")  # Display results
        except ValueError:
            result_text.delete("1.0", END)
            result_text.insert(END, "Please enter a valid positive integer for the number of keywords.\n")
    else:
        result_text.delete("1.0", END)
        result_text.insert(END, "Please enter some text to extract keywords.\n")

# Function to handle file upload
def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
            input_text.delete("1.0", END)  # Clear existing text in the input area
            input_text.insert(END, file_content)  # Load file content into the input area
        except Exception as e:
            messagebox.showerror("Error", f"Could not read the file: {e}")

# Create the main window
root = Tk()
root.title("Keyword Extractor")

# Input label and text area
Label(root, text="Enter Text:").pack()
input_text = Text(root, height=10, width=50)
input_text.pack()

# Upload file button
Button(root, text="Upload File", command=upload_file).pack()

# Number of keywords label and entry
Label(root, text="Number of Keywords:").pack()
num_keywords_entry = Entry(root, width=5)
num_keywords_entry.insert(0, "5")  # Default to 5
num_keywords_entry.pack()

# Extract keywords button
Button(root, text="Extract Keywords", command=extract_keywords).pack()

# Result label and text area with a scrollbar
Label(root, text="Top Keywords:").pack()
result_text = Text(root, height=10, width=50)
result_text.pack()

# Run the Tkinter event loop
root.mainloop()
