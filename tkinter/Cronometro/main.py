import tkinter as tk

root_win = tk.Tk()
root_win.title("Cronómetro")
root_win.geometry("400x300")

cronometer_id = None

laps_num = 0

is_pause = False

def interface_reset():
    lap_button.pack_forget()
    pause_button.pack_forget()
    stop_button.pack_forget()
    start_button.config(text="INICIAR", command=interface)
    start_button.place(relx=0.5, rely=0.4, anchor='center')


def interface():
    start_button.place_forget()

    lap_button.pack(side='left', expand=True)
    pause_button.pack(side='left', expand=True)
    stop_button.pack(side='left', expand=True)
    
    crono(0, 0, 0, 0)

def crono(ms, sec, minu, hr):
    global cronometer_id
    global is_pause
    
    time_text.config(text=f"{hr}:{minu}:{sec}:{ms}")
    time_text.place(relx=0.5, rely=0.2, anchor='center')

    lap_button.config(command=lambda: lap(ms, sec, minu, hr))
    pause_button.config(command=lambda: pause(ms, sec, minu, hr))

    if is_pause is not True:
        is_pause = True
        stop_button.config(command=stop)
    else:
        stop_button.config(command=stop)


    if ms == 999: 
        ms = 0
        sec += 1
        if sec == 59:
            sec = 0
            minu += 1

            if minu == 59:
                minu = 0
                hr += 1
    else:
        ms += 1
    
    cronometer_id = root_win.after(1, lambda: crono(ms, sec, minu, hr))
    
def lap(ms, sec, minu, hr):
    global laps_num
    laps_num += 1
    lap_item = tk.Label(text=f"{laps_num}) {hr}:{sec}:{minu}:{ms}")
    lap_item.pack(anchor='e')

def pause(ms, sec, minu, hr):
    global cronometer_id
    global is_pause

    is_pause = True

    if cronometer_id is not None:
        root_win.after_cancel(cronometer_id)
        pause_button.config(text="Reanudar", command=lambda: reanude(ms, sec, minu, hr))

def reanude(ms, sec, minu, hr):
    global is_pause

    is_pause = False

    pause_button.config(text="Pausa")
    crono(ms, sec, minu, hr)

def stop():
    global cronometer_id
    root_win.after_cancel(cronometer_id)
    cronometer_id = None
    interface_reset()

# MAIN TEXT

main_text = tk.Label(root_win, text="CRONÓMETRO", compound=tk.TOP, font=("Helvetica", 20, "bold"), relief=tk.SOLID, highlightbackground="blue", highlightthickness=2)
main_text.place(relx=0.5, rely=0.06, anchor='center')

# TIME MARK

time_text = tk.Label(text="")

# ACTION BUTTONS

lap_button = tk.Button(text="Vuelta")
pause_button = tk.Button(text="Pausa")
stop_button = tk.Button(text="Detener")

# START BUTTON

start_button = tk.Button(root_win, text="INICIAR", command=interface)
start_button.place(relx=0.5, rely=0.4, anchor='center')

#interface()

root_win.mainloop()
