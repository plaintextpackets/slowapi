from flask import Flask
import time
import ssl

app = Flask(__name__)

# Configuration variable to choose between HTTP and HTTPS
USE_HTTPS = False  # Set to False to use HTTP

@app.route('/')
def home():
    time.sleep(5)  # Delay for 5 seconds
    return 'ok'

if __name__ == '__main__':
    if USE_HTTPS:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.load_cert_chain('cert.pem', 'key.pem')  # Load your certificate and private key
        app.run(port=1234, ssl_context=context, host="0.0.0.0")  # Run with HTTPS
    else:
        app.run(port=1234, host='0.0.0.0')  # Run with HTTP
