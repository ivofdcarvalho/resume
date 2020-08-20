# Resume Project

This project aims to develop my skills as a developer by forcing me to use technologies that I don't usually practice. At the same time, this project also serves to create a curriculum page to present to anyone who might be interested.
The following technologies will be used:

 - **HTML**
 - **CSS**
 - **JavaScript**
 - **PHP**
 - **Python**
 - **SQL**
 - **Docker**
 - **Nginx**
 
Implemented so far:
 - [x] **FrontEnd**
 - [ ] **BackEnd**
 - [ ] **Database**
 - [x] **Docker**

## FrontEnd
##### This section will be implemented with HTML, CSS and  JavaScript.

The **FrontEnd** will consist in a simple web page to display some pertinent information about the Resume.
It uses **JavaScript** to create the carousel made in **HTML** (it intentionally avoids using Bootstrap in order to provide a bigger challenge).

## BackEnd
##### This section will be implemented with Python and PHP.

The **BackEnd** consist of **PHP** code to send an email with the data filled on the **FrontEnd** form and **Python** code to communicate with the **Database** and provide the data for the **FrontEnd**. The intent is to provide a dynamic project where the data is easy to update.

## Database
##### This section will be implemented with SQL 

As a personal preference the **Database** will be implemented using **MySQL**. The diagram can be consulted in the corresponding folder.

## Docker
##### This section will be implemented with Docker (duh!) and Nginx

This project will be converted to **Docker** in order to be easy to deploy it without having to worry about the dependencies and environment.\
Its using **Nginx** to self host the webpage.\
To use the project change the '.env copy' file to '.env' and make the necessary changes to your use case.\
The image **MailHog** is being used to handle the emails and to configure it we need to access http://localhost:8025/.\
For more detail on how to use **MailHog** consult this [URL](https://phauer.com/2017/test-mail-server-php-docker-container/).
