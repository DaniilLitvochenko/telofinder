import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_origin_data():
    x_temp = []
    y_temp = []
    file = open("data.txt", "r")
    while True:
        inp = file.readline()
        if not inp:
            break
        y_temp.append(inp)
        inp = file.readline()
        if not inp:
            break
        x_temp.append(len(inp))
    file.close()
    return(x_temp, y_temp)

def get_marker_data():
    coord = open("output.txt", "r")
    dic = {}
    coordinate = coord.readline().split()
    while True:
        if coordinate[0] == "Sequence:":
            key = coordinate[1]
            dic.setdefault(key,[])
            coordinate = coord.readline().split()
            if not coordinate:
                break
            if coordinate[0] != "0" and coordinate[1] !="0":
                while True:
                    if coordinate[0] == "Sequence:":
                        break
                    if coordinate[0] != "0" and coordinate[1] !="0":
                        dic[key].append(coordinate)
                    coordinate = coord.readline().split()
                    if not coordinate:
                        break
            else:
               coordinate = coord.readline().split()
    coord.close()
    clear_dic = (dict(filter(lambda x:x[1], dic.items())))
    return(clear_dic)

def change_scale(x_mar, x0_mar):
    for i in range(len(x_mar)):
        x_mar[i]-=x0_mar[i]
        x_mar[i] += 1000000 #изменение масштаба отрисовки маркера
        x0_mar[i] -= 1000000
    return(x_mar, x0_mar)

#visualize origin data
origin_data = get_origin_data()
x_temp = origin_data[0]
y_temp = origin_data[1]
fig = go.Figure()
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

marker_data = get_marker_data()

j = 0
for key in marker_data:
    print(key)
    y_mar = [y_temp[j]]
    j += 1
    coord = marker_data[key]
    i = 0
    for item in marker_data[key]:
        print(coord[i])
        c = coord[i]
        scale = change_scale([int(c[1])], [int(c[0])])
        x0_mar = scale[1]
        x_mar = scale[0]
        fig.add_trace(
            go.Bar(
                base = x0_mar,
                x = x_mar,
                y = y_mar,
                marker=go.bar.Marker(
                    color="rgb(0, 176, 243)",
                    line=dict(color="rgb(0, 0, 0)",
                          width=0)
                ),
                orientation="h",
                #showlegend = False
                )
            )
        i += 1 

# update layout properties
fig.update_layout(
    autosize=True,
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
fig.write_html('telomeres_viz_2.html')
