import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def change_bg_color(e):
        pass

    r_slider = ft.Slider(key = "r", min = 0, max = 255, label = "R", on_change = change_bg_color)
    g_slider = ft.Slider(key = "g", min = 0, max = 255, label = "G", on_change = change_bg_color)
    b_slider = ft.Slider(key = "b", min = 0, max = 255, label = "B", on_change = change_bg_color)

    page.add(r_slider, g_slider, b_slider)

ft.app(target = main, assets_dir = "assets")