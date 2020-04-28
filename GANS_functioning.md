# Working of all files, functions etc
*PyWorld wrappers WORLD, which is a free software for high-quality speech analysis, manipulation and synthesis. It can estimate fundamental frequency (F0), aperiodicity and spectral envelope and also generate the speech like input speech with only estimated parameters.*

[WORLD Vocoder](https://github.com/mmorise/World)

sp -> smoothed spectrogram\
ap -> aperiodicity

## preprocess.py
(contains helper functions for preprocess_training.py)

- **load_wavs**
    - return list of all audio files in a directory as floating point time series.
- **world_decompose**
    - pyworld.harvest    -> returns f0 and the timeaxis
    - pyworld.cheaptrick -> returns sp
    - pyworld.d4c        -> returns ap
    - returns these 4 features
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
    - takes as input the mceps
    - returns its transposed array 
- **coded_sps_normalization_fit_transform**
    - takes input the transposed array (from transpose_in_list)
    - returns normalised mceps (x-mean/std), mean of mceps, std of mceps

## preprocess_training.py
(for preprocessing the training data)
- num_mcep - 24
- sampling rate - 16
- number of frames -128
- frame period - 5

1. load all wav files for both directories (source and target) from preprocess.load_wavs
2. get f0, timeaxis, sp, ap, mceps from preprocess.world_encode_data
3. get log mean and log std of f0's using preprocess.logf0_statistics
4. transpose the mceps using preprocess.transpose_in_list
5. get mcep_normalised, mceps_mean, mceps_std from preprocess.coded_sps_normalization_fit_transform
6. save 4 files to cahe folder
    - log mean and log std of both voices from step 3 (logf0s_normalization)
    - mceps_mean and mceps_std from step 5 (mcep_normalization.npz)
    - mcep_normalised from the first voice (coded_sps_A_norm.pickle)
    - mcep_normalised from the target voice (coded_sps_B_norm.pickle)


