# Introduction

FletOpenFile for Flet.

## Examples

```
import flet as ft

from flet_open_file import FletOpenFile


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletOpenFile(
                    tooltip="My new FletOpenFile Control tooltip",
                    value = "My new FletOpenFile Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[FletOpenFile](FletOpenFile.md)


