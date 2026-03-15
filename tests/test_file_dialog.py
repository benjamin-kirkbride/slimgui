import pytest
from slimgui import imgui, file_dialog


@pytest.fixture
def context():
    imgui.set_nanobind_leak_warnings(True)
    ctx = imgui.create_context()
    imgui.get_io().ini_filename = None
    yield
    imgui.destroy_context(ctx)


@pytest.fixture
def null_renderer(context):
    from slimgui.integrations.null import NullRenderer
    renderer = NullRenderer()
    yield renderer


@pytest.fixture
def frame_scope(context, null_renderer):
    io = imgui.get_io()
    io.display_size = 640, 800
    null_renderer.refresh_font_texture()
    imgui.new_frame()


def test_file_dialog_config():
    config = file_dialog.FileDialogConfig()
    assert config.path == ""
    assert config.file_name == ""
    assert config.file_path_name == ""
    assert config.count_selection_max == 1
    assert config.flags == file_dialog.FileDialogFlags.NONE
    assert config.side_pane_width == 250.0

    config.path = "/tmp"
    assert config.path == "/tmp"
    config.file_name = "test.txt"
    assert config.file_name == "test.txt"
    config.count_selection_max = 5
    assert config.count_selection_max == 5


def test_enum_values():
    assert file_dialog.FileDialogFlags.NONE == 0
    assert file_dialog.FileDialogFlags.CONFIRM_OVERWRITE != 0
    assert file_dialog.FileDialogFlags.MODAL != 0

    # ResultMode is not a flag enum, so just check values exist and are distinct
    assert file_dialog.ResultMode.ADD_IF_NO_FILE_EXT != file_dialog.ResultMode.OVERWRITE_FILE_EXT
    assert file_dialog.ResultMode.OVERWRITE_FILE_EXT != file_dialog.ResultMode.KEEP_INPUT_FILE
    assert file_dialog.ResultMode.ADD_IF_NO_FILE_EXT != file_dialog.ResultMode.KEEP_INPUT_FILE

    assert file_dialog.FileStyleFlags.NONE == 0
    assert file_dialog.FileStyleFlags.BY_TYPE_FILE != 0


def test_file_dialog_lifecycle(frame_scope):
    fd = file_dialog.FileDialog()
    assert not fd.is_opened()

    config = file_dialog.FileDialogConfig()
    config.path = "."
    fd.open_dialog("test_key", "Open File", ".txt,.py", config)
    assert fd.is_opened()
    assert fd.is_opened("test_key")
    assert fd.get_opened_key() == "test_key"

    fd.display("test_key")
    fd.close()


def test_get_selection(frame_scope):
    fd = file_dialog.FileDialog()
    config = file_dialog.FileDialogConfig()
    config.path = "."
    fd.open_dialog("sel_key", "Open File", ".txt", config)
    fd.display("sel_key")

    selection = fd.get_selection()
    assert isinstance(selection, dict)

    fd.close()


def test_file_dialog_not_opened():
    fd = file_dialog.FileDialog()
    assert not fd.is_opened()
    assert not fd.is_ok()
    assert fd.get_opened_key() == ""
