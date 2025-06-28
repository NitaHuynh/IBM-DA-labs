import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update
import datetime as dt

# khởi tạo app
app = dash.Dash(__name__)

# đọc df
df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv') 

# trích xuất thêm cột Year và Month từ cột Date
df['Month'] = pd.to_datetime(df['Date']).dt.month_name()
df['Year'] = pd.to_datetime(df['Date']).dt.year

# tạo layout cho app
app.layout = html.Div(children=[
    html.H1('Australia Wildfire Dashboard',style={'textAlign':'center','color':'503D36','font-size':26}),
    # div ngoài
    html.Div([
        # 1st div: input RadioItems & Dropdown
        # RadioItems cho Regions
        html.Div([
            html.H2('Select Region:',style={'margin-right':'2em'}),
            dcc.RadioItems(['NSW','QL','SA','TA','VI','WA'],
            # gtri mặc định ban đầu khi hiển thị của RadioItems
            value='NSW',id='region',inline=True)]),
        # dropdown cho Year
        html.Div([
            html.H2('Select year:',style={'margin-right':'2em'}),
            dcc.Dropdown(id='year',
                options=[{'label':str(year),'value':year}for year in sorted(df['Year'].unique())],
                value=sorted(df['Year'].unique())[0], # chọn năm unique nhỏ nhất
                clearable=False # nút "x" sẽ không hiển thị, và người dùng phải chọn 1 trong các tùy chọn — không thể bỏ chọn hoàn toàn
            )
            ])
        ]),
        # 2nd div: pie & bar chart
        html.Div([
            html.Div([],id='plot1'),
            html.Div([],id='plot2')
        ],style={'display':'flex'})
    ])

# add callback decorator
@app.callback(
    [Output(component_id='plot1',component_property='children'),
    Output(component_id='plot2',component_property='children')],
    [Input(component_id='region',component_property='value'),
    Input(component_id='year',component_property='value')]
)

# hàm callback - xử lý dữ liệu & trả về bđồ
def reg_year_display(input_region,input_year):
    # lọc dữ liệu theo vùng & năm được chọn
    region_data = df[df['Region']==input_region]
    y_r_data = region_data[region_data['Year']==input_year]
    # pie chart: monthly average estimated fire area in year
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean().reset_index()
    fig1 = px.pie(est_data,values='Estimated_fire_area',names='Month',title='{}:Monthly average estimated fire area in year {}'.format(input_region,input_year))
    # bar chart: count of pixels tb theo tháng
    veg_data = y_r_data.groupby('Month')['Count'].mean().reset_index()
    fig2 = px.bar(veg_data,x='Month',y='Count',title='{}: Average Count of Pixels for Presume Vegetation Fires in year {}'.format(input_region,input_year))
    return [
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ]

# run app
if __name__ == '__main__':
    app.run()