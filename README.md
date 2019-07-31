# NHANES Practicum
Details and write-up about this project are available [here](https://www.gong-jj.com/nhanes/).  

## Files:  
1. Files.xlsx
    * Contains the matched indexes of the NHANES files across the years sorted alphabetically, indicates features used for analysis, and re-naming of features across the years for consistency. 
2. run_notebooks.py
    * Script to batch run Jupyter Notebooks
    * Jupyter notebook output from running this code is available in the /output folder for each respective folder
3. /NHANES-Downloader
    * Scripts to download NHANES files and converts them to csv files
4. /Data Cleaning
    * Notebooks that clean, rename, recategorize, and remove missing values for NHANES data files and uploads it to a local NoSQL database.
5. /Data Upload
    * Notebooks that merge appropriate files for analysis, recategorize labels, one-hot encode features, and upload data to a local NoSQL database. 
6. /Data Analysis
    * Notebooks for exploratory data analysis, fitting random forest and XGBoost models to the data, and evaluating the performance of the models. Identify risk factors for hospital utilization and major diseases.
7. /Prevalence
    * Notebooks to generate data (.csv) files for prevalence plots
    * R Notebooks to generate prevalence plots

## Instructions to Run:  
1. Download files from NHANES using NHANES-Downloader scripts
    * Navigate to the NHANES-Downloader folder and follow the [README](./NHANES-Downloader/README.md).  
    * In terminal go to NHANES-Downloader folder and run (MAC):
```bash
$ ./get_data.py  
$ ./raw_to_csv.py
```
2. Run Jupyter Notebooks to clean clean, upload, and anlayze data:
    * Navigate to the root folder and in terminal run:
```bash
$ python run_notebooks.py ./Data\ Cleaning/*.ipynb ./Data\ Upload/*.ipynb
```
3. Run Jupyter Notebooks to analyze data (This may take a while ~15 mins):
    * Navigate to the root folder and in terminal run:
```bash
$ python run_notebooks.py ./Data\ Analysis/*.ipynb
```
4. Run Jupyter Notebooks to generate data for prevalence plots:
    * Navigate to the root folder and in terminal run:
```bash
$ python run_notebooks.py ./Prevalence/*.ipynb
```
5. Run R Markdown files in Q1 and Q2 folders individually to generate prevalence plots:
    * Make sure to set the approriate working directories before running all.
    1. Q1 - Hospital Utilization.Rmd
    2. Q2 - 1. Heart Disease.Rmd
    3. Q2 - 2. Cancer.Rmd
    4. Q2 - 3. Chronic Lung Disease.Rmd
    5. Q2 - 4. Diabetes.Rmd





