from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("Hompage.html")


@app.route("/fdetailsadded")
def fdadd():
    return render_template("Fdadded.html")


@app.route("/fsavedetails", method=["POST", "GET"])
def fsdetail():
    msg = "msg"
    if request.method == "POST":
        try:
            Factory_Name = request.form["fname"]
            Factory_ID = request.form["fid"]
            Mobile_Number = request.form["mnum"]
            Land_Line = request.form["lnum"]
            Email = request.form["email"]
            Factory_GST = request.form["gstnum"]
            Factory_address = request.form["address"]
            with sqlite3.connect("K&N.db") as con:
                cur = con.cursor()
                cur.execute(
                    "Insert into fenroll (Factory_Name, Factory_ID, Mobile_Number, Land_Line, Email, Factory_GST, "
                    "Factory_address) Values (?,?,?,?,?,?,?)",
                    (Factory_Name, Factory_ID, Mobile_Number, Land_Line, Email, Factory_GST, Factory_address))
                con.commit()
                msg = "Factory details added"
        except:
            con.rollback()
            msg = "factory details not added"
        finally:
            return render_template("fdsuccess.html", msg=msg)
            con.close()


@app.route("/fview")
def factoryview():
    con = sqlite3.connect("K&N.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from fenroll")
    rows = cur.fetchall()
    return render_template("fview.html", rows=rows)


@app.route("/vdetailsadded")
def vdadd():
    return render_template("vdadded.html")


@app.route("/vsavedetails", method=["POST", "GET"])
def vsdetail():
    msg = "msg"
    if request.method == "POST":
        try:
            Vendor_ID = request.form["vid"]
            Vendor_Name = request.form["vname"]
            Mobile_Number = request.form["mnum"]
            Land_Line = request.form["lnum"]
            Email = request.form["email"]
            Vendor_GST = request.form["gstnum"]
            Vendor_address = request.form["address"]
            with sqlite3.connect("K&N.db") as con:
                cur = con.cursor()
                cur.execute("Insert into fenroll (Vendor_ID, Vendor_Name, Mobile_Number, Land_Line, Email, "
                            "Vendor_GST, Vendor_address) Values (?,?,?,?,?,?,?)",
                            (Vendor_ID, Vendor_Name, Mobile_Number, Land_Line, Email, Vendor_GST, Vendor_address))
                con.commit()
                msg = "Vendor details added"
        except:
            con.rollback()
            msg = "vendor details not added"
        finally:
            return render_template("vdsuccess.html", msg=msg)
            con.close()


@app.route("/vview")
def vendorview():
    con = sqlite3.connect("K&N.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from venroll")
    rows = cur.fetchall()
    return render_template("fview.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
