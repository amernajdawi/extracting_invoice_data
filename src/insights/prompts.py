EXTRACTION_PROMPT = """Search the electric car charging bill listed at the bottom as "Car charging pdf content:" for the fields or synonyms of them listed below.
If the field names differ but are similar, map them accordingly and convert to the specified units.
If a field is missing and you believe it is public information, search for it; otherwise, write 'unbekannt'.
Adapt to the bill's language but give the results in German.
Capitalize only the first letter of individual words like names or countries.
Predict the salutation from the first name if not stated.
Look for names near addresses if necessary.
Create the 'ID' field with its subfields for each transaction, but write 'ID' only if there is a transaction: Its not a transaction if its a flat rate.
Make the field 'File list' with all its subfields for each file in the prompt. Use only strings and numbers as datatypes and arrays.

Fields to search:
- 'FileList'
  - 'Filename'
  - 'Rechnungsdaten'
    - 'Rechnungsnummer'
    - 'MobilityServiceProvider' (also known as MSP, EMP, or Aussteller)
      - 'Firmenname' (with 'GmbH' if applicable)
      - 'AdresseMSP' (Adresse vom Mobility Service Provider)
        - 'Straße'
        - 'Hausnummer'
        - 'PLZ' (postal code, string)
        - 'Ort'
        - 'Land'
        - 'EMail'
        - 'Tel' (telephone)
        - 'Web' (website of Mobility Service Provider)
    - 'Kunde'
      - 'Kundennummer'
      - 'Kundendaten'
        - 'Anrede' (Herr, Frau, etc.)
        - 'Titel' (Dr., Mag., etc., 'Keiner' if none)
        - 'Vorname'
        - 'Nachname'
        - 'Firmenname'
        - 'UIDNummerKunde' (e.g. starting with AT or DE)
        - 'AdresseKunde'
          - 'Straße'
          - 'Hausnummer'
          - 'PLZ' (postal code, string)
          - 'Ort'
          - 'Land'
    - 'Rechnungssumme'
      - 'BetragExclVAT' (excl. VAT in pdf, as float)
      - 'VATSatz' (in percentage and as float)
  - 'Rechnungspositionen'
    - 'Transaktionen' (possibly multiple per bill, make an ID with its subfields for each charging transaction)
      - 'ID' (x-th transaction, starting from 1)
      - 'Ladedatum' (if available: format: YYYY-MM-DD)
      - 'Ladeuhrzeit' (if available: format: hh:mm:ss)
      - 'LadepunktID' (starts with 'AT*' for Austria, different for each country  bzw. EVSE-ID)
      - 'AdresseLadepunkt'
        - 'Straße'
        - 'Hausnummer'
        - 'PLZ' (postal code, string)
        - 'Ort'
        - 'Land' (search from 'Ort' if missing)
      - 'Tarifname' (letters followed by number, e.g., DC150, AC22 or P&R/P&W)
      - 'Abrechnungseinheit' ('kWh' or 'Zeit' (time), if not clear or dependent on the 'Tarif'/rate: write 'unbekannt')
      - 'LademengeInKWh' (as float if given, otherwise 'unbekannt')
      - 'LademengeInZeit' (format: mm:ss if given, otherwise 'unbekannt')
      - 'PreisProkWh' (excl. VAT)
      - 'PreisProMinute' (calculate into price per minute if its e.g. hour and (excl. VAT))
      - 'Währung' (EUR, Dollar, etc.)
      - 'KostenProTransaktion' (as float if given, otherwise 'unbekannt' and excl. VAT)
      - 'BlockiergebührExclVAT' (as float if given, otherwise 'unbekannt')
      - 'TransaktionskostenProLadevorgang' (as float if given, otherwise 'unbekannt')
- Sammelrechnung (true/false, if order over more than three days)
- 'Grundgebühr' (fixed price for e.g. monthly fee)
    - 'Betrag' (as float if given, otherwise 'unbekannt')
    - 'Zeitraum' ('Jahr' (year) or 'Monat' (month))
  - 'Ausstellungsgebühr' (one-time activation fee, only if fixed price)
    - 'Betrag' (as float if given, otherwise 'unbekannt')
    - 'Zeitraum' ('Jahr' (year) or 'Monat' (month))

Car charging pdf content:
{text}

Take a deep breath before you start working and work precisely.

Provide the result in .json format."""
