---
layout: post
title: Neurónové sieťe vs. Conwayova hra života
lang: sk
ref: nn-vs-conway
permalink: /nn-vs-conway-sk
thumbnail: images/nn-vs-conway/glider.gif
excerpt: >-
    Preskroloval som okolo ukážky nejakého videa o hraní Conwayovej hry života pomocou neurónovej siete a priznávam, že moja prvá reakcia bola: "Pff, to je blbosť". Myslel som totiž, že "hraním hry" sa myslí samotné aplikovanie jej pravidiel — úloha, pri ktorej akékoľvek použitie neurónových sietí nedáva zmysel. Nakoniec sa samozrejme ukázalo, že video bolo skvelé, pretože "hraním hry" myslelo vymýšľanie rôznych zaujímavých obrazcov, na čo sa neurónky naopak perfektne hodia.


    Ale čo keby sme zostali pri tom prvom význame "hrania hry"? Ako stupídne by bolo použiť na to neurónovú sieť? Vlastne celkom dosť. Uvážte, že váhy takej neurónovej siete sa dajú spočítať a zadať ručne. Ale žiadne množstvo stupídnosti by nám nemalo zabrániť urobiť niečo zaujímavé. Kto vie, možno sa pri tom niečo naučíme?


scripts: [mathjax]
tags:
 - "data-science"
