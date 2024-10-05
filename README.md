AlgoWhiz: Your AI DSA Guru-Bot
Overview
AlgoWhiz is an AI-powered chatbot designed to assist users with questions related to Data Structures and Algorithms (DSA). Whether you're looking for explanations of concepts, time complexities, or implementation code, AlgoWhiz is here to help!

Features
Interactive Chat Interface: Ask any DSA-related question.
Predefined Algorithm Code: Get quick access to code snippets for common algorithms like Bubble Sort, Merge Sort, and more.
AI-Powered Responses: Utilizes OpenVINO to provide intelligent responses based on user queries.
Installation
Prerequisites
Python 3.7 or higher
Pip (Python package installer)
Virtual Environment (recommended)
Setup
Clone the repository:


git clone https://github.com/yourusername/Project_oneAPI_hack_kpr.git
cd Project_oneAPI_hack_kpr
Create and activate a virtual environment:


python -m venv venv
.\venv\Scripts\Activate.ps1  # For PowerShell
# or
source venv/bin/activate  # For Unix/Linux
Install the required packages:


pip install -r requirements.txt
Ensure you have the OpenVINO model files in the specified directory (models/ir_model/gpt2.xml).

Running the Application
To run the Streamlit application, execute the following command:


streamlit run app/app.py
This will start a local web server, and you can interact with AlgoWhiz through your web browser.

Usage
Enter your question about data structures or algorithms in the input box.
Click the "Show Bubble Sort Code" button to see predefined answers.
Example questions:
What is a binary search tree?
How do I implement a quick sort algorithm?
Contributing
Contributions are welcome! Please submit a pull request or create an issue for any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For inquiries or feedback, feel free to reach out at: armstrongaldrin@karunya.edu.in


UI/UX Design
The design and user interface of the Interactive Chatbot were created using Figma. You can view the interactive prototype by following the link below:

Figma Prototype: Interactive Chatbot Prototype
