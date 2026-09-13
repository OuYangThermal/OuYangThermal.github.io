---
title: "IGBT / SiC导热绝缘材料怎么选？"
description: "IGBT与SiC功率模块导热绝缘材料选型：低热阻、电气绝缘、厚度、接触热阻、安装压力、平整度和可靠性。"
permalink: /zh/igbt-sic/
lang: zh-CN
alternate_en: /thermal-insulator/thermal-insulator-supplier-for-igbt-modules/
---

<div class="quick"><strong>直接回答</strong><p>IGBT或SiC功率模块选择导热绝缘材料时，第一步不是找最高导热系数，而是确认电气绝缘由模块内部承担，还是由模块与冷板之间的界面承担。确定绝缘系统后，再比较安装厚度下的热阻、接触热阻、平整度适应能力、安装压力、边缘与孔位安全，以及老化后的热学和电气性能。</p></div>

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/igbt-sic-thermal-insulator-selection-matrix.webp' | relative_url }}" width="1672" height="941" loading="lazy" decoding="async" alt="IGBT和SiC功率模块导热绝缘材料选择矩阵，对比薄膜涂层、陶瓷类和柔性绝缘垫片"><figcaption><strong>工程示意图。</strong> Source: OUYANG THERMAL · Owen Ouyang。具体选择取决于完整绝缘系统和应用验证。</figcaption></figure>

## 低热阻与绝缘不是一个指标

热阻需要同时考虑材料本体和两侧接触界面。减薄材料可以降低本体热阻，但薄而硬的材料可能无法补偿粗糙度或平面度，从而提高接触热阻。柔性绝缘垫片更容易贴合，却可能形成更厚的热路径。陶瓷类方案具有不同的热学、电气和机械组合，也必须与表面、安装和应力条件匹配。

电气方面，短时击穿或电气强度数据不能直接等同于持续工作电压。要结合绝缘等级、爬电距离、电气间隙、边缘、孔位、紧固件、污染、温湿度和老化评估完整系统。

## IGBT与SiC应用差异怎么处理

不能简单地规定“SiC一定需要某种材料”。SiC器件可能带来更高功率密度、更快开关和不同结温边界，但实际界面仍由模块结构、底板、绝缘位置、冷却方式、安装压力和可靠性要求决定。IGBT和SiC都应回到相同的界面定义流程。

| 选择条件 | 主要关注点 |
| --- | --- |
| 模块内部已经绝缘 | 可评估薄Grease、PCM或其他非绝缘TIM，但需确认系统责任边界 |
| 界面承担绝缘 | 材料厚度、边缘、孔位、紧固件和老化后绝缘必须验证 |
| 表面平整、BLT可控 | 可以筛选较薄的膜、涂层或刚性方案 |
| 平整度变化或间隙较大 | 需要更好的贴合能力，同时核算压缩后厚度和压力 |
| 大面积安装 | 单位面积压力与总夹紧力都要计算，避免模块或冷板变形 |

## 供应商送样前需要什么

提供模块/冷板界面图、厚度与平面度公差、接触面积、紧固方式、安装压力或扭矩控制、电气功能、温度范围和可靠性要求。比较样品时统一厚度、压力、表面处理、温度和测试方法。

验证至少覆盖尺寸与厚度、热阻、电气测试条件、安装过程、边缘和污染检查、相关温度/功率循环，以及老化后的热学和绝缘复测。还应检查多批次、模切质量、包装、追溯和变更通知。

相关中文页：[TIM总选型]({{ '/zh/thermal-interface-materials/' | relative_url }}) · [导热垫片验证]({{ '/zh/thermal-pad/' | relative_url }}) · [IGBT / SiC选择矩阵]({{ '/zh/engineering-resources/' | relative_url }}#igbt-sic-insulator-matrix)

英文深度页：[IGBT Thermal Insulator Supplier Qualification]({{ '/thermal-insulator/thermal-insulator-supplier-for-igbt-modules/' | relative_url }})

[Benchmark现有界面]({{ '/benchmark-your-current-tim/' | relative_url }}) · [联系Owen Ouyang（欧阳小辉）]({{ '/discuss-your-application/' | relative_url }})

