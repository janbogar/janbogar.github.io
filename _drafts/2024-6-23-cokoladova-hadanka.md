---
layout: post
title: 'Čokoládová hádanka'
lang: sk
ref: chocolate-riddle
thumbnail: "images/cokoladova-hadanka/chocolate.jpeg"
tags:
 - "lahka-matematika"
excerpt: ""
---

Nedávno som na sociálnych médiách zverejnil túto hádanku o čokoláde (link).

Myslím, že vedieť riešiť takéto úlohy je ako vedieť skočiť salto. Ak ste gymnasta, zvládnete to, aj keď vás zobudia o polnoci. Ak už viete ako na to, tak ste na to hrdý a príde vám to relatívne ľahké. Pre niekoho je zas takáto schopnosť nepredstaviteľná - až kým to nezvládne, čím sa preradí do predošlej skupiny. A niekto má takú traumu z predošlých zlyhaní (alebo to jednoducho nepovažuje za zaujímavé), že to ani neskúsi.

Komunikačne zdatný matematik by zhrnul postup riešenia na pár riadkov, lenže to by bol taký odbornícky podfuk. Takmer určite by to totiž nebol popis toho, ako na to riešenie prišiel. Matematici používajú pri riešení problémov množstvo fígľov, ktoré ale nie sú usporiadané exaktné fakty, ale skôr také vágne všeobecné múdra, ktoré by mohol rozdávať pustovník na vrchole hory. V kombinácií s praxou sú to ale práve tieto múdra, ktoré delia tých, čo vedia skočiť salto, od tých, ktorí nevedia ani ako začať.

Tento článok teda nie je len vysvetlením riešenia tejto hádanky. Je o niečom cennejšom a trochu tajomnejšom - je návodom k tomu, ako takéto riešenia hľadať.
Snažil som sa ho napísať tak, aby bol užitočný aj pre niekoho, kto v živote nevyriešil jedinú podobnú úlohu, ale aspoň trochu vie pracovať so zlomkami. Ak si ho niekto taký prečíta, dajte mi prosím vedieť, či svoj účel splnil.

## Múdry muž hovorí: Začni v malom.

Nikdy sa nenechajte obalamutiť zdanlivou zložitosťou problémov - takmer vždy existuje jednoduchá verzia problému, ktorú si môžete ohmatať, a navedie vás k tomu, ako riešiť zložitejšie prípady.
V tomto prípade je samotné zadanie hádanky návod, ako na to. Nezačína so všeobecným počtom ľudí N - začína s 2 ľudmi, najmenším počtom, čo dáva ešte zmysel.

## Múdry muž hovorí: Čmáraj na papier a kresli obrázky.

Postupne si teda problém ohmatáme. Môžeme to spraviť v hlave, ale lepšíe je počmárať celý kus papiera zápiskami a ideálne aj náčrtkami svojich myšlienok. Ak si viete problém predstaviť nejako vizuálne alebo geometricky, čmárajte si obrázky. Mohlo by to vyzerať napríklad takto:

Prvé kolo:
Prvý jedák zje 1/2 a ostane po ňom 1/2.
Druhý jedák zje 1/2 z toho, čo ostalo, čiže 1/2 z 1/2, čo je 1/4. Ostane po ňom 1/4.

Druhé kolo:
Prvý jedák zje 1/2 z toho, čo ostalo, čiže 1/2 z 1/4, čiže 1/8. Ostane po ňom 1/8.
Druhý jedák zje 1/2 z toho, čo ostalo, čiže 1/2 z 1/8, čiže 1/16. Ostane po ňom 1/16.

Prvý jedák zje 1/2 z toho, čo ostalo, čiže 1/2 z 1/16, čiže 1/32. Ostane po ňom 1/32.
Druhý jedák zje 1/2 z toho, čo ostalo, čiže 1/2 z 1/32, čiže 1/64. Ostane po ňom 1/64.

A tak ďalej...

Príliš dlho sa ale vypisovaním nezdržujeme, len dosť na to, aby sme mali pred sebou, ako to celé funguje. Teraz totiž nasleduje druhá časť našeho snaženia, a tu sa naše možnosti štiepia. Je totiž veľa spôsobov riešenia, ktoré vedú k správnemu výsledku.

