# 作品集网站设计规范

> 本文档适用于蒋云凯个人简历主页及作品集子页面的设计开发

---

## 一、基础配置

### 1.1 HTML 基础
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[页面标题] - 蒋云凯作品集</title>
</head>
```

### 1.2 CSS Reset
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
    color: #000;
    line-height: 1.6;
    background: #fff;
    overflow-x: hidden;
}
```

---

## 二、颜色体系

### 2.1 主要颜色
| 用途 | 色值 | 说明 |
|------|------|------|
| 主文字 | `#000` | 标题、重要内容 |
| 次文字 | `#4B5563` | 正文、段落 |
| 辅助文字 | `#6B7280` | 描述、说明 |
| 标签文字 | `#9CA3AF` | section标签、次要信息 |
| 边框/分割线 | `#F3F4F6` | 浅灰边框 |
| 深边框 | `#E5E7EB` | 表格边框等 |

### 2.2 强调色
| 用途 | 色值 | 说明 |
|------|------|------|
| 主强调色 | `#667EEA` | 作品集页面 highlight、边框强调 |
| 次强调色 | `#3730A3` | 主页 highlight、深紫色 |
| 链接色 | `#3730A3` | 可点击的强调文字 |

### 2.3 标签颜色组
```css
/* 紫色系 - 默认 */
.tag { background: #DDD6FE; color: #5B21B6; }

/* 蓝色系 */
.tag.blue { background: #DBEAFE; color: #1E40AF; }

/* 粉色系 */
.tag.pink { background: #FCE7F3; color: #BE185D; }

/* 绿色系 */
.tag.green { background: #D1FAE5; color: #059669; }

/* 橙色系 */
.tag.orange { background: #FED7AA; color: #C2410C; }
```

### 2.4 背景色
| 用途 | 色值 | 说明 |
|------|------|------|
| 页面背景 | `#fff` | 默认白色 |
| 浅灰背景 | `#FAFAFA` | Section交替背景、卡片背景 |
| 主页Hero | `#EBE9F4` | 淡紫色，仅用于主页 |
| 表头背景 | `#F9FAFB` | 表格头部 |

### 2.5 状态色
```css
/* 高亮框 */
.highlight-box { background: #F3F4F6; border-left: 4px solid #667EEA; }
.highlight-box.warning { background: #FEF3C7; border-left-color: #F59E0B; }
.highlight-box.success { background: #D1FAE5; border-left-color: #10B981; }

/* 指标卡片边框 */
.metric-card { border-left: 4px solid #667EEA; }
.metric-card.increase { border-left-color: #10B981; }
.metric-card.decrease { border-left-color: #EF4444; }
```

---

## 三、字体规范

### 3.1 字号体系
| 层级 | 字号 | 字重 | 用途 |
|------|------|------|------|
| H1（主页） | 56-90px | 700-800 | 页面主标题 |
| H1（作品集） | 56px | 700 | Case Hero 标题 |
| H2 Section | 48px | 700 | Section 大标题 |
| H2 Content | 36px | 700 | 内容区标题 |
| H3 | 28px | 600 | 内容子标题 |
| H4 | 20px | 600 | 小标题 |
| 正文 | 16px | 400 | 段落文字 |
| 辅助文字 | 14-15px | 400-500 | 标签、说明 |
| 小字 | 12-13px | 500 | Section Label、时间等 |

### 3.2 行高
- 标题：`1.05` - `1.15`
- 正文：`1.6` - `1.9`
- 列表项：`1.9`

### 3.3 字间距
- 大标题：`-1px` 至 `-2px`（紧缩）
- Section Label：`2px`（稀疏）

---

## 四、Header 导航

### 4.1 样式规范
```css
header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    padding: 35px 80px;
    z-index: 1000;
    background: rgba(255,255,255,0.98);
    backdrop-filter: blur(10px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #F3F4F6; /* 作品集页面有，主页无 */
}
```

### 4.2 Logo
```css
.logo {
    font-size: 22px;
    font-weight: 300;
    letter-spacing: 2px;
    color: #000;
    text-decoration: none;
}

.logo strong {
    font-weight: 700;
}
```

