import ui
import console
 
inputNumber=''
firstNumber = ''
secondNumber=''
operation=''
is_room=''
room_ = ''
time_ = ''

def room_del(event_nds):
	  sv = event_nds.superview
	  sv['room'].text = ''
	  global inputNumber
	  inputNumber=''
	  
def time_del(event_nds):
	  sv = event_nds.superview
	  sv['time'].text = ''
	  global inputNumber
	  inputNumber=''


def check_input(room_obj, is_room):

    if is_room:
        disp = room_obj
    else:
        disp = time_obj
    
    return disp

def room_on(event_nds):
    #print('here')
    global is_room
    is_room = True
    global inputNumber
    inputNumber=''
    
def room_off(event_nds):
	  global is_room
	  is_room = False
	  global inputNumber
	  inputNumber=''

def alert_button(event_nds):
    value = console.input_alert("Title", "メッセージを入力", "", "OK")

 
#数字ボタンに割り当てる処理
def numberButtonAction(event_nds):
    d = check_input(room_obj, is_room)
    global inputNumber
    inputNumber = inputNumber +event_nds.title
    d.text = inputNumber


#ACボタンに割り当てる処理
def acButtonAction(event):
    global inputNumber, firstNumber
    global secondNumber, operation
    inputNumber = ''
    firstNumber=''
    secondNumber=''
    operation=''
    v['label1'].text='0'

def convNumber(no):
    newno = float(no)
    if newno.is_integer():
        return str(int(newno))
    else:
        return str(newno)
        
def send_data(event_nds):
	 sv = event_nds.superview
	 global room_
	 global time_
	 room_ = sv['room'].text
	 time_ = sv['time'].text
	 
	 with open('tmp.txt', 'w') as f:
	     f.write(f'room,{room_}\ntime,{time_}')
	 if (room_ and time_):
	     console.alert(f'room -> {room_}\ntime -> {time_}')
	  
	 
 
v = ui.load_view()
room_obj=v['room']
room_obj.enabled = False
time_obj=v["time"]
time_obj.enabled = False
v.present('sheet')


