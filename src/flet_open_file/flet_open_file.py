from typing import Optional
import flet as ft


@ft.control("OpenFile")
class OpenFile(ft.Service):
    """
    A control to open various files using flutter package `open_file`..

    Note:
        This control is non-visual and should be added to
        [`Page.services`][flet.Page.services]
        list before it can be used.
    """
    last_opened_path: Optional[str] = None

    def before_update(self):
        super().before_update()

    async def open(self, path: Optional[str] = None, timeout: Optional[float] = 10):
        if not path:
            path = self.last_opened_path
        
        self.last_opened_path = path
        await self._invoke_method(
            method_name="open",
            arguments={"path": path},
            timeout=timeout,
        )