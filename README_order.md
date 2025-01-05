############################# User Stories pour la classe Order ################################


  ############################## Création d'une commande #############################
    En tant qu'utilisateur,                                                          #
    Je veux créer une commande basée sur les articles sélectionné dans mon panier,   #
    Afin de pouvoir finaliser mes achats.                                            #
                                                                                     #
         ------ Critères d’acceptation ------                                        #
                                                                                     #
    Le montant total de la commande doit être correctement calculé.                  #
    La commande doit être créée uniquement si le panier contient des articles.       #
    Les articles de la commande doivent correspondre à ceux du panier.               #
                                                                                     #
  ####################################################################################

  ############################################################# Passer une commande ####################################################################
                                                                                                                                                       #
    En tant qu'utilisateur,                                                                                                                            #
    Je veux finaliser ma commande,                                                                                                                     #
    Afin de mettre à jour les stocks des produits commandés et recevoir une confirmation de mon achat.                                                 #
                                                                                                                                                       #
         ------ Critères d’acceptation ------                                                                                                          #
                                                                                                                                                       #
    Lorsque la commande est confirmée via la méthode place_order, les stocks des produits doivent être réduits selon les quantités commandées.         #
    Si la commande est validée avec succès, le système doit retourner un message au format suivant : « Order placed successfully! Total: <total> € ».  #
    Si la commande ne peut pas être validée, les stocks des produits ne doivent subir aucune modification.                                             #
                                                                                                                                                       #
  ######################################################################################################################################################

  #################################### Consulter les détails d'une commande #######################################
                                                                                                                  #
    En tant qu'utilisateur,                                                                                       #
    Je veux consulter les détails de ma commande,                                                                 #
    Afin de vérifier les articles commandés et leur coût total.                                                   #
                                                                                                                  #
         ------ Critères d’acceptation ------                                                                     #
                                                                                                                  #
    Les détails de la commande doivent inclure une liste des articles, au format : <product.name> x <quantity>.   #
    Le coût total doit être affiché à la fin, au format : « Total : <total> € ».                                  #
    Le résultat doit être clair, lisible et correctement structuré.                                               #
                                                                                                                  #
  #################################################################################################################