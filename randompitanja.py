import random

pitanja_inzenjering3 : list = [
"Preispitivanje, poboljšanje i/ili reinženjering je složen i veoma stručan posao koji zahteva dobro poznavanje:",
"Koraci preispitivanja, poboljšanja, reinženjeringa procesa:",
"Simptomi problematičnog procesa",
"Tim za proces treba da čine",
"Šta je cilj snimka stanja procesa?",
"Kako dokumentovati proces?",
"Kako prikupiti podatke o procesu?",
"Prikazati i objasniti PDSA ciklus.",
"Prikazati Model za poboljšanje.",
"Primer PDSA ciklusa.",
"Predlog novog stanja treba organizovati tako da omogući:",
"U koraku projektovanja novog stanja procesa, proces se specifira na način koji omogućava:",
"Rezultat projektovanja novog stanja procesa su dokumenta koja opisuju proces, i to:",
"4 osnovna principa poboljšanja procesa – pravila, pitanja, primeri",
"Navesti i objasniti princip za redizajn procesa koji se odnosi na strukturiranje izvođenja procesa",
"Navesti i objasniti princip za redizajn procesa koji se odnosi na uređivanje tokova informacija",
"Navesti i objasniti princip za redizajn procesa koji se odnosi na projektovanje proizvoda/procesa",
"Šta je reinženjering procesa i navesti elemente reinženjeringa?",
"Šta predstavlja kontinualno poboljšanje procesa?",
"PDCA metodologija",
"Kontinualno poboljšanje procesa se zasniva na 4 principa",
"ADDIE model – opis i slika",
"ADDIE model – primer",
"Koristi kaizen metode",
"Šta je lin pristup?",
"Šta obezbeđuje lin pristup?",
"Navesti i objasniti lin principe.",
"Navesti tipove rasipanja.",
"Šta je Agile metodologija i koja je razlika u odnosu na metod vodopada?",
"Šta je Scrum i koje su karakteristične ključne uloge, ceremonije i artefakti?"]
pitanja_uis : list = [
    "Šta je informacioni sistem?", #1
    "Koji je osnovni zadatak informacionog sistema?",
    "Koji je cilj IS-a?",
    "Objasniti pojmove: podatak, informacija i znanje. Navesti primer za svaki od njih.",
    "Navesti elemente IS-a.",
    "Šta je to model nekog sistema, koja je namena modela?",
    "Koji su ciljevi modelovanja?",
    "Koje su dve kategorizacije modela?",
    "Šta opisuje logički, a šta fizički model?",
    "Na šta se fokusiraju statički, a na šta dinamički aspekti modela?",
    "Kakvo ponašanje imaju realni sistemi? Objasni.",
    "Navedi modele razvoja IS.", #2
    "Šta je model životnog ciklusa i iz čega se sastoji?",
    "Procesi definisanja strategije?",
    "Analiza postojećeg stanja u modelu životnog ciklusa. Definisanje zahteva iz dokumenata.",
    "Analiza postojećeg stanja u modelu životnog ciklusa. Definisanje zahteva intervjuom.",
    "Analiza postojećeg stanja u modelu životnog ciklusa. Dokumentovanje snimka stanja.",
    "Projektovanje u modelu životnog ciklusa.",
    "Aplikativno modeliranje u modelu životnog ciklusa.",
    "Uvođenje u modelu životnog ciklusa.",
    "Faktori rizika koje treba razmotriti prilikom vrednovanja pristupa po modelu životnog ciklusa?",
    "Prednosti pristupa po modelu životnog ciklusa?",
    "Nedostaci modela životnog ciklusa?",
    "Objasniti iterativno-inkrementalni model.",
    "Karakteristike iterativno-inkrementalnog pristupa.",
    "Koje su prednosti iterativno-inkrementalnog razvoja?",
    "Koji su rizici iterativno-inkrementalnog razvoja?",
    "Opisati evolutivni model.",
    "Karakteristike evolutivnog prototipskog razvoja IS?",
    "Elementi evolutivnog prototipskog razvoja IS?",
    "Prednosti i rizici evolutivnog pristupa?",
    "Opisati spiralni model.",
    "Faze u spiralnom modelu?",
    "Karakteristike agilne metode razvoja IS.",
    "Definisane vrednosti u okviru Agilnih metoda?",
    "Metodologije agilnog razvoja IS?",
    "Iz kojih slojeva se sastoji troslojna arhitektura?", #3
    "Karakteristike troslojne arhitekture",
    "Osobine aplikacionog servera?",
    "Dati primer za tanki i debeli klijent.",
    "Podtipovi paralelne arhitekture?",
    "Karakteristike distribuiranih baza podataka?",
    "Prednosti DSUBP?",
    "Kratko definisati SOA.",
    "Prednosti SOA arhitekture?",
    "Iz kojih faza se sastoji aplikativno modeliranje?",
    "Pogled ka korisniku u aplikativnom modeliranju.",
    "Šta se može postići uspešnim korišćenjem pravilno odabranog CASE alata? (prednosti)",
    "CASE arhitektura?",
    "Vertikalna podela CASE alata?",
    "Horizontalna podela CASE alata?",
    "Podela CASE alata prema broju korisnika?",
    "Navesti 4 CASE alata.",
    "Šta je standard?", #4
    "Koje vrste standarda razlikujemo?",
    "Navesti osnovne principe na kojima je izgrađena standardizacija.",
    "Navesti ciljeve standardizacije u IT.",
    "Koja su očekivanja korisnika po pitanju kvaliteta softvera?",
    "Navesti tvorce IT standarda.",
    "Koji su zadaci JTC1/SC7?",
    "Komisija I1/07 ISS u Srbiji, opisati.",
    "Navesti 4 standarda za oblast SE i dati kratak opis.",
    "Šta obuhvata ISO 27000?",
    "Karakteristike ISO 12207?",
    "Koje grupe procesa obuhvata ISO 12207?",
    "ISO 20000",
    "Navesti procese isporuke IT usluga.",
    "Navesti procese podrške IT usluzi.",
    "Promene u organizaciji isporučioca IT usluge?",
    "Navesti 4 prednosti primene IT standarda.",#5
    "Koji su najvažniji faktori uspešnog uvođenja IS-a?",
    "Osnovni procesi uvođenja?",
    "Osnovne funkcije IS?",
    "Šta je usko grlo? Pomodu koje tehnologije se rešava problem uskog grla?",
    "Koje sve ADC tehnologije postoje?",
    "Navesti magnetne i ekektromagnetne ADC tehnologije.",
    "Navesti biometričke ADC tehnologije.",
    "Navesti optičke ADC tehnologije.",
    "Prednosti primene ADC tehnologija?",
    "Objasni tipove popravki.",#6
    "Objasni tipove popoljšanja.",
    "Navedi vrste IS u preduzedu.",
    "Objasni transakcioni informacioni sistem.",
    "Vrste izveštaja iz transakcionog IS.",
    "Koje poslovne funkcije podržavaju IS funkcionalnih oblasti?",
    "Karakteristike ERP, dati primer ERP-a.",
    "Osnovni zadatak ERP?",
    "Modularnost ERP?",
    "Osnovna ideja CRM?",
    "Navesti 4 CRM tačaka dodira sa kupcima.",
    "Primena CRM u funkcionalnim jedinicama?",
    "Koji su razlozi za uvodjenje CRM?",
    "Navesti 4 CRM servisa za kupce.",
    "Šta su supply chains (lanci snabdevanja). Koje procese uključuju i koji je njihov cilj?",
    "Navesti i objasniti tokove supply chain-a.",
    "Koji su segmenti supply chain-a. Ukratko objasni.",
    "Zbog čega nastaju problemi Supply Chanins. Navedi ih.",
    "Koji su problem Globalnog IS?",
    "Šta predstavlja efekat biča, kako ga minimizirati?",
    "Objasni pojmove intranet i ekstranet.",
    "Navesti tradicionalne osnovne zadatke funkcije za razvoj IS.",
    "Navesti 4 nova zadatka funkcije IS.",
    "Iz čega se sastoji organizaciona forma funkcije razvoja informacionog sistema u preduzedu?",
    "Karakteristike transakcionog informacionog sistema – OLTP.",#7
    "Navedi 4 zahteva savremenog poslovanja.",
    "Navedi 4 razloga zbog kojih je danas teško dobiti kvalitetne izveštaje.",
    "Kako definišemo OLAP?",
    "Navedi razlike između OLTP i OLAP.",
    "Šta predstavlja DSS (sistem za podršku u odlučivanju)?",
    "Koji su elementi DSS-a?",
    "Navedi i ukratko objasni tri nivoa DSS tehnologije.",
    "Kako se razvija DSS?",
    "Objasni pojam poslovne inteligencije (BI).",
    "Šta BI omogudava menadžerima?",
    "Navedi karakteristike opšteg modela BI.",
    "Koje su ključne tehnologije BI?",
    "Objasniti pojam data mining.",
    "Šta je GDSS?",
    "Navedi i objasni tri nivoa GDSS tehnologije.",
    "Definisati i navesti karakteristike izvršnog IS (EIS).",
    "Nivoi geografskog IS-a.",
    "Navedi oblasti primene GIS-a i daj primer.",
    "Objasniti pojmove: Implicitno znanje, Eskplicitno znanje.", #8
    "Šta predstavlja proces formalizacije?",
    "Navedi elemente ciklusa upravljanja znanjem.",
    "Koja je osnovna pretpostavka inteligentnih sistema?",
    "Temelji inteligentnog ponašanja su?",
    "Definiši ES (ekspertni sistem).",
    "Koje su karakteristike ekspertnog sistema?",
    "Objasniti kako funkcioniše ekspertni sistem.",
    "Navedi elemente sistema produkcije.",
    "Navedi vrste formalizma.",
    "Navedi 4 razlike između konvencionalnih I ekspertnih sistema.",
    "Prednosti primene ekspertnih sistema u odnosu na čoveka.",
    "Nedostaci primene ekspertnih sistema u odnosu na čoveka.",
    "Navedi 4 oblasti primene ekspertnih sistema.",
    "Navedi pravce razvoja ES.",
    "Karakteristike sistema isporuke znanja.",
    "Navedi i ukratko objasni vrste savremenih organizacija, u zavisnosti da li koriste neki segment e-poslovanja.",#9
    "Virtuelne organizacije. Definicija i vrste virtuelne organizacije.",
    "Vrste telework-a (Kakva može biti lokacija radnog mesta)?",
    "Oblici virtuelne kancelarije?",
    "Navedi 4 karakteristike virtuelnih timova.",
    "Navedi 4 prednosti virtuelnih organizacija.",
    "Navedi 4 standarda na kojima je zasnovana elektronska trgovina.",
    "Dva oblika marketinga u elektronskim uslugama.",
    "Koji su glavni mehanizmi e-trgovine?",
    "Navedi karakteristike B2B relacije.",
    "Navedi karakteristike B2C relacije.",
    "Navedi karakteristike C2C relacije.",
    "Navedi karakteristike C2B2C relacije.",
    "Navedi karakteristike B2B2C relacije.",
    "Koje su prednosti korišdenja E-trgovine?",
    "Navedi 4 vrste elektronskog pladanja.",
    "Navedi tehnološka ograničenja e-trgovine.",
    "Netehnološka ograničenja e-trgovine.",
    "Karakteristike elektronskog poslovanja u javnoj upravi?",
    "Karakteristike G2B?",
    "Karakteristike G2C?",
    "Karakteristike G2G?",
    "Karakteristike G2E?",
    "Prednosti e-učenja.",
    "Nedostaci e-učenja.",
    "Koje su opasnosti po IS prema uzroku nastanka?",#10
    "Klasifikacija namernih pretnji.",
    "Navedi komponente integralne zaštite IS.",
    "Koje su mere bezbednosti pri nabavci, instalaciji, korišćenju i održavanju softvera?",
    "Koje su mere bezbednosti pri, nabavci, instalaciji, korišćenju i održavanju hardvera?",
    "Navedi 4 mere bezbednosti u fazi eksploatacije IS.",
    "Strategija zaštite na internetu?",
    "Navedi i ukratko objasni vrste kontrole.",
    "Navedi tipove kontrolora.",
    "Opisati plan oporavka.",
    "Koji su elementi plana oporavka?",
    "Navedi 4 elementa za test plana oporavka.",
    "Trendovi u razvoju IT sigurnosti.",
    "Na čemu se baziraju etički sistemi vrednosti?", #11
    "Vrste etike?",
    "Šta predstavlja kodeks etičkog i profesionalnog ponašanja?",
    "Navedi etičke aspekte.",
    "Navedi individualna prava.",
    "Pojam privatnosti. Koja dva principa su zaštidena zakonom u vedini zemalja?",
    "Šta je GDPR?",
    "Koji su osnovni aspekti zaštite privatnosti. Ukratko objasni.",
    "Šta je intelektualna svojina? Kako je zaštititi?",
    "Objasniti kako funkcioniše licenciranje softvera.",
    "Navedi 4 pravila računarske etike.",
    "Kako IT utiče na rad pojedinca?",
    "Navedi 4 potencijalno pozitivna uticaja IT.",
    "Navedi 4 potencijalno negativna uticaja IT.",
    "Šta je digitalno raslojavanje? (digitalni jaz). Kako prevazidi digitalni jaz?",
    "Pojam virtuelnog društva i njegove vrste.",
    "Navedi 4 mere uspeha IT projekta.", #12
    "Navedi i objasni bazične strategije razvoja IS.",
    "Navedi strategije nabavke poslovnog softvera.",
    "Kupovina gotovih softverskih rešenja, prednosti i nedostaci.",
    "Iznajmljivanje softvera i korišćenje softvera kao usluge, prednosti i nedostaci.",
    "Korišćenje softvera otvorenog koda, prednosti i nedostaci.",
    "Prednosti i nedostaci razvoja sopstvenog softvera.",
    "Navedi trendove u tehnologiji.",
    "Karakteristike Cloud Computing-a.",
    "Javne usluge ,,Cloud computing-a”?",
    "Usluge Cloud computing-a?",
    "Navedi nedostatke koncepta “cloud computing-a”.",
    "Elementi Green IT.",
    "Objasni pojam virtualizacije.",
    "Šta je Pervasive Computing?",
    "Karakteristike Web 2.0. Dati primer.",
    "Navedi trendove i pokretače savremenog poslovanja od uticaja na razvoj IS.",
    "Šta predstavlja kontinualno unapređenje softvera CPI, a šta Total Quality Management TQM?",
    "Koji su ključni standardi iz oblasti kvaliteta vezani za IS?",
    "Navedi prednosti rada na daljinu.",#DODATNA
    "Navedi nedostatke rada na daljinu.",
    "Šta predstavlja Asocijacija izdavača softvera (SPA)?",
    "Šta je data mining?",
    "Šta predstavlja upravljačka kabina menadžmenta (management cockpit)?",
    "Objasniti model ograđivanja opt-out.",
    "Objasniti model potvrđivanja (pristanka) opt-in.",
    "Čemu služe kontrolne table (DASHBOARDS)?",
    "Šta je BIG DATA?",
    "Objasniti pojam Internet of things (IoT).",
    "Prednosti učenja na daljinu?",
    "Nedostaci učenja na daljinu?"
]
pitanja : list =  ["1.pitanje","2.pitanje","3.pitanje"]

