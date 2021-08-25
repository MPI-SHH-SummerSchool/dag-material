## MPI-SHH Summer School: Doorway to Human History<br/> Phylogenetics Workshop<br/> 19 Aug. 2021

### Megan Michel<br/> (megan_michel@eva.mpg.de, @megan_michel on Mattermost)

Together we will work through some exercises to gain familiarity with phylogenetic methods used in analyses of ancient pathogen single nucleotide polymorphism (SNP) data. We will be analyzing a dataset of genome-wide SNP data from ancient and modern *Yersinia pestis*, the causative agent of the plague. We will start in breakout rooms and come together at the end of the session to discuss our findings.

## Part 1: Preparation
The first thing you need to do is ensure that you have downloaded the data files and have the correct software installed on your machine.
 
1. **MEGA X (Molecular Genetic Evolutionary Analysis)-** https://www.megasoftware.net/  
Download the version of MEGA X suitable for your machine and follow instructions to install.
 
2. **Data files-** https://github.com/meganemichel/Phylogeny_Workshop  
Download this repository to a convenient location on your local machine. If you are comfortable working with Git on the command line follow the following steps:  
* Open a terminal window on your computer 
* Change into the directory where you would like to save the Phylogeny_Workshop materials  
```
cd /path/to/directory
```
* Clone directory
```
git clone https://github.com/meganemichel/Phylogeny_Workshop.git
```

**Note:** If you are not comfortable working with git, navivate to the URL listed above, select the green "Code button", and choose "Download ZIP". Make sure the unzipped directory (containing the subdirectories Alignments, Metadata, etc.) is named `Phylogeny_Workshop`, and move this directory to the desired location in your filesystem. 

## Part 2: SNP Alignments

Within the directory `Phylogeny_Workshop/Alignments`, you will find a file called `AncModern_pestis.fasta`. This file contains a multiple sequence alignment of ancient and modern *Yersinia pestis* sequences. In the termianl, run the following command to take a look at our alignment file. (Note that /path/to/directory refers to the location on your file system containing 'Phylogeny_Workshop')
```
cd /path/to/directory/Phylogeny_Workshop
head Alignments/AncModern_pestis.fasta 
```
**Note:** If you are running PowerShell on a Windows machine, you can view the first few lines of the file using `gc ./Alighments/AncModern_pestis.fasta | select -first 2`

Each sequence consists of a header line containing the sample name and beginning with '>'. The following line includes a string of nucleotides (**A,T,C,G**). What does **N** stand for in our alignment file?

How many *Y. pestis* sequences are present in our file?
```
grep '>' Alignments/AncModern_pestis.fasta  | wc -l
```
**Note:** If you are running PowerShell on a Windows machine, you can use the command `(Select-String -Path "./Alignments/AncModern_pestis.fasta" -Pattern ">").length`

