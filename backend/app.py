from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/scan', methods=['POST'])
def scan():
    file = request.files.get('file')
    url = request.form.get('url')

    if file:
        # Process the file
        file_hash = hashlib.sha256(file.read()).hexdigest()
        result = check_virus_database(file_hash)
    elif url:
        # Process the URL
        url_hash = hashlib.sha256(url.encode()).hexdigest()
        result = check_virus_database(url_hash)
    else:
        return jsonify({'error': 'No file or URL provided'}), 400

    return jsonify(result)

@app.route('/result')
def result():
    # Get the result passed as query parameter
    data = request.args.get('data')
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
