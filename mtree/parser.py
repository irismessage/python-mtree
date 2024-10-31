from pathlib import Path

from mtree.entry import Entry
from mtree.keywords import Keywords, Device, DeviceFields


def parse_device(device: str) -> Device:
    try:
        return int(device)
    except ValueError:
        pass

    fields = device.split(",")
    format_ = fields[0]
    major = int(fields[1])
    minor = int(fields[2])
    try:
        subunit = int(fields[3])
    except IndexError:
        subunit = None
    return DeviceFields(format_, major, minor, subunit)


# could do this whole thing as like a pyparsing grammar instead. might try that?
def parse_keyword(keyword: str, keywords: Keywords):
    """Parse the keywords in the form keyword=value and apply it to the keywords object."""

    key, _, value = keyword.partition("=")

    match key:
        case "cksum":
            keywords.cksum = value
        case "device":
            keywords.device = parse_device(value)
        case "contents":
            keywords.contents = Path(value)
        case "flags":
            keywords.flags = value
        case "gid":
            keywords.gid = int(value)
        case "gname":
            keywords.gname = value
        case "ignore":
            keywords.ignore = True
        case "inode":
            keywords.inode = int(value)
        case "link":
            keywords.link = Path(value)
        case "md5" | "md5digest":
            keywords.md5 = value
        case "ok":
            pass  # todo keep working on ths


def parse(file_contents: str, starting_directory: Path):
    current_directory = starting_directory
    global_keywords = Keywords()
    entries: list[Entry] = []

    for line in file_contents.splitlines():
        if line.startswith("#"):
            # comment (just like this one!)
            continue

        words = line.split()
        first_word = words[0]

        if first_word.startswith("/"):
            # special command
            command = first_word.removeprefix("/")
