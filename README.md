# Micro Finance Bank Management System - Python Qt Version

A comprehensive Python-based desktop application built with PyQt5 and SQLite for managing micro finance banking operations. This is a fully functional, standalone application designed for Windows/Linux/macOS.

## Features

### Dashboard
- Overview of key metrics
- Recent transactions
- Outstanding loans
- EMI collection status

### Customer Management
- Individual Customer Registration with unique Account Number
- Joint Customer Registration with Account Numbers
- SHG (Self Help Group) Registration with Account Numbers
- Customer profile management
- Document verification

### Loan Management
- Loan Application for all customer types
- Loan Approval workflow
- Loan Sanction process
- Loan status tracking
- Loan disbursement

### EMI Management
- EMI Calculator with various tenure options
- EMI Schedule generation
- EMI Collection tracking
- Payment history
- Defaulter tracking

### Reports
- Customer reports
- Loan reports
- Collection reports
- Financial analysis

## System Requirements

- Python 3.8 or higher
- PyQt5
- SQLite3 (included with Python)
- 2GB RAM
- 500MB disk space

## Technology Stack

- **Frontend**: PyQt5 with Qt Designer
- **Backend**: Python 3.8+
- **Database**: SQLite3
- **Reporting**: ReportLab / Matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/t693883-sys/test.git
   cd test
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Default Login Credentials

- **Username**: admin
- **Password**: admin123

## Project Structure

```
microfinance_bank/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── config.py                  # Configuration settings
├── database.py                # Database setup and initialization
├── ui/                        # UI forms (Qt Designer)
│   ├── main_window.ui
│   ├── login_dialog.ui
│   ├── dashboard.ui
│   ├── customer_forms.ui
│   ├── loan_forms.ui
│   ├── emi_forms.ui
│   └── reports.ui
├── ui_compiled/               # Compiled UI files
│   ├── ui_main_window.py
│   ├── ui_login_dialog.py
│   └── ...
├── modules/                   # Business logic
│   ├── customer.py            # Customer operations
│   ├── loan.py                # Loan operations
│   ├── emi.py                 # EMI calculations
│   ├── payment.py             # Payment processing
│   ├── reports.py             # Report generation
│   ├── auth.py                # Authentication
│   └── validators.py          # Data validation
├── resources/                 # Images, icons, styles
│   ├── images/
│   ├── icons/
│   └── styles.qss
├── dialogs/                   # Custom dialogs
│   ├── customer_dialogs.py
│   ├── loan_dialogs.py
│   └── payment_dialogs.py
├── windows/                   # Main window classes
│   ├── main_window.py
│   ├── login_window.py
│   ├── dashboard_window.py
│   └── customer_window.py
└── utils/                     # Utility functions
    ├── helpers.py
    ├── decorators.py
    └── constants.py
```

## Usage

### Customer Registration
1. Login with admin credentials
2. Navigate to Customer > New Customer
3. Select customer type (Individual/Joint/SHG)
4. Fill in required information including account details
5. System auto-generates unique Account Number
6. Save customer record

### Loan Application
1. Go to Loans > New Loan Application
2. Select customer by Account Number
3. Enter loan details
4. Calculate EMI
5. Submit for approval

### EMI Collection
1. Navigate to Collections > EMI Collection
2. Select customer by Account Number
3. Record payment
4. Generate receipt

## License

Proprietery - All rights reserved

## Author

Micro Finance Management Team
