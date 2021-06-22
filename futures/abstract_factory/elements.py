from futures.abstract_factory.interfaces import Button, Checkbox, ElementsFactory


class WindowsButton(Button):
    def click(self):
        print('Windows button click')


class LinuxButton(Button):
    def click(self):
        print('Linux button click')


class DarwinButton(Button):
    def click(self):
        print('MacOS button click')


class WindowsCheckbox(Checkbox):
    def check(self):
        print('Windows check checkbox')


class LinuxCheckbox(Checkbox):
    def check(self):
        print('Linux check checkbox')


class DarwinCheckbox(Checkbox):
    def check(self):
        print('MacOS check checkbox')


class WindowsElementFactory(ElementsFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class LinuxElementFactory(ElementsFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()


class DarwinElementFactory(ElementsFactory):
    def create_button(self) -> Button:
        return DarwinButton()

    def create_checkbox(self) -> Checkbox:
        return DarwinCheckbox()
