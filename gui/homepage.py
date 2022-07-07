from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Listbox, Scrollbar, Toplevel
from gui.setting import show_setting

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_url():
    listbox.delete(0, "end")
    URL = entry_1.get()
    print(URL)

def show_format(button):
    if button==1:
        canvas.itemconfig(example,tex="示例链接 :https://www.bilibili.com/video/ID1RF411u78P  https://bilibili.tv/pjRufMo")
    elif button==2:
        canvas.itemconfig(example,text="示例链接 :https://v.douyin.com/FSXuqh5/")
    elif button==3:
        canvas.itemconfig(example,text="示例链接 :https://www.zhihu.com/zvideo/1456616918891859968")
    elif button==4:
        canvas.itemconfig(example, text="示例链接 :https://www.pearvideo.com/video_1760884")

window = Tk()
window.geometry("960x540")
window.configure(bg="#FFFFFF")
window.title("")
window.iconphoto(False, PhotoImage(file='images/icon.png'))
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=540,
    width=960,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    960.0,
    64.0,
    fill="#F6F4F2",
    outline="")

canvas.create_rectangle(
    0.0,
    64.0,
    160.0,
    540.0,
    fill="#E5E2E1",
    outline="")

canvas.create_rectangle(
    160.0,
    64.0,
    960.0,
    540.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_bilibili.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_format(1),
    relief="flat"
)
button_1.place(
    x=12.0,
    y=111.0,
    width=120.0,
    height=33.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_tiktok.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_format(2),
    relief="flat"
)
button_2.place(
    x=12.0,
    y=151.0,
    width=120.0,
    height=33.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_zhihu.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_format(3),
    relief="flat"
)
button_3.place(
    x=12.0,
    y=191.0,
    width=120.0,
    height=33.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_pearvideo.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_format(4),
    relief="flat"
)
button_4.place(
    x=12.0,
    y=231.0,
    width=120.0,
    height=33.0
)

canvas.create_text(
    39.0,
    87.0,
    anchor="nw",
    text="支持网站",
    fill="#838180",
    font=("Inter", 10 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_setting.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_setting(window),
    relief="flat"
)
button_5.place(
    x=20.0,
    y=476.0,
    width=120.0,
    height=33.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_custom.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=232.0,
    y=101.0,
    width=139.0,
    height=25.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_url.png"))
entry_bg_1 = canvas.create_image(
    533.0,
    170.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=282.0,
    y=161.0,
    width=502.0,
    height=21.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_analyse.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_url(),
    relief="flat"
)
button_7.place(
    x=845.0,
    y=160.0,
    width=55.0,
    height=23.0
)

canvas.create_text(
    232.0,
    165.0,
    anchor="nw",
    text="URL :",
    fill="#000000",
    font=("Inter", 11 * -1)
)
canvas.create_text(
    39.0,
    87.0,
    anchor="nw",
    text="支持网站",
    fill="#838180",
    font=("Inter", 10 * -1)
)

canvas.create_rectangle(
    222.0,
    214.0,
    910.0,
    500.0,
    fill="#F6F4F2",
    outline="")

example=canvas.create_text(
    231.0,
    190.0,
    anchor="nw",
    text="链接示例： ",
    fill="#838180",
    font=("Inter", 10 * -1)
)

canvas.create_text(
    236.0,
    219.0,
    anchor="nw",
    text="序号",
    fill="#000000",
    font=("Inter", 11 * -1)
)

canvas.create_text(
    274.0,
    219.0,
    anchor="nw",
    text="名称",
    fill="#000000",
    font=("Inter", 11 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_download.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=810.0,
    y=469.0,
    width=63.0,
    height=16.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_clear.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=722.0,
    y=470.0,
    width=63.0,
    height=16.0
)

canvas.create_text(
    456.0,
    20.0,
    anchor="nw",
    text="Chaos",
    fill="#000000",
    font=("Inter", 24 * -1)
)

scrollbar = Scrollbar(window, orient="vertical")
listbox = Listbox(
    bg="#FFFFFF",
    bd="0",
    yscrollcommand=scrollbar.set
)
listbox.place(
    x=230,
    y=235,
    width=670,
    height=230
)

window.resizable(False, False)
window.mainloop()
