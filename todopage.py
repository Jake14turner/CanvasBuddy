import streamlit as st
import requests

# Replace with your actual access token
access_token = '9082~vZXVa46Ret7JkhG4NAAyZT67LnEvPzaTneZyFar6BYtaYF7ZLuKEW2hTwQUVRHGr'  # Replace with your actual access token
apiLink = 'https://canvas.instructure.com/api/v1'

# Authentication headers
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Function to get courses
def get_courses():
    courseIDList = []
    courseNameList = []
    link = f'{apiLink}/courses'
    
    while link:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            courses = response.json()
            for course in courses:
                if 'name' in course:
                    courseIDList.append(course['id'])
                    courseNameList.append(course['name'])
            link = response.links.get('next', {}).get('url')  # Pagination for more courses
        else:
            st.error(f"Failed to retrieve courses. Status code: {response.status_code}")
            break
    
    return courseIDList, courseNameList

# Function to get assignments for a course
def get_assignments(course_id):
    assignments = []
    link = f'{apiLink}/courses/{course_id}/assignments'
    
    while link:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for assignment in data:
                assignments.append({
                    'name': assignment.get('name', 'No title'),
                    'due_at': assignment.get('due_at', 'No due date')
                })
            link = response.links.get('next', {}).get('url')  # Pagination for more assignments
        else:
            st.error(f"Failed to retrieve assignments for course {course_id}. Status code: {response.status_code}")
            break
    
    return assignments

# Streamlit interface
st.title("Canvas Course and Assignment Viewer")

# Fetch and display courses
courseIDList, courseNameList = get_courses()

if courseIDList:
    st.header("Courses and Assignments")

    for i, course_name in enumerate(courseNameList):
        st.subheader(f"Course: {course_name}")

        assignments = get_assignments(courseIDList[i])
        
        if assignments:
            st.write("Assignments:")
            for assignment in assignments:
                st.write(f" - **Title**: {assignment['name']}, **Due**: {assignment['due_at']}")
        else:
            st.write("No assignments found.")
else:
    st.write("No courses found or API issue.")
