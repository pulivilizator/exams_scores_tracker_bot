from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    lang: Lang
    registration: Registration
    name: Name
    first_name_input: First_name_input
    last_name_input: Last_name_input

    @staticmethod
    def menu_message() -> Literal["""Main menu"""]: ...

    @staticmethod
    def previous_button() -> Literal["""Back"""]: ...

    @staticmethod
    def next_button() -> Literal["""Next"""]: ...

    @staticmethod
    def skip_button() -> Literal["""Skip"""]: ...


class Lang:
    @staticmethod
    def russian() -> Literal["""Русский 🇷🇺"""]: ...

    @staticmethod
    def english() -> Literal["""English 🇬🇧"""]: ...


class Registration:
    @staticmethod
    def button() -> Literal["""Registration"""]: ...


class Name:
    err: NameErr


class NameErr:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Enter valid text&lt;/b&gt;
The first or last name must not be shorter than 2 characters and can only contain text characters and the ‘-’ sign."""]: ...


class First_name_input:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Enter first name:&lt;/b&gt;"""]: ...


class Last_name_input:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Enter last name:&lt;/b&gt;"""]: ...

