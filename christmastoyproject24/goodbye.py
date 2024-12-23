import customtkinter
from PIL import Image, ImageTk  # 이미지 처리를 위해 Pillow 라이브러리 사용

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
def close_window():
    app.destroy()
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")

def button_function():
    close_window()

image = Image.open("source\\mungsim.png")  # 'example.png'를 원하는 이미지 파일로 변경
image = image.resize((800, 450))  # 이미지 크기 조정
image_tk = ImageTk.PhotoImage(image)

# 이미지 레이블 추가
image_label = customtkinter.CTkLabel(master=app, image=image_tk, text="")  # 텍스트 없이 이미지만 표시
image_label.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)

text_label = customtkinter.CTkLabel(
    master=app,
    text="MERRY CHRISTMAS\nAND\nHAPPY NEW YEAR!",  # 원하는 텍스트 입력
    text_color="green",  # 텍스트 색상
    font=("Arial", 36)  # 글꼴과 크기
)
text_label.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

# 버튼 생성 및 배치 (배경색: 빨간색)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="BYE", command=button_function)
button.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

app.mainloop()