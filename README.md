CSEKU Exam Scheduler
=========================================================

This repository is designed to assist in creating an efficient exam schedule based on student-course enrollment data. The application processes student data to identify courses taken and assists in generating schedules that minimize overlapping exams for students.

* * *

Features
----------------------------------------------------------

*   **Dynamic Exam Scheduling**: Processes student-course enrollment data to create an exam schedule.
*   **Conflict Detection**: Ensures students do not face overlapping exam timings for courses they are enrolled in.
*   **Customizable Inputs**: Allows users to upload their own student-course enrollment data.
*   **Virtual Environment**: Includes a pre-configured virtual environment setup for easy dependency management.

* * *

Usage
----------------------------------------------------------

### Prerequisites

* Install Python (version 3.8 or later is recommended).
* Ensure `pip` is installed for package management.

### Installation Guide

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/SWPRANTA/CSEKU_Exam_Scheduler.git
    cd CSEKU_Exam_Scheduler
                
    
2.  **Set Up Virtual Environment:**
    
A virtual environment folder is included in the repository for dependency isolation. To activate it:
### Windows:
```bash
.\venv\Scripts\activate
```
### Mac/Linux:

```bash
source venv/bin/activate
```
If you want to create your own virtual environment, run:

```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
.\\venv\\Scripts\\activate   # For Windows
```
                
    
3.  **Install Dependencies:**
```bash
pip install -r requirements.txt
```
    
4.  **Run the Application:**
    
Upload your student-course data Excel file (format described below) and run the application script using the following command:
```bash
streamlit run CSEKU_exam_schudle_helper.py
```    

### Input File Requirements

*   The application processes an **Excel file** containing student-course enrollment data.
*   **File Format:**

*   The **top row** must contain course names.
*   The **first two columns** must contain:
    *   **Column 1**: Student IDs.
    *   **Column 2**: Student names.
*   Other columns represent courses with values:
    *   **1**: The student is enrolled in the course.
    *   **0**: The student is not enrolled in the course.

Example:

| Student ID | Student Name | Course 1 | Course 2 | Course 3 |
|------------|--------------|----------|----------|----------|
| 123        | John Doe     | 1        | 0        | 1        |
| 124        | Jane Smith   | 0        | 1        | 1        |
| 125        | Mark Wood    | 1        | 1        | 1        |

* * *

### Customization

1.  **Update Student Data:** Replace the Excel file with your own file containing the student-course data in the specified format.
2.  **Modify Scheduling Logic:** Adjust the logic in the main script for handling specific scheduling requirements or constraints.

* * *

File Structure
--------------

*   **CSEKU_exam_schudle_helper.py**: Main script for processing student data and generating exam schedules.
*   **requirements.txt**: Contains the list of dependencies required to run the application.
*   **venv/**: Virtual environment folder for dependency isolation.
*   **data/**: Place your student-course data file here.

* * *

Technologies Used
-----------------

*   **Python**: Core language for development.
*   **Pandas**: For processing and analyzing student-course data.
*   **OpenPyXL**: For reading Excel files.
*   **Streamlit**: For the better viewing.

* * *

How to Contribute
-----------------

1.  Fork the repository.
2.  Create a new branch for your feature/bug fix.
3.  Submit a pull request with a detailed description of changes.

* * *

License
-------

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

* * *

Enjoy creating efficient exam schedules with **CSEKU Exam Scheduler**! 😊