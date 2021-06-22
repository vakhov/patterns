import platform
from typing import Optional

from futures.abstract_factory.elements import (
    DarwinElementFactory, WindowsElementFactory, LinuxElementFactory
)
from futures.abstract_factory.interfaces import ElementsFactory

MACOS = 'darwin'
WINDOWS = 'windows'
LINUX = 'linux'


class GUI:

    def __init__(self, elements_factory: ElementsFactory) -> None:
        self.el_factory = elements_factory

    def click(self):
        btn = self.el_factory.create_button()
        btn.click()

    def check(self):
        btn = self.el_factory.create_checkbox()
        btn.check()


if __name__ == '__main__':
    cur_os = platform.system().lower()

    elements_factory: Optional[ElementsFactory] = None
    if cur_os == MACOS:
        elements_factory = DarwinElementFactory()
    elif cur_os == WINDOWS:
        elements_factory = WindowsElementFactory()
    elif cur_os == LINUX:
        elements_factory = LinuxElementFactory()
    else:
        print('unknown platform: {cur_os}'.format(cur_os=cur_os))
        exit(1)

    gui = GUI(elements_factory=elements_factory)
    gui.click()
    gui.check()
