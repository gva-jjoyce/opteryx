# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Helper routines for handling types between different dialects.
"""
from enum import Enum


class OPTERYX_TYPES(str, Enum):
    BOOLEAN = "BOOLEAN"
    NUMERIC = "NUMERIC"
    LIST = "LIST"
    VARCHAR = "VARCHAR"
    STRUCT = "STRUCT"
    TIMESTAMP = "TIMESTAMP"
    OTHER = "OTHER"


class TOKEN_TYPES(str, Enum):
    BOOLEAN = "BOOLEAN"
    NUMERIC = "NUMERIC"
    LIST = "LIST"
    VARCHAR = "VARCHAR"
    STRUCT = "STRUCT"
    TIMESTAMP = "TIMESTAMP"
    OTHER = "OTHER"

    IDENTIFIER = "IDENTIFIER"
    WILDCARD = "WILDCARD"
    QUERY_PLAN = "QUERY_PLAN"
    FUNCTION = "FUNCTION"


OPTERYX_TYPE_NAMES = {
    OPTERYX_TYPES.BOOLEAN: "BOOLEAN",
    OPTERYX_TYPES.NUMERIC: "NUMERIC",
    OPTERYX_TYPES.LIST: "LIST",
    OPTERYX_TYPES.VARCHAR: "VARCHAR",
    OPTERYX_TYPES.STRUCT: "STRUCT",
    OPTERYX_TYPES.TIMESTAMP: "TIMESTAMP",
    OPTERYX_TYPES.OTHER: "OTHER",
}


PYTHON_TYPES = {
    "bool": OPTERYX_TYPES.BOOLEAN,
    "datetime": OPTERYX_TYPES.TIMESTAMP,
    "date": OPTERYX_TYPES.TIMESTAMP,
    "dict": OPTERYX_TYPES.STRUCT,
    "int": OPTERYX_TYPES.NUMERIC,
    "float": OPTERYX_TYPES.NUMERIC,
    "float64": OPTERYX_TYPES.NUMERIC,
    "Decimal": OPTERYX_TYPES.NUMERIC,
    "str": OPTERYX_TYPES.VARCHAR,
    "tuple": OPTERYX_TYPES.LIST,
    "list": OPTERYX_TYPES.LIST,
    "set": OPTERYX_TYPES.LIST,
}

PARQUET_TYPES = {
    "bool": OPTERYX_TYPES.BOOLEAN,
    "timestamp[ms]": OPTERYX_TYPES.TIMESTAMP,
    "timestamp[s]": OPTERYX_TYPES.TIMESTAMP,
    "dict": OPTERYX_TYPES.STRUCT,
    "int64": OPTERYX_TYPES.NUMERIC,
    "float64": OPTERYX_TYPES.NUMERIC,
    "double": OPTERYX_TYPES.NUMERIC,
    "string": OPTERYX_TYPES.VARCHAR,
    "tuple": OPTERYX_TYPES.LIST,
    "array": OPTERYX_TYPES.LIST,
    "object": OPTERYX_TYPES.VARCHAR,
}
