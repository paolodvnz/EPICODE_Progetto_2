import numpy as np
import random

class SetValueError(Exception):
    """Richiamato dalla classe Paziente quando vengono create istanze con dati non validi"""
    pass

class Paziente:
    """Classe che rappresenta i pazienti"""

    def __init__(self, nome: str, cognome: str, codice_fiscale: str, eta: int, peso: float, analisi_effettuate):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale.upper()
        self.eta = eta
        self.peso = float(peso)
        self.analisi_effettuate = analisi_effettuate.lower()
        self.risultati_analisi = None
    
    # getter eta
    @property
    def eta(self):
        return self._eta
    
    # setter eta: controlla se è un int maggiore di zero
    @eta.setter
    def eta(self, valore):
        if not isinstance(valore, int) or valore < 0:
            raise SetValueError("Valore età non valido: deve essere maggiore di zero!")
        self._eta = valore

    # getter peso
    @property
    def peso(self):
        return self._peso
    
    # setter peso: controlla se è maggiore di zero
    @peso.setter
    def peso(self, valore):
        if valore <= 0:
            raise SetValueError("Valore peso non valido: deve essere maggiore di zero!")
        self._peso = float(valore)

    # getter codice fiscale
    @property
    def codice_fiscale(self):
        return self._codice_fiscale

    # setter codice fiscale: controlla se è una stringa composta da 16 caratteri
    @codice_fiscale.setter
    def codice_fiscale(self, valore):
        if not isinstance(valore, str) or len(valore) != 16:
            raise SetValueError("Codice fiscale non valido!")
        self._codice_fiscale = valore 

    @property
    def scheda_personale(self) -> str:
        """Fornisce informazioni paziente"""
        return f"Nome: {self.nome} {self.cognome},\nCodice fiscale: {self.codice_fiscale},\nEtà: {self.eta},\nPeso: {self.peso}"
    
    def statistiche_analisi(self):
        """Calcola semplici statistiche dei risultati delle analisi del paziente"""
        
        if self.risultati_analisi.size == 0:
            return f"Nessun analisi eseguita!"

        media = self.risultati_analisi.mean()
        massimo = self.risultati_analisi.max()
        minimo = self.risultati_analisi.min()
        dev_std = self.risultati_analisi.std()

        print(f"{'>'*10} Statistiche analisi di {self.analisi_effettuate} per {self.nome} {self.cognome} {'<'*10}\n")
        print(f"Media risultati: {media:.2f}")
        print(f"Risultato massimo: {massimo:.2f}")
        print(f"Risultato minimo: {minimo:.2f}")
        print(f"Deviazione Standard: {dev_std:.2f}")

        return media

class Medico:
    """Classe che rappresenta i medici"""
    def __init__(self, nome: str, cognome: str, specializzazione: str):
        self.nome = nome
        self.cognome = cognome 
        self.specializzazione = specializzazione

    def __str__(self):
        """Fornisce informazioni medico"""
        return f"Dr/Dr.ssa {self.nome} {self.cognome} - {self.specializzazione}"

    def visita_paziente(self, paziente: object):
        """Fornisce informazioni sulla visita"""
        print(f"Il/La Dr./Dr.ssa {self.nome} {self.cognome} ({self.specializzazione})"
              f" sta visitando il/la paziente {paziente.nome} {paziente.cognome}")

class Analisi:
    """Classe che rappresenta il risultato di un'analisi"""
    def __init__(self, tipo_analisi: str, risultato: float):
        self.tipo_analisi = tipo_analisi.lower()
        self.risultato = risultato

    def valuta(self) -> str:
        """Valuta l'analisi"""
        if self.tipo_analisi == "glicemia":
            if self.risultato < 100:
                stato = "Nella norma"
            elif 100 <= self.risultato <= 125: 
                stato = "Alterato - pre-diabete"
            else:
                stato = "Diabete"  
            return f"Analisi {self.tipo_analisi}: {self.risultato:.2f} --> {stato}\n"
        
        elif self.tipo_analisi == "colesterolo":
            if self.risultato < 200:
                stato = "Nella norma"
            else:
                stato = "Fuori norma"
            return f"Analisi {self.tipo_analisi}: {self.risultato:.2f} --> {stato}\n"

        elif self.tipo_analisi == "emocromo":
            if 13.5 <= self.risultato <= 17.5:
                stato = "Nella norma"
            else:
                stato = "Fuori norma"    
            return f"Analisi {self.tipo_analisi}: {self.risultato:.2f} --> {stato}\n"
        
        else:
            return f"Non eseguiamo analisi di {self.tipo_analisi}"


