# Colors Helper — archivé

[🇫🇷](LISEZMOI.md) · [🇬🇧](README.md)


> **Ce dépôt est archivé depuis le 2026-06-28.** Utilisez plutôt l'un de ces deux :
>
> - **Données palette (en ligne, navigables) :** <https://harchaoui.org/warith/colors/>
>   — base, émotions, concepts et psychologie des couleurs, toutes
>   indexées sur le même jeu hexadécimal Apple-inspired curaté.
>
> - **Code (moderne, maintenu) :** <https://github.com/warith-harchaoui/front>
>   — précisément le skill `front-colors`, qui héberge désormais :
>   - L'audit de contraste WCAG avec suggestions de correction par
>     voisin OKLCH (`front-colors/scripts/audit_contrast.py`)
>   - La simulation des déficiences de vision des couleurs — protanopie
>     / deutéranopie / tritanopie, matrices Machado et al. 2009
>     (`front-colors/scripts/simulate_cvd.py`)
>   - Les primitives partagées — sRGB ↔ linéaire, hex ↔ RGB, OKLab /
>     OKLCH, luminance et contraste WCAG, éclaircissement / assombrissement
>     perceptuels `lighten` / `darken`, accesseurs de palette, classe
>     `Color` (`front-colors/scripts/_colors.py`)
>   - La CSV palette unifiée — une ligne par couleur, projections
>     sémantiques (Base / Émotion / Concepts / Psychologie±) en colonnes
>     (`front-colors/references/palette.csv`)
>
> Plus aucun changement n'atterrira ici. Le paquet n'est *pas* sur
> PyPI ; les instructions d'installation historiques plus bas ne sont
> conservées que pour les utilisateurs dont les scripts ont déjà
> épinglé l'ancien hash de commit.

## Ce que ce dépôt était

`Colors Helper` était une petite librairie Python livrant une palette
curatée (couleurs système Apple + leurs déclinaisons claires dérivées
via le [Tint & Shade Generator](https://maketintsandshades.com)) et
quelques fonctions utilitaires pour la conversion hex / RGB et la
gestion de la CSV palette.

Pourquoi c'est archivé : la math y était naïve (un décalage de `+70`
par canal RGB n'est pas un éclaircissement perceptuel), le nom de
colonne CSV avait dérivé par rapport au fichier en ligne (`"Hex Code"`
côté code vs `Hexcode` côté CSV publiée), il manquait les primitives
contraste / OKLCH / CVD, et la dépendance git sur `os-helper` rendait
le paquet difficile à réutiliser. Toutes ces lacunes sont correctement
adressées à l'intérieur de `front-colors`.

La palette curatée Apple, elle, garde toute sa valeur et continue de
vivre sur <https://harchaoui.org/warith/colors/> et à l'intérieur de
[`front-colors/references/palette.csv`](https://github.com/warith-harchaoui/front/blob/main/front-colors/references/palette.csv).

## Installation historique (ne pas utiliser pour de nouveaux travaux)

```bash
pip install --force-reinstall --no-cache-dir \
    git+https://github.com/warith-harchaoui/colors-helper.git@main
```

## Auteur

[Warith HARCHAOUI](https://www.linkedin.com/in/warith-harchaoui/)
