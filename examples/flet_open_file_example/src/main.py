import flet as ft

from flet_open_file import FletOpenFile


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    openfile = FletOpenFile(
                    tooltip="My new FletOpenFile Control tooltip",
                    value = "C:/Windows/System32/cmd.exe", 
                    text="Open Me",
                )

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=openfile,),

    )

ft.app(main)
