## Install Python 3.10
To get started, you need to install Python 3.10. You can download Python from the official Python website at python.org.

### Windows:

Download the installer and run it.
Make sure to select the "Add Python 3.x to PATH" option during installation.

### Linux:
```
sudo apt update
sudo apt install python3.10
```

### MacOS
```
brew install python@3.10
```

## Install Flask
After installing Python, you need to install Flask, a web framework for Python.

``` pip install Flask ```

## Training a GPT4all Model

### Clone the GPT4All Repository:
`git clone https://github.com/gpt4all/gpt4all.git`
Follow the instruction of GPT4All model with Python version 3.10

## Modify directory used in chat.py file
In line 8, change your suitable directory in MODEL_NAME parameter

## Run Flask
Use the `flask run` command to start the development server.
`flask run`

## Test with Postman
Go to [Postman](https://www.postman.com), enter URL: http://127.0.0.1:5000/chat with POST method, the body is input_text for key and value is your input.
