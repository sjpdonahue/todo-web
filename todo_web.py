import streamlit as st
import functions as func

todos = func.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    func.write(todos)
    st.session_state['new_todo'] = ""


st.title("To-do List")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        del st.session_state[todo]
        del todos[index]
        func.write(todos)
        st.experimental_rerun()

st.text_input(label="InputBox", label_visibility="hidden",
              placeholder="Enter a to-do...",
              on_change=add_todo, key='new_todo')
