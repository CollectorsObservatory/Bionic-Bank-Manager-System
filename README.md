Le fichier BBM-final contient la version la plus récente du programme , les autres fichiers sont ici juste pour montrer l'avancement du projet au fil du temps.
# Bionic Bank Manager

Le Bionic Bank Manager est un système de gestion de comptes bancaires simplifié qui permet aux utilisateurs de gérer leurs comptes, de réaliser des transactions et de suivre les détails de leur compte.

## Fonctionnalités principales

1. **Chargement des comptes** : Au démarrage, le système charge les informations des comptes à partir d'un fichier `accounts.txt`.
2. **Création de compte** : Permet aux utilisateurs de créer un nouveau compte.
3. **Dépôt d'argent** : Les utilisateurs peuvent déposer de l'argent dans leurs comptes.
4. **Retrait d'argent** : Les utilisateurs peuvent retirer de l'argent de leurs comptes.
5. **Transfert d'argent** : Permet le transfert d'argent entre deux comptes.
6. **Obtenir des informations de compte** : Les utilisateurs peuvent obtenir des détails sur un compte spécifique.
7. **Sauvegarde des comptes** : À la fin de chaque transaction, les informations des comptes sont sauvegardées dans le fichier `accounts.txt`.

## Détails techniques

### Classes

- **BionicBankManager** : C'est le cœur du système qui gère toutes les fonctionnalités liées au compte.

### Méthodes principales

- `load_accounts()`: Charge les informations des comptes à partir du fichier `accounts.txt`.
- `create_account(holder_name, gender, balance)`: Crée un nouveau compte.
- `save_accounts()`: Sauvegarde les informations des comptes dans le fichier `accounts.txt`.
- `deposit_money(account_number, amount)`: Permet de déposer de l'argent.
- `withdraw_money(account_number, amount)`: Permet de retirer de l'argent.
- `transfer_money(from_account, to_account, amount)`: Gère le transfert d'argent entre comptes.
- `get_account_info(account_number)`: Retourne les informations d'un compte spécifique.
- `get_account_info_by_name(holder_name)`: Retourne les informations d'un compte basé sur le nom du titulaire.

### Démarrage du programme

Le programme peut être démarré en exécutant le script. Une interface utilisateur graphique, `BBM_GUI`, est utilisée pour interagir avec le `BionicBankManager`.

---

N'hésitez pas à me dire si vous souhaitez apporter des modifications ou ajouter des informations supplémentaires.
