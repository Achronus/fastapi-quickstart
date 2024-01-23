This branch is specific to creating Large Language Models (LLMs) so the behaviour is slightly different from the main branch.

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
- `sqlalchemy`
- `jinja2`
- `python-dotenv`
- `poetry`

Additional packages installed:
- `langchain`
- `llama-index`

Development packages installed:
- `pytest`
- `pytest-cov`
- `hypothesis`

_Note: all libraries and packages are automatically installed to their latest versions when running the tool._

## Why This Tool?

Creating a project from scratch can be a tedious process. So, I wanted to simplify it! This tool is ideal for those that are looking to quickly prototype a project without worrying about `JavaScript` frameworks, such as `Backend Developers` and `ML Engineers`.

The tool does the following:

- Creates a virtual environment in the project folder
- Accesses it, updates `PIP` and installs the required packages
- Creates a `.env` file
- Creates a `backend` directory with a basic application template for `FastAPI`
- Creates a `frontend` directory with some basic `Jinja2` template files
  - Such as a `_base.html` and `index.html`
- Creates a `frontend/public` files directory for storing `css`, `js`, and `img` files locally
  - Adds `TailwindCSS`, `Flowbite`, `HTMX`, and `AlpineJS` static files
- Performs some file cleanup such as removing `node_modules` (if your OS supports TailwindCSS standalone CLI), `venv` and `package.json` files

## Dependencies

The tool is intended to be dynamic and aims to install the most recent packages where possible. To do this, we require [NodeJS](https://nodejs.org/en), `NPM` and [Python](https://www.python.org/downloads/) to be installed on your local machine, with the latest stable versions. 

We use `node_modules` and `PIP` to maintain the latest versions of the core stack, and remove the `node_modules` after creation to simplify the project folder.

Fortunately, `Tailwind` has a [Standalone CLI](https://tailwindcss.com/blog/standalone-cli) that allows us to watch and minify files without needing `NodeJS`!


### Customisation and Configuration

All files added to the project are stored in `setup_assets`. If you want add files, feel free but it is recommended not to mess with the file structure. Here a few things to note:
- All the files are added to the `project` root directory
- Static files **MUST** be stored in a `setup_assets/frontend/static` folder
- The static folder name is changed dynamically during project creation from `frontend/static` -> `frontend/public`

For configuration customisation go to `config.py` in the root directory. Here you have three options:
- Changing the database URL -> `DATABASE_URL`, defaults to a SQLite local database.
- Adding additional PIP packages to the project -> `ADDITIONAL_PIP_PACKAGES`
- Adding additional `.env` file variables -> `ENV_FILE_ADDITIONAL_PARAMS`

Note: the last two options are treated as python `list` objects that accept `strings` only.


### Creation
1. To get started, clone the repository, enter the folder and run `create` with a `name` (e.g., `my_project`) argument inside a `poetry shell`. This creates a new project inside the `parent` directory of the `fastapi-quickstart` directory:

```bash
git clone https://github.com/Achronus/fastapi-quickstart.git
cd fastapi-quickstart
poetry shell
create my_project  # Replace me with custom name!
```

For example, if you have a parent folder called `projects` and are making a project called `todo_app` the project is created in `projects/todo_app` instead of `projects/fastapi-quickstart/todo_app`.


### And That's It!

Everything is setup with a blank template ready to start building a project from scratch. Run the following commands to run the docker `development` server and watch `TailwindCSS` locally!

Not got Docker? Follow these instructions from the [Docker website](https://docs.docker.com/get-docker/).


```bash
cd ../my_project  # Replace me with custom name!
docker-compose up -d --build

poetry shell
poetry install

watch
```

Then access the site at [localhost:8080](http://localhost:8080).


## Folder Structure

The newly created project should look similar to the following:

```bash
project_name
└── config
|   └── docker
|   |   └── Dockerfile.backend
└── project_name
|   └── backend
|   |   └── database
|   |   |   └── __init__.py
|   |   |   └── crud.py
|   |   |   └── models.py
|   |   |   └── schemas.py
|   |   └── routers
|   |   |   └── __init__.py
|   |   └── tests
|   |   |   └── __init__.py
|   |   └── utils
|   |   |   └── __init__.py
|   |   └── .env
|   └── frontend
|   |   └── public
|   |   |   └── css
|   |   |   |   └── flowbite.min.css
|   |   |   |   └── input.css
|   |   |   |   └── style.min.css
|   |   |   └── imgs
|   |   |   |   └── avatar.svg
|   |   |   └── js
|   |   |       └── alpine.min.js
|   |   |       └── flowbite.min.js
|   |   |       └── htmx.min.js
|   |   |       └── theme-toggle.js
|   |   └── templates
|   |       └── components
|   |       |   └── navbar.html
|   |       └── _base.html
|   |       └── index.html
|   └── build.py
|   └── main.py
|   └── tailwind.config.js
|   └── tailwindcss OR tailwindcss.exe
└── .dockerignore
└── .env
└── .gitignore
└── database.db
└── docker-compose.yml
└── poetry.lock
└── pyproject.toml
└── README.md
```
