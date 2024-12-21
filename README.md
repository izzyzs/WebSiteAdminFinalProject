# **Web Site Administration Final Project**

-   I've decided to make a to-do list as my final project for this class.

-   It will include the following HTML pages:
    -   home.html: displays all tasks with buttons for adding, editing, or deleting
    -   add_task.html: allows user to add task (Form)
    -   edit_task.html: allows user to edit task (Form)

## _(From final submission)_

## _**Term Project for Web Site Administration** By Ismael Soumahoro (Solo)_

## **Functionality**

There are three main HTML pages:

-   add_task.html
-   edit_task.html
-   home.html

_add_task_ has a form with 2 fields (for title and description) and a submit button

_edit_task_ has a form with 3 fields (for the 2 from add_task and a checkbox for completed) and a submit button

_home_ displays all the tasks and give the user an option to edit or delete every Task

## **Database Design**

-   There is one simple table: a **Task** table
-   The **Task** has multiple fields and they are
    1. Title (a text value)
    2. Description (a text value)
    3. Completed (a boolean value; true or false)
    4. Created_at (time)
    5. Updated_at (time)
