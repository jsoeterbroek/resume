# werkervaring.py
import pandas as pd
from labella.scale import LinearScale
from labella.timeline import TimelineTex

def makeInput(_df):
    length = len(_df.year_start)
    out = []
    print(_df)
    for i in range(length):
        _dict = {}
        _dict['time'] = _df.year_start[i]
        #dict['year_end'] = _df.year_end[i]
        _dict['text'] = _df.employer[i]
        #dict['job_title'] = _df.job_title[i]
        out = out + [_dict]
    return out

header_list = ['year_start', 'year_end', 'employer', 'job_title']
df = pd.read_csv('werkervaring.csv', names=header_list)
xtimeline = makeInput(df)
ttimeline = TimelineTex(xtimeline, options={'scale': LinearScale()})

ttimeline.export('werkervaring.tex')
