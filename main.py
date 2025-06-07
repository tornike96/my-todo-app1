import streamlit as st
import functions as fc

todos = fc.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fc.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fc.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", placeholder="Add new todo...", key="new_todo", on_change=add_todo)