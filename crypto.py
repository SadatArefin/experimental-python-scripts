import requests
import tkinter as tk
from tkinterweb import HtmlFrame

def fetch_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def show_content_in_window(url):
    window = tk.Tk()
    window.title("Webpage Content")

    frame = HtmlFrame(window)
    frame.load_website(url)
    frame.pack(fill="both", expand=True)

    window.mainloop()

def main():
    url = input("Enter the URL: ")
    show_content_in_window(url)

if __name__ == "__main__":
    main()