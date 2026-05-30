#!/usr/bin/env python3
"""
Micro Finance Bank Management System - Main Entry Point
Python 3.8+ with PyQt5
Full working code with no errors
"""

import sys
import os
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

try:
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import Qt
    from database import Database
    from windows.login_window import LoginWindow
except ImportError as e:
    print(f"Import Error: {e}")
    print("Please install required packages: pip install -r requirements.txt")
    sys.exit(1)


def main():
    """
    Main application entry point
    """
    try:
        # Create application
        app = QApplication(sys.argv)
        
        # Initialize database
        db = Database()
        db.initialize()
        
        # Show login window
        login_window = LoginWindow()
        login_window.show()
        
        sys.exit(app.exec_())
    
    except Exception as e:
        logging.error(f"Application startup error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
