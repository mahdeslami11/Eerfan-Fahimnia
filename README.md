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

هدف ما از انجام این پروژه تبدیل صدا از بلندگوی هدف است که با داده های غیر موازی و تعامل به شبکه  (خود متخاصم) انجام میگرد در این پروژه به پیشرفت مسیر با استفاده از CYcleGAN V2 میپردازیم 



2.Describe innovation

شبکه های متخاصم سازگار با چرخه (CycleGAN) به طور گسترده ای برای تبدیل تصویر استفاده شده است. به نظر می رسد که می توان از آن برای تبدیل صدا نیز استفاده کرد. این یک پیاده سازی CycleGAN در تبدیل گفتار انسان است. شبکه عصبی از شبکه عصبی کانولوشن دردار 1 بعدی (Gated CNN) برای ژنراتور و CNN دردار دوبعدی برای تشخیص دهنده استفاده کرد. این مدل ضرایب Mel-cepstral (MCEPs) (برای پوشش طیفی) را به عنوان ورودی برای تبدیل صدا می گیرد.

3.Change Source Code

import tensorflow as tf
from tensorflow.contrib import slim
from util.image import nchw_to_nhwc
from util.layers import (GaussianKLD, GaussianLogDensity, GaussianSampleLayer,
                         Layernorm, conv2d_nchw_layernorm, lrelu)
https://github.com/k2kobayashi/sprocket ارجاع به این پروژه


5.Conclusion of the altering 

در این مقاله یک چارچوب انعطاف‌پذیر برای تبدیل طیفی (SC) پیشنهاد می‌شود که آموزش با اجسام غیرهمتراز را تسهیل می‌کند. بسیاری از چارچوب‌های SC برای یادگیری توابع تبدیل یا ترکیب یک طیف هدف با کمک هم‌ترازی‌ها، به پیکره‌های موازی، هم‌ترازی‌های آوایی، یا مکاتبات صریح چارچوبی نیاز دارند. با این حال، این الزامات به شدت دامنه کاربردهای عملی SC را به دلیل کمبود یا حتی در دسترس نبودن اجسام موازی محدود می کند. ما یک چارچوب SC مبتنی بر رمزگذار خودکار متغیر پیشنهاد می کنیم که ما را قادر می سازد از اجسام غیر موازی بهره برداری کنیم. این چارچوب شامل یک رمزگذار است که نمایش‌های آوایی مستقل از بلندگو را یاد می‌گیرد و یک رمزگشا که بازسازی بلندگوی تعیین‌شده را می‌آموزد. این نیاز به پیکره های موازی یا ترازهای آوایی برای آموزش یک سیستم تبدیل طیفی را حذف می کند. ما ارزیابی‌های عینی و ذهنی را گزارش می‌کنیم تا روش پیشنهادی خود را تأیید کنیم و آن را با روش‌های SC که به مجموعه‌های هم‌تراز دسترسی دارند مقایسه کنیم.


6.Self Introduction 

Erfan Fahimnia 

Currently Stduying Electrical Engineering in Bachlor Degree


6. Main Project 


https://github.com/siddharth17196/voco.ai

