import pandas as pd, plotly.graph_objects as pgo

data = pd.read_csv("data2.csv")
student_id = data.loc[data['student_id']=="TRL_abc"]
mv = student_id.groupby("level")["attempt"].mean()
fig = pgo.Figure(pgo.Scatter(x =['Level 1','Level 2','Level 3','Level 4'] ,y = mv))
fig.show()