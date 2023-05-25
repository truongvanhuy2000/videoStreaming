from flask import Flask, Response, render_template, request
import os

from webServer.service import grpcClient
from webServer.service.persistentData import persistentData

# Set up environment variable
GRPC_SERVER1 = os.getenv('GRPC_SERVER1')
GRPC_SERVER2 = os.getenv('GRPC_SERVER2')
GRPC_SERVER3 = os.getenv('GRPC_SERVER3')
GRPC_SERVER4 = os.getenv('GRPC_SERVER4')

if (GRPC_SERVER1 is None) and (GRPC_SERVER2 is None) and (GRPC_SERVER3 is None) and (GRPC_SERVER4 is None):
    print("Missing environment variable")
    exit()

db = persistentData('webServer/db/persistentData.json')
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    video_feeds = [
        'video_feed_one',
        'video_feed_two',
        'video_feed_three',
        'video_feed_four'
    ]
    if request.method == 'POST':
        aiModel = request.form['Model']
        view = int(request.form['View'])
        data = {
            'model': aiModel,
            'view': view,
        }
        db.writeData(data)
    else:
        if db.isEmpty():
            aiModel = 'generic'
            view = 2
        else:
            aiModel = db.readData('model')
            view = db.readData('view')
    return render_template('index.html', model=aiModel, views=int(view), video_feeds=video_feeds)
        
@app.route('/<variable>/video_feed_one')
def video_feed_one(variable):
    return Response(grpcClient.request(video="video1", model=variable, addr=GRPC_SERVER1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<variable>/video_feed_two')
def video_feed_two(variable):
    return Response(grpcClient.request(video="video2", model=variable, addr=GRPC_SERVER2),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<variable>/video_feed_three')
def video_feed_three(variable):
    return Response(grpcClient.request(video="video3", model=variable, addr=GRPC_SERVER3),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/<variable>/video_feed_four')
def video_feed_four(variable):
    return Response(grpcClient.request(video="video4", model=variable, addr=GRPC_SERVER4),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def runWebServer():
    app.run(host="0.0.0.0", debug=False)