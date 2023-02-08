from typing import TYPE_CHECKING, Any, Generic, Mapping, TypeAlias, TypeVar
from django.db import models

from typing_extensions import Annotated, final

T = TypeVar("T", covariant=True, bound=Mapping[str, Any])

_Annotations = TypeVar("_Annotations", covariant=True, bound=Mapping[str, Any])


class Annotations(Generic[_Annotations]):
    """Use as `Annotations[MyTypedDict]`"""

    pass
