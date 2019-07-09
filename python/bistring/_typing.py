# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT license.

from typing import Callable, Match, Pattern, Tuple, Union


Bounds = Tuple[int, int]

Range = Union[range, slice, Bounds]

Regex = Union[str, Pattern]

Replacement = Union[str, Callable[[Match], str]]

String = Union[str, "bistr"]