### 4.3 导航链接
```css
.nav-menu {
    display: flex;
    gap: 40px;
    list-style: none;
}

.nav-menu a {
    color: #000;
    text-decoration: none;
    font-size: 15px;
    font-weight: 600;
    transition: all 0.3s;
    position: relative;
}

/* 下划线hover效果 */
.nav-menu a::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 3px;
    right: -3px;
    height: 40%;
    background: #C7D2FE;
    z-index: -1;
    transition: all 0.3s;
}

.nav-menu a:hover::after {
    background: #A5B4FC;
}
```

---

## 五、Section 通用样式

### 5.1 容器与间距
```css
section {
    padding: 100px 80px; /* 作品集页面 */
    /* padding: 120px 80px; 主页 */
}

.section-container {
    max-width: 1400px;
    margin: 0 auto;
}
```

### 5.2 Section 标题组
```css
.section-label {
    font-size: 12px;
    letter-spacing: 2px;
    color: #9CA3AF;
    margin-bottom: 20px;
    text-transform: uppercase;
    font-weight: 500;
}

.section-title {
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 50px;
    color: #000;
    letter-spacing: -0.5px;
}

.section-title .highlight {
    color: #667EEA;
}
```

---

## 六、作品集子页面专用组件

### 6.1 Case Hero
```css
.case-hero {
    background: #FAFAFA;
    min-height: 60vh;
    display: flex;
    align-items: center;
    padding: 180px 80px 80px;
    color: #000;
}

.case-hero h1 {
    font-size: 56px;
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 30px;
    letter-spacing: -1px;
}

.case-hero .subtitle {
    font-size: 24px;
    font-weight: 400;
    margin-bottom: 40px;
    color: #4B5563;
}
```

### 6.2 Hero Tags（标签组）

**重要：所有标签统一使用紫色样式，不使用其他颜色变体**

```css
.hero-tags {
    display: flex;
    gap: 12px;
    margin-bottom: 50px;
    flex-wrap: wrap;
}

.hero-tag {
    padding: 8px 20px;
    background: #DDD6FE;
    color: #5B21B6;
    font-size: 13px;
    font-weight: 500;
}
```

**HTML 示例：**
```html
<div class="hero-tags">
    <span class="hero-tag">标签1</span>
    <span class="hero-tag">标签2</span>
    <span class="hero-tag">标签3</span>
</div>
```

### 6.3 Hero Stats（元信息）
```css
.hero-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 40px;
    max-width: 1000px;
}

.hero-stat {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.stat-label {
    font-size: 13px;
    color: #9CA3AF;
    font-weight: 500;
}

.stat-value {
    font-size: 20px;
    font-weight: 600;
    color: #000;
}
```

### 6.4 内容区样式
```css
.content-block {
    margin-bottom: 60px;
}

.content-block h2 {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 30px;
    color: #000;
}

.content-block h3 {
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 25px;
    margin-top: 50px;
    color: #000;
}

.content-block h4 {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 20px;
    margin-top: 40px;
    color: #000;
}

.content-block p {
    font-size: 16px;
    line-height: 1.9;
    color: #4B5563;
    margin-bottom: 20px;
}

.content-block ul, .content-block ol {
    margin-left: 30px;
    margin-bottom: 25px;
}

.content-block li {
    font-size: 16px;
    line-height: 1.9;
    color: #4B5563;
    margin-bottom: 12px;
}

.content-block strong {
    color: #000;
    font-weight: 600;
}
```

---

## 七、通用组件

### 7.1 高亮框
```css
.highlight-box {
    background: #F3F4F6;
    padding: 30px 40px;
    margin: 40px 0;
    border-left: 4px solid #667EEA;
}

.highlight-box.warning {
    background: #FEF3C7;
    border-left-color: #F59E0B;
}

.highlight-box.success {
    background: #D1FAE5;
    border-left-color: #10B981;
}
```

### 7.2 表格
```css
table {
    width: 100%;
    border-collapse: collapse;
    margin: 30px 0;
    font-size: 14px;
}

thead {
    background: #F9FAFB;
}

th {
    padding: 16px;
    text-align: left;
    font-weight: 600;
    color: #000;
    border-bottom: 2px solid #E5E7EB;
}

td {
    padding: 16px;
    color: #4B5563;
    border-bottom: 1px solid #F3F4F6;
}
```

