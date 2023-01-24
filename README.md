# Voice-conversion

## GMM based method

[Method](GMM/)  

## GAN based method
Based on [this paper](https://arxiv.org/pdf/1904.04631.pdf) on non-parallel voice converison using cyclegan-vc2

[Method](Cyclegan/)


### Directory Structure
```
.
├── LICENSE
├── GMM/
|   ├── requirements.txt
|   ├── GMM.ipynb
|   ├── GMM_HowTo.md
├── Pytorch-CycleGAN-VC2/
│   ├── cache/
│   └── data/
└── README.md
```

## People involved
* [Aniket Pradhan](http://home.iiitd.edu.in/~aniket17133)
* [Akhil Jarodia](https://github.com/akj127)
* [Arav Malk](https://github.com/Arav-malik)
* [Deepanshu Badshah](#)
* [Kshitij Srivastava](#)
* [Siddharth Nair](https://github.com/siddharth17196)

1.Target
تبدیل صدا از بلندگوی منبع به بلندگوی هدف با استفاده از مجموعه داده موازی و GMM هدف مااز انجام این پروژه



2.Describe innovation

تبدیل Oice (VC) تکنیکی است برای تبدیل هویت گوینده موجود در شکل موج گفتار منبع به شکل موجی متفاوت و در عین حال حفظ اطلاعات زبانی شکل موج گفتار منبع. در سال 2016، چالش تبدیل صوتی (VCC) 2016 را در Interspeech 2016 راه اندازی کردیم. هدف چالش سال 2016 درک بهتر تکنیک های مختلف VC بود که بر اساس یک مجموعه داده مشترک آزادانه در دسترس برای بررسی یک هدف مشترک و به اشتراک گذاشتن دیدگاه ها ساخته شده بودند.
