import customtkinter
from PIL import Image, ImageTk  # 이미지 처리를 위해 Pillow 라이브러리 사용

# Appearance와 Theme 설정
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# CTk 윈도우 생성
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")  # 창 크기 설정

def close_window():
    app.destroy()  # 창을 닫는 함수
# 창 배경색 설정
app.configure(bg="green")  # 창 배경을 초록색으로 설정

# 버튼 함수 정의
def button1_function():
    close_window()
    import game
    close_window()

def button2_function():
    close_window()
    import quiz
    

def button3_function():
    close_window()
    import goodbye
    close_window()

# 이미지 로드 및 크기 조정
image = Image.open("source\sled.png")  # 'example.png'를 원하는 이미지 파일로 변경
image = image.resize((800, 350))  # 이미지 크기 조정
image_tk = ImageTk.PhotoImage(image)

# 이미지 레이블 추가
image_label = customtkinter.CTkLabel(master=app, image=image_tk, text="")  # 텍스트 없이 이미지만 표시
image_label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

text_label = customtkinter.CTkLabel(
    master=app,
    text="Christmas Toy Project",  # 원하는 텍스트 입력
    text_color="green",  # 텍스트 색상
    font=("Arial", 36)  # 글꼴과 크기
)
text_label.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

# 버튼 생성 및 배치 (배경색: 빨간색)
button1 = customtkinter.CTkButton(
    master=app, 
    text="game", 
    command=button1_function,
    fg_color="red",  # 버튼 배경색
    text_color="white"  # 버튼 글자 색
)
button1.place(relx=0.3, rely=0.7, anchor=customtkinter.CENTER)

button2 = customtkinter.CTkButton(
    master=app, 
    text="quiz", 
    command=button2_function,
    fg_color="red",  # 버튼 배경색
    text_color="white"  # 버튼 글자 색
)
button2.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

button3 = customtkinter.CTkButton(
    master=app, 
    text="good bye", 
    command=button3_function,
    fg_color="red",  # 버튼 배경색
    text_color="white"  # 버튼 글자 색
)
button3.place(relx=0.7, rely=0.7, anchor=customtkinter.CENTER)

# 메인 루프 실행
app.mainloop()
