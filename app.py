from flask import Flask, render_template, jsonify
import boto3

app = Flask(__name__)

# AWS Rekognition Client
rekognition = boto3.client('rekognition', region_name='us-east-1')

# S3 Bucket Name
BUCKET_NAME = "car-parking-videos"
IMAGE_NAME = "frame_0.jpg"  # Change to any extracted frame

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect_parking():
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': IMAGE_NAME}},
        MaxLabels=10
    )

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
