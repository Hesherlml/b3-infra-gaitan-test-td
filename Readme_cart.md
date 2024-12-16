

# User Stories pour la classe `Cart`

####################################
#  Ajouter de produit au panier    #
####################################

En tant que utilisateur,  
Je veux pouvoir ajouter des produits au panier en choisissant la quantité,  
Afin que je puisse acheter plusieurs articles du même produit et gérer mon panier d'achat.

----- Critères d'acceptation -------

Si la quantité demandée dépasse le stock disponible, une exception est levée avec un message stock épuisé.
Si le produit est déjà dans le panier, la quantité doit être mise à jour a chaque ajout
Les mises à jour de la quantité doit etre en temps réel

####################################
#        Retrait de Porduit        #
####################################

En tant que utilisateur,
Je veux pouvoir retirer des produits du panier,
Afin que je puisse supprimer des articles que je ne souhaite plus prendre.

----Critères d'acceptation-------

Si le produit est dans le panier, il doit être supprimé.
Si le produit n'est pas dans le panier, un message indiquant aucun produit sélectioné.


####################################
#        Contenu du panier         #
####################################

En tant que utilisateur du système,
Je veux pouvoir afficher le contenu du panier,
Afin que je puisse vérifier la liste des produits, leurs quantités et le montant total avant de finaliser mon achat.

------ Critères d'acceptation -------

Si le panier est vide, un message  " panier est vide".
Si des produits est dans le panier, le nom de produits avec la quantité et le montant de chaque  article, et le total HT ou TTC doit etre affiché.



