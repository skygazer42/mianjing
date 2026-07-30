# AI 基础与高频八股面试题（30 题）

## 一句话定位

AI 基础题真正考察的不是背算法名，而是能否从目标函数、假设、优化过程、评估方式和工程边界解释一个模型为什么有效、什么时候失效以及怎样验证。

本目录按“学习与泛化基础—经典算法—训练评估与生产治理”整理 30 道高频题。每题先给可复述结论，再给推导、业务例子、工程取舍、常见坑、延伸追问和原始来源；01–30 Notebook 将对应问题拆成独立、可顺序执行的业务小实验。

## 学习与泛化基础（01–10）

1. [监督学习与无监督学习如何区分？](./01.监督学习与无监督学习如何区分.md)
2. [偏差与方差如何权衡？](./02.偏差与方差如何权衡.md)
3. [过拟合如何诊断和治理？](./03.过拟合如何诊断和治理.md)
4. [数据切分为什么会泄漏？](./04.数据切分为什么会泄漏.md)
5. [标准化与归一化怎么选？](./05.标准化与归一化怎么选.md)
6. [线性回归与逻辑回归有什么区别？](./06.线性回归与逻辑回归有什么区别.md)
7. [L1 与 L2 正则如何选择？](./07.L1与L2正则如何选择.md)
8. [SVM 为什么追求最大间隔？](./08.SVM为什么追求最大间隔.md)
9. [核技巧为什么不用显式升维？](./09.核技巧为什么不用显式升维.md)
10. [PCA 如何降维与白化？](./10.PCA如何降维与白化.md)

## 经典算法与集成学习（11–20）

11. [KMeans++ 初始化与收敛如何解释？](./11.KMeans++初始化与收敛.md)
12. [GMM 与 EM 如何实现软聚类？](./12.GMM与EM.md)
13. [朴素贝叶斯为什么能做文本分类？](./13.朴素贝叶斯.md)
14. [kNN 如何做分类与检索？](./14.kNN.md)
15. [CART 如何选择切分？](./15.CART.md)
16. [随机森林如何降低方差？](./16.随机森林.md)
17. [AdaBoost 如何聚焦难样本？](./17.AdaBoost.md)
18. [GBDT 如何逐步拟合残差？](./18.GBDT.md)
19. [XGBoost 的二阶近似解决什么问题？](./19.XGBoost二阶近似.md)
20. [信息熵与基尼指数怎么选？](./20.信息熵与基尼.md)

## 训练、评估与生产治理（21–30）

21. [交叉验证如何避免泄漏？](./21.交叉验证与泄漏.md)
22. [ROC、PR 与 AUC 如何按业务选择？](./22.ROC-PR-AUC.md)
23. [概率校准与业务阈值如何设计？](./23.概率校准与业务阈值.md)
24. [缺失值与异常值如何处理？](./24.缺失值与异常值处理.md)
25. [SGD、Momentum 与 Adam 怎么理解？](./25.SGD-Momentum-Adam.md)
26. [权重初始化为什么重要？](./26.权重初始化.md)
27. [ReLU、GELU、Sigmoid 如何选择？](./27.ReLU-GELU-Sigmoid.md)
28. [Dropout 为什么只在训练时启用？](./28.Dropout.md)
29. [类别不平衡如何治理？](./29.类别不平衡.md)
30. [模型上线后如何监控漂移？](./30.线上漂移监控.md)

## 可执行 Notebook（01–30 已完成）

1. [监督学习与无监督学习](./01-supervised-unsupervised.ipynb)
2. [偏差与方差](./02-bias-variance.ipynb)
3. [过拟合诊断与治理](./03-overfitting.ipynb)
4. [数据泄漏与安全切分](./04-data-leakage.ipynb)
5. [标准化与归一化](./05-scaling.ipynb)
6. [线性回归与逻辑回归](./06-linear-logistic.ipynb)
7. [L1 与 L2 正则](./07-l1-l2.ipynb)
8. [SVM 最大间隔](./08-svm-margin.ipynb)
9. [核技巧](./09-kernel-trick.ipynb)
10. [PCA 与白化](./10-pca-whitening.ipynb)
11. [KMeans++ 初始化与收敛](./11-kmeans-plus-plus.ipynb)
12. [GMM 与 EM](./12-gmm-em.ipynb)
13. [朴素贝叶斯](./13-naive-bayes.ipynb)
14. [kNN](./14-knn.ipynb)
15. [CART](./15-cart.ipynb)
16. [随机森林](./16-random-forest.ipynb)
17. [AdaBoost](./17-adaboost.ipynb)
18. [GBDT](./18-gbdt.ipynb)
19. [XGBoost 二阶近似](./19-xgboost-second-order.ipynb)
20. [信息熵与基尼](./20-entropy-gini.ipynb)
21. [交叉验证与泄漏](./21-cross-validation-leakage.ipynb)
22. [ROC、PR 与 AUC](./22-roc-pr-auc.ipynb)
23. [概率校准与业务阈值](./23-calibration-threshold.ipynb)
24. [缺失值与异常值](./24-missing-outlier.ipynb)
25. [SGD、Momentum 与 Adam](./25-optimizers.ipynb)
26. [权重初始化](./26-initialization.ipynb)
27. [ReLU、GELU、Sigmoid](./27-activations.ipynb)
28. [Dropout](./28-dropout.ipynb)
29. [类别不平衡](./29-class-imbalance.ipynb)
30. [线上漂移监控](./30-drift-monitoring.ipynb)

## 推荐复习方式

第一遍只复述每题结论；第二遍把公式中的输入、输出、假设与指标讲清；第三遍运行 01–30 的独立 Notebook，观察 baseline、核心中间量、失败样本和修正效果。面试中应主动区分“教学数据验证机制”和“线上数据证明收益”，不能用训练集高分代替泛化、校准、时延与安全证据。
