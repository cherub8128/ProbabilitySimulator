# navbar.py 파일 만들기
import reflex as rx

# 네비게이션 링크 모양을 재사용하기 위해 만든 컴포넌트
def navbar_link(text, url):
  return rx.link(rx.text(text, size="4", weight="medium"), href=url)

def logo(text):
  return rx.hstack(
    # assets 폴더에 logo로 사용할 이미지를 logo.png 이름으로 넣기(flaticon 사이트에서 다운로드)
    rx.image(
      src="/logo.png",
      height="2em",
    ),
    rx.heading(text, size="7", color_scheme="cyan"),
    align_items="center",
  ),

def navbar_comp():
  return rx.box(
    # hstack은 가로로 쌓는 레이아웃 컴포넌트
    rx.hstack(
      logo("확률과 통계 시뮬레이터"),
      rx.hstack(
        navbar_link("홈", "/#"),
        navbar_link("확률", "/prob"),
        navbar_link("통계적 추정", "/stat"),
        rx.color_mode.button(),
        justify="end",
        align="center",
        spacing="5",
      ),
      justify="between",
      align_items="center",
    ),
    bg=rx.color("indigo", 3), 
    padding="0.5em", 
    width="100%",
  )
  
def navbar(*arg,**kwarg):
  return rx.fragment(
    rx.text("Created by 차형준",position="absolute",bottom="10px",right="10px",color_scheme="gray"),
    navbar_comp(),
    rx.vstack(
      *arg,
      **kwarg,
      padding="1em",
      width="100%",
      spacing="4"
    ),
  )