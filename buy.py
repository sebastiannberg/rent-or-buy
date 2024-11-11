from typing import Dict, List

class Buy:
    """
    Representerer en boligkjøp-beregning med eiendomsskatt og formuesskatt.

    Denne klassen lar deg beregne årlige kostnader som eiendomsskatt og formuesskatt basert på 
    boligens pris, gjeld og annen eksisterende formue.
    """

    def __init__(self, antall_år: int, prisantydning: float, fellesgjeld: float, omkostninger: float, 
                 formuesverdi: float, felleskostnader: float, egenkapital: float, eff_rente_boliglån: float, 
                 nedbetalingstid: int, verdistigning: float, inflasjonsrente: float, roi: float, by: str, 
                 strøm: float, parkering: float, internett_og_tv: float, flyttekostnader: float, 
                 møbler: float, vedlikeholdskostnader: float, eksisterende_formue: float) -> None:
        """
        Initialiserer et Buy-objekt med nødvendige verdier.

        Args:
            antall_år (int): Antall år for beregningen.
            prisantydning (float): Boligens prisantydning.
            fellesgjeld (float): Boligens fellesgjeld.
            omkostninger (float): Omkostninger ved kjøp.
            formuesverdi (float): Formuesverdi av boligen.
            felleskostnader (float): Månedlige felleskostnader.
            egenkapital (float): Egenkapital som investeres.
            eff_rente_boliglån (float): Effektiv rente på boliglånet.
            nedbetalingstid (int): Lånets nedbetalingstid i år.
            verdistigning (float): Forventet årlig verdistigning i prosent.
            inflasjonsrente (float): Forventet årlig inflasjon i prosent.
            roi (float): Forventet årlig avkastning på investeringer.
            by (str): Byen hvor boligen er, påvirker eiendomsskatten.
            strøm (float): Årlige strømutgifter.
            parkering (float): Årlige parkeringsutgifter.
            internett_og_tv (float): Årlige utgifter til internett og TV.
            flyttekostnader (float): Kostnader ved flytting.
            møbler (float): Kostnader for møbler.
            vedlikeholdskostnader (float): Årlige vedlikeholdskostnader.
            eksisterende_formue (float, optional): Annen eksisterende formue. Default er 0.
        """
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
        self.by = by.lower()
        self.strøm = strøm
        self.parkering = parkering
        self.internett_og_tv = internett_og_tv
        self.flyttekostnader = flyttekostnader
        self.møbler = møbler
        self.vedlikeholdskostnader = vedlikeholdskostnader
        self.eiendomsskatt_sats: Dict[str, float] = {"oslo": 0.0028, "trondheim": 0.00265}
        self.eiendomsskatt_bunnfradrag: Dict[str, float] = {"oslo": 4700000, "trondheim": 550000}
        self.eksisterende_formue = eksisterende_formue
        self.formuesskatt_kommunal_sats = 0.007
        self.formuesskatt_statlig_sats_lav = 0.003
        self.formuesskatt_statlig_sats_høy = 0.004
        self.formuesskatt_bunnfradrag = 1700000
    
    def prisantydning_over_tid(self) -> List[float]:
        """
        Beregner prisantydningen for hvert år i eierskapsperioden, med årlig verdistigning.

        Returns:
            List[float]: Liste over prisantydning for hvert år i eierskapsperioden.
        """
        årlig_prisantydning = [self.prisantydning]
        for år in range(1, self.antall_år):
            ny_verdi = årlig_prisantydning[-1] * (1 + self.verdistingning / 100)
            årlig_prisantydning.append(ny_verdi)
        return årlig_prisantydning

    def årlig_eiendomsskatt(self) -> float:
        """
        Beregner årlig eiendomsskatt for boligen basert på prisantydning, bunnfradrag, og kommunens eiendomsskattesats.

        Returns:
            float: Årlig eiendomsskatt i NOK.
        """
        # Beregn eiendomsskattegrunnlag som 70 % av prisantydning
        eiendomsskattegrunnlag = self.prisantydning * 0.7
        
        # Finn bunnfradraget for valgt by
        bunnfradrag = self.eiendomsskatt_bunnfradrag.get(self.by, 0)
        
        # Skattepliktig grunnlag etter bunnfradrag
        skattepliktig_grunnlag = max(eiendomsskattegrunnlag - bunnfradrag, 0)
        
        # Få eiendomsskattesatsen for valgt by
        sats = self.eiendomsskatt_sats.get(self.by, 0)
        
        # Beregn årlig eiendomsskatt
        årlig_eiendomsskatt = skattepliktig_grunnlag * sats
        return årlig_eiendomsskatt

    def årlig_formuesskatt(self) -> float:
        """
        Beregner årlig formuesskatt basert på boligens netto formuesverdi, annen eksisterende formue,
        bunnfradrag, og kommunale og statlige formuesskattesatser.

        Returns:
            float: Årlig formuesskatt i NOK.
        """
        # Beregn netto boligformue (formuesverdi minus fellesgjeld)
        boligformue = max(self.formuesverdi - self.fellesgjeld, 0)
        
        # Total nettoformue inkludert annen formue
        total_nettoformue = boligformue + self.eksisterende_formue
        
        # Beregn skattepliktig formue etter bunnfradrag
        skattepliktig_formue = max(total_nettoformue - self.formuesskatt_bunnfradrag, 0)
        
        # Beregn kommunal formuesskatt
        kommunal_formuesskatt = skattepliktig_formue * self.formuesskatt_kommunal_sats
        
        # Beregn statlig formuesskatt med høy og lav sats
        statlig_formuesskatt = 0
        if skattepliktig_formue > 20000000:
            statlig_formuesskatt += (skattepliktig_formue - 20000000) * self.formuesskatt_statlig_sats_høy
            skattepliktig_formue = 20000000
        statlig_formuesskatt += skattepliktig_formue * self.formuesskatt_statlig_sats_lav
        
        # Total årlig formuesskatt
        årlig_formuesskatt = kommunal_formuesskatt + statlig_formuesskatt
        return årlig_formuesskatt

    def årlig_lånekostnad(self) -> float:
        """
        Beregner den årlige kostnaden av lånet, inkludert både rente og avdrag.

        Returnerer:
            float: Årlig lånekostnad i NOK.
        """
        # Beregn årlig betaling basert på annuitetslån
        if self.nedbetalingstid > 0:
            # Antall årlige betalinger
            antall_betalinger = self.nedbetalingstid * 12
            # Månedlig rente
            månedlig_rente = (1 + self.eff_rente_boliglån) ** (1/12) - 1
            # Lånebeløp (prisantydning - egenkapital)
            lånebeløp = max(self.prisantydning - self.egenkapital, 0)

            # Annuitetsformel for månedlig betaling
            månedlig_betaling = lånebeløp * (månedlig_rente * (1 + månedlig_rente) ** antall_betalinger) / \
                                ((1 + månedlig_rente) ** antall_betalinger - 1)
            
            # Årlig lånekostnad (månedlig betaling * 12)
            årlig_lånekostnad = månedlig_betaling * 12
            return årlig_lånekostnad
        return 0.0

    def årlig_driftkostnad(self) -> float:
        """
        Beregner de totale årlige driftskostnadene for boligen, inkludert felleskostnader,
        strøm, parkering, internett og TV, vedlikeholdskostnader, og eventuelle andre utgifter.

        Returns:
            float: Totale årlige driftskostnader i NOK.
        """
        # Beregn totale felleskostnader per år
        årlige_felleskostnader = self.felleskostnader * 12
        
        # Summerer alle årlige driftskostnader
        årlig_driftkostnad = (
            årlige_felleskostnader +    # Årlige felleskostnader
            self.strøm +                # Årlige strømutgifter
            self.parkering +            # Årlige parkeringsutgifter
            self.internett_og_tv +      # Årlige utgifter til internett og TV
            self.vedlikeholdskostnader  # Årlige vedlikeholdskostnader
        )
        
        return årlig_driftkostnad

    def samlet_årlig_kostnad(self):
        pass

    def total_kostnad_over_tid(self):
        pass

    def investering_av_egenkapital(self):
        pass

    def nettogevinst_ved_salg(self):
        pass
