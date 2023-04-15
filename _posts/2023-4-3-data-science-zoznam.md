---
layout: post
title: 'Študijný checklist pre začínajúcu dátovú vedkyňu'
scripts: [toggle]
lang: sk
ref: data-science-checklist
thumbnail: "images/data-science-checklist/datascience.webp"
tags:
 - "všeličo"
 - "programovanie"
excerpt: "Nedávno som stretol niekoho, kto by sa chcel naučiť dátovú vedu - presne ako som sa ju kedysi naučil ja!
Tento článok je pre teba, milá budúca dátová vedkyňa.

Keď sa obzriem späť na svoju kariéru, nikdy nebol problém nájsť dostatok kvalitných a voľne dostupných učebných materiálov na internete. Mal som presne opačný problém - každý článok, video, tutoriál, kniha alebo nástroj sa tvárili ako tá najdôležitejšia vec na svete, bez ktorej sa v žiadnom prípade nezaobídem.
To najťažšie bolo správne rozpoznať priority.

Takže aby som ti s tým pomohol, tu je zoznam konceptov, ktoré by začínajúci dátový vedec mal poznať. Nie je to samozrejme jediná možná vzdelávacia cesta ani jediná správna definícia dátovej vedy (koniec koncov, je to veľmi vágne definovaná pracovná pozícia), ale je to dobrý kompromis medzi stručnosťou a úplnosťou. Ber tento zoznam ako odrazový mostík, ako niečo čo ťa povedie skôr, ako sa budeš vedieť viesť sama.
"
---

<img alt="Tom (z Toma & Jerryho) náhodne miešajúci kuchynské prísady označené ako dáta, Pytorch, Numpy a pod." src="{{site.baseurl}}/images/data-science-checklist/datascience.webp" />

Nedávno som stretol niekoho, kto by sa chcel naučiť dátovú vedu - presne ako som sa ju kedysi naučil ja!
Tento článok je pre teba, milá budúca dátová vedkyňa.

Keď sa obzriem späť na svoju kariéru, nikdy nebol problém nájsť dostatok kvalitných a voľne dostupných učebných materiálov na internete. Mal som presne opačný problém - každý článok, video, tutoriál, kniha alebo nástroj sa tvárili ako tá najdôležitejšia vec na svete, bez ktorej sa v žiadnom prípade nezaobídem.
To najťažšie bolo správne rozpoznať priority.

Takže aby som ti s tým pomohol, tu je zoznam konceptov, ktoré by začínajúci dátový vedec mal poznať. Nie je to samozrejme jediná možná vzdelávacia cesta ani jediná správna definícia dátovej vedy (koniec koncov, je to veľmi vágne definovaná pracovná pozícia), ale je to dobrý kompromis medzi stručnosťou a úplnosťou. Ber tento zoznam ako odrazový mostík, ako niečo čo ťa povedie skôr, ako sa budeš vedieť viesť sama.


### Legenda

- <span style="color:red">Červená</span> - Toto sa nauč detailne, bude to tvoj každodenný chlebíček.
- <span style="color:green">Zelená</span> - Toto sa nauč dosť dobre na to, aby si si prinajhoršom len musela dohľadať nejaké podrobnosti.
- <span style="color:blue">Modrá</span> - Zapamätaj si, že toto existuje a čo to je. Detaily si doštuduješ neskôr podľa potreby.

## Základné nástroje

 - <span style="color:red">Visual Studio Code</span> - Odporúčam tento editor kódu (presnejšie IDE - Integrated Development Environment - slúži na písanie a editovanie kódu, jeho spúšťanie a iné užitočné veci). IDE bývajú plné užitočných funkcií, ale nemusíš sa trápiť tým, že sa ich hneď všetky naučíš používať, nauč sa najprv tie základné. Existujú aj iné dobré voľby než len VS Code, napr. Spyder. Pár ich vyskúšaj a  jeden si vyber. 

- <span style="color:red">Jupyter Notebook</span> - Toto je zároveň formát kódu a IDE užitočné na interaktívne skúmanie a vizualizáciu dát. Je plne kompatibilný s VS Code a s Google Collab.

 - <span style="color:red">Základná práca s linuxovým terminálom (alebo príkazovým riadkom, ak používaš Windows)</span> - Nauč sa ako zmeniť adresár v ktorom sa nachádzaš, vypísať obsah adresára, spustiť príkaz, a zobraziť nápovedu (help) pre daný príkaz.

 - <span style="color:green">Git</span>
 - <span style="color:green">GitHub</span> - alebo nejaká iná služba na hosting Gitu, ako napr. Gitlab alebo Gitea 

