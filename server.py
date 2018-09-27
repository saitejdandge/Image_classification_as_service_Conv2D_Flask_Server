from flask import Flask,request
from master import main,predict,createDataset
app = Flask(__name__)

print("Hello welcome to Pixel, Image classification as service\n\n")

@app.route("/train",methods=['GET'])
def hello():
    main(request.args.get('location'))
    return "Model Trained"

@app.route("/predict",methods=['GET'])
def predict_call():
    predict(request.args.get('location'),request.args.get('file_name'))
    return "Value"

@app.route("/createdataset",methods=['GET'])
def createdataset_call():
    createDataset(request.args.get('keywords'))
    return "Value"

if __name__ == "__main__":
    app.run()