## Múdry muž hovorí: Pravdu je lepšie uvidieť ako vypočítať.

Skúsený počtár by sa na toto pozrel, a hneď by si povedal "Aha! Veď to vyzerá skoro ako nekonečný súčet geometrického radu. A na to predsa poznám vzorec!" Potom by schytil pero, upravoval výrazy, dosadzoval do vzorca (ktorý si pred tým pre istotu vygooglil) a po mnohých útrapách (no dobre, po pár riadkoch, nič hrozné) by mu vyšlo: prvý jedák zje 2/3 čokolády.
Tento postup je samozrejme správny, ale zanecháva po sebe na jazyku istú pachuť a otázku: "Čo z toho?" K výsledku sme sa síce dobrali, ale nič nás nenaučil (okrem precvičovania úprav vzorcov). Navyše, sme si istí, že sme po ceste neurobili žiadnu chybu? Ako to zovšeobecniť? Čo ak sme si zle zapamätali vzorec? A ešte to aj bolo príšerne pracné a nudné.

Matematika nie je počtárstvo, aj keď to tak po prejdení vzdelávacím systémom môže vyzerať. Lepší prístup je na chvíľu spomaliť, pozrieť sa na to, čo už vieme, a zatiaľ, čo sa na to pozeráme, pozrieť sa na to znovu a poriadne.

Všímajme si, čo máme pred sebou, a pozerajme sa na to z rôznych uhlov pohľadu.

V kole, keď zje prvý jedák 1/2, druhý zje 1/4. Keď zje prvý jedák 1/4, druhý zje 1/8. V obch prípadoch zjedol druhý jedák dva krát menej ako ten prvý. Platí to vždy?

No áno, musí to platiť vždy, lebo bez ohľadu na to, koľko čokolády mám na začiatku kola, prvý z nej zje polovicu a druhý štvrtinu, a štvrtina je dvakrát menej ako polovica.

Jednotlivé kúsky čokolády, ktoré každý zje, sú tak popárované do dvojíc (jedna dvojica na každé kolo). A v každej dvojici je toho dvakrát viac pre prvého jedlíka ako pre druhého. Je vlastne úplne jedno, koľko čokolády dokopy zjedia v každom kole, keď vždy bude mať prvý dvakrát viac ako ten druhý. Potom musí mať aj dokopy prvý jedlík dvakrát viac čokolády, ako ten druhý.

No a to je riešenie - Prvý jedák zje dva krát viac čokolády, ako druhý.

Koľko je to, keď si to vyjadrím ako zlomok z celej čokolády?
Chceme rozdeliť čokoládu v pomere 2 ku 1 - to sú spolu tri dieli, každý diel je teda tretina čokolády. Prvý jedlík zje dva diely teda 2/3 čokolády, a druhý jeden diel, teda 1/3 čokolády.

A je to. Aké elegantné, popárovať dokopy všetky sústa, ktoré každý zjedol, a využiť, že v každom kole sa deje to isté (v pomere k množstvu čokolády, s ktorou sa začína).
Múdry muž by teraz na to možno povedal, "Zapamätaj si princíp", a to by bolo niečo o nekonečných cykloch, kde každý krok je len zmenšením toho predošlého v nejakom pomere, pretože vždy keď na takúto situáciu narazíte, môžete ju riešiť podobne. Ale miesto toho hromovým hlasom zvolá niečo iné:

## Múdry muž hovorí: Kriticky preskúmaj svoje predpoklady!

Ozaj, to je dôležité. Nepomýlili sme sa niekde?
Poďme si to prejsť (keďže je takýto elegantný postup krátky, dá sa to ľahko, má len pár krokov).

To, že v každom kole zje prvý polovicu a druhý štvrtinu z čokolády, ktorá v tom kole ešte zostala, je absolútne nepriestrelné, veď to prakticky hovorí priamo zadanie, takže tam chyba nie je.
Takisto to, že je každé kolo rovnaké.
Takže naozaj musí zjesť prvý jedlík dva krát viac, ako ten druhý.

