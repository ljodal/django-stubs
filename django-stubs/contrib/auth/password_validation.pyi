from collections.abc import Mapping, Sequence
from pathlib import Path, PosixPath
from typing import Any, Protocol

from django.contrib.auth import get_user_model
from typing_extensions import TypeAlias

_UserModel = get_user_model()

class PasswordValidator(Protocol):
    def validate(self, __password: str, __user: _UserModel | None = ...) -> None: ...
    def get_help_text(self) -> str: ...

def get_default_password_validators() -> list[PasswordValidator]: ...
def get_password_validators(validator_config: Sequence[Mapping[str, Any]]) -> list[PasswordValidator]: ...
def validate_password(
    password: str, user: _UserModel | None = ..., password_validators: Sequence[PasswordValidator] | None = ...
) -> None: ...
def password_changed(
    password: str, user: _UserModel | None = ..., password_validators: Sequence[PasswordValidator] | None = ...
) -> None: ...
def password_validators_help_texts(password_validators: Sequence[PasswordValidator] | None = ...) -> list[str]: ...

password_validators_help_text_html: Any

class MinimumLengthValidator:
    min_length: int
    def __init__(self, min_length: int = ...) -> None: ...
    def validate(self, password: str, user: _UserModel | None = ...) -> None: ...
    def get_help_text(self) -> str: ...

class UserAttributeSimilarityValidator:
    DEFAULT_USER_ATTRIBUTES: Sequence[str]
    user_attributes: Sequence[str]
    max_similarity: float
    def __init__(self, user_attributes: Sequence[str] = ..., max_similarity: float = ...) -> None: ...
    def validate(self, password: str, user: _UserModel | None = ...) -> None: ...
    def get_help_text(self) -> str: ...

class CommonPasswordValidator:
    DEFAULT_PASSWORD_LIST_PATH: Path
    passwords: set[str]
    def __init__(self, password_list_path: Path | PosixPath | str = ...) -> None: ...
    def validate(self, password: str, user: _UserModel | None = ...) -> None: ...
    def get_help_text(self) -> str: ...

class NumericPasswordValidator:
    def validate(self, password: str, user: _UserModel | None = ...) -> None: ...
    def get_help_text(self) -> str: ...
