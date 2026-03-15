"""Demo showing ImGuiFileDialog integration in slimgui."""

from slimgui import imgui
from slimgui import file_dialog

from util import imgui_window


def run():
    window = imgui_window.ImguiWindow(
        title="File Dialog Demo",
        close_on_esc=True,
    )

    fd = file_dialog.FileDialog()
    selected_path = ""
    selected_files: dict[str, str] = {}

    while not window.should_close():
        window.begin_frame()

        imgui.text("ImGuiFileDialog Demo")
        imgui.separator()

        if imgui.button("Open File"):
            config = file_dialog.FileDialogConfig()
            config.path = "."
            fd.open_dialog(
                "open_file",
                "Choose a file",
                ".py,.cpp,.h,.txt,.md,.*",
                config,
            )

        if imgui.button("Save File"):
            config = file_dialog.FileDialogConfig()
            config.path = "."
            config.flags = file_dialog.FileDialogFlags.CONFIRM_OVERWRITE
            fd.open_dialog(
                "save_file",
                "Save file as",
                ".py,.txt,.md",
                config,
            )

        if imgui.button("Open Multiple"):
            config = file_dialog.FileDialogConfig()
            config.path = "."
            config.count_selection_max = 0  # unlimited
            fd.open_dialog(
                "open_multi",
                "Choose files",
                ".py,.cpp,.h,.txt,.md,.*",
                config,
            )

        imgui.separator()

        if selected_path:
            imgui.text(f"Selected: {selected_path}")

        if selected_files:
            imgui.text("Selection:")
            for name, path in selected_files.items():
                imgui.bullet_text(f"{name} -> {path}")

        # Display whichever dialog is open
        for key in ("open_file", "save_file", "open_multi"):
            if fd.is_opened(key):
                if fd.display(key, min_size=(600, 400)):
                    if fd.is_ok():
                        selected_path = fd.get_file_path_name()
                        selected_files = fd.get_selection()
                    fd.close()

        window.end_frame()
    window.close()


if __name__ == "__main__":
    run()
