# Sistema di Gestione Laboratorio Analisi

Un sistema di gestione per laboratori di analisi mediche che simula la creazione di pazienti, medici, visite ed elaborazione dei risultati delle analisi cliniche.

## Descrizione

Il progetto implementa un sistema object-oriented per la gestione di un laboratorio di analisi mediche. Il sistema permette di:

- Registrare pazienti con i loro dati anagrafici
- Gestire un team di medici specializzati
- Simulare visite mediche
- Generare e analizzare risultati di analisi cliniche (emocromo, glicemia, colesterolo)
- Calcolare statistiche sui risultati
- Valutare automaticamente i risultati secondo parametri clinici standard

## Struttura del Progetto

### Classi Principali

#### `Paziente`
Rappresenta un paziente del laboratorio con le seguenti caratteristiche:
- **Attributi**: nome, cognome, codice fiscale, età, peso, tipo di analisi effettuate
- **Validazione dati**: controlli automatici su età (>0), peso (>0) e codice fiscale (16 caratteri)
- **Metodi principali**:
  - `scheda_personale`: restituisce le informazioni del paziente
  - `statistiche_analisi()`: calcola media, massimo, minimo e deviazione standard dei risultati

#### `Medico`
Rappresenta un medico del laboratorio:
- **Attributi**: nome, cognome, specializzazione
- **Metodi principali**:
  - `visita_paziente()`: simula una visita medica

#### `Analisi`
Gestisce i risultati delle analisi cliniche:
- **Attributi**: tipo di analisi, risultato numerico
- **Metodi principali**:
  - `valuta()`: valuta il risultato secondo parametri clinici standard

#### `SetValueError`
Eccezione personalizzata per la gestione di errori di validazione dati.


## Main

Il programma esegue automaticamente le seguenti operazioni:

1. **Inizializzazione del laboratorio**: 
2. **Stampa delle schede personali** 
3. **Simulazione di visite mediche**
4. **Generazione e analisi dei risultati** 
5. **Valutazione automatica** 

