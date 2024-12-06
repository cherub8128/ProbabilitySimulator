import reflex as rx
from .navbar import navbar
import random as rd
from collections import Counter


class data(rx.State):
    n = 100
    m = 1
    items :list = ["1","2","3","4","5","6"]
    values : list = [[1, 2, 3, 4, 5, 6]]
    extracted : list = [[1, 2, 3, 4, 5, 6]]
    mean : float
    std : float
    sample_mean : float
    sample_std : float
    
    def generate(self):
        n = self.n
        self.values = [list(Counter(rd.choice(self.items)for _ in range(n)).values())]
        self.mean = sum([int(i)*v for i,v in zip(self.items,self.values[0])])/n
        self.std = sum([v*(float(i)-self.mean)**2 for i,v in zip(self.items,self.values[0])])/n
    def choice(self):
        m = self.m
        self.extracted = [list(Counter(rd.choices(self.items,weights=self.values[0],k=m)).values())]
        self.sample_mean = sum([int(i)*v for i,v in zip(self.items,self.extracted[0])])/(m-1)
        self.sample_std = sum([v*(float(i)-self.sample_mean)**2 for i,v in zip(self.items,self.extracted[0])])/(m-1)
    
    def set_n_end(self, n):
        self.n = n[0]
    def set_m_end(self, m):
        self.m = m[0]


def stat():
    return navbar(
        rx.accordion.root(
            rx.accordion.item(
                header="모집단",
                content=rx.data_table(
                    data=data.values,
                    columns=data.items
                ),
            ),
            rx.accordion.item(
                header="모집단의 통계",
                content=rx.vstack(
                    rx.text(f"평균: {data.mean}"),
                    rx.text(f"표준편차: {data.std}"),
                )
            ),
            collapsible=True,
            variant="outline",
            width="100%"
        ),
        rx.heading(data.n),
        rx.slider(
            default_value=data.n,
            on_value_commit=data.set_n_end,
            min=100,
            max=1000,
            width="300px",
        ),
        rx.button("재생성",on_click=data.generate()),
        rx.divider(),
        rx.heading(data.m),
        rx.slider(
            default_value=data.m,
            on_value_commit=data.set_m_end,
            min=1,
            max=data.n,
            width="300px",
        ),
        rx.button("추출",on_click=data.choice()),
        rx.text(f"표본평균 : {data.sample_mean}"),
        rx.text(f"표본표준편차: {data.sample_std}"),
        rx.data_table(
            data=data.extracted,
            columns=data.items
        ),
    )