from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/plot')
def plot():
    from pandas_datareader.data import DataReader
    import datetime
    from bokeh.plotting import figure
    from bokeh.resources import CDN
    from bokeh.embed import components
    
    start = datetime.datetime(2015, 11, 1)
    end = datetime.datetime(2016, 3, 10)
    df = DataReader(name='GOOG', data_source='yahoo', start=start, end=end)
    def inc_dec(o, c):
        if c > o:
            return 'increase'
        elif c < o:
            return 'decrease'
        else:
            return 'equal'
    df['Status'] = [inc_dec(o, c) for o, c in zip(df.Open, df.Close)]
    df['Middle'] = (df.Open + df.Close)/2
    df['Height'] = abs(df.Open - df.Close)

    p = figure(x_axis_type='datetime', width=1000, height=300, 
               sizing_mode='scale_width')
    p.title.text = 'GOOG'
    p.yaxis.axis_label = 'USD'
    p.grid.grid_line_alpha = 0.8
    p.segment(x0=df.index, y0=df.High, x1=df.index, y1=df.Low)
    hours_12 = 12 * 60 * 60 * 1000 # ms
    p.rect(x=df.index[df.Status == 'increase'], 
           y=df.Middle[df.Status == 'increase'], 
           width=hours_12, height=df.Height[df.Status == 'increase'], 
           fill_color='#2ECC71', line_color='#707B7C')
    p.rect(x=df.index[df.Status == 'decrease'], 
           y=df.Middle[df.Status == 'decrease'], 
           width=hours_12, height=df.Height[df.Status == 'decrease'], 
           fill_color='#E74C3C', line_color='#707B7C')
    
    cdn_js = CDN.js_files[0]
    script, div = components(p)

    return render_template('plot.html', cdn_js=cdn_js, script=script, div=div)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
