# 天津中考成绩的数值分析

本文尝试对2023年度天津中考成绩进行分析，讨论学生和郊区学生在不同分数范围下的表现以及估计他们进入高中和大学的情况。

市区学生在高分范围（>750）表现更好，而郊区学生在中等分数范围（~700）表现更好。高中录取方面，市区学生的录取要求分数约为580，而郊区学生为560。

进入大学的情况根据高中入学考试成绩进行估算，其中郊区学生在985211工程大学录取中略处于劣势，而在总计录取中表现出优势。综合而言，学生的地区背景可能会对录取结果产生一定影响，

[High school entrance exam in TianJin](https://observablehq.com/@listenzcc/high-school-entrance-exam-in-tianjin)

---
- [天津中考成绩的数值分析](#天津中考成绩的数值分析)
  - [成绩分布](#成绩分布)
  - [升入高中的学生中，市区及郊区比较](#升入高中的学生中市区及郊区比较)
  - [高考预演](#高考预演)
  - [附录：数据来源](#附录数据来源)


## 成绩分布

市区学生在高分范围（>750分）表现更好。然而，在中等分数范围中（约700分），郊区学生表现更好，具体表现为他们的分布集中于此区域。而经过查询得，天津的高中采用市区和郊区分别录取的方式，分别录取30179名城市学生中的26663名和58460名郊区学生中的50326名。这种分别录取的方式在事实上使得城市学生进入高中更加困难。高中要求的分数标记为实心颜色。市区学生的必要分数约为580分，郊区学生的必要分数约为560分。

![Untitled](%E5%A4%A9%E6%B4%A5%E4%B8%AD%E8%80%83%E6%88%90%E7%BB%A9%E7%9A%84%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90%208e795da69d784f5bb9bd96318e285f90/Untitled.png)

## 升入高中的学生中，市区及郊区比较

接下来，我关注的是进入高中的学生。下图显示了每个分数范围内市区学生和郊区学生之间的比例，比例用点的颜色表示，颜色越红代表这个分数段中市区学生越高，越蓝则反之。显然，在更高的分数范围（> 750）中，市区学生占主导地位。但在较低的分数范围（< 750）中，郊区学生数量超过了城市学生。也就是说，**市区学生，如果他的成绩在 750 分及以下的成绩段中，那么他将在高中升学阶段面临更大的竞争压力。**

![Untitled](%E5%A4%A9%E6%B4%A5%E4%B8%AD%E8%80%83%E6%88%90%E7%BB%A9%E7%9A%84%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90%208e795da69d784f5bb9bd96318e285f90/Untitled%201.png)

## 高考预演

由于我没有大学入学考试成绩，所以图表是根据高中入学考试成绩进行估算的。因此，我使用高中入学考试成绩作为猜测依据。图表中的三条横线表示被大学录取的人数，它们从上到下分别代表A类大学（Total）、211工程院校及以上（985211）和仅985工程院校（985）。如果成绩保持三年不变，那么进入大学的学生成绩对应以下中考分数：

- Total：705
- 985211：750
- 985：760

在“985211”的范围内，市区学生的数量多于郊区学生，比例大约在 1.5 倍到 2.5倍之间。但在“Total”范围内，市区学生并没有显示出优势。

![Untitled](%E5%A4%A9%E6%B4%A5%E4%B8%AD%E8%80%83%E6%88%90%E7%BB%A9%E7%9A%84%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90%208e795da69d784f5bb9bd96318e285f90/Untitled%202.png)

![Untitled](%E5%A4%A9%E6%B4%A5%E4%B8%AD%E8%80%83%E6%88%90%E7%BB%A9%E7%9A%84%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90%208e795da69d784f5bb9bd96318e285f90/Untitled%203.png)

## 附录：数据来源

感谢天津考试部门提供了“一分一档”的数据图，虽然只有图，但我通过合适的 OCR 方法进行识别得到了对应的数值表。开源工程可见

[https://github.com/listenzcc/Tianjin-Highschool-entranceExamine](https://github.com/listenzcc/Tianjin-Highschool-entranceExamine)

其他信息如 2023 年度天津中考和高考招生信息我是从网上获取，链接如下

[2023年天津高考录取率多年来首降，十个百分点的差距，让选择高中成为关键](https://zhuanlan.zhihu.com/p/638991242)

[2023天津中考高中招生人数是多少](https://ruisi.ruisichina.cn/hotnews/7395.html)
