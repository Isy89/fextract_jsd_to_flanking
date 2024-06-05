# fextract_jsd_to_flanking

This is a of [LBFextract](https://github.com/Isy89/LBF) plugin which calculates for all the intervals in a BED file the Jensen-Shannon divergence 
(JSD) between the fragment length distribution in the flanking regions of the interval and the fragment length distribution 
at each position.

It reports the signal as a csvfile and a plot of the signal similar to the following one:

[jsd_to_flanking_ctcf_si![jsd_to_flanking_signal_plot.png](jsd_to_flanking_signal_plot.png)gnal_plot.pdf](jsd_to_flanking_ctcf_signal_plot.pdf)

