# Cover-Letter-Builder
Full-stack application where a user submits the name of the company they are applying to, the position they are applying to, their resume, and the job description, a request will be made using the openai api to generate a well written cover letter containing relevant information about the user

## Setup

1. install python 

2. Clone this repository

3. Navigate into the project directory

   $ cd COVER-LETTER-BUILDER

4. Create a new virtual environment

   $ python -m venv venv

   depending on the name of the folder in your venv directory run one of the following commands

   $ . venv/bin/activate

   OR

   $ . venv/Scripts/activate

5. Install the requirements

   $ pip install -r requirements.txt

6. Make a copy of the example environment variables file

   $ cp .env.example .env

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   $ flask run

   open http://localhost:5000