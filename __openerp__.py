# -*- coding: utf-8 -*-

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 08",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 08
===================================================

Le but de ce module est de montrer les différents types de champs disponible pour créer de nouveaux objets (modèle).

Cet exemple crée le nouveau modèle `tutoriel08`.

Ce module crée également le menu `Tutoriel` et le sous-menu `Tutoriel 08` pour pouvoir accèder à ce modèle.

""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',
  "depends" : ["openerp_tutoriel_07"],              # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
  "init_xml" : [],                                  # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],                                  # Liste des fichiers XML à installer pour charger les données de démonstration

  "update_xml" : ["infosaone_tutoriel08_view.xml"], # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)

  "installable": True,         # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False              # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}

