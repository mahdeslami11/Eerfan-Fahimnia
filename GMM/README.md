## Voice conversion using Gaussian Mixture Models

Converting voice from a source speaker to a target speaker using a parallel dataset and GMMs

### Important info

* Dataset used:
  * CMU Arctic dataset
  * Our own dataset made from an audiobook sampled at 2/3 seconds

## Sys params/Constants

* Sampling frequency: 16000
* FFT size: 1024
* Max utterances to be used together: 100
* Test size: 0.03% of training set
* frame_period = 5
* The number of samples between successive frames/hop length = 80
* Order of mel-cepstrum = 24

## Software libraries used

* sklearn (for gaussian mixture model)
* nnmnkwii (for DTWAligner, Dataset_Model
* librosa (for audio file management)
* pysptk (for audio synthesis)

## References

* T. Toda, A. W. Black, and K. Tokuda, “Voice conversion based on maximum likelihood estimation of spectral parameter trajectory,” IEEETrans. Audio, Speech, Lang. Process, vol. 15, no. 8, pp. 2222–2235, Nov. 2007.
* Kobayashi, Kazuhiro, et al. “Statistical Singing Voice Conversion with Direct Waveform Modification based on the Spectrum Differential.” Fifteenth Annual Conference of the International Speech Communication Association. 2014.
