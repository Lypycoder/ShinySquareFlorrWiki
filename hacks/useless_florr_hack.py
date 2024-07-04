import webbrowser
from js import document, alert
from pyodide.ffi import create_proxy

# Import jQuery (assuming it's available in the Python environment)
# If not, you might need to use a Python alternative or pure JavaScript

def on_document_ready():
    alert('This script does nothing. It could soon. Just let me learn Python.')

# Create an empty list to store hrefs
hrefs = []

# Get elements with class 'headline' and 'a' tag
elements = document.querySelectorAll('.headline > a')

# Iterate through elements and append href attributes to the list
for element in elements:
    hrefs.append(element.getAttribute('href'))

# Create a button element
button = document.createElement('input')
button.type = 'button'
button.value = 'Does this do anything'
button.id = 'CP'

# Set CSS properties for the button
button.style.position = 'fixed'
button.style.top = '0'
button.style.left = '0'

# Append the button to the body
document.body.appendChild(button)

# Define click event handler
def on_button_click(event):
    for href in hrefs:
        alert('What are you thinking of?!')

# Add click event listener to the button
button.addEventListener('click', create_proxy(on_button_click))

# Call the on_document_ready function when the document is ready
document.addEventListener('DOMContentLoaded', create_proxy(on_document_ready))


