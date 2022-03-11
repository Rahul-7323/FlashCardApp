<br>

# Flashcard App

## About The Project
<ul>
<li>
A flashcard is a card bearing information on both sides, which is intended to be used as an aid for memorization.</li>
<li>The front portion of a flashcard contains a cue or a question or a hint and the back portion of the flashcard contains the answer to it. 
</li>
<li>
A deck is a collection of related cards. For example, a Japanese Deck contains Cards related to the Japanese language where the front portion of each card could be a word in English and the back portion of the card is the Japanese translation of the English word.
</li>
<li>
In this project, a web application has been developed using python which implements these flashcards with many features such as having multiple user profiles with different decks, multiple deck storage, deck and card management, a review system to test your memorization, a dashboard, the ability to import/export decks, proper login system and an aesthetically satisfying user interface.
</li>
</ul>


### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
* [Flask-Security](https://pythonhosted.org/Flask-Security/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
* [SQLite](https://www.sqlite.org/index.html)
* [Bootstrap](https://getbootstrap.com/)
<br><br>


## Getting Started

This guide will assume that you are running the code on replit, the same instructions can be easily recreated in any other code editor or IDE. Before starting, please make sure that the project folder contains the following files: `.replit`, `requirements.txt`, `run.sh`, `local_setup.sh`, `local_run.sh`. <b>DO NOT CHANGE THE CONTENTS OF THESE FILES AT ANY COST.<br>
</b><br><br>


## Simple way to run the application

I have already written the appropriate scripts that are required to start the application. All that you have to do is click the `Run` button on the top of the page.<br><br>

## Complex way to run the application
If clicking the `Run` button doesn't work (This happens occasionally due to some bug in replit), then follow the below method instead.



-  ### Prerequisites

   Open the Shell window present near the bottom in replit page and type the following command. This command will run `local_setup.sh` file which will install all the dependencies required for running the application from the `requirements.txt` file.
   ```sh
   sh local_setup.sh
   ```



-  ### Running the application

   After running `local_setup.sh`, type the following command in the same Shell window. This will start the application and will open a web view inside the replit page. In the right corner of the web view, there will be an option called `open in a new tab`, click it to open the entire web application in a separate tab on the browser.
   ```sh
   sh local_run.sh
   ```



## Usage

After the application is up and running, you can start using and play around with its features. For any doubts related to using the app, please watch the [presentation video](https://drive.google.com/file/d/1r1wO9ef5dyex0drmyKPv82QaKSuxgoAv/view?usp=sharing).
<br>
As part of the application, a dummy user has already been populated in the database with few decks already pre-loaded for demonstration purposes. The dummy user can be accessed with the following Login Credentials:<br>
```py
email = "dummy@gmail.com"
password = "password"
```
Also, a folder called `Decks` with 3 decks containing some sample data are provided in the project submission file in order for you to test the *import* feature without the hassle of creating a txt file by yourself and also for entering some sample data using the *add cards* feature easily.<br><br>



## Tips for better experience

For some reason, the application has a better performance and lesser loading speeds in Edge browser when compared to the Chrome browser. Therefore, it is recommended that you copy the URL for the web application and paste it to the Edge browser and use it there.
<br><br>

Project Replit Link: [Click Here](https://replit.com/@RahulM7323/Flashcard-App?v=1)<br>
Presentation Video Link:
[Click Here](https://drive.google.com/file/d/1r1wO9ef5dyex0drmyKPv82QaKSuxgoAv/view?usp=sharing)<br>
Project Report Link:
[Click Here](https://drive.google.com/file/d/1bDZvSikplgzy7gyI3TnfW_dn0-TY0otN/view?usp=sharing)
## Contact

Rahul M - <21f1002513@student.onlinedegree.iitm.ac.in>

