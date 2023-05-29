# NLPCC2023 Shared Task 8: Chinese Spelling Check

## Introduction

### Background

In today's highly developed media landscape, news and other textual content are constantly being produced, but errors in spelling and word usage are not uncommon. Given the sheer volume of content, it is difficult for traditional manual review and regulation to effectively and comprehensively monitor for errors. Therefore, we hope to use AI technology to assist editorial staff in identifying errors in content, thereby improving content quality, increasing editing efficiency, and reducing the risk of errors. This task involves spelling errors such as homophonic errors, visually similar errors, and other types of errors in sentences from Chinese news articles.

### Data Source

Data was obtained from publicly available news articles and books where errors were manually identified and labeled.

### Task Requirements

Identify locations in the content where errors exist and provide corresponding correction suggestions.

### Significance

By using AI technology to assist editorial staff in identifying errors in content, we can improve content quality, increase editing efficiency, and reduce the risk of errors.

## Updates

All updates about this shared task will be posted on this page.

## Important Dates

- 2023/03/15：registration open
- 2023/04/06：release of detailed task guidelines & training data
- 2023/05/05：registration deadline
- 2023/05/21：release of test data
- 2023/05/31：participants’ results submission deadline
- 2023/06/10：evaluation results release and call for system reports and conference paper


## Team Rank
| rank | team | char-detect-P | char-detect-R | char-detect-F1 | char-correct-P | char-correct-R | char-correct-F1 | sentence-FPR |
| ---- | ---- | ------------- | ------------- | -------------- | -------------- | -------------- | ---------------- | ------------- |
| 1 |         Siqi Song-GLN-Soochow University-ResultSubmission052901         | 81.97 | 47.15 | 59.87 | 78.36 | 45.07 | 57.23 | 4.0 |
| 2 |              lixiang-GGbond-ECNU-ResultSubmission052601              | 67.77 | 50.15 | 57.64 | 62.36 | 46.15 | 53.04 | 7.72 |
| 3 |  Hao Yang-HW-TSC-Huawei Text Machine Translation Lab-ResultSubmission052902  | 66.55 | 49.59 | 56.83 | 60.44 | 45.04 | 51.62 | 13.28 |
| 4 |                      Hao Yang-HW-TSC-Huawei Text Machine Translation Lab-ResultSubmission052701                      | 62.47 | 49.93 | 55.5 | 55.79 | 44.59 | 49.57 | 12.44 |
| 5 |        Hao Yang-HW-TSC-Huawei Text Machine Translation Lab-ResultSubmission052901        | 57.38 | 54.26 | 55.78 | 50.61 | 47.85 | 49.19 | 13.4 |
| 6 |     Haojing Huang-RTX5090-Tsinghua Shenzhen International Graduate School-Result Submission052802     | 75.14 | 39.41 | 51.7 | 69.63 | 36.52 | 47.91 | 3.4 |
| 7 |                    Haojing Huang-RTX5090-Tsinghua Shenzhen International Graduate School-Result Submission052702                    | 74.28 | 37.11 | 49.49 | 69.01 | 34.48 | 45.98 | 2.84 |
| 8 |      Haojing Huang-RTX5090-Tsinghua Shenzhen International Graduate School-Result Submission052701      | 74.22 | 37.0 | 49.38 | 68.95 | 34.37 | 45.87 | 2.84 |
| 9 |                Haojing Huang-RTX5090-Tsinghua Shenzhen International Graduate School-Result Submission052801                | 76.19 | 36.04 | 48.93 | 71.42 | 33.78 | 45.87 | 2.28 |
| 10 |             LinWancong-TingZhiDui-HainanUniversity-ResultSubmission052701             | 82.33 | 38.81 | 52.75 | 70.93 | 33.44 | 45.45 | 3.24 |
| 11 |   WancongLin-TingZhiDui-HainanUniversity-ResultSubmission052901   | 66.49 | 46.74 | 54.89 | 54.95 | 38.63 | 45.37 | 7.64 |
| 12 |                  WancongLin-TingZhiDui-HainanUniversity-ResultSubmission052801                  | 70.04 | 41.74 | 52.31 | 58.79 | 35.04 | 43.91 | 5.56 |
| 13 |                     LinWancong-TingZhiDui-HainanUniversity-ResultSubmission052702                     | 45.16 | 47.74 | 46.41 | 39.24 | 41.48 | 40.33 | 11.12 |
| 14 |                   LinWancong-TingZhiDui-HainanUniversity-ResultSubmission052703                   | 45.35 | 47.7 | 46.5 | 39.01 | 41.04 | 40.0 | 11.16 |
| 15 |          Haojing Huang-RTX5090-Tsinghua Shenzhen International Graduate School-Result Submission052703          | 71.08 | 30.41 | 42.6 | 65.37 | 27.96 | 39.17 | 3.16 |
| 16 |               NLPCC_TASK8_PRED               | 34.69 | 52.85 | 41.89 | 32.29 | 49.19 | 38.99 | 3.0 |
| 17 |    LinWancong-TingZhiDui-HainanUniversity-ResultSubmission052601    | 38.9 | 39.44 | 39.17 | 32.98 | 33.44 | 33.21 | 3.76 |
| 18 |                 Hao Yang-HW-TSC-Huawei Text Machine Translation Lab-ResultSubmission052601                 | 24.78 | 50.85 | 33.32 | 22.34 | 45.85 | 30.04 | 11.32 |
| 19 |           Haojing Huang-RTX5090-Tsinghua Shenzhen International Graduate School-Result Submission052601           | 26.76 | 40.33 | 32.17 | 23.22 | 35.0 | 27.92 | 8.04 |
| 20 |            FengXilong-POLab-zut-Result Submission052901            | 19.44 | 29.74 | 23.51 | 18.16 | 27.78 | 21.96 | 2.36 |
| 21 | Xiaoying Wang-ZZUNLP-zzu-ResultSubmission052601 | 19.3 | 44.78 | 26.97 | 15.2 | 35.26 | 21.24 | 4.44 |
| 22 |       FengXilong-POLab-zut-Result Submission052801       | 18.68 | 21.93 | 20.17 | 17.48 | 20.52 | 18.88 | 1.56 |


