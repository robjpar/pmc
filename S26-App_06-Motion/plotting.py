import pandas
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df = pandas.read_csv('times.csv', parse_dates=['start', 'end'])
df['start_str'] = df['start'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['end_str'] = df['end'].dt.strftime('%Y-%m-%d %H:%M:%S')

p = figure(x_axis_type='datetime', height=100, width=500,
           sizing_mode='scale_width', title='Motion Graph')

p.yaxis.major_label_text_color = None
p.yaxis.major_tick_line_color = None
p.yaxis.minor_tick_line_color = None
p.ygrid.grid_line_color = None

cds = ColumnDataSource(df)
q = p.quad(left='start', right='end', bottom=0,
           top=1, color='green', source=cds)

hover = HoverTool(tooltips=[('Start', '@start_str'), ('End', '@end_str')])
p.add_tools(hover)

output_file('motion-graph.html')
show(p)
