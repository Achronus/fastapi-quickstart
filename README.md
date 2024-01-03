# FastAPI Project Quickstart Tool

Welcome to the quickstart tool for creating a `FastAPI` project with the following stack:

- [FastAPI](https://github.com/tiangolo/fastapi)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [TailwindCSS](https://tailwindcss.com/) and [Flowbite](https://flowbite.com/)
- [AlpineJS](https://alpinejs.dev/)
- [HTMX](https://htmx.org/)

The default pip packages installed include:

- `fastapi`
- `uvicorn[standard]`
- `jinja2`
- `python-dotenv`

_Note: all libraries and packages are automatically installed to their latest versions when running the tool._

## Why This Tool?

Creating a project from scratch can be a tedious process. So, I wanted to simplify it! This tool is ideal for those that are looking to quickly prototype a project without worrying about `JavaScript` frameworks, such as `Backend Developers` and `ML Engineers`.

The tool does the following:

- Creates a virtual environment in the project folder
- Accesses it, updates pip and installs the required packages
- Generates a `requirements.txt` file
- Creates a `.env` file
- Creates an `api` directory with a basic application template for `FastAPI`
- Creates a `template` directory with some basic `Jinja2` template files
  - Such as a `_base.html` and `index.html`
- Creates an `assets` directory for storing `css`, `js`, and `img` files locally
  - Adds `TailwindCSS`, `Flowbite`, `HTMX`, and `AlpineJS` static files


## Dependencies

For this tool to work, we require [NodeJS](https://nodejs.org/en), `NPM` and [Python](https://www.python.org/downloads/) to be installed on your local machine.

We use `node_modules` to maintain the latest versions of the core stack (`AlpineJS`, `TailwindCSS`, and `Flowbite`), but remove them from the project after use.


### Configuration

By default, the static files are located in `assets` and template files in `templates`. These are changable in the `config.py` file in the root directory.

There are a few other configurable options in there too, such as `PIP_PACKAGES` and additional `.env` parameters. Refer to `config.py` for more details. 


### Creation
1. To get started, clone the repository, enter the folder and run `setup.py` with a `name` (e.g., `my_project`) argument and apply the `--outside` flag. This creates a new project inside the `parent` directory of the `fastapi-quickstart` directory:

```bash
git clone https://github.com/Achronus/fastapi-quickstart.git
```

```bash
cd fastapi-quickstart
```

```bash
python setup.py my_project --outside
```

For example, if you have a parent folder called `projects` and are making a project called `todo_app` the project is created in `projects/todo_app` instead of `projects/fastapi-quickstart/todo_app`.

Simply remove the flag if you want the project installed in the `fastapi-quickstart` directory.


### Replacing A Project With the Same Name
Looking to replace an existing project with the same name? Use the `--force` flag to delete the old project and create a new one!

```bash
python setup.py my_project --outside --force
```

### And That's It!
Everything is setup with a blank template ready to start building a project from scratch.

Simply, enter the new project folder:

```bash
# If using the --outside flag
cd ../my_project
```

```bash
# Otherwise
cd my_project
```

Access the virtual environment:
```bash
# Windows
venv\Scripts\activate
```

```bash
# Linux/Mac
source venv/bin/activate
```

Run the `uvicorn` server in one terminal and open `localhost:8000` (or `127.0.0.1:8000`) in your browser:

```bash
uvicorn main:app --reload
```

And watch `TailwindCSS` in another (remember to be in the `my_project` folder!):

```bash
tailwindcss -i assets/css/input.css -o assets/css/output.css --watch --minify
```

_Note: while `Node` and `NPM` are needed for the install, we don't use them in the project itself!_

## Folder Structure

The newly created project should look similar to the following:

```bash
project_name
└── assets
|   └── imgs
|   |   └── avatar.svg
|   └── css
|      └── flowbite.min.css
|      └── input.css
|      └── output.css
|   └── js
|      └── alpine.min.js
|      └── flowbite.min.js
|      └── htmx.min.js
|      └── theme-toggle.js
└── templates
|   └── components
|   |   └── navbar.html
|   └── _base.html
|   └── index.html
└── venv
|   └── ...
└── .env
└── .gitignore
└── requirements.txt
└── tailwind.config.js
└── tailwindcss
```
