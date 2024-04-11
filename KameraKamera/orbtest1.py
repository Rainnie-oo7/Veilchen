import cv2  #O.R. B.  = Oriented fast, rotated briefly
import numpy as np

# Funktion zur Berechnung der Entfernung zwischen zwei Punkten
def berechne_entfernung(punkt1, punkt2):
    return np.linalg.norm(np.array(punkt1) - np.array(punkt2))

# Öffne die Kamera
kamera = cv2.VideoCapture(0)

# Lade das Bild des gemusterten Objekts
muster_bild = cv2.imread('muster_bild.jpg', cv2.IMREAD_GRAYSCALE)

# Initialisiere den ORB-Detektor
orb = cv2.ORB_create()

# Finde die Keypoints und Descriptoren mit ORB
kp1, des1 = orb.detectAndCompute(muster_bild, None)

while True:
    # Lies ein Bild von der Kamera
    ret, bild = kamera.read()

    # Konvertiere das Bild in Graustufen
    graustufen_bild = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)

    # Finde die Keypoints und Descriptoren des aktuellen Bildes mit ORB
    kp2, des2 = orb.detectAndCompute(graustufen_bild, None)

    # Initialisiere den Brute-Force Matcher
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Matche die Descriptoren des Musterbilds und des aktuellen Bilds
    matches = matcher.match(des1, des2)

    # Sortiere die Matches nach der Distanz
    matches = sorted(matches, key=lambda x: x.distance)

    # Extrahiere die besten Matches
    gute_matches = matches[:10]

    # Zeichne die Matches auf das Bild
    bild_mit_matches = cv2.drawMatches(muster_bild, kp1, bild, kp2, gute_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # Zeige das Bild mit den Matches an
    cv2.imshow('Mustererkennung', bild_mit_matches)

    # Warte auf eine Taste zum Beenden
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Freigebe Ressourcen und schließe das Fenster
kamera.release()
cv2.destroyAllWindows()
