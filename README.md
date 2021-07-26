# FinalProject
Final Project 3
This was the final project for the Northwestern Bootcamp. Due to scheduling and outside conflicts this is was an individual effort for the final group project. The goal for this project was to see how well individual team statistics could predict that a team would make the playoffs


1. Using an API call I pulled the current NHL team based data from 2020 and 2021
2. I removed direct leading data (W/L), as well as less concrete  or pointed data. For this exercise I wanted to keep the data to hard stats (goals, assists, +/-, blocks, hits)
3. The data was the trained using a simple binary logic gate (0 for missing the playoffs, 1 for making the playoffs)
4. The data was trained through the previous season and trained against the 2021 season. The older seasons were protected from use by a paywall at the API. Otherwise I would have utilized more training points. 

![Data Cleaning](images/sklearnsnapshot.jpg)

5. I utilized the machine learning kit SKlearn (utilizing the poly kernel) to create a model. 

![Saving as Model](images/savingasmodel.jpg)


6. I saved the model, and then the team data as a CSV.

7. Using flask I created a simple interactive webpage, reading the CSV data while utilzing the prediction model. 

8. Once I got the functionality working I hosted the page on heroku to allow for user input. 


![Web App](images/webapp.jpg)