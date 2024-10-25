from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    lang: Lang
    scores: Scores
    registration: Registration
    update_data: Update_data
    name: Name
    first_name_input: First_name_input
    last_name_input: Last_name_input
    score: Score
    common: Common

    @staticmethod
    def menu_message(*, first_name, last_name) -> Literal["""&lt;b&gt;Main menu&lt;/b&gt;
Hello { $first_name }{ $last_name }!"""]: ...

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


class Scores:
    enter: ScoresEnter
    list: ScoresList


class ScoresEnter:
    @staticmethod
    def button() -> Literal["""Add scores ➕"""]: ...


class ScoresList:
    @staticmethod
    def button() -> Literal["""Show scores 📋"""]: ...


class Registration:
    @staticmethod
    def button() -> Literal["""Registration 👤"""]: ...


class Update_data:
    @staticmethod
    def button() -> Literal["""Change personal data ⚙️"""]: ...


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


class Score:
    show: ScoreShow
    enter: ScoreEnter
    name: ScoreName
    quantity: ScoreQuantity

    @staticmethod
    def done() -> Literal["""&lt;b&gt;Added&lt;/b&gt; ✅"""]: ...


class ScoreShow:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Your scores:&lt;/b&gt;"""]: ...


class ScoreEnter:
    @staticmethod
    def name() -> Literal["""&lt;b&gt;Enter the name of the item:&lt;/b&gt;"""]: ...

    @staticmethod
    def scores() -> Literal["""&lt;b&gt;Enter the number of points:&lt;/b&gt;
Click on the button to delete it."""]: ...


class ScoreName:
    err: ScoreNameErr


class ScoreNameErr:
    @staticmethod
    def message() -> Literal["""&lt;b&gt;Enter correct text&lt;/b&gt;"""]: ...


class ScoreQuantity:
    @staticmethod
    def err_message() -> Literal["""&lt;b&gt;Enter the correct number of points from 0 to 100&lt;/b&gt;"""]: ...


class Common:
    @staticmethod
    def text_error() -> Literal["""&lt;b&gt;Send a valid text message&lt;/b&gt;"""]: ...

