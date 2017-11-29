# Assignment 3- Unicornatron webapp support site.

## Overview

### What is this website for?

This website is a coursework assignment for module 3 of the code institutes web development course.

### The goal?

The goal for this assignment is to produce a support and developement site for the "Unicornatron", a fictional unicorn attractor app. The site is to allow users to request features, to be implimented into the fictional app and then donate money to cover development fees of the features they wish to support. Progress is to be tracked via a "todo" application. Additionally, users will to be able to voice their oppinions and vote in polls set out by the dev team and other community members via a forum app on the website. Finally, to assist with keeping our fictional app users in the loop, a blog app will also be included to allow the dev team to give detailed updates about what is being worked on and provide a more in depth status update of current tasks.

## Features 

### Existing Features
- Simple, clear & responsive bootstrap layout.
- Stacked column navbar and clear bootstrap buttons allow for easy site navigation.
- Login system with support for new users to register. Further to this, users are able to reset their passwords if required via e-mail link service.
- Todo app. This displays a list of all current projects in development and provides a status update for each. Selecting the title of each task takes the user to a seperate details page where they can review the current task along with any additional notes related to the progress of the feature being reviewed. In the detail view, the user is provided with the date/ time when the feature's todo entry was last updated.
If users want to request a new feature, they can do so via "add todo". This takes the user to a bootstrap form which when submitted, adds the requested task to the todo list. Once accepted, the admin can add a status and update the todo task entry.
- Funding app allows admins to set payment options for tasks in the todo. Once added the app should list the new entry, price and provide a paypal link. Users can follow this link to donate towards their select app
- Blog app. As noted above, this allows users to view blog entries made by the dev team. No front end access to create blogs as this section is intended for admin use only. Users are to use the forums for communication etc.
- Forum app allowing users to communicate about various app topics. Also support for user and admin generated polls to guage community opinion regarding features to go into development etc.
- Site layout generated via django jinja templating, allowing fast changes for future site updates.
- page footer.

### Features Left to Implement
- Navbar shrink? (might leave as currently works quite well)
- Flesh out site content.
- additional images? Quite spartain atm though all features have been added
- investigate forum poll bug (post button only works once polls have been filled. can untick after to post.)
- E-mail link for password reset is not connected to a mail service.
- Paypal links to sandbox paypal site.

## Tech Used

### Some the tech used includes:

- [pip]
    - **pip**, used by the windows console to manage and install the required addons/ python packages to support this site.

- [django]
	- **django** Is the framework used to produce the site.

- [django-bootstrap](http://getbootstrap.com/)
	- **django-bootstrap** provides much of the basic CSS styling for the site, as well as navigation. Allways for a clean, clear and responsive layout which adapts to different screen sizes.

- [bower](https://bower.io/)
	- **Bower** is used to manage the installation of our libraries and frameworks.

- [django-paypal]
	- **django-paypal** plugin to allow for the django site to interface with paypal's services including allowing for the buy now button. (See funding seciton.)

- [node.js]
	-**node.js** a JavaScript run-time environment for executing JavaScript code server-side.

- [django-emoticons]
	-**django-emoticons** plugin used to allow users to post emoticons in the forum via text entry. e.g. :) provides a smiley face emoticon.

- [arrow]
	-**arrow** allows for creating formatting and converting dates, times, timestamps etc.

- [jinja2]
	-**jinja2** reduces the amount of code required for templating and provides ease of use when linking multiple template elements.

- [django-tinymce]
	-**django-tinymce** implimented in the forum section to allow users to create posts via a "TinyMCE" editor.	

- [Heroku](https://signup.heroku.com/)
	- **Heroku** is the online platform used to host the Flask app (site).