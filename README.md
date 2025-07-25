# Data&Data Internship Assignment

## Overview

This assignment is designed to assess your fundamental skills in:

- Python  
- Database interactions  
- Web scraping  
- Data processing  
- NLP

## Structure

The assignment consists of four main parts:

1. Demonstrating basic CRUD operations  
2. Implementing a simple web scraping script to collect data  
3. Cleaning and inserting the collected data into a local database  
4. Entity matching

## Deliverables

### Code

You will find a structured Jupyter notebook where we expect you to write your code. Please ensure that your code is clean, modular, and easy to follow. 
Feel free to create your own modules and import them into the notebook if it helps with clarity and structure.

Make sure that we can run your notebook from our device in 1 time (i.e. rerun all cells should work).

### Database Interactions

Use `sqlite3` to create and manage a local database. For the connector, you may use either SQLAlchemy or MySQL Connector, depending on your preference. You can also use SQLThunder, it should make things easier.

### Analysis

In the final part of the assignment, we would like you to match the products you scraped with the official product references (provided in the `Data` folder).

Feel free to explore any ideas to match your data to the refs. Creativity is encouraged.

---

## Part 1: CRUD Operations

Implement a class that supports the four basic CRUD operations: **Create, Read, Update, and Delete**, or use SQLThunder.

You should use this class or SQLThunder to interact with a local SQLite database. 
Create a simple table for demonstration purposes, and perform the four operations using just one row (the content is up to you). 
The goal is not to build a complex system, but to show that you understand how to design and implement reusable components in Python.

You will **reuse this class/SQLThunder in Parts 3 and 4** to handle database interactions (e.g., inserting and retrieving data).

---

## Part 2: Web Scraping

Scrape data from profumeriaideale.com website for the brand Valmont.

You only need to extract information relevant to your later matching task, such as:

- Product Name 
- Capacity
- Product Url

Your script should be simple and efficient. We recommend exploring XPath expressions to streamline the scraping process.

You do not need to collect the image_url or other things that you consider irrelevant to your analysis. Save the raw scrapped data into an excel file.

**Note**: Selenium is cool ;)
**Note**: If you cannot manage to scrape the website, we have included the necessary data to proceed with the next steps.

---

## Part 3: Cleaning and Inserting Data

Clean the scraped data and insert it into a table within your SQLite database. Use the class/SQLThunder from Part 1 to handle the insertions.

> Tip: You can convert the cleaned data into a pandas DataFrame before inserting it into the database.

---

## Part 4: Product Reference Matching (Kaggle Competition)

Use any SOTA algorithms to match each offer to its corresponding official reference. You can either find the data in folder `Data_2025` or download it from https://www.kaggle.com/competitions/entity-matching/overview.
Submit your folder containing all the code and data in a ZIP format by email.
Submit your final matching file to the Kaggle Competition Page for evaluation.

