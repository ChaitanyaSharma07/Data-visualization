import pandas as pd
import plotly.express as px

data = pd.read_csv("covid.csv")

type = input("Enter which type of graph you would like to see(bar, scatter, pie): ")

if type == "scatter":
    fig = px.scatter(data, x="date", y="cases", color="country")
    fig.show()
elif type == "bar":
    fig = px.bar(data, x="country", y="cases", color="country")
    fig.show()
elif type == "pie":
    fig = px.pie(data, values="cases", names="country", title="Covid cases")
    fig.show()