if __name__=="__main__":

    # definisco variabili per rappresentare i pazienti
    nomi_pazienti = ["Margherita", "Enrico", "Maria", "Galileo", "Ettore"]
    cognomi_pazienti = ["Hack", "Fermi", "Montessori", "Galilei", "Majorana"]
    pesi = [60, 75, 55, 73, 71]
    eta = [91, 53, 81, 77, 31]
    analisi = ["Emocromo", "Glicemia", "Colesterolo"]
    codici_fiscali = ["HCKMGH22H52D612Z",
                      "FRMERC01P29H501G",
                      "MNTSMR70M71C617B",
                      "GLLGLG64B15G702J",
                      "MJRTTR06M05C351R"
                      ]
    
    # definisco variabili per rappresentare i dottori
    nomi_dottori = ["Rita", "Andrea", "Renato"]
    cognomi_dottori = ["Levi-Montalcini", "Vesalio", "Dulbecco"] 
    specializzazioni = ["Neurobiologia", "Anatomia", "Virologia"]

    # definisco un dizionario per i risultati delle analisi:
    # chiavi --> tipo di analisi
    # valori --> lista con 2 array casuali (il primo nella norma, il secondo fuori norma)
    risultati = {
        "emocromo" : [np.random.normal(15.5, 3, 10), np.random.normal(18.5, 3, 10)],
        "glicemia" : [np.random.normal(85, 20, 10), np.random.normal(130, 20, 10)],
        "colesterolo" : [np.random.normal(150, 50, 10), np.random.normal(250, 50, 10)]
    }

    print(f"\n{'='*20} INIZIALIZZO LABORATORIO ANALISI {'='*20}")

    # creo oggetti Paziente e ne stampo la scheda personale
    pazienti = []
    
    for i in range(len(nomi_pazienti)):
        print(f"\n{'>'*10} Inizializzo {i+1}° paziente...")
        analisi_tmp = random.choice(analisi)
        paziente = Paziente(nomi_pazienti[i], cognomi_pazienti[i], codici_fiscali[i], eta[i], pesi[i], analisi_tmp)
        pazienti.append(paziente)
        print(f"{'>'*10} ...e ne stampo la scheda:\n")
        print(paziente.scheda_personale)

    # creo oggetti Medico e ne stampo le info
    medici = []
    
    for i in range(len(nomi_dottori)):
        print(f"\n{'>'*10} Inizializzo {i+1}° medico...")
        medico = Medico(nomi_dottori[i], cognomi_dottori[i], specializzazioni[i])
        medici.append(medico)
        print(f"{'>'*10} ...e ne stampo le info:\n")
        print(medico)

    # visite pazienti
    print(f"\n{'='*20} VISITE PAZIENTI {'='*20}\n")
    medici[0].visita_paziente(pazienti[0])
    medici[1].visita_paziente(pazienti[1])
    medici[2].visita_paziente(pazienti[2])
    medici[1].visita_paziente(pazienti[3])
    medici[0].visita_paziente(pazienti[4])

    # statistiche analisi e valutazione
    print(f"\n{'='*20} STATISTICHE ANALISI E VALUTAZIONE {'='*20}\n")

    # per ogni paziente....
    for p in pazienti:
        
        # scelgo un array di risultati 
        p.risultati_analisi = np.array(random.choice(risultati[p.analisi_effettuate]))
        
        # calcolo statistiche e ne salvo la media
        media = p.statistiche_analisi()
        
        # valuto il risultato medio ottenuto
        print(f"\n{'>'*10} valutazione...\n")
        analisi = Analisi(p.analisi_effettuate, media)
        print(analisi.valuta())




