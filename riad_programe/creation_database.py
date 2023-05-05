import sqlite3
from datetime import date
# employer
def ajouter_employer(name ,solde):
   conn = sqlite3.connect('attelier_riad.db')
   name = name.upper()
   name = name.strip()
   if(name !='' and solde>=0):
      conn.execute("insert into employer (namee, soldee) VALUES(?, ?)", (name, solde))
      conn.commit()
      conn.close()
   else:
      print('there is a probleme in the information given ')

def delete_employer(name):
   conn = sqlite3.connect('attelier_riad.db')
   name = name.upper()
   name = name.strip()
   if(name !=''):
      conn.execute("delete form employer where namee = (?)", (name))
      conn.commit()
      conn.close()
   else:
      print('there is a probleme in the information given ')
def afficher_employes():
   conn = sqlite3.connect('attelier_riad.db')
   cursor=conn.cursor()
   query="SELECT * FROM employer"
   cursor.execute(query)
   for row in cursor:
      print(row)


# produit
def ajouter_produit(namep,qantite,prix_init):
   conn = sqlite3.connect('attelier_riad.db')
   namep = namep.upper()
   namep = namep.strip()

   qantite = int(qantite)
   prix_init = int(prix_init)
   if (namep != "" and qantite >= 0 and prix_init>=0):
      conn.execute("insert into produit (namep, qantite,prix_init) VALUES(?, ?,?)", (namep, qantite,prix_init))
      conn.commit()
      conn.close()
   else:
      print('there is a probleme in the information given ')
def   list_produits():
   conn = sqlite3.connect('attelier_riad.db')
   cursor=conn.cursor()
   query="SELECT * FROM produit"
   cursor.execute(query)
   return cursor



# client
def ajouter_client(namec,tel,soldec):
   conn = sqlite3.connect('attelier_riad.db')
   namec = namec.upper()
   namec = namec.strip()

   if(namec !='' and soldec>=0):
      conn.execute("insert into client (namec, tel,soldec) VALUES(?,?,?)", (namec, tel,soldec))
      conn.commit()
      conn.close()
   else:
      print('there is a probleme in the information given ')
def afficher_client():
   conn = sqlite3.connect('attelier_riad.db')
   cursor=conn.cursor()
   query="SELECT * FROM client"
   cursor.execute(query)
   for row in cursor:
      print(row)


#fabrication
def fabrication(prod,empl,qte,montat_unite,date):
   conn = sqlite3.connect('attelier_riad.db')
   cursor = conn.cursor()
   if ( montat_unite > 0 and qte>0):
      # add fabrication row

      cursor.execute("insert into fabrication  (empl, prod,montant_fab_unite,qte,date) VALUES(?,?,?,?,?)", (empl,prod,montat_unite,qte,date))

      # modifier article produit
      cursor = conn.cursor()
      column_name = 'qantite'
      table_name = 'produit'
      prod_id = prod
      query = f'SELECT {column_name} FROM {table_name} WHERE code_produit = ?'
      cursor.execute(query, (prod_id,))
      rows = cursor.fetchall()
      for row in rows:
         print(row[0])
         qte_total = row[0]
      print("befor",qte_total)
      qte_total=qte_total+qte
      print("after",qte_total)
      query = f'UPDATE {table_name} SET {column_name} = ? WHERE code_produit = ?'
      cursor.execute(query, (qte_total, prod_id))

      # modifier article employer
      cursor = conn.cursor()
      column_name = 'soldee'
      table_name = 'employer'
      empl_id = empl
      query = f'SELECT {column_name} FROM {table_name} WHERE id_employer = ?'
      cursor.execute(query, (empl_id,))
      rows = cursor.fetchall()
      for row in rows:
         print(row[0])
         old_solde = row[0]
      print("old", old_solde)
      new_solde = old_solde+ (qte*montat_unite)

      print("new", new_solde)
      query = f'UPDATE {table_name} SET {column_name} = ? WHERE id_employer = ?'
      cursor.execute(query, (new_solde, empl_id))

      #THE END
      conn.commit()
      conn.close()
   else:
      print('there is a probleme in the information given ')


#Employer
def Versment_Employer(empl,montant,date):
   pass

