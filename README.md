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
- Accesses it, updates `PIP` and installs the required packages
- Generates a `requirements.txt` file
- Creates a `.env` file
- Creates an `api` directory with a basic application template for `FastAPI`
- Creates a `template` directory with some basic `Jinja2` template files
  - Such as a `_base.html` and `index.html`
- Creates a `static` files directory for storing `css`, `js`, and `img` files locally (name can be set in `config.py` as either `static`, `public`, or `assets`)
  - Adds `TailwindCSS`, `Flowbite`, `HTMX`, and `AlpineJS` static files


## Dependencies

The tool is intended to be dynamic and aims to install the most recent packages where possible. To do this, we require [NodeJS](https://nodejs.org/en), `NPM` and [Python](https://www.python.org/downloads/) to be installed on your local machine, with the latest stable versions. 

We use `node_modules` and `PIP` to maintain the latest versions of the core stack, and remove the `node_modules` after creation to simplify the project folder.

Fortunately, `Tailwind` has a [Standalone CLI](https://tailwindcss.com/blog/standalone-cli) that allows us to watch and minify files without needing `NodeJS`!


### Customisation and Configuration

By default, you can add whatever files you want to the tool as long as they are stored in the `setup_assets` folder. Feel free to explore the default one that comes pre-configured with the tool. Here a few things to note:
- All the files are added to the `project` root directory
- Static files **MUST** be stored in a `setup_assets/static` folder
- The static folder name is changed dynamically based on the `config.py` `STATIC_FILES_DIR` variable

There are a few other configurable options in `config.py`, such as `PIP_PACKAGES` and additional `.env` parameters that you can setup too.


### Creation
1. To get started, clone the repository, enter the folder and run `create` with a `name` (e.g., `my_project`) argument inside a `poetry shell`. This creates a new project inside the `parent` directory of the `fastapi-quickstart` directory:

```bash
git clone https://github.com/Achronus/fastapi-quickstart.git
```

```bash
cd fastapi-quickstart
```

```bash
poetry shell
```

```bash
create my_project
```

For example, if you have a parent folder called `projects` and are making a project called `todo_app` the project is created in `projects/todo_app` instead of `projects/fastapi-quickstart/todo_app`.


### And That's It!
Everything is setup with a blank template ready to start building a project from scratch.

Simply, enter the new project folder:

```bash
cd ../my_project
```

Access the poetry shell:
```bash
poetry shell
```

Run the server in one terminal and open `localhost:8000` (or `127.0.0.1:8000`) in your browser:

```bash
run
```

And watch `TailwindCSS` in another (remember to be in a `poetry shell`!):

```bash
watch
```

## Folder Structure

The newly created project should look similar to the following:

```bash
project_name
└── project_name
|   └── assets
|   |   └── css
|   |      └── flowbite.min.css
|   |      └── input.css
|   |      └── output.css
|   |   └── imgs
|   |   |   └── avatar.svg
|   |   └── js
|   |      └── alpine.min.js
|   |      └── flowbite.min.js
|   |      └── htmx.min.js
|   |      └── theme-toggle.js
|   └── database
|   |   └── __init__.py
|   |   └── crud.py
|   |   └── models.py
|   |   └── schemas.py
|   └── templates
|   |   └── components
|   |   |   └── navbar.html
|   |   └── _base.html
|   |   └── index.html
|   └── tests
|   |   └── __init__.py
|   └── .env
|   └── .gitignore
|   └── main.py
|   └── tailwind.config.js
|   └── tailwindcss
└── poetry.lock
└── pyproject.toml
└── README.md
└── requirements.txt
```