### 7.3 指标卡片网格
```css
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 25px;
    margin: 40px 0;
}

.metric-card {
    background: #FAFAFA;
    padding: 30px;
    border-radius: 4px;
    border-left: 4px solid #667EEA;
}

.metric-card.increase { border-left-color: #10B981; }
.metric-card.decrease { border-left-color: #EF4444; }

.metric-label {
    font-size: 14px;
    color: #6B7280;
    margin-bottom: 10px;
    font-weight: 500;
}

.metric-value {
    font-size: 32px;
    font-weight: 700;
    color: #000;
    margin-bottom: 5px;
}

.metric-change {
    font-size: 14px;
    color: #6B7280;
}
```

### 7.4 引用框
```css
blockquote {
    border-left: 4px solid #D1D5DB;
    padding: 20px 30px;
    margin: 30px 0;
    background: #F9FAFB;
    font-style: italic;
    color: #4B5563;
}

blockquote cite {
    display: block;
    margin-top: 10px;
    font-size: 14px;
    color: #9CA3AF;
    font-style: normal;
}
```

### 7.5 标签组
```css
.tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 20px 0;
}

.tag {
    padding: 6px 16px;
    background: #DDD6FE;
    color: #5B21B6;
    font-size: 13px;
    font-weight: 600;
    border-radius: 0; /* 无圆角 */
}
```

### 7.6 能力矩阵/双列卡片
```css
.capability-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
    margin: 40px 0;
}

.capability-item {
    padding: 35px;
    background: #fff;
    border: 2px solid #F3F4F6;
    transition: all 0.3s;
}

.capability-item:hover {
    border-color: #667EEA;
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
}

.capability-item h3 {
    font-size: 18px;
    margin-top: 0;
    margin-bottom: 15px;
    color: #667EEA;
    font-weight: 600;
}

.capability-item p {
    margin-bottom: 0;
    font-size: 15px;
}
```

### 7.7 图片容器
```css
.image-container {
    margin: 50px 0;
    text-align: center;
}

.image-container img {
    max-width: 100%;
    height: auto;
    border: 1px solid #F3F4F6;
}

.image-caption {
    margin-top: 15px;
    font-size: 14px;
    color: #9CA3AF;
    font-style: italic;
}

/* 数据可视化图片 - 较小显示 */
.image-container.data-viz img {
    max-width: 75%;
}
```

---

## 八、按钮样式

### 8.1 主要按钮（黑色）
```css
.btn-download,
.back-button {
    display: inline-block;
    padding: 16px 40px;
    background: #000;
    color: #fff;
    text-decoration: none;
    font-size: 15px;
    font-weight: 600;
    transition: all 0.3s;
}

.back-button:hover {
    background: #667EEA;
}
```

### 8.2 带装饰边框的按钮（主页专用）
```css
.btn-download {
    position: relative;
    z-index: 1;
}

.btn-download::after {
    content: '';
    position: absolute;
    top: -6px;
    left: -6px;
    right: 6px;
    bottom: 6px;
    border: 2px solid #000;
    z-index: -1;
}

.btn-download:hover {
    transform: translate(-3px, -3px);
}

.btn-download:hover::after {
    transform: translate(3px, 3px);
}
```

---

## 九、Mermaid 图表（可选）

如需使用流程图，引入 Mermaid.js：

```html
<script type="module">
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
    mermaid.initialize({
        startOnLoad: true,
        theme: 'base',
        themeVariables: {
            primaryColor: '#F5F3FF',
            primaryTextColor: '#000000',
            primaryBorderColor: '#667EEA',
            secondaryColor: '#DBEAFE',
            tertiaryColor: '#D1FAE5',
            lineColor: '#9CA3AF',
            fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", sans-serif'
        }
    });
</script>
```

```css
.mermaid-container {
    margin: 50px 0;
    padding: 40px;
    background: #FAFAFA;
    border-radius: 4px;
    overflow-x: auto;
    border: 1px solid #F3F4F6;
}
```

---

## 十、Footer

