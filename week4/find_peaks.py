#!/usr/bin/env python

import sys

#from week4_practice.py import load_bedgraph, bin_array
import numpy 
import scipy.stats
import matplotlib.pyplot as plt


def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, control_for_fname, control_rev_fname, outwig_fname, outbg_fname = sys.argv[1:7]
    fragment_width=198 
    
    # Define what genomic region we want to analyze
    chrom = "chr2R"
    chromstart = 10000000
    chromend =  12000000
    chromlen = chromend - chromstart
    binsize = 200
    number_of_peaks = 200

    # Load the sample bedgraph data, reusing the function we already wrote
    
    forward = load_bedgraph(forward_fname, chrom, 0, chromlen)
    reverse = load_bedgraph(reverse_fname, chrom, 0, chromlen)

    # Combine forward and reverse tags
    combined = forward + reverse


    # Bin tag density using a sliding window
    scores = bin_array(combined, binsize)


    # Identify the top N peak positions
    peaks = find_peaks(scores, number_of_peaks, binsize)


    # Find combined tag densities over the selected peaks by strand
    #reverse_curve = find_profile(reverse, peaks, binsize * 4)
    #forward_curve = find_profile(forward, peaks, binsize * 4)
   
    # Combine tag densities, shifting by our previously found fragment width
    # need to shift forward over by half frag-width 198 and shift reverse over by half

    #make an array of zeros for 1/2 of frag width of 198
    combined_tags = numpy.zeros(chromlen)
    combined_tags[fragment_width// 2: ] += forward[fragment_width// 2: ]
    combined_tags[:-(fragment_width// 2) ] += reverse[:-(fragment_width// 2)  ]
    #combined_tags=forward_curve[0:forward_curve.shape[0]-fragment_width]+ reverse_curve[fragment_width:]
    
    # Load the control bedgraph data, reusing the function we already wrote

    control_forward= load_bedgraph(control_for_fname, chrom, 0, chromlen)
    control_reverse= load_bedgraph(control_rev_fname, chrom, 0, chromlen)
    
    # Combine tag densities
    combined_control_tags = numpy.zeros(chromlen, float)
    combined_control_tags = control_reverse
    combined_control_tags += control_forward

    #control_forward_curve= find_profile(control_forward, peaks, binsize * 4)
    #control_reverse_curve= find_profile(control_reverse, peaks, binsize * 4)

    #combined_control_tags=control_forward_curve[0:control_forward_curve.shape[0]-fragment_width]+ control_reverse_curve[fragment_width:]

    #print(combined_control_tags.shape)
    #print(combined_tags.shape)
    
    # Adjust the control to have the same coverage (# reads) as our sample

    control_sum=numpy.sum(combined_control_tags)
    sample_sum=numpy.sum(combined_tags)
    scale_factor=control_sum/sample_sum
    scaled_control_tags= combined_control_tags /scale_factor

    #print(scaled_control_tags)
    #print(combined_tags)

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base
    #print(scaled_control_tags.shape)
    #print(scaled_control_tags)
    control_binned= bin_array(scaled_control_tags, 1000)/1000

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score

    mean_tags=numpy.average(control_binned)

    for value in range(control_binned.shape[0]):
        if control_binned[value] < mean_tags:
            control_binned[value]= mean_tags

    #print(mean_tags)
    #print(control_binned)

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote

    scores_new = bin_array(combined, fragment_width*2)


    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background

    p_values=1-scipy.stats.poisson.cdf(scores_new, mu=mean_tags*fragment_width*2)

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250

    p_values_log10=numpy.zeros_like(p_values)

    for i in range(p_values.shape[0]):
        if p_values[i]<1e-250:
            p_values_log10[i]=0
        else:
            p_values_log10[i]=-numpy.log10(p_values[i])


    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"

    write_wiggle(p_values_log10, chrom, chromstart, sys.argv[5])


    # Write bed file with non-overlapping peaks defined by high-scoring regions 

    write_bed(scores_new, chrom, chromstart, chromend, fragment_width, sys.argv[6])

def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()

def load_bedgraph(fname, target, chromstart, chromend):
    # Create array to hold tag counts
    coverage = numpy.zeros(chromend - chromstart, int)

    #Read the file in line by line
    for line in open(fname):
        # Break the line into individual fields
        chrom, start, end, score = line.rstrip().split('\t')
        # Check if the data fall in our target region
        if chrom != target:
            continue
        start = int(start)
        end = int(end)
        if start < chromstart or end >= chromend:
            continue
        # Add tags to our array
        coverage[start-chromstart:end-chromend] = int(score)
    return coverage

def bin_array(data, binsize):
    # Create array to hold scores
    binned = numpy.zeros(data.shape[0], data.dtype)

    # For each position in the window, add to the score array
    for i in range(binsize):
        binned[i:data.shape[0] - binsize + i] += data[binsize//2:-binsize//2]
    return binned

def find_peaks(data, target, binsize):
    order = numpy.argsort(data)[::-1]
    return order[:target]

def find_profile(data, peaks, binsize):
    # Create array to hold the combined profile
    results = numpy.zeros(binsize, float)
    for i in range(peaks.shape[0]):
        # For each peak, get the tag density +/- half the binsize
        results += data[peaks[i]-binsize//2:peaks[i]+binsize//2]
    # Return average tag density
    return results / peaks.shape[0]

def find_correlations(reverse, forward):
    # Since we made the profiles 4 times bigger than our estimated fragment size
    # we will search a size from 0 to 2 times our estimate
    width = reverse.shape[0] // 2
    # Create an array to hold correlations
    corrs = numpy.zeros(width, float)
    for i in range(width):
        # For each shift, find correlation of overlapping regions 
        corrs[i] = numpy.corrcoef(reverse[i:], forward[:forward.shape[0]-i])[0, 1]
    return corrs

if __name__ == "__main__":
    main()