## Programovanie

- <span style="color:red">Python</span>
- <span style="color:green">SQL</span>

## Formáty dát

- <span style="color:red">CSV</span> - Základný formát pre tabuľkové dáta.
- <span style="color:green">JSON</span> -  Veľmi rozšírený formát v ktorom sa dajú uložiť aj netabuľkové dáta. Výborný nástroj na skúmanie JSONových súborov je jq.
  
## Pythonové balíky a nástroje

- <span style="color:red">Pandas</span> - Všestranný nástroj s vysokou úrovňu abstrakcie na prácu s tabuľkami. Taký pythonový ekvivalent Excelu. Nauč sa načítať dáta, transformovať ich a vybrať z nich len nejakú časť. Zbytok sa naučiš popri učení ostatných vecí.
- <span style="color:red">Matplotlib</span> - Najrozšírenejší balík na kreslenie graafov. Pod kapotou ho používa a Pandas, Seaborn a Scikit-learn pre ich grafy. Nauč sa ako nakresliť základné grafy, formátovanie (nastaviť nadpis, premenovať osi, zmeniť interval) a ako uložiť obrázok do súboru.
- <span style="color:blue">Seaborn</span> - Veľmi užitočné rozšírenie Matplotlibu, je dobrý nápad zvyknúť si používať ho miesto Matplotlibu aj na základné grafy.
- <span style="color:green">Numpy</span> - Násobenie matíc a iná lineárna algebra, ľubovoľná práca s poliami (tzn. tabuľkami) čísel.
- <span style="color:red">Scikit-learn</span> - Obrovská zbierka modelov a nástrojov na ich evaluáciu, od základných až po pokročilé. Nauč sa aké evaluačné nástroje sú k dispozícií, ako vyzerá interface modelov a ber zoznam dostupných modelov ako inšpiráciu pre ďalšie štúdium.
- <span style="color:blue">Scipy</span> - Pokročilá matematika, štatistika a optimalizácia.
- <span style="color:blue">Pytorch a/alebo Tensorflow</span> - Pythonové balíky pre prácu s neurónovými sieťami.
- <span style="color:green">Pip</span> - Manažér balíkov, budeš ho potrebovať už na nainštalovanie všetkých týchto balíkov.
- <span style="color:blue">Conda</span> - Manažér balíkov a virtuálnych prostredí.

## Matematika

- <span style="color:red">Lineárna algebra:</span>
  - <span style="color:red">Vektory</span>
  - <span style="color:red">Matice a ich násobenie</span>
  - <span style="color:green">Geometrická interpretácia</span>
- <span style="color:red">Štatistika:</span>
  - <span style="color:red">Pravdepodobnosť</span>
  - <span style="color:red">Pravdepodobnostné rozdelenie (distribúcia)</span> a rozdiel medzi pravdepodobnosťou a hustotou pravdepodobnosti
    - <span style="color:red">Normálna (tzn. gausovská) distribúcia</span>
    - <span style="color:red">Kategorická distribúcia</span>
    - <span style="color:green">Binomiálna ditribúcia</span>
    - <span style="color:green">Poissonova ditribúcia</span>
  - <span style="color:green"> Korelácia</span> a <span style="color:green">korelácia ranku (rank correlation)</span>
  - <span style="color:green">Interval spoľahlivosti</span>
  - <span style="color:blue">Koncept štatistického testu</span>
  - <span style="color:blue">P-hodnota</span>
  - <span style="color:blue"> P-hackovanie</span> (ako niečo čomu sa chceš vyhnúť)
- <span style="color:green">Podmienená pravdepodobnosť</span>
- Kognitívne skreslenia a štatistické chyby:
  - <span style="color:green">Simpsonov paradox</span>
  - <span style="color:green">Výberové skreslenie (selection bias)</span>
  - <span style="color:green">Skreslenie preživších (survivorship bias)</span>
  - <span style="color:red">Mätúca premenná (confounding variable) a náhodné korelácie</span>
- <span style="color:blue">Neintuitívne vlastnosti mnohorozmerných priestorov</span>
- <span style="color:blue">Základy Bayesovskej štatistiky:</span>
  - Bayesovo pravidlo
  - Apriori a aposteriori pravdepodobnostná distribúcia
  - Rozdiel medzi "maximum likelihood estimate" a "maximum posterior probability estimate"

