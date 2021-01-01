import ui
import console
import keyboard

def submit_data(sender):
	  v = sender.superview
	  print(v['room_id'].text)
	  console.alert('設定が完了しました！')

v = ui.load_view()
#v.present('sheet')

keyboard.set_view(v)
