# Cross-Browser Testing with Selenium and BrowserStack 🌐

Automate cross-browser testing across **Chrome, Firefox, Edge, Safari, and mobile devices** using **Selenium**, **pytest**, and **BrowserStack**. This project demonstrates running tests on both local and cloud browsers.

[![BrowserStack](https://img.shields.io/badge/BrowserStack-%2300A4E4?logo=browserstack&logoColor=white)](https://www.browserstack.com/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-7.0%2B-green)](https://docs.pytest.org/)

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [1. BrowserStack Account](#1-browserstack-account)
  - [2. Local Drivers](#2-local-drivers-optional)
- [Configuration](#configuration)
- [Run Tests](#run-tests)
  - [Local Browsers](#1-local-browsers)
  - [BrowserStack](#2-browserstack-cloud)
- [Test Examples](#test-examples)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Prerequisites
- Python 3.11+
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Git](https://git-scm.com/downloads)

---

## Setup

### 1. BrowserStack Account
- **Sign Up**: Create a free [BrowserStack account](https://www.browserstack.com/users/sign_up).
- **Get Credentials**:
  - **Username**: From your BrowserStack [account settings](https://www.browserstack.com/accounts/settings).
  - **Access Key**: Found in the same settings page.

### 2. Local Drivers (Optional)
For **local testing**, download:
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
- [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver/releases)
- [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

---

## Configuration

### 1. **Set BrowserStack Credentials**
Create a `.env` file in your project root:
```ini
# .env
BROWSERSTACK_USERNAME = "your_username"
BROWSERSTACK_ACCESS_KEY = "your_access_key"
