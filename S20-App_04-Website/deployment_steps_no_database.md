# Steps to deploy a static Flask website to Heroku

## Git Installation (if not already done)

1. Download and install git from <https://git-scm.com/downloads>.
2. Tell git your email address with `git config --global user.email "my_email@email.com"`. Make sure the email address is inside quotes here.
3. Tell git your username (just pick whatever username) with `git config --global user.name "my_user_name"`. The username should be in quotes.

## Heroku Installation (if not already done)

1. Create an account on www.heroku.com.
2. Download and install Heroku CLI from <https://devcenter.heroku.com/articles/heroku-cli>.

## Virtual Environment Creation (if not already done)

1. Create a virtual Python environment in the directory that contains your app directory with `python -m venv .venv`. Activate the virtual environment with `.venv\Scripts\activate`. Install all the necessary packages, for example `pip install flask`. The virtual environment can be deactivated with `deactivate`.

## HTTP Server Installation (if not already done)

1. Install `gunicorn` with `pip install gunicorn`. Make sure you're using pip from your virtual environment if you have one.

## Configuration Files Preparation (repeat if configuration changed)

1. Create a file named `Procfile` in the main app directory. The file should not have any extension. Then type in this line inside: `web: gunicorn server:app` where `server` should be replaced with the name of your Python script and `app` with the name of the variable holding your Flask app.
2. Create a `requirement.txt` file in the main app directory where the main Python app file is located. You can create that file by running `pip freeze > requirements.txt` in the command line. Make sure you're using pip from your virtual environment if you have one. The `requirement.txt` file should now contain a list of Python packages.
3. Create a `runtime.txt` file in the main app directory and type `python-3.8.2` inside. See <https://devcenter.heroku.com/articles/python-runtimes> for more details.

## Deployment to Heroku

1. Open your computer terminal/command prompt and navigate to the directory where the Python file containing your app code is located.
2. If not already done, initialize a local git repository with `git init`.
3. Add your local application files to git with `git add .`
4. Commit the changes with `git commit -m "first commit"`. Make sure `"first commit"` is inside quotes.
5. Using the terminal, log in to Heroku with `heroku login`.
6. Enter your Heroku email address and password.
7. If not already done, create a new Heroku app with `heroku create my-app-name`. (Run `heroku apps` to list all already created apps.)
8. Before pushing the changes to Heroku, tell Heroku the name of the app you want to use with `heroku git:remote --app my-app-name`.
9. Push the changes to Heroku with `git push heroku master`.
10. That should do it. Go ahead and open your app with `heroku open`.
