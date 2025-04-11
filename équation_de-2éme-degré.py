A = float(input(veuillez saisir le coefficient A ici :))
B = float(input(veuillez saisir le coefficient B ici :))
C = float(input(veuillez saisir le coefficient C ici :))
import math
D = B**2 - 4 * A * C
if D == 0:
  print("l'équation a une seul solution est la suivant : ", -B/(2*A))
elif D > 0:
  print("l'équation a deux solution réelle : ",(-B-(math.sqrt(D)))/(2*A)," et ",(-B+(math.sqrt(D)))/(2*A))
else:
  print("l'équation a aucun solution réelle .")
