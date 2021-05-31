# Graph Theory Project

## Część analityczna:
[Notebook](project.ipynb)
## Część programistyczna:
### Input format:
Lista sąsiedztwa z wagami: </br>
###### Przykład:
```
[
[[1, 8], [4, 3]],
[[2, 9]],
[[4, 7], [5, 2]],
[[5, 5]],
[[2, 7], [3, 4]],
[]
]
```
Albo macierz sąsiedztwa z wagami:
###### Przykład:
```
[
[0, 8, 0, 0, 3, 0],
[0, 0, 9, 0, 0, 0],
[0, 0, 0, 0, 7, 2],
[0, 0, 0, 0, 0, 5],
[0, 0, 7, 4, 0, 0],
[0, 0, 0, 0, 0, 0]
]
```

Listę lub macierz należy umieścić w pliku w formacie JSON,
a następnie w pliku ```main.py``` wstawić ścieżkę do pliku
do zmiennej ```path```

### Zastosowanie
Algorytm Forda-Fulkersona jest stosowany w szeroko pojętej logistyce.
Np. przepływ wody w rurach.