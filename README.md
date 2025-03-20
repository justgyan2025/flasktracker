# Investment Portfolio Tracker

A Flask-based web application for tracking financial investments including stocks, mutual funds, and NPS (National Pension System).

## Features

- Dashboard with portfolio overview
- Stocks portfolio management
- Mutual funds tracking
- NPS investment tracking
- Firebase Firestore integration for data storage
- Responsive design using Tailwind CSS

## Prerequisites

- Python 3.8 or higher
- Firebase account and project
- Firebase service account key

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd investment-tracker
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Firebase:
   - Create a new Firebase project
   - Enable Firestore Database
   - Generate a service account key (JSON file)
   - Save the service account key as `serviceAccountKey.json` in the project root

5. Configure environment variables:
   - Copy the `.env.example` file to `.env`
   - Update the Firebase configuration values in `.env`

6. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
investment-tracker/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
├── serviceAccountKey.json  # Firebase credentials
└── templates/         # HTML templates
    ├── base.html     # Base template with navigation
    ├── dashboard.html
    ├── stocks.html
    ├── mutual_funds.html
    └── nps.html
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 