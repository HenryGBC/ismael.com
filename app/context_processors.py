from random import choice

rutas = ['capressa', 'paella','chupe','Ensalada-cesar','pasta_carbonara','pasta_marinera','pasticho','pollo_suiza',]

def ejemplo(request):

	return {'ruta1': choice(rutas)}
