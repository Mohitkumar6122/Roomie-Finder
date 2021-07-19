from flask import Flask, flash, redirect, render_template, request

app = Flask(__name__)
app.secret_key = 'Secret_key'
data = ""

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form/", methods=["GET", "POST"])
def form():
    return render_template("form.html", title=form)


@app.route("/responses", methods=["POST"])
def responses():
    if request.method == "POST":
        file1 = open("entries.txt", "a")
        global data
        data = ""
        data += request.form["roll_number"] + ","
        print(
            f"Data Requested for the Roll Number in the above form using the flask method id as above  {request.form['Name']}"
        )
        data += request.form["rad1"]
        data += request.form["rad2"]
        data += request.form["rad5"]
        data += request.form["rad4"]
        data += request.form["rad3"]
        file1.write(data)
        file1.write("\n")
        file1.close()
        return redirect("/answer")
    else:
        print("Error in Searching.. !\n Please Try Again..!\n")
        return redirect("/")


@app.route("/answer", methods=["GET", "POST"])
def answer():
    diff = 30000
    file1 = open("entries.txt", "r")
    lines = file1.readlines()
    # print(lines)
    a = int(lines[-1].split(",")[1])
    # print(a)
    l = lines[0]
    for line in lines[0:-2]:
        b = int(line.split(",")[1])
        # print(b)
        if abs(b - a) < diff:
            if abs(b - a) != 0:
                diff = abs(b - a)
                l = line
    rn = l.split(",")[0]
    file1.close()
    return render_template("answer.html", data=str(rn))


@app.route("/about")
def about():
    return render_template("about.html", title=about)


if __name__ == "__main__":
    app.run(debug=True)
