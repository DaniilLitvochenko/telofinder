import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

y_temp = []
x_temp = []
file = open("data.txt", "r")
while True:
    inp = file.readline()
    y_temp.append(inp)
    inp = file.readline()
    x_temp.append(len(inp))
    if not inp:
        break

file.close()

coord = open("output.txt", "r")

y_mar = []
x0_mar = []
x_mar = []
coordinate = coord.readline().split()
while True:
    if coordinate[0] == "Sequence:":
        coordinate = coord.readline().split()
        if not coordinate:
            break
        if coordinate[0] != "0" and coordinate[1] !="0":
            while True:
                if coordinate[0] == "Sequence:":
                    break
                if coordinate[0] != "0" and coordinate[1] !="0":
                    #print(coordinate)
                    x0_mar.append(int(coordinate[0]))
                    x_mar.append(int(coordinate[1]))
                    print(coordinate)
                coordinate = coord.readline().split()
                if not coordinate:
                    break
        else:
           coordinate = coord.readline().split() 

fig = go.Figure()

#bar = go.Bar(
fig.add_trace(
    go.Bar(
        x = x_temp,
        y = y_temp,
        marker=go.bar.Marker(
            color="rgb(253, 240, 54)",
            line=dict(color="rgb(0, 0, 0)",
                      width=2)
        ),
        orientation="h"
    )
)

for i in range(len(x_mar)):
    x_mar[i]-=x0_mar[i]
    
#mark = go.Bar(
fig.add_trace(
    go.Bar(
        base = x0_mar,
        x = x_mar,
        y = y_temp,
        marker=go.bar.Marker(
            color="rgb(0, 176, 243)",
            line=dict(color="rgb(0, 0, 0)",
                      width=2)
        ),
        orientation="h"
    )
)

#fig = make_subplots(specs=[[{"secondary_y": True}]], print_grid=True)
#fig.add_trace(bar, secondary_y=False)
#fig.add_trace(mark, secondary_y=True)

# update layout properties
fig.update_layout(
    autosize=False,
    height=1600,
    width=1400,
    bargap=0.15,
    bargroupgap=0.1,
    barmode="stack",
    hovermode="x",
    margin=dict(r=20, l=300, b=75, t=125),
    title=("Contigs"),
)

fig.show()
fig.write_html('telomeres.html')
