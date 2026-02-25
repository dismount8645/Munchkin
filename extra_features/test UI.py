from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Simple in-memory leaderboard
leaderboard = {}

# HTML templates (inline for simplicity)
form_html = """
<h2>Update Your Munchkin Stats</h2>
<form method="POST">
  Name: <input name="name"><br>
  Level: <input name="level" type="number"><br>
  Gender: <input name="gender" type="number"><br>
  <button type="submit">Submit</button>
</form>
"""

leaderboard_html = """
<h1>Munchkin Leaderboard</h1>
<table border="1" cellpadding="5">
  <tr><th>Name</th><th>Level</th><th>Gear</th><th>Total</th></tr>
  {% for name, stats in data.items() %}
  <tr>
    <td>{{ name }}</td>
    <td>{{ stats.level }}</td>
    <td>{{ stats.gender }}</td>
    <td>{{ stats.level + stats.gear }}</td>
  </tr>
  {% endfor %}
</table>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        level = int(request.form["level"])
        gender = int(request.form["gender"])
        leaderboard[name] = {"level": level, "gender": gender}
        return redirect("/")
    return render_template_string(form_html + leaderboard_html, data=leaderboard)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
