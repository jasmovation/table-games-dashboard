from flask import Flask, render_template, request
import plotly.express as px
from data_utils import load_and_transform_data

app = Flask(__name__)

@app.route('/')
def index():
    df = load_and_transform_data("table_games_data.csv")

    # 🧠 Get dropdown values
    selected_region = request.args.get("region", "All")
    selected_game = request.args.get("gametype", "All")

    # 🧼 Apply filters
    if selected_region != "All":
        df = df[df["Region"] == selected_region]
    if selected_game != "All":
        df = df[df["GameType"] == selected_game]

    # 📊 Bar chart
    bar_fig = px.bar(
        df,
        x="Region",
        y="Revenue",
        color="GameType",
        title="Revenue by Region and Game Type"
    )
    bar_html = bar_fig.to_html(full_html=False)

    # 📊 Pie chart
    pie_fig = px.pie(
        df,
        names="GameType",
        values="Revenue",
        title="Revenue Distribution by Game Type"
    )
    pie_html = pie_fig.to_html(full_html=False)

    # 📋 Dropdown lists
    all_regions = sorted(df["Region"].unique().tolist())
    all_regions.insert(0, "All")

    all_games = sorted(df["GameType"].unique().tolist())
    all_games.insert(0, "All")

    return render_template(
        "index.html",
        bar_html=bar_html,
        pie_html=pie_html,
        selected_region=selected_region,
        selected_game=selected_game,
        all_regions=all_regions,
        all_games=all_games
    )

if __name__ == "__main__":
    app.run(debug=True)
