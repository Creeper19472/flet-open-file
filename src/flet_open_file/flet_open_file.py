from enum import Enum
from typing import Any, Optional

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber


class OpenFileState(Enum):
    OPEN_FILE = "openFile"


class FletOpenFile(ConstrainedControl):
    """
    FletOpenFile Control description.
    """

    def __init__(
        self,
        #
        # Control
        #
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        text: Optional[str] = None,
        #
        # ConstrainedControl
        #
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        #
        # FletOpenFile specific
        #
        value: Optional[str] = None,
    ):
        ConstrainedControl.__init__(
            self,
            tooltip=tooltip,
            opacity=opacity,
            visible=visible,
            data=data,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        self.value = value
        self.text = text

    def _get_control_name(self):
        return "flet_open_file"

    # value
    @property
    def value(self):
        """
        Value property description.
        """
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

    # text 
    @property
    def text(self):
        """
        Text property description.
        """
        return self._get_attr("text")

    @text.setter
    def text(self, text):
        self._set_attr("text", text)

    # state
    @property
    def state(self) -> Optional[OpenFileState]:
        return self.__state

    @state.setter
    def state(self, value: Optional[OpenFileState]):
        self.__state = value
        self._set_enum_attr("state", value, OpenFileState)

    def open_file(self, filepath):
        self.state = OpenFileState.OPEN_FILE
        self.update()

    # def pick_files(
    #     self,
    #     dialog_title: Optional[str] = None,
    #     initial_directory: Optional[str] = None,
    #     file_type: FilePickerFileType = FilePickerFileType.ANY,
    #     allowed_extensions: Optional[List[str]] = None,
    #     allow_multiple: Optional[bool] = False,
    # ):
    #     self.state = OpenFileState.OPEN_FILE
    #     self.dialog_title = dialog_title
    #     self.initial_directory = initial_directory
    #     self.file_type = file_type
    #     self.allowed_extensions = allowed_extensions
    #     self.allow_multiple = allow_multiple
    #     self.update()