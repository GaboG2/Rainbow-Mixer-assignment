import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def change_bg_color(e):
        r = int(r_slider.value)
        g = int(g_slider.value)
        b = int(b_slider.value)
        
        page.bgcolor = f"#{r:02x}{g:02x}{b:02x}"
        header.value = f"Adjust the sliders to change the color of the background.\n{r}, {g}, {b}"
        textStyle.color = f"#{(255 - r):02x}{(255 - g):02x}{(255 - b):02x}"

    r_slider = ft.Slider(key = "r", min = 0, max = 255, value = 0, on_change = change_bg_color)
    g_slider = ft.Slider(key = "g", min = 0, max = 255, value = 0, on_change = change_bg_color)
    b_slider = ft.Slider(key = "b", min = 0, max = 255, value = 0, on_change = change_bg_color)

    textStyle = ft.TextStyle(color = "#ffffff") # by default
    header = ft.Text(value = "Adjust the sliders to change the color of the background.\n0, 0, 0", style = textStyle)

    page.add(
        header,
        ft.Row(controls = [ft.Text(value = "R", style = textStyle), r_slider], alignment = page.vertical_alignment),
        ft.Row(controls = [ft.Text(value = "G", style = textStyle), g_slider], alignment = page.vertical_alignment),
        ft.Row(controls = [ft.Text(value = "B", style = textStyle), b_slider], alignment = page.vertical_alignment)
    )

ft.app(target = main, assets_dir = "assets")