You might wonder how this alignment was generated in the first place. Just as you learned about in the "Introduction to NGS DNA Sequencing and Processing" session, nf-core/eager was used to preprocess, align, and genotype data from ancient and modern *Y. pestis* strains (https://nf-co.re/eager). Genotyping was performed using the GATK UnifiedGenotyper with diploid calling. Next, MultiVCFAnalzer was used to filter SNPS and generate a SNP alignment (Alexander Herbig, https://github.com/alexherbig/MultiVCFAnalyzer). This SNP alignment was further filetered using a custom R script to exlude positions present in less than 98% of analyzed strains (Aida Andrades Valtueña, https://github.com/aidaanva/MDF). Finally, several unpublished samples were excluded from the analysis. For a more thorough overview of methods generally used to construct *Y. pestis* SNP alignments, see Method Details in Andrades Valtueña *et al.* 2017. 

Ok, let's use MEGA X to take a look at this alignment file in more detail. 

Open the MEGA X application. Select the **Data** tab (second from the right) and choose **Open a File/Session...**. First open the complete alignment file (Alignments/AncModern_pestis.fasta). Select **Analyze**. Next, make sure that **Nucleotide Sequences** is highlighted under **Data Type**. Note what symbols will be used for missing/identical data and alignment gaps. Select **Ok** and choose **No** when asked if this is protein-coding nucleotide sequence data. 

In the MEGA X Workspace (below the header bar), click on the tab showing the sequence alignment. Use the buttons at the top to explore the alignment in more detail. How many sites are variable? Why do you think this number different from the total number of SNPs included in our alignment file? 

You can also use MEGA X to contruct a pairwise distance matrix. In the toolbar at the top of the MEGA window, select Distance -> Compute Pairwise Distances. Choose Yes when asked whether you would like to use the active data file. In Analysis Preferences, under "Substitution Model, Model/Method" you can select "No. of Differences" to view the number of SNPs separating each pair of sequences. Alternatively, p-distance gives the proportion of aligned nucleotides at which two sequences differ. All other options can be left at the default settings. If you have questions about any of the other options in Alignment Preferences, you can access MEGA X Help by choosing Help -> Contents or typing Command-H on Mac. 

## Part 3: Contructing Phylogenies

Now that we know how to view our alignment and construct distance matrices, let's build some phylogenies. Select the Phylogeny button from the toolbar and choose a type of phylgony to construct. Your group members may choose to experiment with building different types of phylgenies; alternatively, constructing a Neighbor-Joining tree is a good choice, as it should complete in a very short time. Again, use the active data file and leave Analysis Preferences at default values. Note that we are using Bootstrapping to evaluate the robustness of the phylgeny we infer using a NJ approach. Once MEGA finishes running, you can view the tree that we computed, including a summary of the methods used in it's contruction. You can also experiment with changing the layout/shape of the tree. 

Locate the Tree Rooting button (second button on the left side) and click on the branch leading to *outgroup Y. pseudo* (complete name *Y. pseudotuberculosis*) to select it as an outgroup. *Y. psuedotuberculosis* is a close relative of *Y. pestis* that lives in the soil. After choosing the outgroup, *Y. pseudo* should appear at the bottom of the tree. The visualization may take a few seconds to reload. 

Phylogenetic trees provide the most information if we can interpret them in conjunction with detailed strain metadata (such as the geography and time period for ancient samples). To do this we will export our tree into an interactive visualization program called Microreact (https://microreact.org/showcase). 

Once you have a tree you would like to export, choose File-> Export Current Tree (Newick). Tick the Branch Length and Bootstrap boxes to include this data in our exported tree and select ok (loading may take a minute or so). Newick format is common text-based way of representing phylogenies. Choose File -> Save As and save the .nwk file in the Phylogeny folder of the Phylogeny_Workshop directory. Make sure that the file name ends in .nwk so that it is recognized as a newick format file.

## Part 4: Visualization and Interpretation

Finally, open https://microreact.org/showcase in your favorite webrowser. You can create an free account (My Account) if you would like to save the results of your analysis or continue without an account. Whatever you choose, navigate to the Upload page and choose "browse for files". Select the .nwk file you exported from MEGA. In addition, select the file microreact_data.csv (located in the Phylogeny_Workshop/Metadata directory). This file contains Latitude and Longitude, collection dates, and other associated metadata for the sequences included in our alignment. A final important piece of metadata is the plague outbreak to which each strain belongs (**LNBA** for Late Bronze Age Neolithic, **First Plague** for the Justinianic Plague and Subsequent outbreaks, **Second Plague** for the Black Death and subsequent outbreaks, and **Modern** for the third pandemic and contemporary strains. Take a look at this file in excel to get a better sense of the sequences included in our tree. 

Once both files have been selected, click continue. 

In the resulting window you should see three panes: a map with strain coordinates, a phylogenetic tree, and a timeline. In the timeline panel, ensure that year is selected. Time is displayed in years since the present, so that strains collected today fall at Time 0. Across all three visualizations, points are colored according to the outbreak of the associated strain. Select the eye button at the left side of the screen for a key. Choose the "play button" at the bottom of the screen to view the spread of *Y. pestis* over time and space. 

Here are some topics for further discussion in small groups: 

1. Compare your phylogenies with those of your neighbors. Are the topologies similar or different? Experiment with different layouts for your trees in Microreact (e.g. radial, circular, rectangular). If your trees are different, what do you notice about the bootstrap values on branches with conflicting topologies? 

2. What do you notice about the distribution of the LNBA and historical pandemics across the *Y. pestis* phylogeny? How are ancient strains related to modern *Yersinia pestis*? 

3. When you play the animation, what do you notice about the branch lengths of ancient strains relative to contemporary? How can you explain this observation? If branch lengths for specific ancient strains don't adhere to this pattern, what might that indicate? 

4. The precise postioning of strains within your phylogenies may differ from previously published trees due to differences in methods (e.g. type of phylogeny constructed, choice of substition model, differences in SNP filtering, etc.). Take a look at previosly published trees in the Pestis_Phylogeny_Examples folder. Discuss among your group members how phylogenetic analysis can help us to understand the geographic origin and transmission patterns of epidemics. 

## Sources Cited

Samples analyzed in this tutorial were originally published in the following papers: 

1. Andrades Valtueña, A. *et al.* The Stone Age Plague and Its Persistence in Eurasia. *Curr Biol* **27**, 3683-3691.e8 (2017).
2. Auerbach, R. K. *et al.* Yersinia pestis Evolution on a Small Timescale: Comparison of Whole Genome Sequences from North America. *PLOS ONE* **2**, e770 (2007).
3. Bos, K. I. *et al.* Eighteenth century Yersinia pestis genomes reveal the long-term persistence of an historical plague focus. *eLife* **5**, e12994 (2016).
4. Bos, K. I. *et al.* A draft genome of Yersinia pestis from victims of the Black Death. *Nature* **478**, 506–510 (2011).
5. Chain, P. S. G. *et al.* Insights into the evolution of Yersinia pestis through whole-genome comparison with Yersinia pseudotuberculosis. *PNAS* **101**, 13826–13831 (2004).
6. Chain, P. S. G. *et al.* Complete genome sequence of Yersinia pestis strains Antiqua and Nepal516: evidence of gene reduction in an emerging pathogen. *J Bacteriol* **188**, 4453–4463 (2006).
7. Cui, Y. *et al.* Historical variations in mutation rate in an epidemic pathogen, Yersinia pestis. *PNAS* **110**, 577–582 (2013).
8. Deng, W. *et al.* Genome sequence of Yersinia pestis KIM. *J Bacteriol* **184**, 4601–4611 (2002).
9. Eppinger, M. *et al.* Draft Genome Sequences of Yersinia pestis Isolates from Natural Foci of Endemic Plague in China. *J Bacteriol* **191**, 7628–7629 (2009).
10. Eroshenko, G. A. *et al.* Yersinia pestis strains of ancient phylogenetic branch 0.ANT are widely spread in the high-mountain plague foci of Kyrgyzstan. *PLOS ONE* **12**, e0187230 (2017).
11. Feldman, M. *et al.* A High-Coverage Yersinia pestis Genome from a Sixth-Century Justinianic Plague Victim. *Mol Biol Evol* **33**, 2911–2923 (2016).
12. Garcia, E. *et al.* Pestoides F, an Atypical Yersinia pestis Strain from the Former Soviet Union. in *The Genus Yersinia: From Genomics to Function* (eds. Perry, R. D. & Fetherston, J. D.) 17–22 (Springer, 2007). doi:10.1007/978-0-387-72124-8_2.
13. Keller, M. *et al.* Ancient Yersinia pestis genomes from across Western Europe reveal early diversification during the First Pandemic (541–750). *PNAS* **116**, 12363–12372 (2019).
14. Kislichkina, A. A. *et al.* Three Genetically Different Lineages of Yersinia pestis subsp. Microtus bv. Caucasica (0.PE2) Strains Circulate among Common Voles in Natural Plague Foci in the Caucasus. *Mol. Genet. Microbiol. Virol.* **32**, 191–195 (2017).
15. Kislichkina, A. A. *et al.* Nineteen Whole-Genome Assemblies of Yersinia pestis subsp. microtus, Including Representatives of Biovars caucasica, talassica, hissarica, altaica, xilingolensis, and ulegeica. *Genome Announc* **3**, e01342-15 (2015).
16. Kislichkina, A. A. *et al.* Six Whole-Genome Assemblies of Yersinia pestis subsp. microtus bv. ulegeica (Phylogroup 0.PE5) Strains Isolated from Mongolian Natural Plague Foci. *Genome Announc* **6**, e00536-18 (2018).
17. Kislichkina, A. A. *et al.* Nine Whole-Genome Assemblies of Yersinia pestis subsp. microtus bv. Altaica Strains Isolated from the Altai Mountain Natural Plague Focus (No. 36) in Russia. *Genome Announcements* **6**, e01440-17.
18. Kutyrev, V. V. *et al.* Phylogeny and Classification of Yersinia pestis Through the Lens of Strains From the Plague Foci of Commonwealth of Independent States. *Frontiers in Microbiology* **9**, 1106 (2018).
19. Morelli, G. *et al.* Yersinia pestis genome sequencing identifies patterns of global phylogenetic diversity. *Nat Genet* **42**, 1140–1143 (2010).
20. Parkhill, J. *et al.* Genome sequence of Yersinia pestis, the causative agent of plague. *Nature* **413**, 523–527 (2001).
21. Rasmussen, S. *et al.* Early Divergent Strains of Yersinia pestis in Eurasia 5,000 Years Ago. *Cell* **163**, 571–582 (2015).
22. Song, Y. et al. Complete genome sequence of Yersinia pestis strain 91001, an isolate avirulent to humans. *DNA Res* **11**, 179–197 (2004).
23. Spyrou, M. A. *et al.* Phylogeography of the second plague pandemic revealed through analysis of historical Yersinia pestis genomes. *Nat Commun* **10**, 4470 (2019).
24. Spyrou, M. A. *et al.* Historical Y. pestis Genomes Reveal the European Black Death as the Source of Ancient and Modern Plague Pandemics. *Cell Host Microbe* **19**, 874–881 (2016).
25. Spyrou, M. A. *et al.* Analysis of 3800-year-old Yersinia pestis genomes suggests Bronze Age origin for bubonic plague. *Nat Commun* **9**, 2234 (2018).
26. Yu, H. *et al.* Paleolithic to Bronze Age Siberians Reveal Connections with First Americans and across Eurasia. *Cell* **181**, 1232-1245.e20 (2020).
27. Zhgenti, E. *et al.* Genome Assemblies for 11 Yersinia pestis Strains Isolated in the Caucasus Region. *Genome Announc* **3**, e01030-15 (2015).


