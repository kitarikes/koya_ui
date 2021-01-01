import ui
import console
import keyboard

def submit_data(sender):
		value = console.input_alert("Title", "メッセージを入力", "", "OK")
		v = sender.superview
		v['room'].text = value
		console.alert('設定が完了しました！')

v = ui.load_view()
#v.present('sheet')

keyboard.set_view(v)
