gen1=['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#']
gen2=['B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#']
gen3=['G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#']
gen4=['D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#']
gen5=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
gen6=['E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#']
shiban=[gen1,gen2,gen3,gen4,gen5,gen6]
mel=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
def all_code():
    code={}
    for i in range(12):
        code[mel[i]]={mel[i],mel[i+4],mel[i+7]}     #M code
        code[mel[i]+'6']={mel[i],mel[i+4],mel[i+7],mel[i+9]}
        code[mel[i]+'7']={mel[i],mel[i+4],mel[i+7],mel[i+10]}
        code[mel[i]+'M7']={mel[i],mel[i+4],mel[i+7],mel[i+11]}
        code[mel[i]+'69']={mel[i],mel[i+2],mel[i+4],mel[i+7],mel[i+9]}
        code[mel[i]+'79']={mel[i],mel[i+2],mel[i+4],mel[i+7],mel[i+10]}
        code[mel[i]+'add9']={mel[i],mel[i+2],mel[i+4],mel[i+7]}
        code[mel[i]+'M79']={mel[i],mel[i+2],mel[i+4],mel[i+7],mel[i+11]}
        
        code[mel[i]+'m']={mel[i],mel[i+3],mel[i+7]}     #m code
        code[mel[i]+'m6']={mel[i],mel[i+3],mel[i+7],mel[i+9]}
        code[mel[i]+'m7']={mel[i],mel[i+3],mel[i+7],mel[i+10]}
        code[mel[i]+'mM7']={mel[i],mel[i+3],mel[i+7],mel[i+11]}
        code[mel[i]+'m69']={mel[i],mel[i+2],mel[i+3],mel[i+7],mel[i+9]}
        code[mel[i]+'m79']={mel[i],mel[i+2],mel[i+3],mel[i+7],mel[i+10]}
        code[mel[i]+'madd9']={mel[i],mel[i+2],mel[i+3],mel[i+7]}
        code[mel[i]+'mM79']={mel[i],mel[i+2],mel[i+3],mel[i+7],mel[i+11]}
        
        code[mel[i]+'-5']={mel[i],mel[i+4],mel[i+6]}
        code[mel[i]+'m-5']={mel[i],mel[i+3],mel[i+6]}
        code[mel[i]+'m7-5']={mel[i],mel[i+3],mel[i+6],mel[i+10]}
        
        code[mel[i]+'sus4']={mel[i],mel[i+5],mel[i+7]}
        code[mel[i]+'sus2']={mel[i],mel[i+2],mel[i+7]} #sus2 is on code of sus4
        code[mel[i]+'aug']={mel[i],mel[i+4],mel[i+8]}
        code[mel[i]+'dim']={mel[i],mel[i+3],mel[i+6],mel[i+9]}
        
    return code
 
def all_scale():
    scale={}
    for i in range(12):
        scale[mel[i]+'M']={mel[i],mel[i+2],mel[i+4],mel[i+5],mel[i+7],mel[i+9],mel[i+11]}
        scale[mel[i]+'m']={mel[i],mel[i+2],mel[i+3],mel[i+5],mel[i+7],mel[i+8],mel[i+10]} #natural
        scale[mel[i]+'m2']={mel[i],mel[i+2],mel[i+3],mel[i+5],mel[i+7],mel[i+8],mel[i+11]} #harmonic
        scale[mel[i]+'m3']={mel[i],mel[i+2],mel[i+3],mel[i+5],mel[i+7],mel[i+9],mel[i+11]} #melodic
        scale[mel[i]+'Mpenta']={mel[i],mel[i+2],mel[i+4],mel[i+7],mel[i+9]}
        scale[mel[i]+'mpenta']={mel[i],mel[i+3],mel[i+5],mel[i+7],mel[i+10]}
    return scale


#tkinter
import tkinter
from tkinter import font
 
root = tkinter.Tk()
root.title("guitar starter")
root.geometry("1700x500+150+150")
C = tkinter.Canvas(root, height=500, width=1700)

