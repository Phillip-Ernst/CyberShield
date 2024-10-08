from flask import Flask, request, jsonify
import hashlib
from services.db_service import check_virus_database  # Import the database service

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    file = request.files.get('file')
    url = request.form.get('url')

    if file:
        # Hash the file content
        file_hash = hashlib.sha256(file.read()).hexdigest()
        # Use the service to check the hash in the database
        result = check_virus_database(file_hash)
        return jsonify(result)

    elif url:
        # Hash the URL
        url_hash = hashlib.sha256(url.encode()).hexdigest()
        # Use the service to check the hash in the database
        result = check_virus_database(url_hash)
        return jsonify(result)

    else:
        return jsonify({'error': 'No file or URL provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)