No a potom je už len jeden krok, rozdeliť celé čokoládu v pomere 2:1. Aha! Nemôže tam byť skrytá nejaká habaďúra? No jasné, čo ak takto dokopy nezjedia celú čokoládu, ale len nejakú jej časť? To sme len tak predpokladali, že ju zjedia celú, ale vlastne sme si to nikdy neoverili. Ak by vás samých toto nenapadlo, nezúfajte. Matematikov by to napadlo len preto, že im niekto podobný príklad už predtým ukázal.

Teoreticky si vieme predstaviť, že ako z čokolády postupne odjedajú, k nejakému kúsku sa nikdy nedostanú. Napríklad by dokopy mohli zjesť len, ako príklad, 90%, pričom prvý jedák by zjedol 60% čokolády a druhý 30%. To by bolo v pomere 2:1, ale menej, ako nám vyšlo pred tým, teda 2/3 a 1/3.

Našli sme skrytý prepdoklad. Predpokladali sme, bez toho aby sme vedeli, či je to naozaj pravda, že takto zjedia celú čokoládu. Čo ak ale existuje nejaký kúsok čokolády, ku ktorému sa nikdy nedostanú, po ľubovoľnom množstve kôl?

Skúsený počtár by vedel, že takto zjedia čokoládu naozaj celú, pretože je vyzbrojený znalosťami nekonečného geometrického radu, a teda vie, že 1/2 + 1/4 + 1/8 + ... = 1. Lenže tento článok nie je pre počtárov, takže: môže existovať nejaký kúsk čokolády, ktorý nikdy nezjedia? Zjedia ju celú?

## Múdry muž hovorí: Nepozeraj sa na to, čo je, ale na to, čo nie je.
Po chvíli dumania sa musíme vrátiť na začiatok. Môžeme sa napríklad pozrieť na to, koľko dokopy zjedia čokolády po každom kole. Opäť použijeme prvé múdro a začneme v malom, s prvými kolami.

Po prvom: 1/2 + 1/4 = 3/4
Po druhom: 3/4 + 1/8 + 1/16 = ???

Uf, no to je hnusné už po dvoch kolách, čo teraz? Môžeme počtársky upravovať vzorce, ale ako sme si už vysvetlili, to má plno nevýhod. Miesto toho bude lepšie zmeniť smer a skúsiť sa na to pozrieť nejako inak. A jeden často užitočný spôsob, ako zmeniť smer, je nepozerať sa na to, čo máme, ale na to, čo chýba.

Čo keby sme sa miesto toho, koľko toho zjedli, pozreli na to, koľko čokolády ešte zostalo? Koľko čokolády zjedli je potom len celá čokoláda mínus to, čo zostalo. Koľko čokolády zostalo sme si ale predsa už napísali, keď sme začínali s riešením.

Po prvom kole: 1/4
Po druhom kole: 1/16
Po treťom kole: 1/64

A tak ďalej. Och, no to je krásne, vyzerá to, že po každom kole ostane len štvrtina z toho, čo zostalo po predošlom kole. Prečo je to tak a platí to naozaj v každom kole?
Každé kolo je rovnaké, začína s ostatkom po predošlom kole, a vždy z neho prvý jedák zje polovicu, druhý štvrtinu, a ostane po nich jedna štvrtina toho, s čím v tom kole začínali. Takže áno, naozaj po každom kole ostane štvrtina z toho, čo po predošlom.

Takže zostatok čokolády po i-tom kole je 1/4^i. To je stále sa zmenšujúci zlomok (exponenciálne sa zmenšujúci, aby sme boli presní), ktorý je stále menší a menší, a ako by množstvo kôl išlo do nekonečna, množstvo nezjedenej čokolády by išlo k nule. {% include collapsible.html content="Ak by sme boli naozaj dôsledný, tento skrytý predpoklad by sme si tiež mali dokázať. Robí sa to tak, že si ukážeme, že akékoľvek malé číslo si vyberiem, pre dostatočne veľké i bude 1/4^i menšie, ale nikdy nepodlezie 0. Nie je to nič zložité, ale raz treba s dokazovaním prestať, a oprieť sa o to, čo už vieme s dostatočnou istotu, lebo sme si to niekedy dokázali sami, alebo to dokázal pred nami niekto, komu veríme. Mimochodom, presne toto je časť učiva prvého semestra matematickej analýzy na matfyze, neformálne sme tu vlastne prišli k definícií limity." %}. Takže náš skrytý predpoklad bol našťastie správny: čokoládu si naozaj rozdelia celú, len im to bude nekonečne dlho trvať - v každom kole k tomu budú bližšie a bližšie. Takže naozaj prvý jedák zje po nekonečnom počte kôl 2/3 čokolády, a druhý 1/3 (teda, presnejšie povedané, dostanú sa k tomu ľubovoľne blízko, ak počkáme dostatočne mnoho kôl).

