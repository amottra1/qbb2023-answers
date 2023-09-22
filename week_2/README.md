Step 1.1

How many 100bp reads are needed to sequence a 1Mbp genome to 3x coverage?

(Coverage*Total size)/(# base pairs/read)= # reads needed
(3*1Mbp)/100bp= 30,000 reads needed


Step 1.3

In your simulation, how much of the genome has not been sequenced (has 0x coverage)?

~5% of the genome has 0 coverage

How well does this match Poisson expectations? How well does the normal distribution fit the data?

Poisson matches fairly well, a bit better than the normal distribution.



Step 1.4

In your simulation, how much of the genome has not been sequenced (has 0x coverage)?

~0.003% has 0 coverage

How well does this match Poisson expectations? How well does the normal distribution fit the data?

Poisson matches very well and normal also matches pretty well, but not quite as well.



Step 1.5

In your simulation, how much of the genome has not been sequenced (has 0x coverage)?

~0.001% has 0 coverage

How well does this match Poisson expectations? How well does the normal distribution fit the data?

Poisson matches very well, still slightly better than normal. As coverage is increasing, the match gets better.



Step 2.4

dot -Tpng edges.dot -o ex2_digraph.png


Step 2.5

Assume that the maximum number of occurrences of any 3-mer in the actual genome is 4. Using your graph from Step 2.4, write one possible genome sequence that would produce these reads. 

ATT-TTC-TCT-CTT-TTA-TAT-ATT-TTG-TGA-GAT-ATT-TTC-TCA-CAT-ATT-TTT


Step 2.6

In a few sentences, what would it take to accurately reconstruct the sequence of the genome?

We would need to know the expected size of the sequence and likely the starting point of the sequence. It would be helpful to know how many times certain kmers occured.


Step 3.1

Use ChatGPT (or Bard or your favorite LLM) to write an essay on why you are interested in genomics. Make sure to ask for references. Record both your prompt(s) and the output from the LLMin your README.md

Write 2 paragraph essay on why genomics is interesting and important. Please provide at least 2 references

Genomics, the study of an organism's complete set of genes and their functions, is a captivating and vital field of research that has garnered widespread interest and importance in recent years. At its core, genomics offers a comprehensive view of the genetic makeup of organisms, providing insights into the fundamental building blocks of life. This holistic understanding of genes, their interactions, and variations within populations has transformative implications in various domains, including healthcare and biological research. It allows us to delve into the genetic underpinnings of diseases, paving the way for personalized medicine and more effective treatments. Moreover, genomics aids in the conservation of biodiversity, enhances crop breeding for food security, and unravels the mysteries of evolution, making it both intriguing and indispensable

Two references supporting the importance of genomics are:

National Human Genome Research Institute. (2021). The Importance of Genomics. https://www.genome.gov/about-genomics/importance
Collins, F. S., & Varmus, H. (2015). A new initiative on precision medicine. New England Journal of Medicine, 372(9), 793-795. doi:10.1056/NEJMp1500523
These references highlight the significance of genomics in advancing our understanding of genetics and its far-reaching applications in medicine and research.

Step 3.2

In your README.md, comment on the output from the LLM: Does it make logical sense? Does it include any phrases you would not have written? Do the cited papers exist and support the claims from the LLM?

It does make logical sense for the most part. Some of the verbiage is a bit strange such as "far-reaching applications." The cited references both exist and somewhat support what the LLM is saying but not entirely.








