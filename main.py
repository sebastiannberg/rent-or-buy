import numpy as np

from buy import Buy
from rent import Rent

RENT_CONFIG = {

}

BUY_CONFIG = {
    "antall_år": 1,
    "prisantydning": 2000000,
    "fellesgjeld": 160000,
    "omkostninger": 200000,
    "formuesverdi": 520000,
    "felleskostnader": 7600,
    "egenkapital": 300000,
    "eff_rente_boliglån": 0.052,
    "nedbetalingstid": 25,
    "verdistigning": 0.02,
    "inflasjonsrente": 0.02,
    "roi": 40,
    "by": "trondheim",
    "strøm": 600,
    "parkering": 400,
    "internett_og_tv": 900,
    "flyttekostnader": 2000,
    "møbler": 25000,
    "vedlikeholdskostnader": 2000,
    "eksisterende_formue": 0
}

buy = Buy(**BUY_CONFIG)
