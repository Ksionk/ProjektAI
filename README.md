===PROJEKT=== 

Numer grupy: 10 
Nazwa projektu: Analiza czynników sukcesu finansowego w branży filmowej
Opis: Projekt analityczny badający fundamenty branży filmowej pod kątem korelacji nakładów finansowych (budżetu) i finalnego przychodu rynkowego. Analiza ma na celu określenie, czy sukces komercyjny jest bezpośrednią pochodną zainwestowanego kapitału.

===GRUPA=== 

Lab grupa, ID, Nazwisko, Imie 

P2. Drugi etap projektu, 71903, Barej, Jakub 

P2. Drugi etap projektu, 73001, Skuza, Szymon 

P2. Drugi etap projektu, 78417 Oskar Mitek


===WKLAD=== 

ID, Nazwisko, Imie: Krótki opis wkładu każdego studenta do grupowego projektu na tym etapie. 
71903, Barej, Jakub: Kierownik inżynier projektu. Odpowiedzialny za sformułowanie celów badania, nadzór nad analizą korelacji Pearsona oraz opracowanie końcowych wniosków dotyczących zjawiska Blockbusterów.
73001, Skuza, Szymon: Młodszy asystent. Odpowiedzialny za proces czyszczenia danych, w tym filtrację rekordów zerowych (budżet/przychód 0 USD) oraz przygotowanie danych do normalizacji statystycznej.
78417 Oskar Mitek: Dokumentalista projektu. Odpowiedzialny za opracowanie dokumentacji technicznej Etapu 2 oraz przygotowanie i sformatowanie pliku README zgodnie z wymaganiami.


===PYTANIA BADAWCZE=== 

1. W jakim stopniu wysokość budżetu determinuje finalny przychód filmu?
2. Czy produkcje o najwyższych budżetach charakteryzują się najwyższym wskaźnikiem zwrotu z inwestycji?
3. Czy zależność między wydatkami a wpływami jest liniowa, czy istnieją progi budżetowe, powyżej których ryzyko finansowe drastycznie rośnie?

===ZRODLA DANYCH===  

Nazwa zrodla: Kaggle  
Nazwa danych: TMDB 5000 Movie Dataset 
Dataset URL: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

===ZMIENNE=== 

budget (budżet), revenue (przychód)

===CECHY=== 

Współczynnik korelacji Pearsona, Rentowność (ROI), Zmienność wyników w segmentach budżetowych

===ANALIZA=== 

1. Obliczenie korelacji Pearsona (wynik 0.73) między budżetem a przychodem.
2. Analiza zjawiska Blockbusterów – badanie skrajnie wysokich wartości przychodowych.
3. Wykres rozrzutu z linią regresji ilustrujący stabilność trendu finansowego.

===SRODOWISKO=== 

Python version: Python 3.13 
Main libraries: torch==2.9.1, torchvision==0.24.1, nltk==3.9.1, numpy==2.0.2 

===ZAWARTOSC===  

|--- READ.md
|--- Raport Etap 2.pdf 
|--- .gitignore  
|--- tmdb_5000_movies.csv
|--- analiza.py
