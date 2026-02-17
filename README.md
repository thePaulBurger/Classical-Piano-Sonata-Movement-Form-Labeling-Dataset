# Classical Piano Sonata Movement Form Labeling Dataset

This repository contains a CSV dataset of sonata form labels used during my Master's research. It was created to support structural form labelling of Classical piano sonatas and is based on annotations from established musicological sources.

## Contents

- `labels.csv` — The main dataset containing formal structure labels for selected piano sonatas.
- `label_sources.csv` — Documentation of the musicologists and analytical sources used in the labeling process.
- `audio_sources.csv` — Documentation of the audio recordings used.

## Background

The dataset focuses on piano sonatas composed during the Classical period (roughly 1730–1828), a time marked by formal discipline, structural clarity, and unambiguous section boundaries. These characteristics make the period especially well-suited for the study of automatic form recognition.

Each movement in the dataset is labeled according to analyses from published musicological sources (books, monographs, and theses), ensuring academic rigor and consistency. In cases where multiple sources provided different labels for the same movement, all variants are included.

## Composers Included

The dataset includes works by major Classical-era composers such as:

- Wolfgang Amadeus Mozart (1756–1791)
- Franz Joseph Haydn (1732–1809)
- Ludwig van Beethoven (1770–1827)
- Muzio Clementi (1752–1832)
- Carl Czerny (1791 - 1857)

Some works, such as those by Czerny and Clementi, may be considered late-Classical.

## Usage

The dataset is provided in standard CSV format and can be parsed using any common data analysis software (e.g., Python, R, Excel). No special installation is required.

## Citation

If you use this dataset in academic work, **please cite the original research and credit the dataset appropriately.** For now, please use:

P. A. D. Burger and J. P. Jacobs, "Automatic Self-Similarity Based Form Labelling of Classical-Period Piano Sonata Movements From Audio Recordings," in IEEE Transactions on Audio, Speech and Language Processing, vol. 33, pp. 3414-3427, Aug. 2025, doi: 10.1109/TASLPRO.2025.3594301.

```bibtex
@article{burger2025,
  author = {Burger, Paul Alwyn Desmond and Jacobs, J P},
  journal={IEEE Transactions on Audio, Speech and Language Processing}, 
  title={Automatic Self-Similarity Based Form Labelling of Classical-Period Piano Sonata Movements From Audio Recordings}, 
  year={2025},
  month = {Aug.},
  volume={33},
  pages={3414--3427},
  doi={10.1109/TASLPRO.2025.3594301}
}
```

or:

P. A. D. Burger and J. P. Jacobs, “Direct labelling of form of Classical-period piano sonata movements from audio recordings,” in Proc. 11th Int. Conf. on DLFM, ser. DLfM ’24. Stellenbosch, South Africa: Association for Computing Machinery, Jun. 27, 2024, pp. 1–5.

BibTeX entry:

```bibtex
@inproceedings{burger2024,
  author = {Burger, Paul Alwyn Desmond and Jacobs, J P},
  title = {Direct Labelling of Form of {Classical}-Period Piano Sonata Movements From Audio Recordings},
  year = {2024},
  isbn = {9798400717208},
  publisher = {Association for Computing Machinery},
  doi = {10.1145/3660570.3660577},
  booktitle = {Proc. 11th Int. Conf. on DLFM},
  pages = {1--5},
  month = {Jun. 27,},
  numpages = {5},
  address = {Stellenbosch, South Africa},
  series = {DLfM '24}
}
```

## License

This dataset is shared under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), which allows sharing and adaptation with appropriate credit.

---
