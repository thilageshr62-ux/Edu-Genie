# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS/JavaScript educational assistant based on the supplied project documentation.

## Features

- Ask academic questions
- Explain concepts for beginners
- Generate exactly 3 MCQs with 4 options each
- Summarize educational passages
- Generate beginner-to-advanced learning paths
- Interactive quiz answer checking in the browser
- REST API endpoints for every feature
- Health check endpoint
- Environment-variable based Gemini API configuration

## Project structure

```text
EduGenie/
├── main.py
├── config.py
├── gemini_service.py
├── schemas.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── app.js
└── tests/
    └── test_app.py
```

## Windows CMD setup

Open CMD inside the extracted `EduGenie` folder.

### 1. Check Python

```bat
python --version
```

Python 3.10 or newer is recommended.

### 2. Create a virtual environment

```bat
python -m venv .venv
```

### 3. Activate it

```bat
.venv\Scripts\activate
```

You should see `(.venv)` at the start of the CMD line.

### 4. Install dependencies

```bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Create the environment file

```bat
copy .env.example .env
```

Open `.env` in VS Code and replace:

```text
GEMINI_API_KEY=your_api_key_here
```

with your real Gemini API key.

You can also change the model in `.env`:

```text
GEMINI_MODEL=gemini-3.8-flash
```

### 6. Start EduGenie

```bat
python -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## API documentation

FastAPI automatically provides:

```text
http://127.0.0.1:8000/docs
```

and:

```text
http://127.0.0.1:8000/redoc
```

## Test the project

With the virtual environment active:

```bat
pytest
```

## Stop the server

Press:

```text
CTRL + C
```

## Deactivate the virtual environment

```bat
deactivate
```

## Important

Never commit or share your `.env` file because it contains your API key.

If your API key is missing, the application will show a clear configuration error instead of silently failing.

## Troubleshooting

### `python` is not recognized

Install Python 3.10+ and enable "Add Python to PATH", then open a new CMD window.

### `pip` is not recognized

Use:

```bat
python -m pip install -r requirements.txt
```

### Gemini API key error

Check that `.env` exists in the same folder as `main.py` and contains:

```text
GEMINI_API_KEY=your_real_key
```

Then restart Uvicorn.

### Model not available

Change `GEMINI_MODEL` in `.env` to a model currently available to your Gemini API account.

### Port already in use

Run:

```bat
python -m uvicorn main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001
```
