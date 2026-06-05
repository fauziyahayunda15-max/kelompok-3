from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/healthycoffee", methods=["POST"])
def healthycoffee():

    data = request.json

    print("\n===== DATA DARI HTML =====")
    print("Nama :", data["nama"])
    print("Kopi :", data["kopi"])
    print("Gula :", data["gula"])
    print("Susu :", data["susu"])
    print("Cream :", data["cream"])
    print("Boba :", data["boba"])
    print("==========================\n")

    return jsonify({
        "status": "success",
        "message": "Data berhasil diterima Python"
    })

if __name__ == "__main__":
    app.run(debug=True)