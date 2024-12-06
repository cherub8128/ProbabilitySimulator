import reflex as rx
from .navbar import navbar
from .prob import prob
from .stat import stat

def index():
    return navbar(
      
    )

# em에 영향을 주는 폰트 사이즈
style = {
    "font_size": "20px",
    "font_family": "Noto Sans KR, sans-serif", # 글씨체를 바꾸기
}

# 바꿀 글씨체를 불러오기 위한 변수
font =  "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100..900&display=swap"

# 글씨체와 폰트 사이즈를 바꾸기 위해서는 App에 매개변수를 아래와 같이 추가한다.
app = rx.App(stylesheets=[font,], style=style)
app.add_page(index, title="확률과 통계")
app.add_page(prob, title="확률")
app.add_page(stat, title="통계")
