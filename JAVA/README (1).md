# Débruitage d'image par analyse en composantes principales

**Projet-Bruitage** est une application de traitement d’images développée en Java avec JavaFX, qui permet de bruiter et débruiter des images en utilisant la méthode de l’Analyse en Composantes Principales (ACP). L’utilisateur peut personnaliser de nombreux paramètres et analyser les résultats avec des mesures de performance visuelles et quantitatives (PSNR, MSE).

## Fonctionnalités principales

- Traitement d'images en couleurs ou en niveaux de gris  
- Conversion automatique d’images couleur en niveaux de gris  
- Bruitage et débruitage selon la méthode ACP  
- Personnalisation complète des paramètres :  
  - Taille des patchs  
  - Taille des imagettes  
  - Type de seuillage  
  - Type de seuil  
  - Variance  
  - Méthode d’extraction  
  - Type de chevauchement  
  - Nombre d’itérations  
- Mesure de la performance du débruitage :  
  - Affichage de la PSNR (Peak Signal-to-Noise Ratio)  
  - Affichage du MSE (Mean Squared Error)  
- Visualisation et analyse :  
  - Ouverture de graphiques comparant les performances selon les différents paramètres possibles  
  - Affichage des images avec possibilité de rotation et d'agrandissement dans une nouvelle fenêtre

## Technologies utilisées

- Java  
- JavaFX pour l’interface graphique  
- Eclipse IDE (développement)  
- SceneBuilder (design de l’interface)  
- FXML pour la structure UI  

## Installation

### Installer Eclipse (si ce n'est pas déjà fait)

1. **Installer Eclipse**  
   - Rendez-vous sur le site officiel : https://www.eclipse.org/  
   - Téléchargez et installez **Eclipse IDE for Java Developers**

2. **Télécharger JavaFX SDK 21.0.7**  
   - Télécharger la version JavaFX : https://gluonhq.com/products/javafx/  
     - OS adapté à votre ordinateur (exemple : Linux)  
     - Type : SDK  
     - Version : 21.0.7  
     - Architecture : x64  
   - Décompressez-le dans un dossier de votre choix, par exemple :  
     ```
     /home/utilisateur/openjfx-21.0.7_linux-x64_bin-sdk
     ```

---

### Importer et configurer le projet dans Eclipse

1. **Importez le projet**  
   - Ouvrez Eclipse dans le dossier de votre choix  
   - Cliquez sur `File` > `Import...`  
   - Sélectionnez `General > Existing Projects into Workspace`  
   - Cochez la case `Select archive file:`  
   - Cliquez sur `Browse` et choisissez le dossier contenant le projet (`projet-image_NonExecutable.jar`)  
   - Cliquez sur `Finish`

2. **Ajouter JavaFX au projet**  
   - Clic droit sur le projet > `Java Build Path` > onglet `Libraries`  
   - Cliquez sur `Classpath`, puis sur `Add External JARs...`  
   - Naviguez jusqu’à :  
     ```
     /VOTRE_CHEMIN/javafx-sdk-21.0.7/lib
     ```  
   - Sélectionnez tous les fichiers `.jar` et cliquez sur `Apply and Close`

3. **Configurer les arguments VM pour JavaFX**  
   - Commencez par 'Run' une première fois le projet avec l’icône de la petite flèche verte sur la bannière en haut d’Eclipse  
   - Choisissez `Main-(default package)`, `OK` puis `Proceed`  
   - Vous aurez ces erreurs dans votre console :  
     
     `Error: Could not find or load main class Main  
     Caused by: java.lang.NoClassDefFoundError: javafx/application/Application` 
     
   - Puis clic droit sur le projet > `Run As` > `Run Configurations...`  
   - Allez sur `Arguments` et dans VM arguments, copiez :  

     `--module-path /VOTRE_CHEMIN/openjfx-21.0.7_linux-x64_bin-sdk/javafx-sdk-21.0.7/lib --add-modules javafx.controls,javafx.fxml,javafx.swing`

     **Remarques** :  
     - Remplacez `/VOTRE_CHEMIN/...` par le chemin réel vers votre répertoire JavaFX  
     - Remplacez `21.0.7` par la version que vous avez téléchargée (si elle est différente)

   - Cliquez sur `Apply` puis `Run`

4. **Exécutez le projet**  
   - Cliquez sur le bouton `Run` (flèche verte)  
   - L'application se lance avec l'interface graphique JavaFX

### Lancer le projet depuis le terminal

- Décompresser le .zip nommé : `renduExecutable_Groupe2.zip`
- À partir du terminal, allez dans le dossier où se trouve le `ProjetBruitage_Executable.jar` qui se trouve dans le .zip decompressé plus tôt
- Copiez la commande suivante dans le terminal :  

	`java -jar --module-path /VOTRE_CHEMIN/openjfx-21.0.7_linux-x64_bin-sdk/javafx-sdk-21.0.7/lib --add-modules javafx.controls,javafx.fxml,javafx.swing ProjetBruitage_Executable.jar`
	

**Bien penser à modifier `VOTRE_CHEMIN` par votre chemin réel vers votre répertoire JavaFX, ainsi que la version si nécessaire**

## Analyse graphique

L'application permet également d’afficher des graphes de performance, en allant sur le `Menu` (les trois traits horizontaux en haut à droite de chaque page), dans `Graphique`, pour comparer les différentes méthodes possibles de débruitage.

## Auteurs

Ce projet a été réalisé par le Groupe 2 :

- `Artigas Zoé`  
- `Bourgin Clément`  
- `Hariscain Enzo`  
- `Mialet Romane`  
- `Niang Mariam`

Dans le cadre du projet de traitement d’images (Java/JavaFX - ACP), CY Tech, année 2024–2025.

