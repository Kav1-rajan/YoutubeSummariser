1. Clone the repository
Open your terminal or command prompt and run:

````bash
git clone https://github.com/Kav1-rajan/YoutubeSummariser.git
cd YoutubeSummariser
````

2. Create a .env file
In the root directory of the project, create a file named .env and add the following line:

GROQ_API=your_api_key_here

Replace your_api_key_here with your actual API key.

3. Install dependencies
It’s recommended to use a virtual environment:
````bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
````

4. Run the project
````bash
python main.py
````
