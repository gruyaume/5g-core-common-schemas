# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from pydantic import BaseModel


class TwapId(BaseModel):
    ssId: str
    bssId: str = None
    civicAddress: bytes = None
