from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# In-memory storage for image URLs
image_urls = [
    "https://picsum.photos/1920/1080?random=1",
    "https://picsum.photos/1920/1080?random=2",
    "https://picsum.photos/1920/1080?random=3",
    "https://picsum.photos/1920/1080?random=4",
    "https://picsum.photos/1920/1080?random=5"
]

def get_random_url():
    if not image_urls:
        return None
    timestamp = int(time.time() * 1000)  # Get current timestamp in milliseconds
    index = abs(hash(str(timestamp))) % len(image_urls)
    return image_urls[index]

@app.route('/random-image', methods=['GET'])
def get_random_image_url():
    url = get_random_url()
    if url is None:
        return jsonify({"error": "No images available"}), 404
    return jsonify({"url": url})

@app.route('/add-image', methods=['POST'])
def add_image_url():
    new_url = request.json.get('url')
    if not new_url:
        return jsonify({"error": "URL is required"}), 400
    image_urls.append(new_url)
    return jsonify({"message": "URL added successfully"}), 201

@app.route('/all-images', methods=['GET'])
def get_all_image_urls():
    return jsonify({"urls": image_urls})

if __name__ == '__main__':
    app.run(debug=True)
