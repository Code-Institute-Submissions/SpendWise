## Testing 

## Table of Contents
--------------------------------------

<br>

- [Testing Strategy](#testing-strategy)
- [User story testing](#user-story-testing)
- [Validator Testing](#validator-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)


------

<br>

## Testing Strategy

<br>

<br>

- I decided on a manual testing strategy for the development of the site. I did this to ensure the website is user-friendly and check issues with navigation, layout, and usability that may not be apparent through automated testing.


<br>


------------

<br>


<br>

## User Story Testing

<br>
<br>

#### Epic 1: User Register
-----------

<br>

#### User story 1: Sign-up

<br>

> As a site user I can sign-up so that I use the website
- Acceptance Criteria 1: Given when I click the register button, then the website displays the register form.
- Acceptance Criteria 2: Given when I fill out a username and password, then I have an account on website.

### All tests passed

----------

<br>

### User story 2:  User Login

<br>

> As a site user I can login into my account so that use the website
- Acceptance Criteria 1: Given when I click the login button, then the website displays the login form.
- Acceptance Criteria 2: Given when I fill in my username and password, then I can login into my existing account.

### All tests passed

----------

<br>

### User story 3:  User Logout
<br>

> As a site user I can logout of my account so that I can stop using website features.
- Acceptance Criteria 1: Given when I click the logout button, then the website displays the logout page.
- Acceptance Criteria 2: Given when I click the signout button, then my account is logged out.

### All tests passed

----------

<br>

### Epic 2: CRUD
--------

<br>

###  User story 4: See expenses
<br>

>As a site user I can see my expenses that were added so that track my spending
- Acceptance Criteria 1: Given when I view expenses main page, then the website displays all my expenses.


### All tests passed

----------

<br>

### User story 5: Add expenses
<br>

>As a site user I can see my expenses that were added so that I keep track of all expenses
- Acceptance Criteria 1: Given when I click the add expense button, then the website displays the  add expense form
- Acceptance Criteria 2: Given when I submit the form, then the expense is diplayed.

### All tests passed

----------

<br>


### User story 6:  Update expenses 
<br>

>As a site user I can edit an expense so that I make changes to my expenses
- Acceptance Criteria 1: Given when I click the edit expense button, then the website displays the edit expense form.
- Acceptance Criteria 2: Given when I click the submit button, then the expense is updated.

### All tests passed

----------

<br>

###  User story 7: Delete expenses
<br>

>As a site user I can delete an expense so that I delete an expense that I dont want
- Acceptance Criteria 1: Given when I click the delete expense button, then the expense is removed from expenses page

### All tests passed

----------

<br>




## Validator testing
<br>

----------

<br>




## Python pep 8

<br>


All the custom Python code was was tested manually thoughout the project and with the following pep8 validator.



<br>
<br>


### views.py 
<br>

- Test passed

<br>

![alt text](static/images/viewspep8.JPG)

<br>

---------------------
<br>

### models.py 

<br>

- I left these line length errors as they dont affect readability

<br>

![alt text](static/images/modelspep8.JPG)

<br>

---------------------
<br>

### urls.py (app)

<br>

- Test passed

<br>

![alt text](static/images/eurlspep8.JPG)

<br>

---------------------

<br>

### urls.py (project)

<br>

- Test passed

<br>

![alt text](static/images/urlspep8.JPG)

<br>

---------------------

<br>

### forms.py 

<br>

- Test passed

<br>

![alt text](static/images/formspep8.JPG)

<br>

---------------------
<br>

### settings.py 

<br>

- I left these errors as they dont affect readability

<br>

![alt text](static/images/settingspep8.JPG)

<br>

---------------------

<br>
<br>

## Jshint



<br>
<br>

### main.js 

<br>

- Test passed

<br>

![alt text](static/images/jsfile.JPG)

<br>

----------------

<br>



<br>


## WC3 HTML Validatior

<br>

--------------

<br>


### home_page.html

<br>

- Test passed

<br>

![alt text](static/images/homehtml.JPG)

<br>

---------------------
<br>

### expenses_page.html

<br>

- Test passed

<br>

![alt text](static/images/expenseshtml.JPG)

<br>

--------

<br>

<br>

## WC3 CSS Validatior

<br>

-------

<br>



### style.css

<br>


- Test passed

<br>


![alt text](static/images/css.JPG)

<br>

---------------------

<br>
<br>

## Light house testing




----------

<br>

- Main pages

<br>

![alt text](static/images/ligth2.JPG)

<br>

![alt text](static/images/ligth1.JPG)

<br>

------------------

<br>


<br>

## Manual Testing

<br>

----
<br>

### Site responsiveness

<br>

- I manually tested the responsiveness of the website on many devices. I used Chrome DevTools to simulate different screen sizes also. I made sure there were not significant issues such as overlapping text, images not scaling properly, and buttons that are difficult to click. 

<br>

![alt text](static/images/response.JPG)

<br>


---------


<br>

### Browser compatiabiliy 

<br>

- I checked that the website worked in the following browsers: Google Chrome, Mozilla Firefox, Apple Safari, Microsoft Edge. 

<br>

-------

## Bugs

<br>

- Sometimes, the user will get a 404 page error when they try to delete an expense. To reproduce the bug, the user needs to delete a large number of expense items. 

<br>

![alt text](static/images/deletebug.JPG)

<br>

-------

<br>






