# taochen at SemEval-2022 Task 5: Multimodal Multitask Learning and Ensemble Learning

This repository contains codes and data for SemEval task 5: Multimedia Automatic Misogyny Identification (MAMI) challenge.

## Usage

### Dataset

Clone the repository to your desired directory.
Download the dataset from [data.zip](https://drive.google.com/file/d/13bK7dlWv59ubY15zjOS-LmgBWsomAiiQ/view?usp=sharing) and unzip the files to your home directory (you may specify a different directory by modifying a configuration file).

### Prerequisite

1. Create two virtual environments named `baseline` and `mmf` with `conda create`.
2. Install their corresponding package requirements (`baseline_requirements.txt` and `mmf_requirements.txt`, respectively).\
The two steps can be jointly achieved in one command. For example, for the `mmf` environment:

```bash
conda create --name mmf --file mmf_requirements.txt
```

### Setup for feature extraction
1. Under your home directory, run the below bash command.
```bash
git clone https://gitlab.com/vedanuj/vqa-maskrcnn-benchmark
```
2. Go to the `vqa-maskrcnn-benchmark` folder and run the following commands in order
```bash
rm -rf build
```
```bash
nvcc -V
```
```bash
python setup.py build develop
```

## Reproducibility
Please refer to the following .ipynb notebooks (in sequence) for reproduce results.
1. data_augmentation.ipynb
2. ensemble_preparation.ipynb
3. ensemble_learning.ipynb

## License

```bibtex
@inproceedings{tao-kim-2022-taochen,
    title = "taochen at {S}em{E}val-2022 Task 5: Multimodal Multitask Learning and Ensemble Learning",
    author = "Tao, Chen  and
      Kim, Jung-jae",
    booktitle = "Proceedings of the 16th International Workshop on Semantic Evaluation (SemEval-2022)",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.semeval-1.89",
    doi = "10.18653/v1/2022.semeval-1.89",
    pages = "648--653",
}
```
