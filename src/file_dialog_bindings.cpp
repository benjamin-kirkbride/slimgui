#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/map.h>
#include <nanobind/stl/tuple.h>

#include "imgui.h"
#include "ImGuiFileDialog.h"

namespace nb = nanobind;
using namespace nb::literals;

void file_dialog_bindings(nb::module_& m) {
    // --- Enums ---

    nb::enum_<ImGuiFileDialogFlags_>(m, "FileDialogFlags", nb::is_arithmetic())
        .value("NONE", ImGuiFileDialogFlags_None)
        .value("CONFIRM_OVERWRITE", ImGuiFileDialogFlags_ConfirmOverwrite)
        .value("DONT_SHOW_HIDDEN_FILES", ImGuiFileDialogFlags_DontShowHiddenFiles)
        .value("DISABLE_CREATE_DIRECTORY_BUTTON", ImGuiFileDialogFlags_DisableCreateDirectoryButton)
        .value("HIDE_COLUMN_TYPE", ImGuiFileDialogFlags_HideColumnType)
        .value("HIDE_COLUMN_SIZE", ImGuiFileDialogFlags_HideColumnSize)
        .value("HIDE_COLUMN_DATE", ImGuiFileDialogFlags_HideColumnDate)
        .value("NO_DIALOG", ImGuiFileDialogFlags_NoDialog)
        .value("READ_ONLY_FILE_NAME_FIELD", ImGuiFileDialogFlags_ReadOnlyFileNameField)
        .value("CASE_INSENSITIVE_EXTENTION_FILTERING", ImGuiFileDialogFlags_CaseInsensitiveExtentionFiltering)
        .value("MODAL", ImGuiFileDialogFlags_Modal)
        .value("DISABLE_THUMBNAIL_MODE", ImGuiFileDialogFlags_DisableThumbnailMode)
        .value("DISABLE_PLACE_MODE", ImGuiFileDialogFlags_DisablePlaceMode)
        .value("DISABLE_QUICK_PATH_SELECTION", ImGuiFileDialogFlags_DisableQuickPathSelection)
        .value("SHOW_DEVICES_BUTTON", ImGuiFileDialogFlags_ShowDevicesButton)
        .export_values();

    nb::enum_<IGFD_ResultMode_>(m, "ResultMode")
        .value("ADD_IF_NO_FILE_EXT", IGFD_ResultMode_AddIfNoFileExt)
        .value("OVERWRITE_FILE_EXT", IGFD_ResultMode_OverwriteFileExt)
        .value("KEEP_INPUT_FILE", IGFD_ResultMode_KeepInputFile)
        .export_values();

    nb::enum_<IGFD_FileStyleFlags_>(m, "FileStyleFlags", nb::is_arithmetic())
        .value("NONE", IGFD_FileStyle_None)
        .value("BY_TYPE_FILE", IGFD_FileStyleByTypeFile)
        .value("BY_TYPE_DIR", IGFD_FileStyleByTypeDir)
        .value("BY_TYPE_LINK", IGFD_FileStyleByTypeLink)
        .value("BY_EXTENTION", IGFD_FileStyleByExtention)
        .value("BY_FULL_NAME", IGFD_FileStyleByFullName)
        .value("BY_CONTAINED_IN_FULL_NAME", IGFD_FileStyleByContainedInFullName)
        .export_values();

    // --- FileDialogConfig ---

    nb::class_<IGFD::FileDialogConfig>(m, "FileDialogConfig")
        .def(nb::init<>())
        .def_rw("path", &IGFD::FileDialogConfig::path)
        .def_rw("file_name", &IGFD::FileDialogConfig::fileName)
        .def_rw("file_path_name", &IGFD::FileDialogConfig::filePathName)
        .def_rw("count_selection_max", &IGFD::FileDialogConfig::countSelectionMax)
        .def_rw("flags", &IGFD::FileDialogConfig::flags)
        .def_rw("side_pane_width", &IGFD::FileDialogConfig::sidePaneWidth);

    // --- FileDialog ---

    nb::class_<IGFD::FileDialog>(m, "FileDialog")
        .def(nb::init<>())
        .def("open_dialog", &IGFD::FileDialog::OpenDialog,
             "key"_a, "title"_a, "filters"_a, "config"_a = IGFD::FileDialogConfig())
        .def("display", [](IGFD::FileDialog& self, const std::string& key, int flags,
                           std::tuple<float, float> min_size, std::tuple<float, float> max_size) {
                 return self.Display(key, flags,
                     ImVec2(std::get<0>(min_size), std::get<1>(min_size)),
                     ImVec2(std::get<0>(max_size), std::get<1>(max_size)));
             },
             "key"_a,
             "flags"_a = ImGuiWindowFlags_NoCollapse,
             "min_size"_a = std::make_tuple(0.0f, 0.0f),
             "max_size"_a = std::make_tuple(FLT_MAX, FLT_MAX))
        .def("close", &IGFD::FileDialog::Close)
        .def("is_ok", &IGFD::FileDialog::IsOk)
        .def("is_opened", nb::overload_cast<const std::string&>(&IGFD::FileDialog::IsOpened, nb::const_),
             "key"_a)
        .def("is_opened", nb::overload_cast<>(&IGFD::FileDialog::IsOpened, nb::const_))
        .def("was_opened_this_frame", nb::overload_cast<const std::string&>(&IGFD::FileDialog::WasOpenedThisFrame, nb::const_),
             "key"_a)
        .def("was_opened_this_frame", nb::overload_cast<>(&IGFD::FileDialog::WasOpenedThisFrame, nb::const_))
        .def("get_opened_key", &IGFD::FileDialog::GetOpenedKey)
        .def("get_file_path_name", [](IGFD::FileDialog& self, IGFD_ResultMode_ mode) {
                 return self.GetFilePathName(mode);
             },
             "mode"_a = IGFD_ResultMode_AddIfNoFileExt)
        .def("get_current_file_name", [](IGFD::FileDialog& self, IGFD_ResultMode_ mode) {
                 return self.GetCurrentFileName(mode);
             },
             "mode"_a = IGFD_ResultMode_AddIfNoFileExt)
        .def("get_current_path", &IGFD::FileDialog::GetCurrentPath)
        .def("get_current_filter", &IGFD::FileDialog::GetCurrentFilter)
        .def("get_selection", [](IGFD::FileDialog& self, IGFD_ResultMode_ mode) {
                 return self.GetSelection(mode);
             },
             "mode"_a = IGFD_ResultMode_KeepInputFile)
        .def("set_file_style", [](IGFD::FileDialog& self, IGFD_FileStyleFlags flags, const char* criteria,
                                  std::tuple<float, float, float, float> color, const std::string& icon, ImFont* font) {
                 ImVec4 c(std::get<0>(color), std::get<1>(color), std::get<2>(color), std::get<3>(color));
                 self.SetFileStyle(flags, criteria, c, icon, font);
             },
             "flags"_a, "criteria"_a, "color"_a, "icon"_a = "", "font"_a = nb::none())
        .def("clear_file_styles", &IGFD::FileDialog::ClearFilesStyle)
        .def("set_locales", &IGFD::FileDialog::SetLocales,
             "locale_category"_a, "locale_begin"_a, "locale_end"_a);
}