Bolo toto preverovanie predpokladov vôbec nutné? Ak si chcete byť výsledkom istý, tak áno. Pozrite sa do dodatku, tam ukazujem príklad, keď rovnaký postup vedie k chybnému výsledku práve preto, lebo tento predpoklad neplatí.

Prvú časť našej hádanky sme teda vyriešili, a keďže sme našli pár užitočných princípov, s druhou časťou si už hravo poradíme.

## Múdry muž hovorí: Zovšeobecňuj.

Najprv si to zas rozpíšme. Už dopredu vieme, že sa oplatí venovať pozornosť tomu, čo ostane po každom kole, aby sme vedeli, či zjedia spolu celú čokoládu, a aj preto, lebo to zjednodušuje výpočty.

Prvé kolo:
Prvý zje 1/3, ostanú 2/3. Druhý zje 1/3 z 2/3 = 2/9, ostanú 2/3 z 2/3, teda 4/9. Treti zje tretinu zo 4/9, teda 4/27, ostane 8/27.

Druhé kolo:
To isté ako prvé kolo, ale začína sa s 8/27 čokolády.

Druhé kolo už ani nemusím rozpisovať. Viem, že môžem zas usporiadať sústa našich troch jedákov do trojíc podľa kôl. Sústa v každom kole budú len zmenšeninou súst v tých predošlých kolách, ale ich vzájomné pomery budú rovnaké. V každom kole teda zje prvý jedák tretinu z toho čo je k dispozícií, druhý 2/9 a tretí 4/27. Aj celkovo si teda rozdelia čokoládu v tomto pomere. Ale zjedia ju celú?

Opäť sa pozrime na to, čo zostane po každom kole. Po prvom kole ostane 8/27 z celej čokolády, po druhom kole 8/27 z 8/27, a tak ďalej. Po i-tom kole zostane (8/27)^i. Keďže 8/27 je menej ako 1, tak znovu platí, že množstvo čokolády sa s pribúdajúcimi kolami priblížuje ľubovoľne blízko k 0. To by sme si zas mohli dokazovať, ale tu by múdry muž povedal: "Niekoré veci si skrátka treba pamätať". Exponenciála so základom menším ako 1 sa približuje k 0. V tomto pomáha prax alebo Google či Wolfram Alpha. Prinajhoršom si môžete predpoklad odložiť na neskôr, a tvrdiť len "Ak tento prepdoklad platí, platí aj môj výsledok."{% include collapsible.html content= "Poviem vám tajomstvo: takto je vystavaná úplne celá teoretická matematika. Predpokladu, ktorý sme jednoducho odložili a nechali tak, sa hovorí axióm."%}.

Takže opäť platí, že čokoládu zjedia celú. Koľko to presne vychádza pre každého z nich?

Tu už sa počtárstvu vyhneme len ťažko. Múdry muž hovorí: "Občas si treba vyhrnúť rukávy a nestrácať trpezlivosť." Niektoré matematické výkony sú skrátka nad možnosti ľudskej mysle nevyzbrojenej perom a papierom (a opäť platí, že pre každého je táto hranica inde). Ale aj tu sa dá pristupovať k veciam elegantne a skúmať, z ktorej strany to ide najjednoduchšie. Len si to vyžaduje prax, aby človek odhadol najľahšiu cestu hneď a nie až na tretí pokus.

Napríklad takto: Všetky tie zlomky vynásobíme 27 (ich vzájomný pomer sa tým teda nezmení). Takže dostaneme, že si čokoládu rozdelia v pomere 27\*1/3=9 ku 27\*2/9=6 ku 27\*4/27=4. To je po vykrátení 9 ku 6 ku 4, spolu 19 dielov, takže prvý zjedol 9/19 celej čokolády, druhý 6/19 a tretí 4/19.

## Múdry muž hovorí: Zovšeobecňuj viac.
Tak a čo ak bude ľudí N?


