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

<a title="Pradana Aumars, CC BY-SA 4.0 &lt;https://creativecommons.org/licenses/by-sa/4.0&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Structure_ADN.png"><img width="512" alt="Structure ADN" src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Structure_ADN.png"></a>

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
  <a title="I, Madprime, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:DNA_replication_split.svg"><img width="200" alt="DNA replication split" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/DNA_replication_split.svg/256px-DNA_replication_split.svg.png"></a>
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

- Separate strands, add primer (starting point)
- Add mix of nucleotides, some with special 'terminators'
- Pass through size-filtering, read order of terminators

# Pros and cons of Sanger Sequencing

- Pros
  - More precise (less errors)
  - Longer reads
- Cons
  - Resource heavy: lot of input DNA
  - Slow: one. fragment. at. a. time.

# What is NGS?

- NGS: Next Generation Sequencing
  - MASSIVELY multiplexed! 
  - Sequence millions and even billions of DNA reads at once!

> Not really 'next' anymore, consider it more 'second' generation (see: Nanopore)

# What is NGS?

<iframe src='https://gfycat.com/ifr/BlackGreedyAurochs' frameborder='0' scrolling='no' allowfullscreen width='640' height='412'></iframe><p> <a style="font-size:12px" href="https://gfycat.com/blackgreedyaurochs">via Gfycat</a></p>

# What is NGS?

<div>
  <span style="">Market leader:</span>
  <img style="vertical-align:middle" src="https://assets.illumina.com/content/dam/illumina-common/logo/illumina-full_logo-RGB-black.svg" width=200>
</div>

![](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Illumina_HiSeq_2500.jpg)

<a title="Konrad Förstner, CC0, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Illumina_HiSeq_2500.jpg"><img width="512" alt="Illumina HiSeq 2500" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Illumina_HiSeq_2500.jpg/512px-Illumina_HiSeq_2500.jpg"></a>

(Others: Roche 454, PacBio, IonTorrent etc.)

# How does it work?

Basically same concept, but with pretty pictures!

i.e. attach flouresent nucleotides, one colour per `A` `C` `G` `T`

<p style="color:red"><b>A</b></p>
<p style="color:blue"><b>G</b></p>
<p style="color:green"><b>T</b></p>
<p style="color:gold"><b>C</b></p>

Fire a lazer and take a picture!

# Where does this happen?

Flow cell (map)

Has Lawn

# Where does this happen?

But how do you get your DNA to attach to the lawn?

Libray construction = adapters+ indexes

# Sequencing-by-synthesis

Once attached, make lots of copies (clustering)

# Sequencing-by-synthesis

Separate, add primer

# Sequencing-by-synthesis

Add the flouresnt nucleotides, only complement will bind

# Sequencing-by-synthesis

Fire the lazer, and take a photo

# Rinse and repeat!

# Improving quality

Throughout limits

Paired end

# Paired end sequencing

Once end, bendover, attach other end (turnaround) and start from the _end_ of the molecule

# Cons of NGS sequencing

- less accurate (laser/photo can get wrong)
- chemistry limits (DNA strands gets old through heat cycling for denautring; dirty environment from suboptiomal wash steps etc.) mean short reads (compensated by volume)




