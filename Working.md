# Working of all files, functions etc
*PyWorld wrappers WORLD, which is a free software for high-quality speech analysis, manipulation and synthesis. It can estimate fundamental frequency (F0), aperiodicity and spectral envelope and also generate the speech like input speech with only estimated parameters.*

[WORLD Vocoder](https://github.com/mmorise/World)

## preprocess.py
(contains helper functions for preprocess_training.py)

- **load_wavs**
    - return list of all audio files in a directory as floating point time series.
- **world_decompose**
    - pyworld.harvest    -> returns f0 and the timeaxis
    - pyworld.cheaptrick -> returns sp
    - pyworld.d4c        -> returns ap
- **world_encode_spectral_envelop**
    - pyworld.code_spectral_envelope
    - returns the Mel-cepstral coeffs
- **world_encode_data**
    - store all f0, timeaxis, sp, ap for all wav files in lists (using world_decompose)
    - store all mel cepstral coeffs in a list (using world_encode_spectral_envelop)
    - returns list of f0, timeaxis, sp, ap, mceps
- **logf0_statistics**
    - calculate log of masked array of f0's
    - returns mean and std dev of this arrray
- **transpose_in_list**
    - returns transposed array 
- **coded_sps_normalization_fit_transform**
    - 

## preprocess_training.py
(for preprocessing the training data)
- num_mcep - 24
- sampling rate - 16
- number of frames -128
- frame period - 5