## Dataset

The development dataset comprises of 1000 sentence pairs, consisting of both incorrect and correct sentences. The file format is such that each line contains a raw sentence followed by its corresponding correct answer, separated by a tab character: **Input**`\t`**Gold**. (For further details, please refer to the `data` folder.)

You are free to use the development dataset for local training and testing. You may also use any other open-source datasets such as [SIGHAN13](http://ir.itc.ntnu.edu.tw/lre/sighan7csc.html), [SIGHAN14](http://ir.itc.ntnu.edu.tw/lre/clp14csc.html), [SIGHAN15](http://ir.itc.ntnu.edu.tw/lre/sighan8csc.html), [Lang8](http://tcci.ccf.org.cn/conference/2018/taskdata.php), [HSK](https://cloud.tsinghua.edu.cn/f/9e46b10b52564736b0f3/), [CGED](https://github.com/blcuicall/cged_datasets), [MuCGEC](https://github.com/HillZhang1999/MuCGEC), [YACLC](https://github.com/blcuicall/YACLC), [CTC2021](https://github.com/destwang/CTC2021) and so on.

The errors in the original sentences fall into three categories:

### Homophonic Spelling Errors: 

```
【例】公司在处理技术、产品设计、检验检测等方面有着坚实的基础和出色的造诣，形成了较强的技术优式。
【答案】公司在处理技术、产品设计、检验检测等方面有着坚实的基础和出色的造诣，形成了较强的技术优势。
【例】知觉告诉他，这是正确的选择。
【答案】直觉告诉他，这是正确的选择。
【例】碳成本激增或将危机油气行业。
【答案】碳成本激增或将危及油气行业。
【例】给予多特征融合的目标跟踪算法系统通过图像处理和分析技术、机器学习和模式识别来识别和分析人体的位置和运动。
【答案】基于多特征融合的目标跟踪算法系统通过图像处理和分析技术、机器学习和模式识别来识别和分析人体的位置和运动。
```

### Visually Similar Errors:

```
【例】严格落实“开喷淋、常冲洗、勤酒水”等防治措施。
【答案】严格落实“开喷淋、常冲洗、勤洒水”等防治措施。
【例】书本是人类灵魂的桥梁,是人类思想选代升级的阶梯,是人类认知传承的纽带。
【答案】书本是人类灵魂的桥梁,是人类思想迭代升级的阶梯,是人类认知传承的纽带。
```

### Other Types of Errors:

```
【例】然而几个以前，张大妈还深陷在窨井盖爆炸的阴影中。
【答案】然而几个月前，张大妈还深陷在窨井盖爆炸的阴影中。
【例】我县聚焦青年人才成长，以人才制度创新推进区域性青年人才高地建设，打造人擦荟萃、要素集聚、业态繁荣的创新创业热土。
【答案】我县聚焦青年人才成长，以人才制度创新推进区域性青年人才高地建设，打造人才荟萃、要素集聚、业态繁荣的创新创业热土。
【例】老一辈科学家身上充沛着为科学而献身的可贵精神。
【答案】老一辈科学家身上充满着为科学而献身的可贵精神。
```

## Evaluation Metrics

The following metrics will be used to evaluate the performance of the system:

### Detection Level

* The detection precision is calculated as the number of overlapping positions between the detected errors and the standard detection answers divided by the total number of detected errors, expressed as a percentage. The formula is as follows:

$$
\text{Detection Precision} = \frac{(|\{\text{Detection Outputs}\} \cap \{\text{Detection Answers}\}|}{|\{\text{Detection Outputs}\}|)} * 100\%
$$



* The detection recall is calculated as the number of overlapping positions between the detected errors and the standard detection answers divided by the total number of standard detection answers, expressed as a percentage. The formula is as follows:

$$
\text{Detection Recall} = \frac{(|{\text{\{Detected Outputs}\}} \cap {\text{\{Detection Answers}\}}|)}{|{\text{\{Detection Answers}\}}|} * 100\%
$$



* The detection F1-score is the harmonic mean of the detection precision and recall. The formula is as follows:

$$
\text{Detection F1-score} = 2 * \frac{(\text{Detection Precision} * \text{Detection Recall})}{(\text{Detection Precision} + \text{Detection Recall})}
$$

### Correction Level

* The correction precision is calculated as the number of corrected characters that match the standard correction answers divided by the total number of edited characters, expressed as a percentage. The formula is as follows:

$$
\text{Correction Precision} = \frac{(|{\{\text{Corrected Characters}\}} \cap {\{\text{Correction Answers}\}}|)}{|{\{\text{Corrected Characters}\}}|} * 100\%
$$



* The correction recall is calculated as the number of corrected characters that match the standard correction answers divided by the total number of standard correction answers, expressed as a percentage. The formula is as follows:

$$
\text{Correction Recall} = \frac{(|{\{\text{Corrected Characters}\}} \cap {\{\text{Correction Answers}\}}|)}{|{\{\text{Correction Answers}\}}|} * 100\%
$$



* The correction F1-score is the harmonic mean of the correction precision and recall. The formula is as follows:

$$
\text{Correction F1-score} = 2 * \frac{(\text{Correction Precision} * \text{Correction Recall})}{(\text{Correction Precision} + \text{Correction Recall})}
$$

These evaluation metrics are used to assess the performance of the AI model in detecting and correcting spelling errors in textual content. The precision, recall, and F1 scores for both detection and correction provide a comprehensive evaluation of the model's ability to identify and rectify errors accurately and efficiently. The higher the scores, the better the performance of the model.

### False Positive Rate

Given the practical considerations of real-world applications, we incorporate the **false positive rate** at the sentence level into our analysis. Specifically, this involves calculating the proportion of correctly formed sentences that are incorrectly altered by the model.

### Evaluation Method

We provide an evaluation program in the `csc_evaluation` file. The usage is as follows:

```bash
python csc_evaluation.py --gold_file="gold.txt" -- modelout_file="modelout.txt"
```

The Python version used is 3.*.

* --gold_file: The file path for the test set in the format "**input**`\t`**gold**`\n`". The two columns of text have equal lengths.

* --modelout_file: The file path for the model output in the format "**input**`\t`**output**`\n`". The two columns of text have equal lengths.

The data in the first column of the gold_file and modelout_file should be consistent.

Output: 

* Sentence-level false positive rate (FPR), 
* Character-level: 
  * error detection precision, recall, F1
  * error correction precision, recall, F1.



## Testing Instructions and Submission

The test dataset includes one original sentence per line. The distribution of the test dataset is similar to the development dataset. The test dataset will be released via email before May 21st, 2023. Kindly ensure to check the email address that you used during registration for the dataset.

For submission, the following materials should be packaged as one `zip` file and sent to xjyin@pku.edu.cn.

* Submission File: Please write the final results into a text file, encoded in utf-8 format. Each line of the file should consist of a sentence pair, with the original sentence and the model output separated by a tab character: **Input**`\t`**Output**. Specifically, the submission file must contain the **same number of lines** as the input file.
* Code: The code folder should contain all the codes of data augmentation, data processing, model training and model inference.
* Document:
  * Data Description: The document needs to contain a brief description of data used in the experiment, as well as the data augmentation methods. 
  * Sharing Link of Additional Data: Additional data used in the experiment should be uploaded to a cloud storage, i.e., net disk, and the sharing link should be included in the document.
  * Code Reproduction Process: The submitted code may be checked and reproduced by us, so please briefly explain the process of reproducing the code in the document.



If you have any questions, please contact [xjyin@pku.edu.cn](mailto:xjyin@pku.edu.cn) via email.