#1)samo print
#print(random.choice(pitanja))

#2)messagebox
import tkinter
import tkinter.messagebox

#tkinter.messagebox.showinfo("Pintanje", random.choice(pitanja))

#3)app
def obrada(prozor : tkinter.Tk, labela : tkinter.Label, dugme : tkinter.Button, i : list, pitanja_len : int) -> None:
  if len(pitanja) > 0:
      random_pitanje : str = random.choice(pitanja)
      pitanja.remove(random_pitanje)
      labela.config(text = random_pitanje)
      i[0] += 1
      prozor.title(f"random pintanje ({i[0]}/{pitanja_len})")
  else:
      prozor.title(f"random pintanje - by @mihajloslav")
      labela.config(text = "NEMA VIŠE PINTANJA!!!", pady= 20)
      dugme.destroy()

def random_pitanje() -> None:
  i : list = [0]
  pitanja_len : int = len(pitanja)

  prozor : tkinter.Tk = tkinter.Tk()
  prozor.title(f"random pintanje ({i[0]}/{pitanja_len})")
  prozor.geometry("1000x100")

  labela : tkinter.Label = tkinter.Label(prozor, text = "", font = ("Arial", 14))
  labela.pack(pady = 20)

  dugme : tkinter.Button = tkinter.Button(prozor, text = "Random pintanje", command = lambda : obrada(prozor, labela, dugme, i, pitanja_len))
  dugme.pack()
  obrada(prozor, labela, dugme, i, pitanja_len)
  prozor.mainloop()

random_pitanje()