## Dodatok

Sľúbil som príklad, kde podobný postup dáva chybné výsledky, ako dôkaz toho, že svoje predpoklady si treba poctivo preverovať.

Ukážem vám dva, každý chybný iným spôsobom.

Prvý je tento. Predstavte si variantu pôvodnej hádanky: dvaja jedlíci sa striedajú, prvý zje na začiatku tretinu celej čokolády, a potom každý ďalší zje tri krát menej, ako ten predošlý (čiže nie tretinu zo zvyšku, ale tretinu z toho, čo zjedol ten predchádzajúci). Takže začínajú takto: prvý zje 1/3, druhý zje 1/3^2=1/9, potom zas prvý 1/3^3= 1/27, potom druhý 1/3^4 = 1/81 a tak ďalej.

Povedali by ste si, že druhý zje vždy tri krát menej ako prvý, takže ak by si rozdelili celú čokoládu v pomere 3 ku 1, prvý by zjedol 3/4 a druhý 1/4. Lenže aha, ak celkový súčet všetkých ich súst označím S, tak po troche algebry dostanem:

1/3 + 1/3^2 +1/3^3 + 1/3^4 + ... = S
1/3 * (1+ 1/3 + 1/3^2 +1/3^3 + 1/3^4 +)=S
1/3 * (1+ S)=S
1 + S = 3S
1 = 2S
S=1/2

Takže dokopy zjedia len jednu polovicu z celej čokolády. {% include collapsible.html content="Technicky vzaté by tu bolo treba dokázať konvergenciu, viď ďalší príklad, ale to už nechám na čitateľa. Alebo mi skrátka verte."%} Ako by potom mohol zjesť prvý z nich 3/4 čokolády? No nezje, takýmto spôsobom sa budú stále pomalšie a pomalšie blížiť k tomu, že zjedia polovicu čokolády, ale tú hranicu jednej polovice nikdy neprekročia. Prvý z nich teda zje 3/8 a druhý 1/8 čokolády.

Druhý príklad je trochu abstraktný, ale zato veľmi poučný.

Predstavte si, že máme takýto nekonečný súčet:

1-1+1-1+1-1... = ?

Poviete si že možno by sa dali znovu všetky jeho prvky popárovať do dvojíc, vždy +1 a -1. Keďže v každej dvojici je súčet 0, tak súčet všetkých dvojíc bude zas len nula.

Lenže potom aha:

0= 1-1+1-1+1-1... = 1 - (1-1+1-1...) = 1-0 = 1

Takže 0=1. Očividne je tu niekde chybka. Chybka je v tom, že o nekonečnom rade sa dá hovoriť, že má niečo ako súčet len vtedy, keď sa k nemu limitne blíži. Ako postupne pridávame čísla z tohoto radu, tak ich súčet sa postupne k tomu "celkovému" musí blížiť (alebo ho aj dosiahnuť). {% include collapsible.html content= "Exaktne je to takto. Číslo, ku ktorému sa súčet radu blíži, nazývame limita súčtu radu. Akokoľvek maličkú vzdialenosť od tejto limity si vymyslím, tak viem vždy nájsť nejaké konkrétne číslo N také, že ak sčítam N a viac členov radu, tak bude súčet k tejto limite bližšie, ako táto vzdialenosť. Všimnite si, že to pripušťa aj možnosť, že sa súčet od svojej limity môže dočasne aj vzdaľovať, ale len dočasne. Tiež si všímnite, že pre náš rad 1-1+1-1... žiadna taká limita neexistuje."%}

Rad 1-1+1-1+1... túto vlastnosť nemá. Ako postupne sčitujeme jeho členov, tak celkový súčet skáče medzi 0 a 1, ale k žiadnemu z nich (ani akéjkoľvek inej hodnote) sa neblíži.

Odborne sa tomu hovorí, že rad nekonverguje. V hádanke s čokoládou takýto scenár nehrozil {% include collapsible.html content="Na konvergenciu nám stačí, že množstvo zjedenej čokolády vždy stúpa, ale nemôže prekročiť celkové množstvo čokolády. Viď https://en.wikipedia.org/wiki/Monotone_convergence_theorem " %}, ale pri rôznych abstraktnejšch problémoch môže ľahko nastať.

