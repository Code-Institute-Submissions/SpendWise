# ExpenseAid

## Expense Tracking App
------------------------------------
### put main image here

You can view the site here [here](https://.herokuapp.com/). 


-----

## Table of Contents
--------------------------------------

- [Description](#description)
- [Design](#design)
- [UX](#ux)
- [Agile Development](#agile-development)
- [Features](#features)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)
-
- [Author ](#author)

------

## Description
The expenses tracker app is a website designed to help users track their spending and stay within their budget. With this app, users can easily add expenses as they occur, and the app will automatically calculate the total amount spent.

The user can also set an initial budget and the app will automatically deduct your expenses from your budget, giving you an up-to-date picture of your spending.

To use the app, users start by specifying an initial budget. They can then add expenses by entering the amount spent, along with a description of the expense. The app will subtract the total amount of the expenses from the total budget, so users can easily see how much they have left to spend.

The app is designed to be user-friendly, with a simple interface that makes it easy to enter and track expenses.

Overall, the expenses tracker app is a useful tool for anyone who wants to stay on top of their finances and make sure they are staying within their budget.

#### website description

-------
## Design
-------

#### Mwirefromas
---
1 for home page and 1 for expenses 
*  

### The Sites Ideal User

*
### Site Goals






## Agile Development

### Epics

1. 12345

### User Stories


-----------------------------------------------------------------
### User Stories

I have these user stories that were completed for the project

- Epic 1: User Register
	*  Sign-up - As a site user I can sign-up so that I use the website
	*  User Login - As a site user I can login into my account so that use the website
    *  User Logout - As a site user I can logout of my account so that stop using website features

- Epic 2: Expenses CRUD
	*  See expenses - As a site user I can see my expenses that were added so that track my spending
	*  Add expenses - As a site user I can see my expenses that were added so that I keep track of all expenses
	*  Update expenses - As a site user I can edit an expense so that I make changes to my expenses
	*  Delete expenses - As a site user I can delete an expense so that I delete an expense that I dont want




## Features

**Features planned:**

### User Register
### User Login 
### User Logout
### Budget calculator
### Epxenses CRUD


## Technologies used


- HTML5: Usedfor the structure of the website.

- CSS: To style the website

- JavaScript: Used to add interactiviy to website.

- Python: Used to program django.

- Django: This was the main framework for the website..

- ElephantSQL: Used to host PostgreSQL database.

### Packages used
![alt text](/static/css/pack.JPG)

## Deployment

The site was deployed via Heroku, and the live link can be found here - [Expensed](https://dashboard.heroku.com/apps/expensed)

### Project Deployment

I deployed my project to Herou using the following steps:

- Login to [Heroku](https://www.heroku.com/).
- On the Heroku website, navagate to "Create New App".
- Name the project.
- This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
- Navagage to the Resources Tab and add 'Heroku Postgres' to the Add ons.
- Go to the settings tab, and copy the DATABASE_URL to the Config vars.
- Create an env.py file in the djagno repository. Import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. It should look like this: os.environ["DATABASE_URL"] = "Pasted URL".
- In the env.py file, create a secret key. It should look like this: os.environ["SECRET_KEY"] = " Your Secret key ".
- Copy your secret key and paste it into a Heroku config var. Use SECRET_KEY as the var key.
- Copy and paste the following into your projects settings.py file : from pathlib import Path, import os, import dj_database_url,if os,path.isfile("env.py"):import env.
- Remove djangos insecure key and replace it with: SECRET_KEY = os.environ.get('Your secret key').
- Comment out the database section the setting.py file. Replace it with: DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} .
- Add DISABLE_COLLECTSTATIC to Heroku Config Vars. Set the value to 1.
- Link the file to the templates directory in Heroku. Under the BASE_DIR line, insert the following  { TEMPLATES_DIR = os.path.join(BASE_DIR,'templates') }.
- Change the templates directory to TEMPLATES_DIR. It should look like this 'DIRS': [TEMPLATES_DIR].
- Add Heroku Hostname to ALLOWED_HOSTS. It should look like this:  ALLOWED_HOSTS =["ProjectName.herokuapp.com", "localhost"].
- Create 3 new folders on top level directory: media, static, templates.
- In the Settings.py file - add the STATIC files settings - storagepath, the url, directory path, root path, media url and default file storage path.
-  Make a new file call Procfile. Add the following code: web: gunicorn ProjectName.wsgi
- Add, commit and push all changes to Github.
- Navigate to the deployment tab in Heroku. Link your github repo to Heroku and deploy the branch manually. View the build log for any errors.It will dipslay a link to the live site.


### Forking the project

 
- Sign/regester in to Github and go to my repository at https://github.com/Thomas-Longworth/Expense-tracker .
- Navagage the Fork button at the top right of the page and select it.
- The fork is now created and copied to your repositories.


### Cloning the project
  
- Sign/regester in to Github and go to my repository at https://github.com/Thomas-Longworth/Expense-tracker .
- Select the green ‘code’ button.
- Choose which clone option you want(HTTPS, SSH or Github CLI). 
- Copy the url.
- Open git bash
- Type ‘git clone’ and then paste the URL you copied. Press Enter.

|
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))