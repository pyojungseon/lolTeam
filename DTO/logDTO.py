import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class logDTO:
    id : str = ""
    content : str = ""
    tag : str = ""
