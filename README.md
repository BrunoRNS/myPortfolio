# Archived Portfolio

> **This repository is archived and is no longer maintained.**

This portfolio was originally built based on the excellent **developer-portfolio** template by **hhhrrrttt222111**, adapted by me to run in a Django environment instead of Node.js.

The live website is no longer available, and some links, references, and project information in this repository are outdated. Rather than removing it, I decided to keep it archived as a record of my previous work and as an example of how I customized and extended the original template.

Although this project is no longer maintained, it represents an important step in my learning journey and showcases part of my earlier frontend and Django work. My current portfolio is now the procedural-generated one developed for SerisLab.

Thank you for stopping by!

# Bruno RNS - Personal Portfolio

This is the source code for my personal portfolio, built with Django. It showcases my skills, projects, and contact information, and features a contact form that sends notifications via GitHub issues for me.

> It is based on [developer portfolio - of hhhrrrttt222111](https://github.com/hhhrrrttt222111/developer-portfolio). This repository gives a more complete template, it was made to run in node.js but I have adapted it to run in django context.

## Features

- **Modern Django Web App**: Built with Django 5, using best practices for security and performance.
- **Skills & Projects Showcase**: Displays my technical skills and selected projects with descriptions and links.
- **Contact Form**: Visitors can send messages directly from the site; messages are sent as GitHub issues for notification.
- **Responsive Design**: Works well on desktop and mobile devices.
- **Open Source**: Licensed under the GNU General Public License v3.0.

## Getting Started

### Visit it online

You can visit my portfolio online at [My Portfolio](https://myportfolio-kn09.onrender.com).

### Using it yourself

#### Prerequisites

- Python 3.11+
- python3-virtualenv or python3-venv
- Redis (for caching)
- Docker (optional)

#### Acknowledgements

> You must change the credentials based on .env-example file, if you want to run the app locally. Or if you want to use my Portoflio as template, also remember to change with your data.

#### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/BrunoRNS/myPortfolio.git
   cd myPortfolio
   ```

2. **Set up environment variables:**
   - Copy `.env-example` to `.env` and fill in your secrets:

     ```sh
     cp .env-example .env
     ```

3. **Install dependencies:**

   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Run migrations and collect static files:**

   ```sh
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

5. **Start the development server:**

   ```sh
   python manage.py runserver
   ```

#### Usage

- Visit `http://localhost:8000` to view the portfolio.
- Use the contact form to send a message (requires valid email).

### Testing

Run all Django tests:

```sh
bash tests/testDjango.sh
```

### Deployment

You can deploy using Docker:

```sh
docker build -t myportfolio .
docker run -p 8000:8000 --env-file .env myportfolio
```

## Documentation

For more information, visit the [documentation](docs/DOCS.md).

## Contributing

Contributions are welcome, even though this project is primarily a personal portfolio. If you have any suggestions or find any bugs, please open an issue or a pull request. I'll be happy to discuss and consider them.

## License

This project is licensed under the [GNU General Public License v3.0](docs/LICENSE.md).

## Contact

- [GitHub](https://github.com/BrunoRNS)
- [Discord](https://www.discord.com/users/1353359440266526753)
- Email: <brunoriansouza@gmail.com>

---

Made with ❤ by Bruno RNS
