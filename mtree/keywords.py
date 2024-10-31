from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum, auto
from pathlib import Path
from typing import Literal, Optional, Union

DeviceFormat = Literal[
    "native",
    "386bsd",
    "4bsd",
    "bsdos",
    "freebsd",
    "hpux",
    "isc",
    "linux",
    "netbsd",
    "osf1",
    "sco",
    "solaris",
    "sunos",
    "svr3",
    "svr4",
    "ultrix",
]


@dataclass
class DeviceFields:
    format: DeviceFormat
    major: int
    minor: int
    subunit: Optional[int] = None


Device = Union[DeviceFields, int]


class Type(StrEnum):
    block = auto()
    char = auto()
    dir = auto()
    fifo = auto()
    file = auto()
    link = auto()
    socket = auto()


@dataclass
class Keywords:
    """Represents the keywords for an entry."""

    cksum: Optional[str] = None
    device: Optional[Device] = None
    contents: Optional[Path] = None
    flags: Optional[str] = None  # todo
    gid: Optional[int] = None
    gname: Optional[str] = None
    ignore: Optional[bool] = None  # todo
    inode: Optional[int] = None
    link: Optional[Path] = None
    md5: Optional[str] = None
    mode: Optional[int] = None
    nlink: Optional[int] = None
    nochange: Optional[bool] = None  # todo check how all bools should be
    optional: Optional[bool] = None
    resdevice: Optional[Device] = None
    ripemd160digest: Optional[str] = None
    sha1: Optional[str] = None
    sha384: Optional[str] = None
    sha512: Optional[str] = None
    size: Optional[int] = None
    time: Optional[datetime] = None
    type: Optional[Type] = None
    uid: Optional[int] = None
    uname: Optional[str] = None
