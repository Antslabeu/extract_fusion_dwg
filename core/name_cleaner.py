import re


GUID_PATTERN = re.compile(
    r"\.[0-9a-fA-F\-]{36}\.f2d$"
)


def clean_name(filename: str) -> str:

    name = filename

    if name.startswith("_"):
        name = name[1:]

    name = GUID_PATTERN.sub("", name)

    if name.endswith(".f2d"):
        name = name[:-4]

    return name.strip()