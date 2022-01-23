# TP4

Notre Space Invaders a été programmer en language programmé objet.

Pour cela nous avons créé plusieurs classes.

La première classe est la classe "alien". Elle est initialisée avec ses coordonnées, son rayon et sa forme. Ensuite, il y a trois méthodes.
La méthode déplacement (qui vérifie que l'alien ne dépasse pas la fenêtre), la méthode tir (qui produit un tir partant de l'alien) et la méthode collision (qui gère la collision entre le vaisseau et l'alien).

La deuxième classe est la classe "tir_alien". Elle est initialisée avec ses coordonnées (qui dépendent de l'alien) et sa forme. Ensuite, il y a deux méthodes.
La méthode déplacement (qui vérifie que l'alien ne dépasse pas la fenêtre) et la méthode collision (qui gere la collision entre le tir de l'alien et le vaisseau).

La troisième classe est la classe "vaisseau". Elle est initialisée avec ses coordonnées (qui dépendent de l'alien), son chargement (en missile) et sa forme. Ensuite, il y a trois méthodes.
La méthode déplacement (qui vérifie que le vaisseau ne dépasse pas la fenêtre), la méthode tir (qui produit un tir partant du vaisseau) et la méthode Reload (qui permet au vaisseau de recharger son missile).

La quatrième classe est la classe "tir_vaisseau". Elle est initialisée avec ses coordonnées (qui dépendent du vaisseau) et sa forme. Ensuite, il y a deux méthodes.
La méthode déplacement (qui vérifie que l'alien ne dépasse pas la fenêtre) et la méthode collision (qui gère la collision entre le tir du vaisseau et l'alien).

La cinquième classe est la classe "groupe_aliens". Cette classe permet de créer un groupe d'aliens définis par le nombre de rang et de colonnes d'alien et par les tirs. Les tirs sont programmés pour partir de n'importe quel alien sur un temps aléatoire.

La sixieme classe est la classe "vie". Cette classe permet de calculer et d'afficher le nombre de vies du vaisseau. Le nombre de vies diminue en fonction du nombre de collisions avec les tirs des aliens.

La septieme classe est la classe "score". Cette classe permet de calculer et d'afficher le score. Le score augmente en fonction du nombre d'aliens touchés par les tirs du vaisseau.

La huitieme classe est la classe "protection". Cette classe permet de créer des groupes ("ilots") qui permettent de protéger le vaisseau des tirs des aliens.                            