### 10.1 样式规范
```css
footer {
    padding: 60px 80px;
    text-align: center;
    background: #FAFAFA;  /* 灰色背景，与页面形成层次 */
}

footer p {
    font-size: 13px;
    color: #9CA3AF;
}
```

### 10.2 HTML 结构
**重要：所有作品集页面 Footer 必须使用统一结构**

```html
<footer>
    <div class="section-container">
        <a href="index.html" class="back-button">← 返回作品集首页</a>
        <p style="margin-top: 30px;">© 2025 蒋云凯. All rights reserved.</p>
    </div>
</footer>
```

**注意事项：**
- Footer 背景必须为 `#FAFAFA`（灰色）
- copyright 文字必须添加 `margin-top: 30px` 与返回按钮保持间距
- 返回按钮使用 `.back-button` 样式

---

## 十一、响应式断点

```css
/* 大屏幕适配 */
@media (max-width: 1200px) { ... }

/* 平板适配 */
@media (max-width: 968px) { ... }

/* 小屏幕适配 */
@media (max-width: 768px) {
    header { padding: 25px 30px; }
    .nav-menu { gap: 20px; }
    .case-hero { padding: 140px 30px 60px; }
    .case-hero h1 { font-size: 38px; }
    .case-hero .subtitle { font-size: 18px; }
    .hero-stats { grid-template-columns: repeat(2, 1fr); gap: 25px; }
    section { padding: 60px 30px; }
    .section-title { font-size: 32px; }
    .content-block h2 { font-size: 28px; }
    .content-block h3 { font-size: 22px; }
    .metrics-grid { grid-template-columns: 1fr; }
    .capability-grid { grid-template-columns: 1fr; }
}

/* 手机适配 */
@media (max-width: 480px) { ... }
```

---

## 十二、页面模板结构

### 12.1 作品集子页面结构
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <!-- Meta + Title -->
    <style>
        /* CSS 样式 */
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <a href="index.html" class="logo"><strong>YUNKAI</strong> JIANG</a>
        <nav>
            <ul class="nav-menu">
                <li><a href="index.html">返回首页</a></li>
            </ul>
        </nav>
    </header>

    <!-- Case Hero -->
    <section class="case-hero">
        <div class="hero-container">
            <h1>项目标题</h1>
            <p class="subtitle">项目副标题/一句话描述</p>
            <div class="hero-tags">
                <span class="hero-tag">标签1</span>
                <span class="hero-tag">标签2</span>
            </div>
            <div class="hero-stats">
                <div class="hero-stat">
                    <span class="stat-label">我的角色</span>
                    <span class="stat-value">xxx</span>
                </div>
                <!-- 更多 stats -->
            </div>
        </div>
    </section>

    <!-- 核心成果 Section -->
    <section id="results">
        <div class="section-container">
            <div class="section-label">Key Results</div>
            <h2 class="section-title">核心<span class="highlight">成果</span></h2>
            <div class="metrics-grid">
                <!-- metric-card -->
            </div>
        </div>
    </section>

    <!-- 项目背景 Section -->
    <section id="overview">
        <div class="section-container">
            <div class="section-label">Project Background</div>
            <h2 class="section-title">项目<span class="highlight">背景</span></h2>
            <div class="content-block">
                <!-- 内容 -->
            </div>
        </div>
    </section>

    <!-- 更多 Sections... -->

    <!-- Footer -->
    <footer>
        <div class="section-container">
            <a href="index.html" class="back-button">← 返回作品集首页</a>
            <p style="margin-top: 30px;">© 2025 蒋云凯. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

---

## 十三、设计原则

1. **无圆角设计**：所有按钮、标签、卡片均不使用圆角（border-radius: 0 或 4px 微圆角）
2. **黑白为主，紫色强调**：主色调为黑白灰，强调色使用紫色系 `#667EEA`
3. **大留白**：Section 间距保持 80-120px，内容区保持充足呼吸感
4. **字重对比**：标题使用 600-800 粗字重，正文使用 400 常规字重
5. **负字间距标题**：大标题使用 -1px 到 -2px 字间距，更紧凑专业
6. **状态色语义**：绿色表示增长/成功，红色表示下降/警告，橙色表示中性提示
