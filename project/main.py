import wx
import db

class MainFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent, title='Course Management System', size=(1000, 700))

        panel = wx.Panel(self)
        notebook = wx.Notebook(panel)

        self.add_course_panel = AddCoursePanel(notebook)
        self.manage_courses_panel = ManageCoursesPanel(notebook)
        self.filter_courses_panel = FilterCoursesPanel(notebook)

        notebook.AddPage(self.add_course_panel, 'Add Course')
        notebook.AddPage(self.manage_courses_panel, 'Manage Courses')
        notebook.AddPage(self.filter_courses_panel, 'Filter Courses')

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND | wx.ALL, 8)
        panel.SetSizer(sizer)

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.on_page_changed)

    def on_page_changed(self, event):
        self.manage_courses_panel.refresh_list()
        self.filter_courses_panel.refresh_filters()
        event.Skip()

class AddCoursePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = db

        fg = wx.FlexGridSizer(0, 2, 10, 10)
        fg.AddGrowableCol(1, 1)

        fg.Add(wx.StaticText(self, label='Course ID:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_course_id = wx.TextCtrl(self)
        fg.Add(self.txt_course_id, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Full Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_full_name = wx.TextCtrl(self)
        fg.Add(self.txt_full_name, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Short Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_short_name = wx.TextCtrl(self)
        fg.Add(self.txt_short_name, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Summary:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_summary = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        fg.Add(self.txt_summary, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Category ID:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_cat_id = wx.TextCtrl(self)
        fg.Add(self.txt_cat_id, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Category Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_cat_name = wx.TextCtrl(self)
        fg.Add(self.txt_cat_name, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Category Path:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_cat_path = wx.TextCtrl(self)
        fg.Add(self.txt_cat_path, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Category Path Names:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_cat_path_names = wx.TextCtrl(self)
        fg.Add(self.txt_cat_path_names, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Top Category:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_top_cat = wx.TextCtrl(self)
        fg.Add(self.txt_top_cat, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Level ID:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_level_id = wx.TextCtrl(self)
        fg.Add(self.txt_level_id, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Level Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_level_name = wx.TextCtrl(self)
        fg.Add(self.txt_level_name, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='CEFR:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_cefr = wx.TextCtrl(self)
        fg.Add(self.txt_cefr, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Series:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_series = wx.TextCtrl(self)
        fg.Add(self.txt_series, 1, wx.EXPAND)

        btn_add = wx.Button(self, label='Add Course')
        btn_add.Bind(wx.EVT_BUTTON, self.on_add)

        btn_clear = wx.Button(self, label='Clear')
        btn_clear.Bind(wx.EVT_BUTTON, self.on_clear)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(btn_add, 0, wx.RIGHT, 8)
        btn_sizer.Add(btn_clear, 0)

        outer = wx.BoxSizer(wx.VERTICAL)
        outer.Add(fg, 1, wx.ALL | wx.EXPAND, 12)
        outer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM, 12)

        self.SetSizer(outer)

    def on_add(self, evt):
        try:
            course_id = int(self.txt_course_id.GetValue())
            full_name = self.txt_full_name.GetValue()
            short_name = self.txt_short_name.GetValue()
            summary = self.txt_summary.GetValue()
            cat_id = int(self.txt_cat_id.GetValue())
            cat_name = self.txt_cat_name.GetValue()
            cat_path = self.txt_cat_path.GetValue()
            cat_path_names = self.txt_cat_path_names.GetValue()
            top_cat = self.txt_top_cat.GetValue()
            level_id = self.txt_level_id.GetValue()
            level_name = self.txt_level_name.GetValue()
            cefr = self.txt_cefr.GetValue()
            series = self.txt_series.GetValue()

            db.add_course(course_id, full_name, short_name, summary, cat_id, cat_name,
                         cat_path, cat_path_names, top_cat, level_id, level_name, cefr, series)
            wx.MessageBox('Course added successfully!', 'Success', wx.OK | wx.ICON_INFORMATION)
            self.on_clear(evt)
        except ValueError as e:
            wx.MessageBox(str(e), 'Error', wx.OK | wx.ICON_ERROR)
        except Exception as e:
            wx.MessageBox(f'Error: {str(e)}', 'Error', wx.OK | wx.ICON_ERROR)

    def on_clear(self, evt):
        self.txt_course_id.SetValue('')
        self.txt_full_name.SetValue('')
        self.txt_short_name.SetValue('')
        self.txt_summary.SetValue('')
        self.txt_cat_id.SetValue('')
        self.txt_cat_name.SetValue('')
        self.txt_cat_path.SetValue('')
        self.txt_cat_path_names.SetValue('')
        self.txt_top_cat.SetValue('')
        self.txt_level_id.SetValue('')
        self.txt_level_name.SetValue('')
        self.txt_cefr.SetValue('')
        self.txt_series.SetValue('')

class ManageCoursesPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = db

        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.list_ctrl.InsertColumn(0, 'ID', width=50)
        self.list_ctrl.InsertColumn(1, 'Full Name', width=200)
        self.list_ctrl.InsertColumn(2, 'Short Name', width=150)
        self.list_ctrl.InsertColumn(3, 'Level', width=100)
        self.list_ctrl.InsertColumn(4, 'CEFR', width=80)
        self.list_ctrl.InsertColumn(5, 'Series', width=100)

        btn_edit = wx.Button(self, label='Edit')
        btn_edit.Bind(wx.EVT_BUTTON, self.on_edit)

        btn_delete = wx.Button(self, label='Delete')
        btn_delete.Bind(wx.EVT_BUTTON, self.on_delete)

        btn_refresh = wx.Button(self, label='Refresh')
        btn_refresh.Bind(wx.EVT_BUTTON, self.on_refresh)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(btn_edit, 0, wx.RIGHT, 8)
        btn_sizer.Add(btn_delete, 0, wx.RIGHT, 8)
        btn_sizer.Add(btn_refresh, 0)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 8)
        sizer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM, 8)

        self.SetSizer(sizer)
        self.refresh_list()

    def refresh_list(self):
        self.list_ctrl.DeleteAllItems()
        courses = db.get_all_courses()
        for course in courses:
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), str(course['_id']))
            self.list_ctrl.SetItem(index, 1, course['name']['full'])
            self.list_ctrl.SetItem(index, 2, course['name']['short'])
            self.list_ctrl.SetItem(index, 3, course['level']['name'])
            self.list_ctrl.SetItem(index, 4, course['level']['CEFR'])
            self.list_ctrl.SetItem(index, 5, course['series'])

    def on_edit(self, evt):
        selected = self.list_ctrl.GetFirstSelected()
        if selected == -1:
            wx.MessageBox('Please select a course to edit.', 'Error', wx.OK | wx.ICON_ERROR)
            return
        course_id = int(self.list_ctrl.GetItemText(selected))
        course = db.get_course(course_id)
        if course:
            # Open edit dialog
            EditCourseDialog(self, course).ShowModal()
            self.refresh_list()

    def on_delete(self, evt):
        selected = self.list_ctrl.GetFirstSelected()
        if selected == -1:
            wx.MessageBox('Please select a course to delete.', 'Error', wx.OK | wx.ICON_ERROR)
            return
        course_id = int(self.list_ctrl.GetItemText(selected))
        if wx.MessageBox(f'Are you sure you want to delete course {course_id}?', 'Confirm Delete',
                        wx.YES_NO | wx.ICON_QUESTION) == wx.YES:
            db.delete_course(course_id)
            self.refresh_list()

    def on_refresh(self, evt):
        self.refresh_list()

class EditCourseDialog(wx.Dialog):
    def __init__(self, parent, course):
        super().__init__(parent, title='Edit Course', size=(600, 400))
        self.course = course

        fg = wx.FlexGridSizer(0, 2, 10, 10)
        fg.AddGrowableCol(1, 1)

        fg.Add(wx.StaticText(self, label='Full Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_full_name = wx.TextCtrl(self, value=course['name']['full'])
        fg.Add(self.txt_full_name, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Short Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_short_name = wx.TextCtrl(self, value=course['name']['short'])
        fg.Add(self.txt_short_name, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Summary:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_summary = wx.TextCtrl(self, value=course['summary'], style=wx.TE_MULTILINE)
        fg.Add(self.txt_summary, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Level Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_level_name = wx.TextCtrl(self, value=course['level']['name'])
        fg.Add(self.txt_level_name, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='CEFR:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_cefr = wx.TextCtrl(self, value=course['level']['CEFR'])
        fg.Add(self.txt_cefr, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Series:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_series = wx.TextCtrl(self, value=course['series'])
        fg.Add(self.txt_series, 1, wx.EXPAND)

        btn_update = wx.Button(self, label='Update')
        btn_update.Bind(wx.EVT_BUTTON, self.on_update)

        btn_cancel = wx.Button(self, label='Cancel')
        btn_cancel.Bind(wx.EVT_BUTTON, self.on_cancel)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(btn_update, 0, wx.RIGHT, 8)
        btn_sizer.Add(btn_cancel, 0)

        outer = wx.BoxSizer(wx.VERTICAL)
        outer.Add(fg, 1, wx.ALL | wx.EXPAND, 12)
        outer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM, 12)

        self.SetSizer(outer)

    def on_update(self, evt):
        updates = {
            "name.full": self.txt_full_name.GetValue(),
            "name.short": self.txt_short_name.GetValue(),
            "summary": self.txt_summary.GetValue(),
            "level.name": self.txt_level_name.GetValue(),
            "level.CEFR": self.txt_cefr.GetValue(),
            "series": self.txt_series.GetValue()
        }
        db.update_course(self.course['_id'], updates)
        wx.MessageBox('Course updated successfully!', 'Success', wx.OK | wx.ICON_INFORMATION)
        self.EndModal(wx.ID_OK)

    def on_cancel(self, evt):
        self.EndModal(wx.ID_CANCEL)

class FilterCoursesPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = db

        fg = wx.FlexGridSizer(0, 2, 10, 10)
        fg.AddGrowableCol(1, 1)

        fg.Add(wx.StaticText(self, label='Level Name:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.cmb_level = wx.ComboBox(self, style=wx.CB_READONLY)
        fg.Add(self.cmb_level, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='CEFR:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.cmb_cefr = wx.ComboBox(self, style=wx.CB_READONLY)
        fg.Add(self.cmb_cefr, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Series:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.cmb_series = wx.ComboBox(self, style=wx.CB_READONLY)
        fg.Add(self.cmb_series, 1, wx.EXPAND)

        fg.Add(wx.StaticText(self, label='Search Text:'), 0, wx.ALIGN_CENTER_VERTICAL)
        self.txt_search = wx.TextCtrl(self)
        fg.Add(self.txt_search, 1, wx.EXPAND)

        btn_filter = wx.Button(self, label='Filter')
        btn_filter.Bind(wx.EVT_BUTTON, self.on_filter)

        btn_search = wx.Button(self, label='Search')
        btn_search.Bind(wx.EVT_BUTTON, self.on_search)

        btn_clear = wx.Button(self, label='Clear')
        btn_clear.Bind(wx.EVT_BUTTON, self.on_clear)

        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(btn_filter, 0, wx.RIGHT, 8)
        btn_sizer.Add(btn_search, 0, wx.RIGHT, 8)
        btn_sizer.Add(btn_clear, 0)

        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, 'ID', width=50)
        self.list_ctrl.InsertColumn(1, 'Full Name', width=200)
        self.list_ctrl.InsertColumn(2, 'Short Name', width=150)
        self.list_ctrl.InsertColumn(3, 'Level', width=100)
        self.list_ctrl.InsertColumn(4, 'CEFR', width=80)
        self.list_ctrl.InsertColumn(5, 'Series', width=100)

        outer = wx.BoxSizer(wx.VERTICAL)
        outer.Add(fg, 0, wx.ALL | wx.EXPAND, 12)
        outer.Add(btn_sizer, 0, wx.ALIGN_RIGHT | wx.RIGHT | wx.BOTTOM, 8)
        outer.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 8)

        self.SetSizer(outer)
        self.refresh_filters()

    def refresh_filters(self):
        self.cmb_level.Clear()
        self.cmb_level.Append('')
        levels = db.get_distinct_values('level.name')
        for level in levels:
            self.cmb_level.Append(level)

        self.cmb_cefr.Clear()
        self.cmb_cefr.Append('')
        cefrs = db.get_distinct_values('level.CEFR')
        for cefr in cefrs:
            self.cmb_cefr.Append(cefr)

        self.cmb_series.Clear()
        self.cmb_series.Append('')
        series_list = db.get_distinct_values('series')
        for s in series_list:
            self.cmb_series.Append(s)

    def on_filter(self, evt):
        level = self.cmb_level.GetValue()
        level = level if level != '' else None

        cefr = self.cmb_cefr.GetValue()
        cefr = cefr if cefr != '' else None

        series = self.cmb_series.GetValue()
        series = series if series != '' else None

        courses = db.filter_courses(level_name=level, cefr=cefr, series=series)
        self.display_courses(courses)

    def on_search(self, evt):
        search_text = self.txt_search.GetValue()
        if search_text:
            courses = db.search_courses(search_text)
            self.display_courses(courses)

    def on_clear(self, evt):
        self.cmb_level.SetValue('')
        self.cmb_cefr.SetValue('')
        self.cmb_series.SetValue('')
        self.txt_search.SetValue('')
        self.list_ctrl.DeleteAllItems()

    def display_courses(self, courses):
        self.list_ctrl.DeleteAllItems()
        for course in courses:
            index = self.list_ctrl.InsertItem(self.list_ctrl.GetItemCount(), str(course['_id']))
            self.list_ctrl.SetItem(index, 1, course['name']['full'])
            self.list_ctrl.SetItem(index, 2, course['name']['short'])
            self.list_ctrl.SetItem(index, 3, course['level']['name'])
            self.list_ctrl.SetItem(index, 4, course['level']['CEFR'])
            self.list_ctrl.SetItem(index, 5, course['series'])

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()