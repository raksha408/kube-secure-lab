from flask import Flask, request, jsonify
import logging
import random
import time
import sys

app = Flask(__name__)

# Configure logging to stdout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [Module:%(module)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("NetflixVideoDB")

@app.route('/')
def health_check():
    logger.info("Health check endpoint accessed.")
    return jsonify({"status": "healthy"}), 200

@app.route('/api/load_movie', methods=['POST'])
def load_movie():
    logger.info(f"Received movie streaming request from {request.remote_addr}")
    # Simulating processing
    time.sleep(0.5)
    
    # Introduce random failures to generate error logs for analysis
    if random.random() < 0.3:
        logger.error("Video database did not respond while loading movie data.")
        return jsonify({"error": "Video Server Unreachable"}), 504
    elif random.random() < 0.1:
        logger.critical("Authentication failure: Invalid user subscription tokens detected.")
        return jsonify({"error": "Unauthorized"}), 401
    
    logger.info("Movie loaded successfully.")
    return jsonify({"stream_id": random.randint(1000, 9999), "status": "playing"}), 200

if __name__ == '__main__':
    logger.info("Starting NetflixVideoDB Service on port 5000")
    app.run(host='0.0.0.0', port=5000)
