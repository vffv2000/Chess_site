# Project 
This project is a website developed in Python using the Django framework and Django Rest Framework (DRF), and aiogram.
# Description
One of the key features of the project is the presence of an asynchronous bot on the Telegram messenger, which provides interaction with the website database through the API. Thanks to this bot, users can manage their data on the website without leaving the messenger, which simplifies the interaction process and makes it more convenient.

With the help of the asynchronous bot on Telegram, users can easily view articles on the website and manage them without the need to visit the site. The bot provides access to the website database, which allows users to view a list of articles, their descriptions, and content, as well as add new articles or delete existing ones.

When a user wants to view a list of articles, they send a request to the bot, and the bot sends the list of articles in response. The user can choose any article from the list and get its content by sending a request to the bot. The user can also add a new article by sending a request to the bot with the necessary information about the article, and the bot will add it to the website database.

Article deletion works similarly - the user sends a request to delete a specific article, and the bot deletes it from the website database. All actions performed through the bot are instantly updated on the website, which provides a unified and up-to-date set of data for all users.
# Usage

To use the Telegram bot, you need to add it to your Telegram contacts and start a conversation with it. You can then send commands to the bot to view articles, add new articles, or delete existing articles.

The following commands are available:

-   `/start` - start the conversation with the bot.
-   `/help` - display a list of available commands.
-   `/list` - display a list of available articles.
-   `/post <article_id>` - display the content of a specific article.
-   `/add <title>, <description>, <content>` - add a new article to the database.
-   `/delete <article_id>` - delete a specific article from the database.
-   `/ahelp` - display a list of available commands for admins.

# Technologies Used
- Python
> Main programming language used for the project.
- Django
> Web framework used for building the web application.
- Django Rest Framework (DRF)
> RESTful API framework used for building APIs.
- aiogram
> Python framework used for building Telegram bots.
- yaml
> Used for storing and reading configuration settings.
-   HTML
> A markup language used for creating web pages and web applications.
-   CSS
> A stylesheet language used for describing the presentation of a document written in HTML.


# How to Run
- Clone the repository
- Create a virtual environment and activate it
- Install the required packages using the command pip install -r requirements.txt
- Create a file named .env and add the necessary environment variables (Telegram bot token, database information)
- Run the server using the command python manage.py runserver
- Start the bot by running the command python bot.py


# Contributing

If you want to contribute to the project, you can fork the repository, make your changes, and submit a pull request. Please make sure to follow the coding style used in the project and include tests for your changes.
