from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from tkinter.filedialog import askdirectory

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def select_path():
    path = askdirectory()
    print(path)

def show_setting(window):
    setting = Toplevel()
    setting.title("设置")
    setting.geometry("334x183")
    setting.configure(bg = "#FFFFFF")


    canvas = Canvas(
        setting,
        bg = "#FFFFFF",
        height = 183,
        width = 334,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        49.0,
        47.0,
        anchor="nw",
        text="下载目录：",
        fill="#000000",
        font=("Inter", 18 * -1)
    )

    button_image_path = PhotoImage(
        file=relative_to_assets("button_path.png"))
    button_path = Button(
        setting,
        text='点击选取路径',
        borderwidth=0,
        highlightthickness=0,
        command=lambda: select_path(),
        relief="flat"
    )
    button_path.place(
        x=167.0,
        y=44.0,
        width=112.0,
        height=29.0
    )

    canvas.create_text(
        49.0,
        110.0,
        anchor="nw",
        text="视频默认画质：",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    canvas.create_text(
        49.0,
        80.0,
        anchor="nw",
        text="当前目录：Download/chaos",
        fill="#A0A0A0",
        font=("Inter", 12 * -1)
    )
    setting.resizable(False, False)
    setting.mainloop()
