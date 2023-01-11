from board import Board
from board_list import BoardList
from user import User
from flet import Page


class DataStore:

    def add_board(self, model) -> None:
        raise NotImplementedError

    def get_board(self, id) -> Board:
        raise NotImplementedError

    def get_boards(self) -> list[Board]:
        raise NotImplementedError

    def update_board(self, model, update):
        raise NotImplementedError

    def remove_board(self, board) -> None:
        raise NotImplementedError

    def add_user(self, model) -> None:
        raise NotImplementedError

    def get_users(self) -> list[User]:
        raise NotImplementedError

    def get_user(self, id) -> User:
        raise NotImplementedError

    def remove_user(self, id) -> None:
        raise NotImplementedError

    def add_list(self, board, model) -> None:
        raise NotImplementedError

    def get_lists(self) -> list[BoardList]:
        raise NotImplementedError

    def get_list(self, id) -> BoardList:
        raise NotImplementedError

    def get_lists_by_board(self, board) -> list[BoardList]:
        raise NotImplementedError

    def remove_list(self, board, id) -> None:
        raise NotImplementedError