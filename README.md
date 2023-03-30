# **NBA stats 2021-22** 

## **FEATURES**

- ### **TECHNOLOGIES**

  ### **Languages Used**
  This tool is created using Python language.

  ### **Libraries Used**
  Git - For version control These commands were used for version control during project:
  - git add . - To add files before committing
  - git commit -m "type your message mentioning changes" - To commit changes to the local repository
  - git push - To push all committed changes to the GitHub repository
  - GitHub - To create my repositories, save and store my project files.
  - gspread is a Python API for Google Sheets and requires Python 3+. It allows user to open, read, write, share spreadsheets. Additionally it enables user to select, create, delete worksheets and to format cell ranges.
  - pandas- Python Data Analysis Library pandas is an open source data analysis and manipulation tool, built on top of the Python programming language. It supports Python 3.8, 3.9 and 3.10 officially. My codes are largely based on pandas code, as they contain extensive functions very well suited for parsing and analysing data.
  - pprint — Data pretty printer — Python 2.7, 3.5 onwards. The pprint module provides “pretty-print” to Python data structures. The formatted representation arranges objects on a single line if it can, and breaks them onto multiple lines if they don’t fit within the allowed width. I used it in order to visualize the lists in more user friendly style.
   Provides
  - numPy provides:
    -  An array object of arbitrary homogeneous items
    - Fast mathematical operations over arrays
    - Linear Algebra, Fourier Transforms, Random Number Generation

 - ### **TESTING**
    - Python Linter Test
 As advised by tutors, I validated Code Institute Python linter. Test result: No errors found. Check in screenshot below.

 - ### **DEPLOYMENT**
    - On the Heroku dashboard, select "New" and click "Create new app"
    - Create a unique app name
    - Select your region
    - Click "Create app"
    - Go to the settings tab:
    - Scroll down to the config vars section and select "Reveal Config Vars"
    - Add necessary config vars
    - In this case, in the key field enter "PORT" and the value field enter "8000"
    - Click "Add"
    - Scroll down to Buildpacks and click "Add buildpack"
    - Add the necessary buildpacks.
    - In this case, select "python" and click "Save changes"
    - Then, select "node.js" and click "Save changes"
    - Go to the Deploy tab:
    - Select GitHub and confirm connection to GitHub account
    - Search for the repository and click "Connect"
    - Scroll down to the deploy options
    - Select automatic deploys if you would like automatic deployment with each new push to the GitHub repository
    - In manual deploy, select which branch to deploy and click "Deploy Branch"
    - Heroku will start building the app
    - The link to the app can be found at the top of the page by clicking "Open app"

 - ### **ACKNOWLEDGEMENTS**
     I'd like to thank my mentor, Akshat Garg, for providing advices and feedback for this project.