<!-- Please update value in the {}  -->

<h1 align="center">Django Blog App</h1>

<div align="center">
  <h3>
    <!-- <a href="http://esadd.pythonanywhere.com/">
      Demo
    </a> -->
     | 
    <a href="https://github.com/esadakman/django-blog-app">
      Project
    </a> 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Built With](#built-with)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

![dj-blog-app](https://user-images.githubusercontent.com/98649983/190132200-98912acc-fc58-4c6d-a744-f1a28fba731e.gif)

### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- HTML
- CSS
- JS
- Django
- Bootstrap
- SASS

## Project Structure

```bash
.──── django-blog-app (repo)
│
├── main
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│─── blog
│     │── __init__.py
│     ├── __pycache__
│     ├── admin.py
│     ├── apps.py
│     ├── migrations
│     ├── models.py
│     ├── static
│     │   └── blog
│     │       ├── images
│     │       │   └── logo.png
│     │       ├── css
│     │       │   ├── main.scss
│     │       │   └── style.css
│     │       └── js
│     │           └── app.js
│     ├── templates
│     │   └── blog
│     │       ├── home.html
│     │       ├── likes_area.html
│     │       ├── post_confirm_delete.html
│     │       ├── post_detail.html
│     │       ├── post_form.html
│     │       └── post_detail.html
│     ├── tests.py
│     ├── urls.py
│     └── views.py
├──── users
│      ├── __init__.py
│      ├── __pycache__
│      ├── admin.py
│      ├── migrations
│      ├── apps.py
│      ├── forms.py
│      ├── models.py
│      ├── signals.py
│      ├── models.py 
│      ├── templates
│      │   └── users
│      │       ├── login.html
│      │       ├── profile.html 
│      │       └── register.html
│      ├── tests.py
│      ├── urls.py
│      └── views.py
│─── templates
│      ├── base.html
│      ├── footer.html
│      └── navbar.html
├─── media
│      ├── profile_pics
│      ├── user_directory_path
│      ├── blog_default_png
│      └── default.webp
├── manage.py
├── db.sqlite3
├── requirements.txt
└── .env

```

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/esadakman/django-blog-app

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Add .env file for secret key

# Run the app
    $ python manage.py runserver
```

## Acknowledgements

- Created a Blog application with Django that allows users to create, edit and delete posts.
- The homepage lists all blog posts and each post has a dedicated detail page for comments and likes.

## Contact

- Website [@esadakman](https://esadakman.github.io/)
- GitHub [@esadakman](https://github.com/esadakman)
- Linkedin [@esadakman](https://www.linkedin.com/in/esadakman/)