## Vizualizácia a deskriptívna štatistika
 - <span style="color:red">Čiarový graf (lineplot)</span>
 - <span style="color:red">Bodový graf (scatterplot)</span>
 - <span style="color:red">Histogram</span>
 - <span style="color:blue">Krabicový diagram (boxplot)</span>
 - <span style="color:blue">Vyhladenie histogramu pomocou KDE (kernel density estimate)</span>
 - <span style="color:green">Kvantily</span>
 - <span style="color:red">Priemer, mód, medián, variancia a štandardná odchýlka</span>

## Modelovanie

- Rozdiel medzi <span style="color:red">regresiou</span> a <span style="color:red">klasifikáciou</span>
- <span style="color:red">Lineárna regresia</span> a <span style="color:red">logistická regresia</span>
- <span style="color:red">Overfitting</span> a strátegie proti nemu:
  - <span style="color:red">Rozdelenie dát na trénovanie/testovanie/validáciu</span>
  - <span style="color:green">Cross-validácia</span>
  - <span style="color:green">Regularizácia</span>
  - <span style="color:blue">Obohacovanie dát (data augmentation)</span>
- <span style="color:green">Normalizácia dát</span> - ktoré modely ju potrebujú a ktoré nie
- <span style="color:red">Chybová matica (confusion matrix)</span>  a ako z nej vypočítať rôzne metriky:
  - <span style="color:red">sensitivita (recall)</span>
  - <span style="color:red">špecificita</span>
  - <span style="color:red">precision</span>
  - <span style="color:red">accuracy</span>
  - ako sa navzájom ovplivňujú
- <span style="color:green">ROC krivka</span> a plocha pod ROC krivkou (možno aj krivka precission-recall)
- Dôsledky <span style="color:blue">nevyvážených dáta (data imbalance)</span> pri trénovaní a evaluačných metrikách
- <span style="color:green">Rozhodovacie rozhranie (decision boundary)</span> - lineárny vs. nelineárny model, koncept lineárne separovateľných dát
- <span style="color:blue">Feature engineering</span>, obzvlášť ako pomoocu neho premeniť lineárny model na nelineárny, viď tiež "kernel trick".
- <span style="color:green">Rozhodovací strom</span>
- <span style="color:blue">Neurónové siete</span> pre klasifikáciu
- <span style="color:blue">Kompromis medzi systematickou chybou a varianciou (Bias Vs variance tradeoff)</span>
- <span style="color:blue">Skupinové modely (ensemble models)</span>
- <span style="color:blue">Zhluková analýza (clustering)</span>
- <span style="color:blue">Tématické modelovanie dokumentov (topic modeling)</span>
- <span style="color:blue">Dimenzionálna redukcia</span>
- <span style="color:blue">Autoenkódery a embeddingy</span>

## Etika

- Skreslené dáta vedú k skresleným modelom.
- Dezinterpretácia výstupu modelu - užívateľ nerozumie matematike tak ako ty.
- Prehnaná dôvera v spoľahlivosť modelu - užívateľ nerozumie obmedzeniam modelu tak ako ty.
- Nezamýšľané použitie - užívatelia si robia čo sa im zachce, občas je to skvelé, občas je to hlúpe a občas je to kruté.
- Automatické rozhodovanie - nerob to, lepší nápad je pomáhať sa rozhodovať ľuďom, ale mysli pri tom na predošlé body.
- Kedy nerobiť strojové učenie - dobré užívateľské rozhranie a dobrá matematika sú často lepšie riešenia ako dobrý model.

## Ako vyzerá typický pracovný postup dátového vedca?

Okrem premýšľania nad prioritami, formovania a testovania hypotéz, komunikácie a iných činností pozostáva väčšinou "remeselná" časť dátovej vedy z týchto krokov:

- Načítaj dáta.
- Preskúmaj ich - ako dáta vyzerajú, koľko ich je, aké dáta chýbajú, sú nejako skreslené? Sú reprezentatívne voči skutočnému svetu? Aké dáta vlastne potrebuješ? Sú tam nejaké odľahlé, extrémne hodnoty?
- Zosumarizuj vlastnosti dát pomocou deskriptívnej štatistiky a vizualizácie.
- Vyčisti dáta: odstráň duplicity a vysporiadaj sa s chýbajúcimi dátami a extrémnymi hodnotami.
- Modeluj dáta - pochop, akú odpoveď hľadáš a aký model ti ju vie poskytnúť.
- Vyhodnoť model - robí to, čo po ňom chceš? Ak nie, vráť sa k predchádzajúcemu kroku.
- Vizualizuj a jasne odkomunikuj svoje závery. Čo znamená výstup modelu? Ako veľmi si si svojimi závermi istá?
- Ak je to potrebné, nasaď model pre opakované použitie.

## Záver
Veľa šťastia!