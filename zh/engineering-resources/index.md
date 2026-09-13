---
title: "导热材料工程资源与工具"
description: "OUYANG THERMAL中文导热材料工程资源：供应商验证、第二供应商、压缩与BLT、凝胶失效、IGBT/SiC绝缘及热阻计算器。"
permalink: /zh/engineering-resources/
lang: zh-CN
alternate_en: /engineering-resources/
---

<div class="quick"><strong>直接回答</strong><p>本页集中整理OUYANG THERMAL可用于工程讨论和内部评审的原创检查表、流程图、决策图与计算工具。它们用于明确问题和设计验证计划，不替代项目测试、产品安全评估或客户批准。</p></div>

## 六项核心资源

### 1. 导热垫片供应商12项验证 {#thermal-pad-12-gate-checklist}

解决“一个样品测试通过，是否可以进入量产”的问题。检查范围从需求、厚度、压缩、热学、电气和模切，一直到可靠性、多批次、Pilot Build和变更管理。

[查看中文送样与量产验证指南]({{ '/zh/thermal-pad/' | relative_url }}) · [查看英文12-Gate原图与深度页]({{ '/thermal-pad-supplier-china/' | relative_url }})

### 2. TIM第二供应商验证流程 {#tim-second-source-workflow}

解决“候选材料参数相近，为什么仍不能直接替换”的问题。正确流程是先冻结需求和现有材料Benchmark，再进行Sample、热学/机械/电气、可靠性、多批次和Pilot Build验证，最后进入供应商资格与RFQ。

[查看英文Second-Source流程图]({{ '/engineering-resources/' | relative_url }}#tim-second-source-workflow)

### 3. 压缩率、BLT与接触热阻 {#thermal-pad-compression-blt-guide}

解决“压缩越多是否一定散热越好”的问题。压缩可能改善接触，但也会改变BLT并增加器件、PCB或壳体受力。必须同时验证最大间隙接触和最小间隙压力。

[查看中文导热垫片指南]({{ '/zh/thermal-pad/' | relative_url }}) · [查看英文决策图]({{ '/engineering-resources/' | relative_url }}#thermal-pad-compression-blt-guide)

### 4. 导热凝胶失效诊断 {#thermal-gel-failure-diagnosis}

用于区分Void、Slump、Pump-Out、Squeeze-Out和Incomplete Cure。排查时应把来料与储存、计量混合、点胶、装配几何和可靠性循环分开记录。

[查看中文导热凝胶指南]({{ '/zh/thermal-gel/' | relative_url }}) · [查看英文失效诊断图]({{ '/engineering-resources/' | relative_url }}#thermal-gel-failure-diagnosis)

### 5. IGBT / SiC导热绝缘选择矩阵 {#igbt-sic-insulator-matrix}

用于比较薄膜/涂层、陶瓷类和柔性绝缘垫片，以及模块内部已经绝缘时可评估的非绝缘TIM。重点不是给出统一答案，而是确认绝缘系统、厚度、接触、压力、返修与老化验证。

<figure class="engineering-visual"><img src="{{ '/assets/images/visual-content/igbt-sic-thermal-insulator-selection-matrix.webp' | relative_url }}" width="1672" height="941" loading="lazy" decoding="async" alt="IGBT和SiC导热绝缘材料选择矩阵"><figcaption><strong>工程示意图。</strong> Source: OUYANG THERMAL · Owen Ouyang。需要结合完整绝缘系统验证。</figcaption></figure>

[查看中文IGBT / SiC选型页]({{ '/zh/igbt-sic/' | relative_url }})

### 6. 理论热阻计算器

输入导热系数、厚度/BLT和接触面积，计算均匀材料层的理论本体热阻 `R=t/(kA)`。结果不包含接触热阻、平整度、压力、老化和散热器边界。

[打开Thermal Resistance Calculator]({{ '/engineering-resources/thermal-resistance-calculator/' | relative_url }})

## 使用与引用

可在技术和教育内容中引用，但请注明来源为 **OUYANG THERMAL**，并链接至对应原始资源。所有图表都是工程筛选与验证框架，不代表客户案例、认证结果或通用设计限值。

[返回中文首页]({{ '/zh/' | relative_url }}) · [TIM总选型]({{ '/zh/thermal-interface-materials/' | relative_url }}) · [Benchmark现有TIM]({{ '/benchmark-your-current-tim/' | relative_url }}) · [联系Owen Ouyang（欧阳小辉）]({{ '/discuss-your-application/' | relative_url }})

