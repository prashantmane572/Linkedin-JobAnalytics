# Linkedin-JobAnalytics
LinkedIn Job Analytics is a data-driven project that leverages Python, Beautiful Soup, and Selenium to scrape and analyze job information from LinkedIn. It offers insights on industry trends, top job locations, and company analysis. With visualizations and tables, users gain valuable insights for optimizing their job search strategies.






## Prerequisites

1. **Web Scraping using Python**:
   - [Selenium](https://www.selenium.dev/): A Python library used for automating web browsers, which is essential for web scraping.
   - [Time](https://docs.python.org/3/library/time.html): A standard Python library that provides various time-related functions, useful for adding delays in web scraping operations.
   - [Pandas](https://pandas.pydata.org/): A powerful data manipulation library in Python, used for data analysis and handling structured data.
   - [NumPy](https://numpy.org/): A fundamental package for scientific computing in Python, used for working with large arrays and matrices.

2. **Google Chrome Browser Driver**:
   - To access web pages using Python and interact with them through the Chrome browser, you'll need to install the appropriate [Chrome browser driver](https://sites.google.com/a/chromium.org/chromedriver/).

3. **Python Jupyter Notebook**:
   - Used for data cleaning and data separation tasks.
   - [NumPy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/): Required libraries for working with numerical arrays and structured data within Jupyter Notebook.

4. **Excel**:
   - Utilized for data storage purposes. You can export and save your data in Excel format for further analysis or sharing.

5. **SQL**:
   - Used for data analysis to extract insights from the collected data.
   - Basic SQL knowledge is necessary to perform data querying and analysis tasks.

6. **Tableau**:
   - A powerful data visualization tool that helps create interactive and visually appealing dashboards and reports based on your data analysis.

Make sure you have the necessary installations and setups for the above tools and libraries before running the LinkedIn Job Analysis project.



## Project Content

1. **`Web Scrapping`** (Folder)
   - `chromedriver.exe`: The Chrome browser driver used for web scraping.
   - `main.py`: This Python file is responsible for scraping the required data from the website.

2. **`scrapped raw data.csv`**: An Excel file that contains the raw extracted data from the portal.

3. **`Data Cleaning of Scrapped data.ipynb`** using Python: Details about the data cleaning process performed on the scraped data.

4. **`Data`** (Folder)
   - `jobs.csv`: Contains details about the job.
   - `company.csv`: Contains company details.
   - `details.csv`: Contains details about the applied job.

5. **`Database Schema.pdf`**: Contains the prepared database star schema.

6. **`SQL Analysis.sql`**: Details about the data analysis performed using SQL queries.

7. **`Dashboard - Tableau.twbx`**: Contains the Tableau dashboard created for visualizing the analyzed data.

8. **`Job analytics- Project presentation.pptx`**: Presentation slides ppt providing an overview of the job analytics project.

Please refer to the specific files and folders for more detailed information on their content and usage.


## About Project

### Problem Statement
Scrape data from the professional networking platform Linkedin using Python library called Beautifulsoup (or similar) and collate information in the in specific format and make 3 tables using the data.

For analysis purposes, extract the sections highlighted in red in the screenshot below.

![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/ee38ce6a-d63b-4207-b3db-dae53b255bc3)


### Methodology

The project follows the following methodology:
| Step | Description |
|------|--------------|
| 1.     | **Data Collection**: Utilize web scraping techniques with a Python library such as Beautiful Soup or a similar library to extract data from the LinkedIn platform. Specifically, scrape the sections highlighted in red in the provided screenshot to gather the required information for analysis.|
| 2.     | **Data Cleaning and Preprocessing**: Perform data cleaning tasks to ensure the extracted data is accurate and consistent. Handle missing values, remove duplicates, and format the data appropriately for further analysis.|
| 3.     | **Exploratory Data Analysis (EDA)**: Conduct exploratory data analysis on the collected data. Generate descriptive statistics, visualize distributions, and explore relationships between variables. Identify any patterns or trends that may be relevant to the analysis.|
| 4.     | **Data Transformation and Formatting**: Prepare the data for analysis by transforming it into a specific format suitable for the desired analysis. This may involve reshaping the data, aggregating it, or applying other necessary transformations. |
| 5.     | **Data Analysis**: Apply appropriate analytical techniques to derive insights from the data. This may include statistical analysis, data mining, or machine learning algorithms depending on the project requirements. Perform the analysis with a clear objective in mind, such as identifying key trends, patterns, or correlations. |
| 6.      | **Data Visualization with Tableau**: Utilize Tableau, a powerful data visualization tool, to create interactive and visually appealing visualizations. Present the analyzed data through charts, graphs, and dashboards to effectively communicate the findings. |
| 7.     | **Data Organization in Tables**: Organize the extracted data into three different tables based on their relationships. Explain the relationships and connections between these tables in a database schema. |
| 8.     | **Summary and Conclusions**: Summarize the results of the data analysis and draw meaningful conclusions based on the insights gained. Highlight the key findings, implications, and any actionable recommendations that arise from the analysis.|
| 9.     | **Documentation and Presentation**: Prepare comprehensive documentation in the form of a PowerPoint presentation (PPT). Include details about the project objectives, methodology, data sources, data analysis techniques used, visualizations, and key findings. Use the presentation to effectively present the project's findings and insights. |

By following this methodology, the project aims to extract, clean, analyze, and visualize the relevant data from LinkedIn. The use of Tableau and the organization of data into tables provide a structured and visually appealing representation of the insights gained from the analysis. The documentation prepared in the form of a PPT presentation ensures clear communication of the project's objectives, methodology, and findings.


### Database Information

#### Sample Dataset
The scraped data obtained from the website is in the following format:
![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/5acc2642-10f4-4727-be9c-27de5778e7b8)

#### Schema
After scraping the data, it was cleaned and separated into three different tables: **`company`**, **`jobs`**, and **`details`**. 
Below is the star schema representing the relationship between these tables.
![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/a3b34fcd-dddc-48b2-9d4b-9b7629315850)


### Insights

- **Job Market Analysis**: The most job offering domains are data analyst 20.36% and developer 20% compared to other domains.

![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/eec6defd-ff19-4bb3-8a34-0da6281f10fb)

- **Top Hiring Companies**: Based on the dataset, Uplers, Southerland, and Infosys are the companies with the highest number of job postings.
- **Applicant Insights**: Some jobs have a high number of applicants, indicating strong competition, while others have relatively fewer applicants, suggesting lower competition and potentially higher chances of securing the job.

![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/c4a24f50-467c-437e-bb24-ac893a96dbde)


- **Geographical Job Distribution**: The majority of job opportunities are concentrated in states like Karnataka, Rajasthan, Tamil Nadu, and Maharashtra. 

![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/2e8c5030-1203-4da2-b0fd-75f2575e598c)

- **Thriving Job Market in Bangalore**: Within Bangalore, more companies are available across different fields of job.

- **Industry Analysis**: The IT Services and IT Consulting industry has the most job postings.

![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/e7de57d8-805e-4611-8562-7a80de4b366d)



### Challenges

- The ultimate challenge was figuring out how to scrape data from the website.
- On the first day, we conducted research on web scraping techniques.
- After exploring various options, we determined that Selenium would best fit our requirements.

### Learning

- Throughout the project, we gained knowledge about Selenium through various resources.
- Reference links:
  - [YouTube Tutorial 1](https://youtu.be/lTypMlVBFM4)
  - [YouTube Tutorial 2](https://youtu.be/Xjv1sY630Uc)
- We also referred to the [official Selenium documentation](https://www.selenium.dev/documentation/) for detailed information.

### Dashboard 
Tableau Dashboard: [Linkdean Job Analysis Dashboard](https://public.tableau.com/app/profile/prashantmane572/viz/Linkdean_Jobanalysis/JobAnalysis?publish=yes)

![image](https://github.com/prashantmane572/Linkedin-JobAnalytics/assets/126981770/8d7134a1-08e3-4a65-9889-2c1ba467f227)


## Conclusion

In this project, we successfully scraped job data from LinkedIn, cleaned and analyzed the data, and visualized the findings. Here are the key takeaways:

- The job market analysis revealed that the most in-demand domains are data analyst and developer.
- Top hiring companies, including Uplers, Southerland, and Infosys, had a significant number of job postings.
- Job opportunities were concentrated in states like Karnataka, Rajasthan, Tamil Nadu, and Maharashtra.
- Bangalore emerged as a thriving job market, offering a diverse range of job opportunities across different fields.
- The IT Services and IT Consulting industry showcased the highest number of job postings.
- Job involvement types varied from full-time to part-time and contract, and job levels spanned from entry-level to senior management.
- Applicant insights highlighted varying levels of competition, with some jobs receiving a high number of applicants and others having relatively lower competition.

The Tableau dashboard [here](https://public.tableau.com/app/profile/prashantmane572/viz/Linkdean_Jobanalysis/JobAnalysis?publish=yes) provides a detailed visualization of the analyzed data.

By following this methodology and utilizing Tableau for visualization, we gained valuable insights into the job market, enabling us to understand trends, identify top companies, explore geographical job distributions, and analyze job involvement and applicant insights.

This project serves as a valuable resource for job seekers, employers, and policymakers, aiding them in making informed decisions based on the analyzed data and visualizations.



## Note: Demo Project for Study Purposes

<small>This project is intended as a demonstration for educational purposes only. It serves as an example of how to scrape data from LinkedIn, clean and analyze the data, and visualize the findings using Tableau. The data used in this project is simulated or anonymized and does not reflect real-world data.</small>

<small>Please note that approximately 300 job listings were scraped from LinkedIn for the purpose of this demo. The data may not represent the actual job market conditions or trends.</small>

<small>Feel free to explore the code, methodologies, and visualizations presented here to enhance your understanding of web scraping, data analysis, and data visualization techniques. However, please refrain from using this project or its code for any commercial or production purposes without proper authorization.</small>

<small>If you have any questions or suggestions, please reach out to the project maintainers.</small>

<small>Happy studying and learning!</small>
