# Fitting exorings to the eclipses of PDS 110

This is a Jupyter notebook reading in photometric data of PDS 110 and
fitting exorings to the 2008 and 2011 eclipses.

## Quick start

Clone this repository with:

    git clone https://github.com/mkenworthy/pds_110_exorings.git

and then run the Jupyter notebook with:

    jupyter notebook plot_PDS_110_exoring_fig_5.ipynb

Prerequisites include `astropy`.

## The eclipses of PDS 110

As published in [Osborn et al. (2017)](https://arxiv.org/abs/1705.10346), two eclipses lasting about 20 days
and with an extinction of 30 percent were detected in the WASP exoplanet
survey and KELT survey.

The star is [PDS
110](http://simbad.u-strasbg.fr/simbad/sim-id?Ident=PDS+110), a very young star in Orion.

The two eclipses show substructure - rapid fluctuations in the flux
during one or more of the nights that indicate clumpy material moving
across the disk of the star.

These fluctuations are similar to those seen towards the young star
J1407 in 2007, which [Kenworthy and Mamajek
(2015)](http://adsabs.harvard.edu/abs/2015ApJ...800..126K) interpret as being due
to the transit of a giant Hill
sphere filling ring system orbiting around an unseen secondary
companion.
The rings block the light from J1407 over two months, with rapid
fluctuations from ring edges transiting the disk of the star.

The next eclipse for PDS 110 is predicted to occur in September 2017, and observers
are encouraged to take photometric data during this time.

## The code

The disk geometry was fit to the light curve gradients using the method
detailed in Kenworthy and Mamajek (2015) using the exorings code.

The ring radii and transmissions were fitted by eye.

You are encouraged to try fitting rings to the data and improve the
current fit!

Fitting to the 2008 eclipse is relatively easy, but fitting the two
eclipses simultaneously with the same disk geometry and ring structure
has not been as successful. Several hypotheses are discussed in the
paper.

