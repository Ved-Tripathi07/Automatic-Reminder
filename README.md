# Automated Email Sender

This Python script automates the personalized sending of emails based on the time of day. It utilizes predefined letter templates for morning, afternoon, evening, and night greetings, allowing customization for each recipient.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [Configuration](#configuration)
6. [Execution](#execution)
7. [File Structure](#file-structure)
8. [Sample Usage](#sample-usage)
9. [Notes](#notes)
10. [Contributing](#contributing)
11. [License](#license)

---

## Introduction

The Automated Email Sender is a Python script designed to simplify the process of sending personalized greetings to recipients based on the time of day. By using predefined templates, the script crafts unique messages and sends them via email to designated recipients.

---

## Features

- Sends personalized emails based on the time of day.
- Customizable letter templates for morning, afternoon, evening, and night greetings.
- Easy configuration for email credentials, recipient lists, and file paths.

---

## Requirements

To run this script, ensure you have the following:

- Python 3.x installed
- Necessary Python packages (install using `pip install smtplib`)

---

## Setup

1. Clone this repository or download the script files.

2. Ensure Python 3.x is installed on your system.

---

## Configuration

1. Open the `automated_email_sender.py` script.

2. Modify the following variables to suit your setup:
    - `MY_EMAIL`: Your email address used for sending emails.
    - `MY_PASSWORD`: Password for the specified email address.
    - `to_email`: List of recipient email addresses.
    - File paths for letter templates in the morning, afternoon, evening, and night.

---

## Execution

1. Open a terminal or command prompt.

2. Navigate to the directory containing the script.

3. Run the script using Python:
    ```
    python main.py
    ```

---

## File Structure

- `automated_email_sender.py`: Main Python script for sending automated emails.
- `letter_templates/`: Directory containing letter templates for different times of the day.
- `README.md`: Documentation file explaining script usage and setup instructions.

---

## Sample Usage

The script will automatically detect the time of day and send appropriate greetings to the specified recipients.

---

## Notes

- Ensure proper handling of sensitive information, such as email credentials.
- Review and adjust the time ranges or intervals in the script based on your preferences.

---

## Contributing

Contributions are welcome! Fork the repository, make your changes, and create a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).
