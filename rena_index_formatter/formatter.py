import os
import re
import codecs
import tkinter as tk
from tkinter import filedialog

_Re_list = re.compile(
    r'B\.(?P<id>.*)[\r\n]+'
    r'(?P<hidden>Y\?1[\r\n]+|)'
    r'(?P<ranked>R\?1[\r\n]+|)'
    r'N\?(?P<name>.*)[\r\n]+'
    r'S\?(?P<song>.*)[\r\n]+'
    r'C\?(?P<cover>.*)[\r\n]+'
    r'P\?(?P<preview>.*)[\r\n]+'
    r'U\?(?P<charter>.*)[\r\n]+'
    r'W\?(?P<artist>.*)[\r\n]+'
    r'I\?(?P<desc>.*)[\r\n]+'
    r'H\?(?P<difficulties>.*)[\r\n]+'
    r'M\?(?P<charts>.*)[\r\n]+'
    r'E\.'
)

_Re_difficulties = re.compile(r'(?P<name>[A-Za-z0-9]*),(?P<level>[\-A-Za-z0-9]*);')
_Re_charts = re.compile(r'(?P<file>[^;]*);')

lst = []

window_title = "rena index file generator"

def file_select():
    rena_path.set(filedialog.askopenfilename())
    
def file_write():
    try:
        with codecs.open(rena_path.get(), 'r', encoding="UTF-8") as fo:
            s_list = fo.read()
    except:
        tk.showerror(title=window_title, message="Can't open index file.")
 
    for id_, hidden, ranked, name, song, cover, preview, charter, artist, desc, difficulties, charts in re.findall(_Re_list, s_list):
        diffs = re.findall(_Re_difficulties, difficulties)
        charts = re.findall(_Re_charts, charts)
        '''if len(diffs) != len(charts):
            print(f'Corrupted item: {id_}:{name}')
            continue'''
        _charts = []
        for (k, level), file in zip(diffs, charts):
            _charts.append({
                'difficulty': k,
                'level': level,
                'file': file,
            })
        json_dic = {
            'id': id_,
            'hidden': bool(hidden),
            'ranked': bool(ranked),
            'name': name.strip(),
            'song': song,
            'cover': cover,
            'preview': preview,
            'charter': charter.strip(),
            'artist': artist.strip(),
            'desc': desc,
            'charts': _charts
        }
        lst.append(json_dic)

    res = []
    for dic in lst:
        if  ( dic['ranked'] and item_list['Rank Status']['Variables'][1].get() ) or \
            ( (not dic['ranked']) and item_list['Rank Status']['Variables'][2].get() ):
            pass
        else:
            continue

        charts = dic['charts']
        diffs = []
        _charts = []
        for chart in charts:
            try:
                cur_level = int(chart['level'])
            except:
                cur_level = 20
            cur_diff = chart['difficulty'].lower()
            if  ( cur_diff == 'casual' and item_list['Difficulty']['Variables'][1].get() ) or \
                ( cur_diff == 'normal' and item_list['Difficulty']['Variables'][2].get() ) or \
                ( cur_diff == 'hard' and item_list['Difficulty']['Variables'][3].get() ) or \
                ( cur_diff == 'mega' and item_list['Difficulty']['Variables'][4].get() ) or \
                ( cur_diff == 'giga' and item_list['Difficulty']['Variables'][5].get() ) or \
                ( item_list['Difficulty']['Variables'][6].get() ):
                if  ( cur_level <= 10 and item_list['Level Range']['Variables'][1].get() ) or \
                    ( cur_level == 11 and item_list['Level Range']['Variables'][2].get() ) or \
                    ( cur_level == 12 and item_list['Level Range']['Variables'][3].get() ) or \
                    ( cur_level == 13 and item_list['Level Range']['Variables'][4].get() ) or \
                    ( cur_level == 14 and item_list['Level Range']['Variables'][5].get() ) or \
                    ( cur_level == 15 and item_list['Level Range']['Variables'][6].get() ) or \
                    ((cur_level == 16 or cur_level == 17) and item_list['Level Range']['Variables'][7].get() ) or \
                    ( item_list['Difficulty']['Variables'][8].get() ):
                    diffs.append(f'{chart["difficulty"]},{chart["level"]};')
                    _charts.append(f'{chart["file"]};')
            else:
                pass
        if not len(diffs):
            continue

        data = [f'B.{dic["id"]}']
        if dic['hidden']:
            data.append('Y?1')
        if dic['ranked']:
            data.append('R?1')
        data.append(f'N?{dic["name"]}')
        data.append(f'S?{dic["song"]}')
        data.append(f'C?{dic["cover"]}')
        data.append(f'P?{dic["preview"]}')
        data.append(f'U?{dic["charter"]}')
        data.append(f'W?{dic["artist"]}')
        data.append(f'I?{dic["desc"]}')
        data.append(f'H?{"".join(diffs)}')
        data.append(f'M?{"".join(_charts)}')
        data.append('E.\n')
        res.append('\n'.join(data))

    with codecs.open('__rena_index_2_generated', 'w', encoding="UTF-8") as fr:
        fr.write('\n'.join(res))

    tk.showinfo(title=window_title, message="Generation finished successfully.")

