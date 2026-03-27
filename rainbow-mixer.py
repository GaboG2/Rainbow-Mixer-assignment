import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def change_bg_color(e):
        pass

    r_slider = ft.Slider(key = "r", min = 0, max = 255, on_change = change_bg_color)
    g_slider = ft.Slider(key = "g", min = 0, max = 255, on_change = change_bg_color)
    b_slider = ft.Slider(key = "b", min = 0, max = 255, on_change = change_bg_color)

    page.add(
        ft.Row(controls = [ft.Text("R"), r_slider], alignment = page.vertical_alignment),
        ft.Row(controls = [ft.Text("G"), g_slider], alignment = page.vertical_alignment),
        ft.Row(controls = [ft.Text("B"), b_slider], alignment = page.vertical_alignment)
    )

ft.app(target = main, assets_dir = "assets")