def dosu(root,x):
    Rdic1={'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
    Rdic2={0:'R',1:'b9',2:'9',3:'m3',4:'M3',5:'p4',6:'b5',7:'p5',8:'aug',9:'6',10:'7',11:'M7'}
    Rdic_re={}
    for i in Rdic1:
        if i==root:
            root_number=Rdic1[i]
    for i in Rdic1:
        if Rdic1[i]-root_number>=0:
            Rdic_re[i]=Rdic2[Rdic1[i]-root_number]
        elif Rdic1[i]-root_number<0:
            Rdic_re[i]=Rdic2[Rdic1[i]-root_number+12]
    return Rdic_re[x]
 
def btn_click():#code
    code_name=txt.get()
    if len(code_name)>=2:
        if code_name[1]=='#':
            base=code_name[0:2]
        else:
            base=code_name[0]
    else:
        base=code_name[0]
    labels=[[0 for j in range(len(shiban[0]))] for i in range(len(shiban))]
    for i in range(len(shiban)):
        for j in range(len(shiban[0])):
            if shiban[i][j] == base:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=shiban[i][j], bg="red", fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            elif shiban[i][j] in all_code()[code_name]: #all_code()["C7"]
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=shiban[i][j], fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            else:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=shiban[i][j], fg="#badfbf", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            C.create_line(60*j+185, 30, 60*j+185, 340, fill='black')
            C.create_line(185, 50*i+55, 60*23+185, 50*i+55, fill='black')

def btn1_2_click():
    code_name=txt.get()
    if len(code_name)>=2:
        if code_name[1]=='#':
            base=code_name[0:2]
        else:
            base=code_name[0]
    else:
        base=code_name[0]
    labels=[[0 for j in range(len(shiban[0]))] for i in range(len(shiban))]
    for i in range(len(shiban)):
        for j in range(len(shiban[0])):
            if shiban[i][j] == base:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=dosu(base,shiban[i][j]), bg="red", fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            elif shiban[i][j] in all_code()[code_name]: #all_code()["C7"]
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=dosu(base,shiban[i][j]), fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            else:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=dosu(base,shiban[i][j]), fg="#badfbf", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            C.create_line(60*j+185, 30, 60*j+185, 340, fill='black')
            C.create_line(185, 50*i+55, 60*23+185, 50*i+55, fill='black')
 
def btn2_click():#scale
    scale_name=txt2.get()
    if len(scale_name)>=2:
        if scale_name[1]=='#':
            base=scale_name[0:2]
        else:
            base=scale_name[0]
    else:
        base=scale_name[0]
    labels=[[0 for j in range(len(shiban[0]))] for i in range(len(shiban))]
    for i in range(len(shiban)):
        for j in range(len(shiban[0])):
            if shiban[i][j] == base:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=shiban[i][j], bg="red", fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            elif shiban[i][j] in all_scale()[scale_name]:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=shiban[i][j], fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            else:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=shiban[i][j], fg="#badfbf", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            C.create_line(60*j+185, 30, 60*j+185, 340, fill='black')
            C.create_line(185, 50*i+55, 60*23+185, 50*i+55, fill='black')
 
def btn3_click():#scale_dosu
    scale_name=txt2.get()
    if len(scale_name)>=2:
        if scale_name[1]=='#':
            base=scale_name[0:2]
        else:
            base=scale_name[0]
    else:
        base=scale_name[0]
    labels=[[0 for j in range(len(shiban[0]))] for i in range(len(shiban))]
    for i in range(len(shiban)):
        for j in range(len(shiban[0])):
            if shiban[i][j] == base:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=dosu(base,shiban[i][j]), bg="red", fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            elif shiban[i][j] in all_scale()[scale_name]:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=dosu(base,shiban[i][j]), fg="Blue", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            else:
                font1=font.Font(family='Helvetica', size=20, weight='bold')
                labels[i][j]=tkinter.Label(root, text=dosu(base,shiban[i][j]), fg="#badfbf", font=font1)
                labels[i][j].place(x=60*j+140, y=50*i+40)
            C.create_line(60*j+185, 30, 60*j+185, 340, fill='black')
            C.create_line(185, 50*i+55, 60*23+185, 50*i+55, fill='black')
 

txt = tkinter.Entry(width=10)
txt.place(x=150, y=400)
btn = tkinter.Button(root, text='コード表示', command=btn_click)
btn.place(x=240, y=400)

btn1_2=tkinter.Button(root, text='コード度数表示', command=btn1_2_click)
btn1_2.place(x=240,y=440)

txt2 = tkinter.Entry(width=10)
txt2.place(x=350, y=400)
btn2 = tkinter.Button(root, text='スケール表示', command=btn2_click)
btn2.place(x=440, y=400)

btn2 = tkinter.Button(root, text='スケール度数表示', command=btn3_click)
btn2.place(x=440, y=440)
 
labels=[[0 for j in range(len(shiban[0]))] for i in range(len(shiban))]
for i in range(len(shiban)):
    for j in range(len(shiban[0])):
        if shiban[i][j] in {"C"}: #all_code()["C"]
            font1=font.Font(family='Helvetica', size=20, weight='bold')
            labels[i][j]=tkinter.Label(root, text=shiban[i][j], fg="Blue", font=font1)
            labels[i][j].place(x=60*j+140, y=50*i+40)
        else:
            font1=font.Font(family='Helvetica', size=20, weight='bold')
            labels[i][j]=tkinter.Label(root, text=shiban[i][j], fg="#badfbf", font=font1)
            labels[i][j].place(x=60*j+140, y=50*i+40)
        C.create_line(60*j+185, 30, 60*j+185, 340, fill='black')
        C.create_line(185, 50*i+55, 60*23+185, 50*i+55, fill='black')
 
font2=font.Font(family='Helvetica', size=13, weight='bold')
label2=tkinter.Label(root, text="開放弦", fg="red", font=font2)
label2.place(x=130, y=340)
 
labels2=[0 for j in range(len(shiban[0])-1)]
for j in range(len(shiban[0])-1):
    labels2[j]=tkinter.Label(root, text=str(j+1), fg="red", font=font2)
    labels2[j].place(x=60*j+140+65, y=50*6+40)
 
labels3=[0 for i in range(len(shiban))]
for i in range(len(shiban)):
    labels3[i]=tkinter.Label(root, text=str(i+1)+"弦", fg="red", font=font2)
    labels3[i].place(x=90, y=50*i+50)
 
C.pack()
root.mainloop()
 
