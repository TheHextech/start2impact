# General info

Questo progetto consiste in alcuni script per la gestione di vari tipi di file, con i quali metterai in pratica le tue competenze di Python e NumPy.

Non è **detto che tu conosca già tutti i costrutti e le librerie che dovrai usare per portare a termine il progetto: fa parte del gioco!**

---

## Step 1
Inizia creando, in un notebook, uno script Python che_ iteri in ordine alfabetico sui file della cartella *files*_ e, a seconda del tipo (audio, documento, immagine), li sposti nella relativa sottocartella (qui sotto trovi un esempio). Se la sottocartella non esiste, il tuo script dovrà crearla automaticamente.

Durante il ciclo, lo script deve stampare le informazioni dei file: nome, tipo e dimensione in byte. Questo è l'output desiderato:

	bw type:image size:94926B
	ciao type:doc size:12B
	daffodil type:image size:24657B
	eclipse type:image size:64243B
	pippo type:doc size:8299B
	song1 type:audio size:1087849B
	song2 type:audio size:764176B
	trump type:image size:10195B

Oltre a stamparne le informazioni via via che li sposti, tieni traccia dei file creando un documento _recap.csv_ con le stesse informazioni. Trovi un esempio in questa cartella.

La struttura finale della cartella files dovrà essere:

```
    - files            
        - audio
            - song1.mp3
            - song2.mp3
        - docs
            - ciao.txt
            - pippo.odt
        - images
            - bw.png
            - daffodil.jpg
            - eclipse.png
            - trump.jpeg    
        - recap.csv

```

Commenta il codice con i passaggi che fai. Questo vale anche per i prossimi Step.

**Attenzione**: lo script, ogni volta che viene lanciato per spostare nuovi file, deve _aggiornare_ (e non sovrascrivere) le sottocartelle e il file di recap. Per controllare che tutto funzioni correttamente, puoi aggiungere altri file alla cartella files e fare un test; oppure, puoi dividere gli 8 file originali in due gruppi e lasciarne uno per il test.

**Consiglio**: puoi usare le librerie _os_, _shutil_ e _csv_.

Quindi, riassumendo, bisogna iterare in ordine alfabetico sui files della cartella files:
- A seconda del tipo, spostarli nella sottocartella relativa (se questa non esiste crearla automaticamente)
- stampare le info dei file e conservarle in un file recap.csv
- lo script lanciato deve spostare nuovi file, non solo quelli di esempio, aggiornando le sottocartelle e il file di recap

---

## Step 2
Inserisci lo script che hai creato in un piccolo eseguibile (chiamalo _addfile.py_ e posizionalo in questa cartella, a fianco del notebook) dotato di _interfaccia a linea di comando_ (CLI).

Lo scopo dell'eseguibile è spostare un _singolo_ file (che si trova nella cartella files) nella sottocartella di competenza, aggiornando il recap.

L'interfaccia dell'eseguibile ha come unico argomento (obbligatorio) il nome del file da spostare (comprensivo di formato, es: 'trump.jpeg'). Nel caso in cui il file passato come argomento non esista, l'interfaccia deve comunicarlo all'utente.

**Consiglio**: oltre alle precedenti, puoi usare le librerie _sys_ e _argparse_.

---
## Step 3

Una immagine in scala di grigio ha un solo livello di colore, una RGB ne ha 3, una RGBA 4 (l'ultimo è detto canale _alpha_).

Il modulo _Image_ della libreria _PIL_ permette di caricare un'immagine, che può essere trasformata in un array NumPy attraverso la funzione _np.array_. A partire da tale array, è possibile capire se l'immagine caricata è in scala di grigio, RGB o RGBA.

Aggiungi al notebook dello Step 1 uno script che iteri sulla sottocartella _images_ e costruisca una tabella riassuntiva come questa (prodotta con la libreria _tabulate_):

Oltre al nome del file, la tabella riporta:

-   altezza dell'immagine, in pixel
-   larghezza dell'immagine, in pixel
-   se l'immagine è in scala di grigio, la colonna _grayscale_ indica la media dei valori dell'unico livello di colore
-   se l'immagine è a colori, le altre colonne indicano la media dei valori di ogni livello di colore.

---

**Corretto in data 2021-12-07.  Superato con 500/500**.