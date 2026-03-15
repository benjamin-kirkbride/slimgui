import enum
from typing import overload, Any

import slimgui_ext.imgui


class FileDialogFlags(enum.IntEnum):
    NONE = 0

    CONFIRM_OVERWRITE = 1

    DONT_SHOW_HIDDEN_FILES = 2

    DISABLE_CREATE_DIRECTORY_BUTTON = 4

    HIDE_COLUMN_TYPE = 8

    HIDE_COLUMN_SIZE = 16

    HIDE_COLUMN_DATE = 32

    NO_DIALOG = 64

    READ_ONLY_FILE_NAME_FIELD = 128

    CASE_INSENSITIVE_EXTENTION_FILTERING = 256

    MODAL = 512

    DISABLE_THUMBNAIL_MODE = 1024

    DISABLE_PLACE_MODE = 2048

    DISABLE_QUICK_PATH_SELECTION = 4096

    SHOW_DEVICES_BUTTON = 8192

NONE: FileStyleFlags = FileStyleFlags.NONE

CONFIRM_OVERWRITE: FileDialogFlags = FileDialogFlags.CONFIRM_OVERWRITE

DONT_SHOW_HIDDEN_FILES: FileDialogFlags = FileDialogFlags.DONT_SHOW_HIDDEN_FILES

DISABLE_CREATE_DIRECTORY_BUTTON: FileDialogFlags = FileDialogFlags.DISABLE_CREATE_DIRECTORY_BUTTON

HIDE_COLUMN_TYPE: FileDialogFlags = FileDialogFlags.HIDE_COLUMN_TYPE

HIDE_COLUMN_SIZE: FileDialogFlags = FileDialogFlags.HIDE_COLUMN_SIZE

HIDE_COLUMN_DATE: FileDialogFlags = FileDialogFlags.HIDE_COLUMN_DATE

NO_DIALOG: FileDialogFlags = FileDialogFlags.NO_DIALOG

READ_ONLY_FILE_NAME_FIELD: FileDialogFlags = FileDialogFlags.READ_ONLY_FILE_NAME_FIELD

CASE_INSENSITIVE_EXTENTION_FILTERING: FileDialogFlags = FileDialogFlags.CASE_INSENSITIVE_EXTENTION_FILTERING

MODAL: FileDialogFlags = FileDialogFlags.MODAL

DISABLE_THUMBNAIL_MODE: FileDialogFlags = FileDialogFlags.DISABLE_THUMBNAIL_MODE

DISABLE_PLACE_MODE: FileDialogFlags = FileDialogFlags.DISABLE_PLACE_MODE

DISABLE_QUICK_PATH_SELECTION: FileDialogFlags = FileDialogFlags.DISABLE_QUICK_PATH_SELECTION

SHOW_DEVICES_BUTTON: FileDialogFlags = FileDialogFlags.SHOW_DEVICES_BUTTON

class ResultMode(enum.Enum):
    ADD_IF_NO_FILE_EXT = 0

    OVERWRITE_FILE_EXT = 1

    KEEP_INPUT_FILE = 2

ADD_IF_NO_FILE_EXT: ResultMode = ResultMode.ADD_IF_NO_FILE_EXT

OVERWRITE_FILE_EXT: ResultMode = ResultMode.OVERWRITE_FILE_EXT

KEEP_INPUT_FILE: ResultMode = ResultMode.KEEP_INPUT_FILE

class FileStyleFlags(enum.IntEnum):
    NONE = 0

    BY_TYPE_FILE = 1

    BY_TYPE_DIR = 2

    BY_TYPE_LINK = 4

    BY_EXTENTION = 8

    BY_FULL_NAME = 16

    BY_CONTAINED_IN_FULL_NAME = 32

BY_TYPE_FILE: FileStyleFlags = FileStyleFlags.BY_TYPE_FILE

BY_TYPE_DIR: FileStyleFlags = FileStyleFlags.BY_TYPE_DIR

BY_TYPE_LINK: FileStyleFlags = FileStyleFlags.BY_TYPE_LINK

BY_EXTENTION: FileStyleFlags = FileStyleFlags.BY_EXTENTION

BY_FULL_NAME: FileStyleFlags = FileStyleFlags.BY_FULL_NAME

BY_CONTAINED_IN_FULL_NAME: FileStyleFlags = FileStyleFlags.BY_CONTAINED_IN_FULL_NAME

class FileDialogConfig:
    def __init__(self) -> None: ...

    @property
    def path(self) -> str: ...

    @path.setter
    def path(self, arg: str, /) -> None: ...

    @property
    def file_name(self) -> str: ...

    @file_name.setter
    def file_name(self, arg: str, /) -> None: ...

    @property
    def file_path_name(self) -> str: ...

    @file_path_name.setter
    def file_path_name(self, arg: str, /) -> None: ...

    @property
    def count_selection_max(self) -> int: ...

    @count_selection_max.setter
    def count_selection_max(self, arg: int, /) -> None: ...

    @property
    def flags(self) -> int: ...

    @flags.setter
    def flags(self, arg: int, /) -> None: ...

    @property
    def side_pane_width(self) -> float: ...

    @side_pane_width.setter
    def side_pane_width(self, arg: float, /) -> None: ...

class FileDialog:
    def __init__(self) -> None: ...

    def open_dialog(self, key: str, title: str, filters: str, config: FileDialogConfig = ...) -> None: ...

    def display(self, key: str, flags: int = 32, min_size: tuple[float, float] = (0.0, 0.0), max_size: tuple[float, float] = (3.4028234663852886e+38, 3.4028234663852886e+38)) -> bool: ...

    def close(self) -> None: ...

    def is_ok(self) -> bool: ...

    @overload
    def is_opened(self, key: str) -> bool: ...

    @overload
    def is_opened(self) -> bool: ...

    @overload
    def was_opened_this_frame(self, key: str) -> bool: ...

    @overload
    def was_opened_this_frame(self) -> bool: ...

    def get_opened_key(self) -> str: ...

    def get_file_path_name(self, mode: ResultMode = ResultMode.ADD_IF_NO_FILE_EXT) -> str: ...

    def get_current_file_name(self, mode: ResultMode = ResultMode.ADD_IF_NO_FILE_EXT) -> str: ...

    def get_current_path(self) -> str: ...

    def get_current_filter(self) -> str: ...

    def get_selection(self, mode: ResultMode = ResultMode.KEEP_INPUT_FILE) -> dict[str, str]: ...

    def set_file_style(self, flags: int, criteria: str, color: tuple[float, float, float, float], icon: str = '', font: slimgui_ext.imgui.Font | None = None) -> None: ...

    def clear_file_styles(self) -> None: ...

    def set_locales(self, locale_category: int, locale_begin: str, locale_end: str) -> None: ...
