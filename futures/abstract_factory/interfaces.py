from __future__ import annotations

from abc import ABC, abstractmethod


class ElementsFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass
