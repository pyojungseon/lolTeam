import dataclasses as dc

@dc.dataclass(unsafe_hash=True)
class tierDTO:
    id: str = ""
    tier: str = ""
    top: str = ""
    jug: str = ""
    mid: str = ""
    adc: str = ""
    sup: str = ""
