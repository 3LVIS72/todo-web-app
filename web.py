import streamlit as st
import time
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Todo-Liste")
st.subheader("Das sind meine Todos:")

todo_status = {}

for index, todo in enumerate(todos):
    todo_status[todo] = st.checkbox(todo, key=index)
    if todo_status[todo]:
        st.write(f"{todo} wurde als erledigt markiert!")

for todo, checked in todo_status.items():
    if checked:
        time.sleep(3)  # Verzögerung von 3 Sekunden
        todos.remove(todo)
        functions.write_todos(todos)
        st.experimental_rerun()

new_todo = st.text_input(label="Gib einen neuen Todo Punkt ein:", placeholder="Neuer Todo Punkt...",
                         on_change=add_todo, key='new_todo')
