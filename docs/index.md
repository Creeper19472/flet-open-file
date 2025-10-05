# Introduction

FletOpenFile for Flet.

## Examples

```python
import flet as ft
from flet_open_file import OpenFile


async def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    open_file_service = OpenFile()
    page._services.append(open_file_service)
    await open_file_service.open("./README.md")

ft.run(main)
```

## Classes

[OpenFile](FletOpenFile.md)


