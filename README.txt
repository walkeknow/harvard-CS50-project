My CS50 final project "Fifty Words Of GRE" is a Django Web App that serves as a vocabulary assistant
for students preparing for competitive English proficiency exams like the GRE, SAT etc.

Implementation:

1. Model:

    The dataset I used was a long list of advanced words which I passed into a python
    program which returned the serial number and meanings of the word in a dictionary.
    I passed that dictionary into my SQLlite database with models.py

2. View:

    In my views.py I sample the dataset, i.e extract 50 words from the SQLite database
    and pass them as objects to my template in order to allow the user to view and learn
    50 words at a time

3. Template:

    In my templates directory I have an HTML page that displays these words and their meanings
    aesthetically by using files defined in a static directory i.e. an external CSS stylesheet,
    images and downloaded bootstrap files.

I have uploaded my project video on YouTube:

link - https://www.youtube.com/watch?v=OiCKEfKG-b8