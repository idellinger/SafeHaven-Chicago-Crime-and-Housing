![logo_notext](https://github.com/idellinger/chicago-crime-property-analysis/assets/51415637/31d3e280-7a86-4ee3-9501-748d3991a3dc)

# Chicago Crime and Property Analysis

## Overview

This project aims to analyze crime and property data in Chicago to identify patterns and insights that can help in understanding the relationship between crime rates and property values. The project involved extensive data wrangling, feature engineering, exploratory data analysis, and modeling.

## Team Members

- Israel Dellinger
- Seth Kulow
- Rashid Baset

## Project Structure

The project is structured into several stages, each documented in separate Jupyter Notebooks:

1. **Data Wrangling (`1_data-wrangling.ipynb`)**
   - In this notebook, we clean and preprocess the raw data. This includes handling missing values, normalizing data formats, and merging different datasets.

2. **Feature Engineering (`2_Feature_Engineering.ipynb`)**
   - Here, we create new features from the existing data to improve our models. This includes creating time-based features, calculating crime rates per area, and more.

3. **Exploratory Data Analysis (EDA) (`3_EDA.ipynb`)**
   - This notebook contains visualizations and statistical analyses to uncover trends in the data. We use various plots and summary statistics to understand the distribution and relationships between variables.
  
4. ** (`4_Chicago-Crime-Property-Analysis.ipynb`)**
   - This notebook focuses on the relationship between crime rates and property values in Chicago. 

5. **Crime Count Model (CrimeCountModelfinal.ipynb`)**
   - In this notebook, we develop and evaluate machine learning models to predict crime counts in different areas of Chicago. We experiment with different algorithms and tune hyperparameters to achieve the best performance.

6. **Home Page Script (`0_🏡_Home.py`)**
   - This Python script sets up the home page for the project's presentation. It includes the necessary code to run a web application showcasing our project's results.

## Data Sources

- **Chicago Crime Data**: This dataset is sourced from the Chicago Data Portal and maintained by the Chicago Police Department. It includes reported incidents of crime (excluding murders) that occurred in Chicago. Each row in the dataset represents a single reported crime incident. Data collected from 2014-2023. [More information](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data)
- **Chicago Property Data**: Collected using the HomeHarvest real estate scraping library, this dataset extracts and formats data to resemble MLS listings. It fetches properties directly from Realtor.com and structures the data similarly to MLS listings. Each row represents a single property listing. Data collected from 2014-2023.[More information](https://github.com/Bunsly/HomeHarvest)

## Installation

To run the notebooks and scripts in this project, you'll need to have the following dependencies installed:

- Python 3.7+
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask (for the home page script)

You can install the required packages using pip:

```sh

pip install pandas numpy scikit-learn matplotlib seaborn flask

```

## Usage

1\. Clone the repository

```sh

git clone https://github.com/your-repo/chicago-crime-property-analysis.git

cd chicago-crime-property-analysis

```

2\. Start Jupyter Notebook

```sh

jupyter notebook

```

3\. Open and run the notebooks in the following order:

- `1_data-wrangling.ipynb`
- `2_Feature_Engineering.ipynb`
- `3_EDA.ipynb`
-  4_Chicago-Crime-Property-Analysis.ipynb`
- `/modeling/CrimeCountModelfinal.ipynb`
   

4\. To run the web application showcasing the project results, navigate to the directory containing 0_🏡_Home.py and execute the following command:

```sh

python 0_🏡_Home.py

```

This will start a local server, and you can view the application by navigating to http://127.0.0.1:5000 in your web browser.

You can access the application via https://safe-haven.onrender.com/.

## Results

Our analysis revealed several key insights, including:

- Certain neighborhoods with higher crime rates tend to have lower property values.
- Temporal patterns in crime rates can inform property investment decisions.
- The predictive models developed can help city officials and real estate investors in making data-driven decisions.