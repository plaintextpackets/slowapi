# Slow API

## Overview

This Flask app is a simple demonstration of a basic API that responds to requests with a delay. The app listens on the root route ('/') and introduces a delay of 5 seconds before responding with 'ok'. It can be configured to run over either HTTP or HTTPS.

## Features

- **Simple API**: A single route (`/`) that simulates a delayed response.
- **Configurable Protocol**: Easily switch between HTTP and HTTPS.
- **Delay Response**: Introduces a fixed delay of 5 seconds before responding to each request.

## Requirements

- Python 3
- Flask
- OpenSSL (for generating self-signed certificates, if using HTTPS)

## Installation

1. Clone the Repository:

```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install Dependencies:


```
pip install flask
```

3. Generate Self-Signed SSL Certificate for HTTPS:

Run this command to generate a self-signed SSL certificate and key:

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

Note: For production, use a certificate from a trusted certificate authority.

## Configuration

HTTP/HTTPS Toggle: Set the USE_HTTPS variable in app.py to True to use HTTPS or False to use HTTP.