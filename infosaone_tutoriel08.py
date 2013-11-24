# -*- coding: utf-8 -*-


from osv import osv
from osv import fields

# Doc : http://doc.openerp.com/v6.1/developer/03_modules_2.html


#Remarque : Le nom de la class n'a pas d'importance, mais par convention, mettre le même que le nom du modèle
class infosaone_tutoriel08(osv.osv):

    #Nom du modèle à créer
    _name='infosaone.tutoriel08'


    # Exemple de fonction permettant d'alimenter la liste de choix 'extra07'
    def _get_selection(self, cursor, user_id, context=None):
        return (
           ('choice1', 'Choix 1'),
           ('choice2', 'Choix 2'),
           ('choice3', 'Choix 3'))
        
    # Exemple de fonction pour calculer le champ 'extra08'
    def _calcul_extra08(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for id in ids:
            myself = self.browse(cr, uid, id, context=context)
            res = 0.0
            if myself:
                res = myself.extra02 * myself.age
                result[id] = res

        return result

    _columns={
            'name':fields.char("Name",size=128),
            'age':fields.integer("Age"),
            'taille':fields.integer("Taille"),
            'extra01':fields.boolean("boolean"),
            'extra02':fields.float("float",digits=(8,2)),
            'extra03':fields.text("text"),
            'extra04':fields.date("date"),
            'extra05':fields.datetime("datetime"),
            'extra06':fields.selection((('c1','Choix 1'), ('c2','Choix 2'), ('c3','Choix 3')),'selection'),
            'extra07':fields.selection(_get_selection,"selection avec fonction"),
            'extra08':fields.function( _calcul_extra08, method=True, type='float', string='Champ calculé', store=True, readonly=True),
            'image': fields.binary('Image', required=True),
            'image_filename': fields.char('Image filename', size=500),
            'lafamille': fields.many2many('infosaone.famille', id1='famille_id', id2='lafamille_id'      , string='Famille')
    }



infosaone_tutoriel08()