---
Jupyter notebook pre túto stránku nájdete na tomto [odkaze](https://github.com/janbogar/small_projects/blob/master/NN_vs_Conway/NN%20plays%20Conways%20Game%20of%20Life.ipynb).

{{page.excerpt}}

V tomto článku:
 - Navrhneme neurónovú sieť, ktorá bude hrať Conwayovu hru života.
 - Implementujeme ju v Pythone pomocou Pytorch.
 - Nastavíme ručne jej váhy tak, aby perfektne simulovala pravidlá hry.
 - Natrénujeme ju do perfektnej presnosti z náhodnej inicializácie, len aby sme zistili, aké je to ťažké. Ukáže sa, že celkom dosť.

![glider_gun.gif]({{site.baseurl}}/images/nn-vs-conway/Gospers_glider_gun.gif)

## Pravidlá hry
[Conwayova hra života](https://cs.wikipedia.org/wiki/Hra_%C5%BEivota) sa hrá na štvorcovej mriežke, kde každá bunka (tzn. políčko) môže byť živá alebo mŕtva. Hrá sa na kolá a to, či bude v nasledujúcom kole bunka živá alebo mŕtva, určujú tieto tri pravidlá:
 - Živá, ak je teraz mŕtva a má troch živých susedov.
 - Živá, ak je teraz živá a má dvoch alebo troch živých susedov.
 - Mŕtva v ostatných prípadoch.
 
Susedov bunky tvorí všetkých 8 políčok okolo nej — vertikálne, horizontálne aj diagonálne susediace. Tieto jednoduché pravidlá, aplikované v každom kole, vedia vytvoriť úžasne zložité a chaotické vzory.{% include collapsible.html content=" Ak rozmýšľate, ako sa takáto hra dá vyhrať, tak je to hra pre jedného a vyhráva každý, koho baví, ako podivne sa obrazce na ploche vyvíjajú."%}

Tieto pravidlá prirodzene tvoria jednoduchý algoritmus obsahujúci "if else" podmienku a boolovské (tzn. binárne) premenné. Pre taký jednoduchý algoritmus naozaj nedáva zmysel, kvôli výkonu alebo z iného dôvodu, nahradiť ho neurónovou sieťou — zložitým reťazcom vážených súm a nelineárnych funkcií, ktoré miesto binárnych premenných operujú s (typicky) 64 bitovými číslami.

Tieto pravidlá implementujeme ako funkciu. Vstup do nej bude pole s rozmermi 3x3, s hodnotami 1 a 0 pre živé a mŕtve bunky a výstup bude hodnota prostrednej bunky v ďalšom kole. Túto funkciu by sme potom mohli v každom kole aplikovať na každú 3x3 oblasť hracej plochy, a dostali by sme tak hodnoty políčok v ďalšom kole. Nie je to najefektívnejšia implementácia {% include collapsible.html content='Efektívnu implementáciu nájdete napríklad v [tomto videu](https://www.youtube.com/watch?v=ndAfWKmKF34)' %}, ale je elegantná a ako uvidíme, zíde sa nám aj pri našej snahe zneužívať neurónové siete.

Tu je táto funkcia v Pythone, spolu s funkciou, ktorá generuje všetky možné polia 3x3 (zíde sa nám pri trénovaní a testovaní).

```python
import torch
import numpy as np
import matplotlib.pyplot as plt
import random
import sklearn.metrics as mtr

np.set_printoptions(precision=2)
```


```python
def conway_rule_straightforward(arr):
    center = arr[1,1]
    sum_perimeter = np.sum(arr) - center
    if (sum_perimeter == 3 and center == 0) or (sum_perimeter in (2,3) and center == 1):
        return 1
    else:
        return 0

def conway_rule(arr):
    """Equivalent to conway_rule_straightfoward, just more elegant. Check it for yourself!"""
    sum_total = np.sum(arr)
    sum_perimeter=sum_total - arr[1,1]
    if sum_total >= 3 and sum_perimeter <= 3:
        return 1
    else:
        return 0
```


```python
def generate_neighborhoods():
    """Generate all possible 3x3 squares."""
    X=[]
    for i in range(2**9):
        x=[int(i) for i in format(i,"b")]    #turn binary string to list of integers
        x=[0 for i in range((9-len(x)))] + x    #pad with 0
        X.append(np.reshape(np.array(x),(3,3)))    #to array
    return np.array(X)
```


```python
#example
x=generate_neighborhoods()[100]
y=conway_rule(x)
print(f"On the next turn, the centre cell of this square\n{x}\nwill have a value:\n{y}")
```

    On the next turn, the centre cell of this square
    [[0 0 1]
     [1 0 0]
     [1 0 0]]
    will have a value:
    1

```python
#check if both implementations of the rules give the same results
for i in generate_neighborhoods():
    y1=conway_rule_straightforward(i)
    y2=conway_rule(i)
    if not y1==y2:
        print(f"Error on input:\n{i}\nconway_rule_straightforward: {y1}\nconway_rule: {y2}")
        break
else:
    print("Everything checks out!")
```

    Everything checks out!


## Ako z toho urobiť neurónovú sieť?

Obvyklým spôsobom je použiť strojové učenie — ručne definujeme štruktúru neurónovej siete a potom ju natrénujeme, tzn. použijeme nejaký algoritmus (napr. gradientný zostup) na postupné pošťuchovanie jej parametrov až kým nebude jej výstup dostatočne pripomínat výstup, ktorý chceme.

Ale nemusíme to tak robiť. Neurónové siete sú len špeciálna trieda parametrických funkcií, podobne ako "kvadratické funkcie" alebo "Fourierove rady" a podobne. Môžeme sa skrátka tuho zamyslieť a prísť s potrebnými parametrami sami.

Tu je pár vhľadov, ktoré nám s tým pomôžu:
 - Pravidlá sme už implementovali ako funkciu, ktorá má na vstupe pole 3x3 a ktorú potom postupne aplikujeme na každé také pole na hracej ploche. To je ale predsa presne to, čo robia konvolučné neurónové siete! Takže hľadáme konvolučnú neurónovú sieť s 3x3 konvolučným filtrom.
 - Jediný neurón s dvoma vstupmi dokáže simulovať logickú AND funkciu (alebo ľubovoľnú inú logickú funkciu, viď. [túto stránku](https://towardsdatascience.com/perceptrons-logical-functions-and-the-xor-problem-37ca5025790a)).
 - Môžeme využiť symetriu pravidiel hry. Z pohľadu pravidiel sú si všetky susedné bunky rovnocenné, na ich polohe nezáleží, závisí len na celkovom poočte živých susedov. Neurónová sieť teda tiež môže mať túto symetriu, a všetky váhy na obvode konvolučného filtra môžu byť rovnaké (nemusí to tak nutne byť, ale hodí sa nám to).


Na základe týchto myšlienok, tu je implementácia pravidiel hry pomocou neurónovej siete. Je to v podstate priamy prepis funkcie `conway_rule` do neurónovej siete. Pamätajte ale, že táto implementácia nie je jediná možná.

<div style="background-color:white;padding:10px">
<img alt="neurónová sieť" src="{{site.baseurl}}/images/nn-vs-conway/neural_network.png">
</div>

Táto sieť pozostáva z konvolučnej siete s konvolučným filtrom 3x3, ktorý má dva kanály: na obrázku červený a modrý. Výstup červeného kanála je väčší ako 0.5, ak je v susedstve centrálnej bunky menej živých buniek ako 4. Výstup modrého kanála je viac ako 0,5 vtedy, ak sú v oblasti (vrátane centrálnej bunky) viac ako dve živé bunky. Výstupy týchto kanálov sú potom vstupy posledného neurónu, ktorú robí (približne) AND operáciu. Ak sú obidva vstupy práve 0,5, ich váhovaný súčet preváži nad biasom (-80) a výstup neurónu bude viac ako 0,5, čo hovorí, že bunka bude v ďalšom kole živá.
Ak budú ale o trochu menej {% include collapsible.html content="Priznávam, že toto dovysvetlenie som napísal pár rokov neskôr ako pôvodný článok, a už netuším, prečo som vybral parametre tohoto neurónu práve -80, 50 a 50. Asi som si povedal, že -80, 40 a 40 by bolo na hrane, tak to trochu posuniem. O koľko presne to ale je možné posunúť bez zmeny výsledku by už bolo náročnejšie spočítať, takže som to asi len odhadol a preveril, že to funguje."%}, bias nepreváži a výstupná hodnota bude menej ako 0,5, čo značí, že bunka bude v ďalšom kole mŕtva.

No a to je všetko. Vždy, keď aplikujeme túto konvolučnú sieť na hracie pole, vypočíta, akú hodnotu bude mať každá bunka v budúcom kole.

## Okrajové podmienky

Hra by sa mala hrať na nekonečnej mriežke. Keďže by to bolo celkom náročné implementovať, nahradíme to mriežkou, ktorá je konečná, ale napája sa sama na seba — každá bunka na okraji hracej plochy bude brať ako svojich susedov aj zodpovedajúce bunky z opačného okraja plochy. Tejto finte sa hovorí aj periodické okrajové podmienky a je to to isté, ako keby sme nehrali na nekonečnej rovine, ale na toruse.

Toto napojenie dosiahneme jednoducho tak, že k neurónovej sieti pridáme prípravný krok (preprocessing), počas ktorého ku každému okraju hracej plochy skrátka prilepíme bunky z jej opačného okraja. Tento preprocessing bude voliteľný, takžo keď ho vypneme a sieť spustíme na mriežke 3x3, výstup bude len hodnota pre prostrednú bunku a nie pre všetky bunky na malom 3x3 toruse.

```python
class ConwayStep(torch.nn.Module):
    """Neural network that computes a step of Conway's Game of Life. """
    def __init__(self,handcrafted=True):
        """If handcrafted is true, the handcrafted weights are used.
        Otherwise, the weights are initialised randomly."""
        
        super(ConwayStep,self).__init__()
        layer1=torch.nn.Conv2d(in_channels=1,   #because input from every cell is just one number, not a vector
                               out_channels=2,    #because middle layer has two neurons
                               stride=1,          #because we want the output for every cell
                               padding=0,         #because padding is done in preprocessing
                               kernel_size=(3,3))

        layer2=torch.nn.Conv2d(in_channels=2,     #because middle layer has two neurons
                               out_channels=1,     #because output is just one number: value for the center cell on the next turn
                               stride=1,
                               padding=0,
                               kernel_size=(1,1))
        
        if handcrafted:
            layer1.weight.data=torch.tensor([[[[-10.,-10.,-10.],
                                               [-10., 0.,-10.],
                                               [-10.,-10.,-10.]]],
                                             [[[10.,10.,10.],
                                               [10.,10.,10.],
                                               [10.,10.,10.]]]])
            layer1.bias.data=torch.tensor([40.,-20.])
            layer2.weight.data=torch.tensor([[[[50.]],[[50.]]]])
            layer2.bias.data=torch.tensor([-80.])

        self.network=torch.nn.Sequential(layer1,
                                         torch.nn.Sigmoid(),
                                         layer2,
                                         torch.nn.Sigmoid())
    
    def preprocess(self,batch,pad=False):
        """
        If pad is True, pads the array with the cells from the opposite edge, 
        so there are periodic boundary conditions.
        """
        if len(batch.shape)==2:
            batch=batch[None,:,:] #add empty dimension if only one sample is in the batch
        if pad:
            batch=np.pad(batch,pad_width=((0,0),(1,1),(1,1)),mode="wrap")
        return torch.Tensor(batch[:,None,:,:])   #add empty dimension for channels
    
    def postprocess(self,batch, threshold=0.5):
        """
        Applies thresholding (default threshold is 0.5)
        """
        batch=batch.detach().numpy()[:,0,:,:] #removes empty channels dimension
        batch=1*(batch > threshold)    #applies thresholding
        return batch.squeeze()   #remove empty dimensions

    def forward(self,x):
        return self.network(x)
```


```python
net=ConwayStep()
```


```python
#example
def show_grid(x):
    plt.pcolormesh(x, edgecolors='w', linewidth=2, cmap="Greens")
    ax = plt.gca()
    ax.set_aspect('equal')
    plt.setp(ax.get_xticklabels(),  visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.show()
    
x=np.array([[0,0,0,0,0],
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0]])
print(f"Grid on current turn:\n\n{x}\n")

y_raw=net(net.preprocess(x,pad=True))
print(f"Output of the network before thresholding:\n\n{y_raw.detach().numpy()}\n")

y=net.postprocess(y_raw)
print(f"Grid on the next turn:\n\n{y}")

```

    Grid on current turn:
    
    [[0 0 0 0 0]
     [0 0 0 0 0]
     [0 1 1 1 0]
     [0 0 0 0 0]
     [0 0 0 0 0]]
    
    Output of the network before thresholding:
    
    [[[[9.36e-14 9.36e-14 9.36e-14 9.36e-14 9.36e-14]
       [9.38e-14 6.69e-03 1.00e+00 6.69e-03 9.38e-14]
       [9.38e-14 6.69e-03 1.00e+00 6.69e-03 9.38e-14]
       [9.38e-14 6.69e-03 1.00e+00 6.69e-03 9.38e-14]
       [9.36e-14 9.36e-14 9.36e-14 9.36e-14 9.36e-14]]]]
    
    Grid on the next turn:
    
    [[0 0 0 0 0]
     [0 0 1 0 0]
     [0 0 1 0 0]
     [0 0 1 0 0]
     [0 0 0 0 0]]


```python
#check if neural network gives the same results as the rules

X=generate_neighborhoods()
np.random.shuffle(X)
Y_label=np.array([conway_rule(i) for i in X])
Y_pred=net.postprocess(net(net.preprocess(X,pad=False)))

for x,label,prediction in zip(X,Y_label,Y_pred):
    if not label==prediction:
        print(f"Error on input:\n{x}\nconway_rule: {label}\nneural network: {prediction}\n")
        break
else:
    print("Everything checks out!")
```

    Everything checks out!


# Ako natrénovať neurónovú sieť?

Je to priamočiare:
 - Náš trénovací dataset bude obsahovať všetky možné 3x3 mriežky a očakávané výstupy (labels) bude generovať funkcia `conway_rule`, pretože to sú skrátka všetky možné dáta, aké ku Conwayovej hre života môžu existovať.
 - Použijeme online learning, čiže batch size bude 1.
 - Ako loss funkciu použijeme cross entropiu a ako optimizátor Adam, pretože táto kombinácia je len málokedy zlou voľbou.
 - Metriky, na ktoré sa zameriame, budú hodnota loss funkcie a oblasť pod ROC krivkou (`roc_auc`), vypočítané pre celý dataset na konci každej epochy. Keď dosiahne sieť perfektnú presnosť, jej roc_auc bude 1. Loss funkcia sama o sebe nemá takú jasnú interpretáciu, pretože môže klesať aj keď sa presnosť modelu už nemení.

Teda, aspoň takýto bol plán, ale ukázalo sa, že niekedy trvá sieti veľmi, veľmi dlho skonvergovať (ak vôbec skonverguje).
Občas som mal šťastie a skonvergovala po pár stovkách epoch, občas sa zasekla na niekoľko tisíc epoch, v závislosti od počiatočnej náhodnej inicializácie siete.

Ukázalo sa, že Adam nie je vždy najlepšia voľba, pretože trochu prekvapivo, obyčajný stochastický gradientný zostup s learning rate hodnotou 0.01 skonvergoval spoľahlivo do 200 epoch. Stochastický gradientný zostup s hybnosťou skonvergoval ešte rýchlejšie.

```python
net_trained=ConwayStep(handcrafted=False)

loss_func = torch.nn.BCELoss()

# this fails to converge
#optimizer = torch.optim.Adam(net_trained.parameters(),lr=0.01)
#num_epochs=5000

optimizer = torch.optim.SGD(net_trained.parameters(),lr=0.01,momentum=0.9,nesterov=True)
num_epochs=100

data=list(zip(X,Y_label))
batch_size=1

logs=[]
def detach_state_dict(state_dict):
    return {k:v.clone().detach().numpy() for k,v in state_dict.items()}    

for epoch in range(num_epochs):
    random.shuffle(data)
    for i,start in enumerate(range(len(data)//batch_size)):
        x,y_label=zip(*data[start:start+batch_size])

        # optimization
        optimizer.zero_grad()

        y_pred = net_trained(net_trained.preprocess(np.array(x)))
        loss = loss_func(y_pred, torch.tensor(y_label).type(torch.FloatTensor))
        loss.backward()
        
        optimizer.step()
        
    #logging, metrics and printing after each epoch
    with torch.no_grad():
        Y_pred=net_trained(net_trained.preprocess(X))
        loss=loss_func(Y_pred, torch.tensor(Y_label).type(torch.FloatTensor)).item()
        Y_pred=Y_pred.detach().numpy().squeeze()
        
    fpr,tpr,thresholds=mtr.roc_curve(Y_label,Y_pred)
    roc_auc=mtr.roc_auc_score(Y_label,Y_pred)
    print(f"epoch={epoch} loss={loss} roc_auc={roc_auc}")
    logs.append(dict(epoch=epoch,
                     fpr=fpr,
                     tpr=tpr,
                     thresholds=thresholds,
                     Y_pred=Y_pred,
                     loss=loss,
                     roc_auc=roc_auc,
                     state_dict=detach_state_dict(net_trained.state_dict())))
    plt.plot(fpr,tpr,label="roc")
    plt.plot(fpr,thresholds,".",label="thresholds")
    plt.legend()
    plt.show()
```


```python
plt.title("Training log")
plt.plot([i["loss"] for i in logs],label="loss")
plt.plot([i["roc_auc"] for i in logs],label="roc_auc")
plt.xlabel("epoch")
plt.legend()
plt.show()
```


<div class="lighter_background">
<img src="{{site.baseurl}}/images/nn-vs-conway/NN%20plays%20Conways%20Game%20of%20Life_13_0.png" alt="graf vývoja metrík počas tréningu">
</div>


To je celé. Natrénovaná neurónová sieť dosiahla perfektnú presnosť, keďže plocha pod ROC je 1. Pre nás veľmi pohodlne, threshold s hodnotou 0.5 perfektne oddeľuje obidve triedy (živé a mŕtve bunky), takže ho nemusíme nijak nastavovať. Môžeme sa skrátka pohodlne oprieť a užívať si tieto neefektívne vypočítané klzáky.


```python
def show_grid(grid):
    plt.gca().set_xticks(np.arange(grid.shape[0]+1)-0.5,minor=True)
    plt.gca().set_yticks(np.arange(grid.shape[1]+1)-0.5,minor=True)
    plt.grid(which="minor", color="grey", linestyle='-', linewidth=2)
    plt.tick_params(which="both", bottom=False, left=False, labelbottom=False, labelleft=False)
    for edge, spine in plt.gca().spines.items():
        spine.set_visible(False)
    plt.imshow(grid)
    plt.show()

glider=np.array([[0,1,0],
                 [0,0,1],
                 [1,1,1]])

grid=np.zeros((8,8))
grid[0:3,0:3]=glider
    
show_grid(grid)

for i in range(1,20):
    plt.title(f"\nTurn {i}\n")
    grid=net_trained.postprocess(net_trained(net_trained.preprocess(grid,pad=True)),threshold=0.1)
    show_grid(grid)
```


![glider]({{site.baseurl}}/images/nn-vs-conway/glider.gif)



# Ručne vs. strojovo

Tu sú váhy našej natrénovanej neurónovej siete:


```python
net_trained.state_dict()
```

    OrderedDict([('network.0.weight',
                   tensor([[[[ 4.2063,  4.2074,  4.2075],
                             [ 4.2058,  0.2082,  4.2068],
                             [ 4.2066,  4.2060,  4.2068]]],
                  
                           [[[-3.6498, -3.6486, -3.6481],
                             [-3.6492, -3.4376, -3.6488],
                             [-3.6483, -3.6495, -3.6493]]]])),
                 ('network.0.bias', tensor([-15.2391,   8.6001])),
                 ('network.2.weight',
                   tensor([[[[-15.1833]],
                            [[-14.1411]]]])),
                 ('network.2.bias', tensor([6.7846]))])



Vidíme, že trénovaná sieť je úžasne podobná tej, ktorú sme vytvorili ručne. Nasledujúci graf zobrazuje, ako sa váhy siete vyvíjali počas tréningu. Všímajte si druhý kanál prvej vrstvy (oranžové krivka). Počas druhého skoku v presnosti všetky váhy v tejto časti siete skonveregovali k rovnakej hodnote, čo prelomilo symetriu medzi kanálmi a umožnilo sieti perfektne fitnúť dáta.


```python
keys=["max(perimeter of layer 1, channel 1)",
       "min(perimeter of layer 1, channel 1)",
       "center of layer 1, channel 1",
       "bias of layer 1, channel 1", 
       "max(perimeter of layer 1, channel 2)",
       "min(perimeter of layer 1, channel 2)",
       "center of layer 1, channel 2",
       "bias of layer 1, channel 2",
      "layer 2, channel 1 weight",
      "layer 2, channel 2 weight",
      "bias of layer 2"]

plots={k:[] for k in keys}

for record in logs:
    state_dict=record["state_dict"]
    
    weights=state_dict["network.0.weight"].squeeze()[0]
    perimeter=np.concatenate([weights[[0,2],:].ravel(),
                                weights[:,[0,2]].ravel()])
    plots[keys[0]].append(max(perimeter))
    plots[keys[1]].append(min(perimeter))
    plots[keys[2]].append(weights[1,1])
    plots[keys[3]].append(state_dict["network.0.bias"].squeeze()[0])
    
    weights=state_dict["network.0.weight"].squeeze()[1]
    perimeter=np.concatenate([weights[[0,2],:].ravel(),
                                weights[:,[0,2]].ravel()])
    plots[keys[4]].append(max(perimeter))
    plots[keys[5]].append(min(perimeter))
    plots[keys[6]].append(weights[1,1])
    plots[keys[7]].append(state_dict["network.0.bias"].squeeze()[1])
    
    plots[keys[8]].append(state_dict["network.2.weight"].squeeze()[0])
    plots[keys[9]].append(state_dict["network.2.weight"].squeeze()[1])
    plots[keys[10]].append(state_dict["network.2.bias"][0])

    
%matplotlib inline
plt.figure(figsize=(10,7))
for k,v in plots.items():
    if "perimeter" in k:
        linestyle="dashed"
    elif "bias" in k:
        linestyle='dotted'
    else:
        linestyle="solid"
    
    if "layer 1, channel 1" in k:
        color="red"
    elif "layer 1, channel 2" in k:
        color="orange"
    else:
        color="blue"
    plt.plot(v,color,label=k,linestyle=linestyle)

plt.legend(bbox_to_anchor=(1.08, 1), loc='upper left')    
plt.ylabel("weights")
plt.xlabel("epochs")
plt.xlim(0,60)

ax2=plt.gca().twinx()
color = 'tab:green'
ax2.set_ylabel('roc_auc, loss', color=color)
ax2.plot([i["roc_auc"] for i in logs], color=color, label= "roc_auc")
ax2.plot([i["loss"] for i in logs],"black",label="loss")
ax2.legend(bbox_to_anchor=(1.08, 0), loc='lower left')    
ax2.tick_params(axis='y', labelcolor=color)

plt.show()
```

<div class="lighter_background">
<img src="{{site.baseurl}}/images/nn-vs-conway/NN%20plays%20Conways%20Game%20of%20Life_19_0.png"
alt="Vývoj váh neurónovej siete počas tréningu."></div>


## Prečo Adam zlyhal?

Krátka odpoveď: Ešte neviem.

Dlhá odpoveď:

Myšlienka za neurónovými sieťami a gradientným zostupom je, že priestor parametrov je väčšinou mnohorozmerný (jeden rozmer za každý jeden parameter siete). V priestoroch s vysokým počtom rozmerov sú väčšinou lokálne minimá funkcií vzácne, pretože na to, aby bol nejaký bod minimom funkcie, musí byť minimom v každom jednom rozmere. Keď je tých rozmerov napr. 1000, tak je niečo také celkom nepravdepodobné, a gradientný zostup sa teda nemá kde zaseknúť.

Lenže v našom prípade má sieť len 23 parametrov, efektívne ešte menej. Pri použití Adama sa sieť naučila symetriu dát za menej ako 100 epoch Od tej chvíle boli všetky váhy po obvode konvolučného filtra prakticky identické, takže efektívne mala naša sieť len 9 parametrov. Obvyklé predpoklady o mnohorozmerných priestoroch tu už možno neplatia.

Môj odhad teda je, že Adam sa zasekol na nejakej plošine alebo v lokálnom minime a nevedel sa z neho dostať. Prišlo mi, že väčšinou nezvládol prelomiť symetriu medzi kanálmi. Ale prečo presne táto situácia nastala a prečo sa čistému gradientnému zostupu darilo lepšie sú dobré otázky, čo jasne dokazuje, že je naozaj možné sa niečo naučiť aj zo stupídnych nápadov.

Anglická verzia tohoto článku bola zverejnená 23.9.2020.