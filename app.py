import plotly.express as px
import pandas as pd
# data importée
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# vente par region
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')

# Vente par produit
figure = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure.write_html('ventes-par-produit.html')

# CA par produit
données['ca'] = données['prix'] * données['qte']

figure = px.pie(données, values='ca', names='produit', title="Chiffre d'affaire vendue par produit")
figure.write_html('ca-par-produit.html')

print('Graphiques générés avec succès !')
