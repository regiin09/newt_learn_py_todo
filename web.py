#https://regiin09-newt-learn-py-todo-web-nzzwpp.streamlit.app/
import streamlit as st
from funtions import load_todos, save_todos, add_todo

# Load existing tasks from file
if "tasks" not in st.session_state:
    st.session_state["tasks"] = load_todos()

def add_task():
    new_task = st.session_state["new_task_input"].strip()
    if new_task:
        add_todo(new_task, st.session_state["tasks"])
        save_todos(st.session_state["tasks"])  # Save to file
        st.session_state["new_task_input"] = ""  # Clear input field
        st.rerun()

st.title("📝 Simple To-Do App")

# Input for new task
st.text_input("Add a new task:", key="new_task_input", on_change=add_task)

# Display tasks with checkboxes
remaining_tasks = []
for index, task in enumerate(st.session_state["tasks"]):
    if not st.checkbox(task.strip(), key=f"task_{index}"):
        remaining_tasks.append(task)

# Update session state and file if tasks are removed
if len(remaining_tasks) != len(st.session_state["tasks"]):
    st.session_state["tasks"] = remaining_tasks
    save_todos(remaining_tasks)
    st.rerun()
