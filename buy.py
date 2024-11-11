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
        self.eiendomsskatt_sats = {"oslo": 0.0028, "trondheim": 0.00265}
        self.eiendomsskatt_bunnfradrag = {"oslo": 4700000, "trondheim": 550000}
        self.formuesskatt_bunnfradrag = 1700000

    def kalkuler_årlig_eiendomsskatt(self):
        # 1. Beregn grunnlaget for eiendomsskatten (70 % av prisantydning)
        eiendomsskattegrunnlag = self.prisantydning * 0.7

        # 2. Trekk fra bunnfradrag for valgt by
        bunnfradrag = self.eiendomsskatt_bunnfradrag[self.by.lower()]
        skattepliktig_grunnlag = max(eiendomsskattegrunnlag - bunnfradrag, 0)

        # 3. Beregn eiendomsskatt ved å multiplisere med satsen for valgt by
        sats = self.eiendomsskatt_sats[self.by.lower()]
        årlig_eiendomsskatt = skattepliktig_grunnlag * sats

        return årlig_eiendomsskatt

    def kalkuler_årlig_formuesskatt(self, eksisterende_formue=0):
        # Beregn nettoformue inkludert eventuell annen eksisterende formue
        boligformue = max(self.formuesverdi - self.fellesgjeld, 0)
        total_nettoformue = boligformue + eksisterende_formue

        # Trekk fra bunnfradrag
        skattepliktig_formue = max(total_nettoformue - self.formuesskatt_bunnfradrag, 0)

        # Kommunal formuesskatt
        kommunal_sats = 0.007
        kommunal_formuesskatt = skattepliktig_formue * kommunal_sats

        # Statlig formuesskatt
        statlig_formuesskatt = 0
        if skattepliktig_formue > 20000000:
            statlig_formuesskatt += (skattepliktig_formue - 20000000) * 0.004
            skattepliktig_formue = 20000000
        statlig_formuesskatt += skattepliktig_formue * 0.003

        # Total formuesskatt
        årlig_formuesskatt = kommunal_formuesskatt + statlig_formuesskatt

        return årlig_formuesskatt
