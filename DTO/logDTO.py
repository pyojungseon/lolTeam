import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class logDTO:
    tag : str = ""
    content : str = ""
