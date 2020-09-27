import json

import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_canvas import DashCanvas

app = dash.Dash(__name__)

# ➊ レイアウトを作成する
app.layout = html.Div([DashCanvas(id="my_canvas"), html.Div(id="my_callback")])


@app.callback(
    # ➋ 入力項目にID名"my_canvas"の"json_data"属性を指定
    Output("my_callback", "children"),
    [Input("my_canvas", "json_data")],
)
def show_json_data(json_data):
    if json_data is None:  # ➍ json_dataがない場合コールバックを更新しない
        dash.exceptions.PreventUpdate
    return json.dumps(json_data)  # ➎ json_data存在する場合、返り値とする


if __name__ == "__main__":
    app.run_server(debug=True)