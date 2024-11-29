import pandas as pd
import streamlit as st

# Load the student course data from an Excel file
student_course = pd.read_excel('./data/students_courses_2024_2nd_term.xlsx')

# Extract the list of course columns
courses_columns = student_course.columns[2:].to_list()

# Function to search for students by their name
def search_student_by_name(keyword):
    keyword = keyword.lower()
    results = []
    for _, row in student_course.iterrows():
        student_name = str(row['student_name']).lower()
        if keyword in student_name:
            courses_taken = [col for col in courses_columns if row[col] == 1.0]
            results.append({
                'SID': row['SID'],
                'Student Name': row['student_name'],
                'Courses Taken': ', '.join(courses_taken)
            })
    return results

# Function to search for students by their courses
def search_student_by_courses(course_keywords):
    course_keywords = [keyword.lower() for keyword in course_keywords]
    results = []
    for _, row in student_course.iterrows():
        courses_taken = [col for col in courses_columns if row[col] == 1.0]
        matching_courses = [course for course in courses_taken if any(keyword in course.lower() for keyword in course_keywords)]
        if len(matching_courses) == len(course_keywords):  # Ensure all courses match
            results.append({
                'SID': row['SID'],
                'Student Name': row['student_name'],
                'Courses Taken': ', '.join(courses_taken)
            })
    return results

# Function to search for students by their SID
def search_student_by_sid(sid):
    results = []
    for _, row in student_course.iterrows():
        if row['SID'] == sid:
            courses_taken = [col for col in courses_columns if row[col] == 1.0]
            results.append({
                'SID': row['SID'],
                'Student Name': row['student_name'],
                'Courses Taken': ', '.join(courses_taken)
            })
    return results

# Streamlit app
st.title("KU CSE Exam Schedule Helper")

# Search options
search_type = st.selectbox("Search by", ["Student Name", "SID", "Courses"])

if search_type == "Student Name":
    keyword = st.text_input("Enter student name keyword:")
    if st.button("Search"):
        results = search_student_by_name(keyword)
        if results:
            st.write("Search Results:")
            st.table(pd.DataFrame(results))
        else:
            st.warning("No students found with that name.")

elif search_type == "SID":
    try:
        sid = st.number_input("Enter Student ID (SID):", value=0, step=1)
        if st.button("Search"):
            results = search_student_by_sid(sid)
            if results:
                st.write("Search Results:")
                st.table(pd.DataFrame(results))
            else:
                st.warning("No students found with that SID.")
    except ValueError:
        st.error("Please enter a valid SID.")

elif search_type == "Courses":
    course_keywords = st.text_input("Enter course names (separated by spaces):")
    if st.button("Search"):
        course_keywords = course_keywords.split()
        results = search_student_by_courses(course_keywords)
        if results:
            st.write("Search Results:")
            st.table(pd.DataFrame(results))
        else:
            st.warning("No students found taking the specified courses.")
