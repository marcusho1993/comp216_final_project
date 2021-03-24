
"""
Winter 2021
COMP 216-001
Lab 09 & 10 - Data Display

Team members:

1. Vincent Tse - 301050515
2. Santiago Yepes Carrera - 301082274
3. Erwin Joshua Manuel - 301107750
4. Hoi Fong Ho - 301084469
5. Kenneth Austin - 301040904
"""

from tkinter import *
from tkinter import ttk, messagebox


def create_form():
    # main window
    window = Tk()
    window.title("Data Display - GUI")

    frame = ttk.Frame(window, width=600, height=400)
    frame.grid()
    frame['padding'] = (5, 10)
    frame['borderwidth'] = 10

    """
    row 1 - stock price field
    """
    label_stock_price = ttk.Label(frame, text="Stock Price:")
    label_stock_price.grid(row=0, column=0, sticky=(W, E))

    entry_stock_price = StringVar()
    ttk.Entry(frame, textvariable=entry_stock_price).grid(row=0, column=1, sticky=(W, E))
    
    """
    row 2 - buttons
    """
    ttk.Button(frame, text='Reset', command=lambda: reset_form()).grid(row=1, column=0, sticky=(W, E))
    ttk.Button(frame, text='Set Price', command=lambda: send_form()).grid(row=1, column=1, sticky=(W, E))
    ttk.Button(frame, text='Exit', command=lambda: window.quit()).grid(row=1, column=2, sticky=(W, E))

    def send_form():
        stock_price = int(entry_stock_price.get())
        if stock_price < min_gauge_value:
            messagebox.showinfo(title="Form Information", message=f'Minimum value must be {min_gauge_value}')
            reset_form()
        elif stock_price > max_gauge_value:
            messagebox.showinfo(title="Form Information", message=f'Maximum value must be {max_gauge_value}')
            reset_form()
        else:
            # set gauge value
            update_gauge(stock_price)
            # set progress bar value
            progress_bar['value'] = stock_price
            label_pb_value = ttk.Label(frame, text=entry_stock_price.get())
            label_pb_value.grid(row=2, column=2)



    def reset_form():
        window.destroy()
        create_form()

    
    """
    row 3 - draw gauge
    """
    # Create Canvas objects    
    gauge_canvas_width = 400
    gauge_canvas_height = 250
    gauge_canvas = Canvas(frame, width=gauge_canvas_width, height=gauge_canvas_height)
    gauge_canvas.grid(row=2, column=1)
    # gauge parameters
    gauge_coord = 10, 50, 350, 350 # define the size of the gauge (x1, y1, x2, y2)
    min_gauge_value = 0 # chart low range
    max_gauge_value = 100 # chart hi range
    # draw background arc
    gauge_canvas.create_arc(gauge_coord, start=30, extent=120, fill="white",  width=1)    
    # draw hi/low color bands
    gauge_canvas.create_arc(gauge_coord, start=30, extent=120, outline="green", style= "arc", width=40)
    gauge_canvas.create_arc(gauge_coord, start=50, extent=20, outline="yellow", style= "arc", width=40)
    gauge_canvas.create_arc(gauge_coord, start=30, extent=20, outline="red", style= "arc", width=40)
    # add needle/value pointer
    gauge_needle = gauge_canvas.create_arc(gauge_coord, start= 148, extent=1, width=7)
    # add labels
    gauge_canvas.create_text((gauge_coord[0]+gauge_coord[2])/2, 15, font="Times 20 italic bold", text="Stock Price Gauge")
    gauge_canvas.create_text(gauge_coord[0], (gauge_coord[3]-gauge_coord[1])/2, font="Times 12 bold", text=min_gauge_value)
    gauge_canvas.create_text(gauge_coord[2], (gauge_coord[3]-gauge_coord[1])/2, font="Times 12 bold", text=max_gauge_value)
    gauge_needle_value = gauge_canvas.create_text((gauge_coord[0]+gauge_coord[2])/2, 220, font="Times 15 bold", text="0")


    def update_gauge(new_value):
        gauge_canvas.itemconfig(gauge_needle_value, text = str(new_value))
        # Rescale value to angle range (0%=120deg, 100%=30 deg)
        angle = 120 * (max_gauge_value - new_value)/(max_gauge_value - min_gauge_value) + 30
        gauge_canvas.itemconfig(gauge_needle, start = angle)


    """
    row 4 - draw progress bar
    """
    # create progress bar
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("TProgressbar", foreground='green', background='green')
    progress_bar = ttk.Progressbar(frame, style='TProgressbar', orient=VERTICAL, length=200, mode='determinate')
    progress_bar.grid(row=2, column=2)
    # add progress bar labels
    label_pb_min = ttk.Label(frame, text=min_gauge_value)
    label_pb_min.grid(row=2, column=2, sticky='S')
    label_pb_max = ttk.Label(frame, text=max_gauge_value)
    label_pb_max.grid(row=2, column=2, sticky='N')



    # launch form
    mainloop()


if __name__ == '__main__':
    create_form()
