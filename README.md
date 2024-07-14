# Personal Blog Website

This is a personal blog website built using Django, HTML, CSS, and Python. It allows you to manage your blog content through a user-friendly admin panel with features for data manipulation and dynamic URL routing.

## Features

- **Admin Panel:** Manage your blog posts and categories easily from the Django admin interface.
- **Dynamic URL Routing:** Ensure clean and SEO-friendly URLs for your blog posts and pages.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS
- **Programming Language:** Python

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/NikhilAmbure/Personal-Blog-Website.git
    cd Personal-Blog-Website
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the admin panel:**
    Open your browser and go to `http://127.0.0.1:8000/admin`

## Usage

- Use the admin panel to add, edit, or delete blog posts and categories.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can customize this README further as needed.
