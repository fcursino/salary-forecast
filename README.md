# 📚 Salary Forecast

## Project Steps
- 📊 Exploratory Data Analysis
- 🛠️ Preparing the training and test data set
- 🤖 Model training
- ✔️ Validating the model
- 🚀 Creating the API and UI to make the model available for use

The aim of the project is to develop an AI model that can predict the salaries of a company's employees according to the number of years they have been with the company and the level of their job within a dataset. 📊💼✨

## Prerequisites
- [Python 3.11.7](https://www.python.org/downloads/release/python-3117/)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/fcursino/salary-forecast.git
   cd salary-forecast/
2. Install pip:

   ```bash
   python -m pip install -U pip
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
4. Run the FastAPI with uvicorn:

   ```bash
   uvicorn api_modelo_salario:app --reload
5. Run the build of streamlit UI:

   ```bash
   streamlit run app_streamlit_salario.py
6. Access your 'localhost:8501' page on browser:
   
   ![GIF](https://github.com/fcursino/salary-forecast/blob/main/test.gif)
