# autoWP

## Description
AutoWP is a Python-based project designed to automate wordpress posting harnessing AI, making tasks more efficient and streamlined. This repository includes multiple Python scripts aimed at different functionalities, such as data importing and processing.

## Workflow:
1. Calculate current day of the year to use as row number
2. Fetch title column in Excel file current row number using importer.py 
3. Combine opening prompt with title data
4. Submit API request to Gemini
5. Submit API request to wordpress API to create post
6. Upload all files to Azure Repo or similar
7. Create scheduled trigger to run daily

## Features
- **Data Importing:** Use `importer.py` to automate the import of data.
- **Data Processing:** Utilize `gemini.py` and `single.py` for data processing tasks.
- **Excel Integration:** Includes an Excel file (`effectivecopy.xlsx`) for data handling and processing.
- **CI/CD Pipeline:** Integrates with CI/CD Pipelines for continuous integration and deployment.

## Technologies Used
- Python
- Google Gemini API
- Wordpress API

## Setup Instructions
1. Clone the repository to your local machine using `git clone [repository URL]`.
2. Navigate to the project directory.
3. Install the required dependencies.
4. Run the Python scripts as needed for your specific tasks.

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.

## Limitation
1. Excel row must be more than 366

## TODO
1. To handle exception if excel row is less than 366