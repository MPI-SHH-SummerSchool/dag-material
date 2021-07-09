---
title: 'Intro to NGS processing'
author: James A. Fellows Yates
autosize: true
output: 
  revealjs::revealjs_presentation:
    transition: 'slide'
    reveal_options:
      slideNumber: true
      progress: true
      controls: false
      
css: slides.css
---

# Intro to NGS processing

# Who am I?

# Who am I?


- Education
  - B.Sc. Bioarchaeology (University of York, UK)
  - M.Sc. Naturwissenschaftliches Archäologie (University of Tübingen, DE)
  - Ph.D. Archaeogenetics (MPI-SHH / MPI-EVA, DE)

- Experience
  - Number of genetics classes taken: 0
  - Number of bioinformatics classes taken: 0

<p align="center">
<img src="https://openmoji.org/data/color/svg/E040.svg" width=50><img src="https://openmoji.org/data/color/svg/E045.svg" width=50> @jfy133
</p>

# Today we will 

1. Introduce what NGS sequencing is
2. How do you generate Illumina NGS sequencing **data**
3. [Practical] How to evaluating NGS data 

# What is Sequencing?

Converting the chemical nucleotides of a DNA molecule 

to 

```ACTG``` on your computer screen

<p align="center">
<img src="https://openmoji.org/data/color/svg/1F9EC.svg" width="20%">
<img src="https://openmoji.org/data/color/svg/27A1.svg" width="20%">
<img src="https://openmoji.org/data/color/svg/1F5A5.svg" width="20%">
</p>


# What is NGS?

NGS: Next Generation Sequencing

- MASSIVELY multiplexed! 
- Sequence millions and millions and millions and millions of DNA reads at once!

> Not really 'next' anymore, consider it more 'second' generation (see: Nanopore)

Market leader: <img src="https://assets.illumina.com/content/dam/illumina-common/logo/illumina-full_logo-RGB-black.svg" width="20%">


# How does it work?

```bash
cat 1.fastq 2.fastq
```


