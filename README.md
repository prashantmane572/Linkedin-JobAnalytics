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



## Installation

1. Provide step-by-step installation instructions if applicable.



## Usage

1. Explain how to use your project.
2. Include examples or code snippets if necessary.



## Contributing

Describe how others can contribute to your project (if applicable).



## License

Add a license statement to specify how your project can be used.



## Acknowledgments

Give credit to any resources or individuals that helped you during the project.



## Contact

Provide your contact information if others want to reach out to you regarding the project.
