import tkinter as tk
from tkinter import scrolledtext
import textwrap
import google.generativeai as genai

# Set up generative model
genai.configure(api_key='AIzaSyA5XSNSmCedWb0IKmyRfsjI9-b5686Gp3s')  # Replace 'YOUR_API_KEY' with your actual API key
model = genai.GenerativeModel('gemini-pro')

# Function to generate response
def generate_response():
    input_text = input_text_box.get("1.0", "end-1c")
    input_text += " Choose the problem from the following options: Civil, Criminal, Domestic, Real Estate, Corporate, Tax, Immigration, Education, Environmental, Healthcare, Human rights, Immigraation, patent , tax."
    response = model.generate_content(input_text)
    formatted_response = response.text.replace('•', '*')
    output_text_box.delete("1.0", tk.END)  # Clear previous content
    output_text_box.insert(tk.END, formatted_response)

# Create GUI window
window = tk.Tk()
window.title("AI Legal Assistant")

# Create input text box
input_text_box = scrolledtext.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
input_text_box.pack(pady=10)

# Create generate button
generate_button = tk.Button(window, text="Generate Response", command=generate_response)
generate_button.pack(pady=5)

# Create output text box
output_text_box = scrolledtext.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
output_text_box.pack(pady=10)

# Run the GUI
window.mainloop()
