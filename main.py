import flet as ft

def main(page: ft.Page):
    page.title = "calculator"
    t = ft.Text(value="", size=20)
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.width = 300
    page.window.height = 500
    page.window.resizable = False

    def handle_btn(val):
        def handler(e):
            if "=" in t.value:
                if val in "+-*/":
                    t.value = t.value.split("=")[-1] + val
                else:
                    t.value = val
            else:
                t.value += val
            page.update()
        return handler

    def com_c(e):
        t.value = ""
        page.update()

    def com_can(e):
        if "=" in t.value:
            t.value = ""
        elif len(t.value) != 0:
            t.value = t.value[:-1]
        page.update()

    def com_equal(e):
        if not t.value or "=" in t.value:
            return
        try:
            result = eval(t.value)
            if result == int(result):
                result = int(result)
            t.value = t.value + "=" + str(result)
        except:
            t.value = "خطأ"
        page.update()

    def make_btn(label, handler, color=None):
        return ft.Button(
            content=label,
            on_click=handler,
            color=color,
        )

    buttons = [
        [make_btn("7", handle_btn("7")), make_btn("8", handle_btn("8")),
         make_btn("9", handle_btn("9")), make_btn("*", handle_btn("*"), "orange")],
        [make_btn("4", handle_btn("4")), make_btn("5", handle_btn("5")),
         make_btn("6", handle_btn("6")), make_btn("/", handle_btn("/"), "orange")],
        [make_btn("1", handle_btn("1")), make_btn("2", handle_btn("2")),
         make_btn("3", handle_btn("3")), make_btn("+", handle_btn("+"), "orange")],
        [make_btn("C", com_c, "red"), make_btn("0", handle_btn("0")),
         make_btn("=", com_equal, "green"), make_btn("-", handle_btn("-"), "orange")],
    ]

    bt_can = ft.IconButton(
        icon=ft.Icons.CANCEL_SHARP,
        on_click=com_can,
    )

    column_bt = ft.Column([ft.Row(row) for row in buttons])

    maincolumn = ft.Column([
        ft.Container(content=ft.Column([
            t,
            ft.Container(content=bt_can, alignment=ft.Alignment(1, 1))
        ])),
        ft.Container(content=column_bt, padding=5)
    ], spacing=10)

    main_con = ft.Container(maincolumn, alignment=ft.Alignment(0, 0))
    page.add(main_con)

ft.app(target=main)
