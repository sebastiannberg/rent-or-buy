import numpy as np

class Rent:
    
    def __init__(self, antall_år, månedsleie, årlig_økning_månedsleie, depositum, inflasjonsrate, strøm, parkering, internett_og_tv, roi, flyttekostnader, møbler):
        self.antall_år = antall_år
        self.månedsleie = månedsleie
        self.årlig_økning_månedsleie = årlig_økning_månedsleie
        self.depositum = depositum
        self.inflasjonsrate = inflasjonsrate
        self.strøm = strøm
        self.parkering = parkering
        self.internett_og_tv = internett_og_tv
        self.roi = roi
        self.flyttekostnader = flyttekostnader
        self.møbler = møbler
        
    def total_rent_cost(self):
        total_cost = self.depositum + self.flyttekostnader + self.møbler
        årlig_leie = self.månedsleie * 12
        for år in range(self.antall_år):
            total_cost += årlig_leie + self.strøm + self.parkering + self.internett_og_tv
            årlig_leie *= (1 + self.årlig_økning_månedsleie)
        return total_cost

class Buy:
    
    def __init__(self, antall_år, prisantydning, fellesgjeld, omkostninger, formuesverdi, felleskostnader, egenkapital, eff_rente_boliglån, nedbetalingstid, verdistigning, inflasjonsrente, roi, by, strøm, parkering, internett_og_tv, flyttekostnader, møbler, vedlikeholdskostnader):
        self.antall_år = antall_år
        self.prisantydning = prisantydning
        self.fellesgjeld = fellesgjeld
        self.omkostninger = omkostninger
        self.formuesverdi = formuesverdi
        self.felleskostnader = felleskostnader
        self.egenkapital = egenkapital
        self.eff_rente_boliglån = eff_rente_boliglån
        self.nedbetalingstid = nedbetalingstid
        self.verdistingning = verdistigning
        self.inflasjonsrente = inflasjonsrente
        self.roi = roi
        self.by = by
        self.strøm = strøm
        self.parkering = parkering
        self.internett_og_tv = internett_og_tv
        self.flyttekostnader = flyttekostnader
        self.møbler = møbler
        self.vedlikeholdskostnader = vedlikeholdskostnader
        self.eiendomsskatt_sats = {"oslo": 0.0028, "trondheim": 0.0026}
        self.eiendomsskatt_bunnfradrag = {"oslo": 4700000, "trondheim": 550000}
        self.formuesskatt_bunnfradrag = 1700000
