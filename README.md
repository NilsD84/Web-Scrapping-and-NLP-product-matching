# Data&Data Internship Assignment

## Overview

This assignment is designed to assess your fundamental skills in:

- Python  
- Database interactions  
- Web scraping  
- Data processing  
- Data analysis  

## Structure

The assignment consists of four main parts:

1. Demonstrating basic CRUD operations  
2. Implementing a simple web scraping script to collect data  
3. Cleaning and inserting the collected data into a local database  
4. Reading data from the local database and analyzing it  

## Deliverables

### Code

You will find a structured Jupyter notebook where we expect you to write your code. Please ensure that your code is clean, modular, and easy to follow. Feel free to create your own modules and import them into the notebook if it helps with clarity and structure.

### Database Interactions

Use `sqlite3` to create and manage a local database. For the connector, you may use either SQLAlchemy or MySQL Connector, depending on your preference.

### Analysis

In the final part of the assignment, we would like you to derive insights from both the data you collected and the historical data from 2021 (provided in the `Data` folder).  
Possible analysis angles include:

- Price evolution by collection  
- Price comparison across countries  

Feel free to explore additional ideas if anything interesting stands out. Creativity is always appreciated.

Your findings should be clearly presented, with readable graphs and legends. At the end of the analysis, please include a short summary of your conclusions.

If you run short on time, feel free to include a note about what you would have liked to explore further—this is optional but helpful.

---

## Part 1: CRUD Operations

Implement a class that supports the four basic CRUD operations: **Create, Read, Update, and Delete**.

You should use this class to interact with a local SQLite database. 
Create a simple table for demonstration purposes, and perform the four operations using just one row (the content is up to you). 
The goal is not to build a complex system, but to show that you understand how to design and implement reusable components in Python.

You will **reuse this class in Parts 3 and 4** to handle database interactions (e.g., inserting and retrieving data).

The objective here is to **test your ability to implement a clean, well-structured class** and to write **modular, maintainable code**. 
Your class should be written in a way that allows easy integration into a larger codebase — for example, with clear method naming, minimal repetition, and separation of concerns.

> Tip: Think of this class as part of a future codebase. Would another developer understand and reuse it without needing to rewrite it?

This part is foundational, so take the time to structure it well — good class design will make the next parts of the assignment easier and more consistent.


---

## Part 2: Web Scraping

Scrape data from Panerai's official website for 4 countries: France, United Kingdom, Japan, and the United States.

You only need to extract information relevant to your later analysis, such as:

- Watch name  
- Reference number  
- Price  

You can infer the collection from the watch name and the currency based on the country.

Your script should be simple and efficient. We recommend exploring XPath expressions to streamline the scraping process.

You do not need to collect the image_url or other things that you consider irrelevant to your analysis.

**Note**: Selenium is cool ;)

---

## Part 3: Cleaning and Inserting Data

Clean the scraped data and insert it into a table within your SQLite database. Use the class from Part 1 to handle the insertions.

> Tip: You can convert the cleaned data into a pandas DataFrame before inserting it into the database.

---

## Part 4: Data Analysis

Read the data from your local database using the class created in Part 1. Then, combine it with the 2021 dataset provided in the `Data` folder to perform your analysis.

Use clear, well-labeled graphs, and include concise interpretations in Markdown cells directly below each chart.

At the end of the notebook, provide a brief recap of your findings.

**Note:** Inflation adjustments are not required for this analysis.
