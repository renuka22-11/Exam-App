from flask import Flask

#create flask app
app = Flask(__name__)

#add all the routes

@app.route("/", methods=["GET"])
def root():
    return "Welcome TO ITIL exam"

@app.route("/modules", methods=["GET"])
def root1():
    return "Security Concepts, FCN, COSA, DevOPS, Compliance-Audit, NDC, PKI, Cyber-Forensics"

@app.route("/me", methods=["GET"])
def root2():
    return "230344223038 Renuka More 9373942822"

#run the application
app.run(host="0.0.0.0", port=4000, debug=True)
