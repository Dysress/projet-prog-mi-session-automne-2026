"""Lance l'autocorrecteur sur fusee.py.

Exécutez simplement ce fichier : les tests de tests.json sont appliqués
à fusee.py et le rapport s'affiche à l'écran.
"""
import os
import sys

# Se placer dans le dossier de ce fichier pour trouver fusee.py,
# tests.json et les modules compilés, peu importe d'où on lance le script.
DOSSIER = os.path.dirname(os.path.abspath(__file__))
os.chdir(DOSSIER)
sys.path.insert(0, DOSSIER)

try:
    import PyCorrecteur
except ImportError:
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"Impossible de charger PyCorrecteur pour Python {version}.")
    print("Vérifiez que vous utilisez la version de Python demandée dans le cours.")
    sys.exit(1)

if __name__ == "__main__":
    sys.exit(PyCorrecteur.main(["--tests", "tests.json", "--screen", "--output", "resultats.md"]))
