"""Data models"""
from . import database


class Chats(database.Model):
    """Data model for chats info."""

    __tablename__ = "chats"
    chat_hash = database.Column(
        database.String(16),
        primary_key=True,
        index=True
    )
    chat_id = database.Column(
        database.Integer
    )
    description = database.Column(
        database.Text,
        nullable=True
    )

    def __repr__(self):
        return f"<Chat {self.chat_hash} for {self.chat_id} peer>"


# class Timetable(database.Model):
#     """Data model for timetables."""
#
#     __tablename__ = "timetable"
#
#
# class SystemCommands(database.Model):
#     """Data model for system commands."""
#
#     __tablename__ = "system-commands"
#
#
# class UserCommands(database.Model):
#     """Data model for user commands."""
#
#     __tablename__ = "user-commands"
