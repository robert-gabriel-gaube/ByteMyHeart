  Welcome file 

Welcome to ByteMyHeart!
=======================

This is a file meant for showcasing how to run and use the application ByteMyHeart created in Django.

How to get the application
==========================

Clone the repository like this:

git clone [https://github.com/robert-gabriel-gaube/ByteMyHeart.git](https://github.com/robert-gabriel-gaube/ByteMyHeart.git)

Setup your python
-----------------

Firstly you should have python installed. In the making of this project we used Python 3.11.2.  
If you don’t have python installed, you can get it here.  
[https://www.python.org/](https://www.python.org/)

(Optional) Create a venv (virtual environment)
----------------------------------------------

For python projects you can create virtual environments. They are basically lightweight containers in which you can install the dependencies you need to run certain applications.  
You can create a venv like this:

    python -m venv /path/to/new/virtual/environment
    

After that you can start the virtual environment using one of these commands

    # For linux systems
    source /path/to/new/virtual/environment/Scripts/activate
    # For windows systems
    cd /path/to/new/virtual/environment/Scripts/
    activate.bat
    

Installing dependencies
-----------------------

You can install dependencies using the following command in the ByteMyHeart folder

    pip -m install requirements.txt
    

Setting up the project
----------------------

Before you can run the project you need to run the following command

    python manage.py migrate
    

Running the application
-----------------------

You can start running the application using this command

    python manage.py runserver
    

After running this command follow the link that will be displayed in the terminal

Tests
=====

We created some tests for validating some code. You can run this command for running these tests.

    python manage.py test
    

And for seeing the coverage, run this command

    coverage run ./manage.py test