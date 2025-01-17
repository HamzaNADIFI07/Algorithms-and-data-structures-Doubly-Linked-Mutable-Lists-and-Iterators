# Tp_itérateurs


## État du TP

Décrivez ici l'état d'avancement du TP.

## Réponses aux questions

Indiquez ici les réponses aux questions posées dans le TP. Vous
reprendrez le numéro de la section et le numéro de la question. Par
exemple pour répondre à la question 3 de la section 2.4 vous indiquerez :

### Première phase : la liste doublement chaînée

##### Q1:
La fonction `__print_without_iterator_reversed` est fait comme la première fonction fournie `__print_without_iterator_forward`, mais au lieu de commencer par la tete et puis avancer vers les autres **Cell** avec `.next`, on fait le contraire, on commence par la queue et on accède aux autres élements **Cell** avec `/prev`.

- **Le rendu du test 0 est comme suit:**

_Commande executée: `python3 test.py`_
```bash
1 2 3 4 
4 3 2 1 
```
### Deuxième phase : ajout des itérateurs

##### Q1:
Pour définir la classe `ListIterator`, on aura besoin des informations suivantes:
- `head`
- `tail`

```python
self.list=list
self.tail=list.tail
self.head=list.head
```