def checkbox_all(cata_name):
    if item_list[cata_name]['variables'][0].get():
        for id, name in enumerate(item_list[cata_name]['list']):
            item_list[cata_name]['checkboxes'][id].select()
        else:
            item_list[cata_name]['checkboxes'][id].deselect()

if __name__ == '__main__':
    mainWindow = tk.Tk()
    mainWindow.geometry("600x450")
    mainWindow.title(window_title)

    item_list = {
        'Rank Status':{
            'list':[
                'Ranked',
                'Unranked',
            ]
        },
        'Difficulty':{
            'list':[
                'Casual',
                'Normal',
                'Hard',
                'Mega',
                'Giga',
                'Tera & Others',
            ]
        },
        'Level Range':{
            'list':[
                '≤Lv.10',
                'Lv.11',
                'Lv.12',
                'Lv.13',
                'Lv.14',
                'Lv.15',
                'Lv.16-17',
                'Lv.17+ & Others',
            ]
        }
    }

    frame_upper = tk.Frame(mainWindow)
    frame_upper.pack(side='top')
    for column, catagory in enumerate(item_list):
        tk.Label(frame_upper, text=catagory, width=10, height=5).grid(row = 0, column=column, padx='10px')
        item_list[catagory]['checkboxes'] = []
        item_list[catagory]['variables'] = []
        item_list[catagory]['variables'].append(tk.IntVar())
        tk.Checkbutton(
            frame_upper, 
            text="All",
            variable=item_list[catagory]['variables'][0],
            onvalue=1,
            offvalue=0,
            command=lambda: checkbox_all(cata_name=catagory)
        ).grid(
            row = 1, 
            column = column, 
            sticky='w', 
            padx='10px'
        )

        for id, item in enumerate(item_list[catagory]['list']):
            item_list[catagory]['variables'].append(tk.IntVar())
            checkbox = tk.Checkbutton(
                frame_upper, 
                text=item,
                variable=item_list[catagory]['variables'][id + 1],
                onvalue=1,
                offvalue=0
            )
            checkbox.grid(
                row = id + 2, 
                column = column, 
                sticky='w', 
                padx='10px'
            )
            item_list[catagory]['checkboxes'].append(checkbox)
        


    frame_lower = tk.Frame(mainWindow)
    frame_lower.pack(side='bottom')
    rena_path = tk.StringVar()
    tk.Label(frame_lower, text='__rena_index_2 File:').grid(row=0, column=0)
    tk.Entry(frame_lower, textvariable = rena_path).grid(row=0, column=1)
    tk.Button(frame_lower, text='File Select', command=file_select).grid(row=0, column=2)
    tk.Button(frame_lower, text='Generate File', command=file_write).grid(row=0, column=3)

    mainWindow.mainloop()