import calendar, sys
import pyperclip
from calendar import TextCalendar
import PySimpleGUI as sg
sg.theme('LightPurple')
# Remove this line in Windows and Linux 
# os.chdir('/storage/emulated/0')
#Without this all activity will be apps personal folder deep inside Android folder
layout=[
    [sg.Text('Dr Santhosh Rajamani\'s Calendar Maker'),],
    [sg.Text('                     Enter Year like 1765',size=(25,1)
    ),sg.Input('1989',size=(10,1),key='-YR-')],

    [sg.Text('Enter Month number November', size=(25,1)),
     sg.Input('11',size=(10,1),key='-MON-')],
    [sg.Multiline(size=(45,15), key='-OUT-'),],
    [sg.Button('Copy',key='-COPY-', size=(8,1)),
    sg.Button('Clear',key='-CLEAR-',size=(8,1)),
    sg.Button('Exit',key='-EXIT-',size=(8,1))
    ,

    ],
    [
    sg.Button('Generate a Month',key='-GEN-',size=(24,1))
    ],

    [
    sg.Button('Generate a text Year',key='-GENYR-',size=(24,1))
    ],
    [
    sg.Button('Generate a colorful Year in HTML',key='-GENYRHTML-',size=(24,1))
    ],

    ]

def DefaultValues(window1):
    window1['-YR-'].update('2021')
    window1['-MON-'].update('12')
    window1['-OUT-'].update('')


window = sg.Window('Dr. Santhosh Calendar Generator', layout, finalize=True)
DefaultValues(window)

#def List2String(List1):
#string1=""
#return string1.join(List1)

#print(ARRAY2D)

while True:             # Event Loop
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        window.close()
        sys.exit()
        break
            
    if event == '-CLEAR-':
        DefaultValues(window)
        continue
            
    if event == '-COPY-':
        txt25=values['-OUT-']
        if not txt25:continue
        pyperclip.copy(txt25)
        continue
            
    if event == '-GEN-':
        s1=values['-YR-']
        if not s1: continue
        try:
            year=int(s1)
        except:
            sg.popup('Please enter an Year')
            DefaultValues(window)
            continue
        
        s1=values['-MON-']
        if not s1: continue
        try: month=int(s1)
        except:
            sg.popup('Please enter an month 1 Jan  to 12 Dec ')
            DefaultValues(window)
            continue
        
        if month <=0 or month>12:
            sg.popup('Please enter an month 1 Jan  to 12 Dec ')
            DefaultValues(window)               
            continue
        
        x1=calendar.month(year, month)
        
        txt1=values['-OUT-']
        
        if not txt1: 
            txt1=x1
            
        else:
            txt1=f'{txt1} \n\n {x1}'
        window['-OUT-'].update(txt1)  
        continue
                
    if event == '-GENYR-':
        s1=values['-YR-']
        if not s1: continue
        try: year=int(s1)
        except:
            sg.popup('Please enter an Year')
            DefaultValues(window)
            continue
        cal=TextCalendar()
        x1=cal.formatyear(theyear=year,w=2,l=1,c=6,m=1)
        x1=f"Calendar of the Year {year}\n\n {x1}"
        txt1=values['-OUT-']
        if not txt1:
            txt1=x1
        else:
            txt1=f'{txt1} \n\n {x1}'
        window['-OUT-'].update(txt1)
        fname=sg.popup_get_text('Enter name of Text file to save', title='Input Name', default_text=f'Calendar_{year}.txt')
        if not fname: continue
        with open(fname, 'w') as file:
            file.writelines(txt1)
            file.close()
        continue      
                #        calendar.HTMLCalendar(firstweekday=0)
                # #       

    if event == '-GENYRHTML-':
        s1=values['-YR-']
        if not s1: continue
        try:
            year=int(s1)
        except:
            sg.popup('Please enter an Year')
            DefaultValues(window)
            continue
        cal=calendar.HTMLCalendar()
        x1=cal.formatyear(year,1)
        x2=f'<html><head><title>Calendar of the Year : {year} </title></head><body><p class="month">Calendar of the Year : {year}<hr/></p><p>'
        x2=x2+' <style>.month {background: #e8eaf6;} table {border-collapse: collapse; width: 100%;} th,td {text-align: left; padding: 10px;} tr:nth-child(even) { background-color: #7986cb;} tr:nth-child(odd) {background-color: #c5cae9;}</style>'
        txt1=f'{x2} \n\n {x1} </p></body></html> '
        txt1= txt1.replace('border="0"', 'border="1"')
        txt1=txt1.replace('</table>', '</table> <hr/></p><p>')
        #sg.popup(txt1)
        window['-OUT-'].update(txt1)
        fname=sg.popup_get_text('Enter name of colorful HTML file to save', title='Input Name', default_text=f'Calendar_{year}.htm')
        if not fname: continue
        with open(fname, 'w') as file:
            file.writelines(txt1)
            file.close()
        continue
    
window.close()

        
 
