---
title: 'Intro to NGS processing'
author: James A. Fellows Yates
date: 2021-08-17
autosize: true
output: 
  revealjs::revealjs_presentation:
    template: assets/modifiedTemplate.html
    transition: 'slide'
    reveal_options:
      slideNumber: true
      progress: true
      controls: false
css: slides.css
---

# Who am I?

- Education
  - B.Sc. Bioarchaeology (University of York, UK)
  - M.Sc. Naturwissenschaftliches Archäologie (University of Tübingen, DE)
  - Ph.D. Archaeogenetics (MPI-SHH / MPI-EVA, DE)

- Experience
  - Number of genetics classes taken: 0
  - Number of bioinformatics classes taken: 0

<div>
  <img style="vertical-align:middle" src="https://openmoji.org/data/color/svg/E040.svg" width=50>
  <img style="vertical-align:middle" src="https://openmoji.org/data/color/svg/E045.svg" width=50>
  <span style=""> @jfy133</span>
</div>

# Today we will 

1. Introduce what DNA sequencing is
2. Explain how Illumina **NGS** sequencing **data** is generated
3. How to evaluating NGS data [Practical]

# Introduction DNA {data-background="assets/img/IMPRS_SHH_SummerSchool_2021-SectionSlide.jpg" style="color:white;text-align:left" class="center"}

# What is DNA?

> Deoxyribonucleic acid (/diːˈɒksɪˌraɪboʊnjuːˌkliːɪk, -ˌkleɪ-/ (DNA) is a molecule composed of two polynucleotide chains that coil around each other to form a double helix carrying genetic instructions for the development, functioning, growth and reproduction of all known organisms and many viruses. - [Wikipedia](https://en.wikipedia.org/wiki/DNA)

# What is DNA?


<a title="Zephyris, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://en.wikipedia.org/wiki/File:DNA_Structure%2BKey%2BLabelled.pn_NoBB.png"><img width="512" alt="Structure ADN" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/DNA_Structure%2BKey%2BLabelled.pn_NoBB.png/1024px-DNA_Structure%2BKey%2BLabelled.pn_NoBB.png"></a>

# What is DNA?

<a title="Pradana Aumars, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Structure_ADN.png"><img width="256" alt="Structure ADN" src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Structure_ADN.png"></a>

# The rules

- Four nucleotides
  - Pyrimidines: `C`ytosine, `T`hymine
  - Purines: `G`uanine `A`denine & 
- Base pairing: one pyrimidine with one purine
  - `C` with `G` (think: CGI)
  - `A` to `T` (think: AT-AT walker)
- Complementary
  - `C` on one strand, `G` on the other (or _v.v._)
  - `A` on one strand, `T` on the other (or _v.v._)

# The rules

- Make copy of a DNA strand with a _polymerase_
  - Unwind the DNA
  - Separate the strands
  - Make new strand: find a `C`, get new `G` (etc)

<p style="align:center">
  <a title="I, Madprime, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:DNA_replication_split.svg"><img width="256" alt="DNA replication split" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/DNA_replication_split.svg/256px-DNA_replication_split.svg.png"></a>
</p>
  
# How do we get DNA?

<a title="CNX OpenStax, CC BY 4.0 &lt;https://creativecommons.org/licenses/by/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Figure_17_01_02.jpg"><img width="512" alt="Figure 17 01 02" src="https://upload.wikimedia.org/wikipedia/commons/9/9d/Figure_17_01_02.jpg"></a>

# Introduction to DNA Sequencing {data-background="assets/img/IMPRS_SHH_SummerSchool_2021-SectionSlide.jpg" style="color:white;text-align:left" class="center"}

# What is Sequencing?

Converting the chemical nucleotides of a DNA molecule 

to 

```ACTG``` on your computer screen

<p align="center">
<img src="https://openmoji.org/data/color/svg/1F9EC.svg" width="20%">
<img src="https://openmoji.org/data/color/svg/27A1.svg" width="20%">
<img src="https://openmoji.org/data/color/svg/1F5A5.svg" width="20%">
</p>

# Historically

- Sanger sequencing

<a title="Estevezj, CC BY-SA 3.0 &lt;https://creativecommons.org/licenses/by-sa/3.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Sanger-sequencing.svg"><img width="512" alt="Sanger-sequencing" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Sanger-sequencing.svg/512px-Sanger-sequencing.svg.png"></a>

- Sanger sequencing
  - Separate strands, add primer (starting point)
  - Add random mix of nucleotides, but some with special 'terminators'
  - Pass through size-filtering, read order of terminators

# Pros and cons of Sanger Sequencing

- Pros
  - More precise (less errors)
  - Longer reads
- Cons
  - Resource heavy: lot of input DNA
  - Slow: one fragment at a time

# What is NGS?

- NGS: Next Generation Sequencing
  - MASSIVELY multiplexed! 
  - Sequence millions and millions and millions and millions of DNA reads at once!

> Not really 'next' anymore, consider it more 'second' generation (see: Nanopore)

<div>
  <span style="">Market leader:</span>
  <img style="vertical-align:middle" src="https://assets.illumina.com/content/dam/illumina-common/logo/illumina-full_logo-RGB-black.svg" width=200>
</div>

# How does it work?

Basically same concept, but 



