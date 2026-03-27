import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def change_bg_color(e):
        page.bgcolor = f"#{r_slider.value:02x}{g_slider.value:02x}{b_slider.value:02x}"

    r_slider = ft.Slider(key = "r", min = 0, max = 255, label = "R")
    g_slider = ft.Slider(key = "g", min = 0, max = 255, label = "G")
    b_slider = ft.Slider(key = "b", min = 0, max = 255, label = "B")

    page.add(r_slider, g_slider, b_slider)

ft.app(target = main, assets_dir = "assets")