# 个人主页 & 作品集项目指南

**项目地址**: https://kaysensei.com
**GitHub 仓库**: https://github.com/jiangyksensei/resume-portfolio
**部署平台**: Cloudflare Pages

---

## 📁 项目结构

```
resume-portfolio/
├── index.html                  # 主页（个人介绍 + 项目列表）
├── resume-jyk.html            # 在线简历（HTML版）
├── 蒋云凯-简历.pdf             # PDF简历（供下载）
│
├── 案例详情页
│   ├── yalla-case-study.html      # Yalla项目案例
│   ├── nali-health.html           # 纳里健康案例
│   ├── home-care-service.html     # 居家护理案例
│   └── project-wemai-final.html   # 微脉项目案例
│
├── images/                     # 所有图片资源
│   ├── avatar.jpg             # 头像（压缩版，1.1MB）
│   ├── 7_research_*.jpg       # 研究框架图（压缩版）
│   └── ...                    # 其他项目图片
│
├── backup/                     # 备份文件
│   └── index.copy.html        # 主页备份
│
├── docs/                       # 文档
│   └── DESIGN-SPEC.md         # 设计规范
│
└── .gitignore                  # Git忽略配置
```

---

## 🚀 快速开始

### 本地预览
直接在浏览器中打开 `index.html` 即可预览。

### 修改内容
1. 编辑对应的 HTML 文件
2. 如果修改了图片，确保文件大小合理（建议单个图片 < 500KB）
3. 如果修改了 `resume-jyk.html`，需要重新生成 PDF

---

## 📝 常见操作

### 1. 更新简历内容

**编辑简历**：
```bash
# 编辑 resume-jyk.html
open resume-jyk.html
```

**重新生成 PDF**：
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --print-to-pdf="蒋云凯-简历.pdf" \
  --print-to-pdf-no-header \
  --no-pdf-header-footer \
  resume-jyk.html
```

### 2. 添加新项目案例

1. 创建新的 HTML 文件（参考 `yalla-case-study.html` 结构）
2. 将项目图片放到 `images/` 目录
3. 在 `index.html` 的项目列表中添加链接
4. 提交并推送到 GitHub

### 3. 优化图片

**压缩 PNG 为 JPEG**（建议大图片使用）：
```bash
# 压缩单个图片
sips -s format jpeg -s formatOptions 80 images/原图.png --out images/原图.jpg

# 批量压缩
for f in images/*.png; do
  sips -s format jpeg -s formatOptions 80 "$f" --out "${f%.png}.jpg"
done
```

**优化建议**：
- 头像、截图：< 500KB
- 大型框架图：< 500KB
- 小图标：< 100KB
- 优先使用 JPG/WebP 格式

---

## 🌐 部署流程

### 初次部署（已完成）
✅ GitHub 仓库已创建
✅ Cloudflare Pages 项目已配置
✅ 自定义域名 kaysensei.com 已绑定
✅ SSL 证书已自动配置

### 更新网站内容

```bash
# 1. 提交更改
git add -A
git commit -m "更新说明"

# 2. 推送到 GitHub（需要使用 token）
git remote set-url origin https://ghp_YOUR_TOKEN@github.com/jiangyksensei/resume-portfolio.git
git push

# 3. 清理 token（安全起见）
git remote set-url origin https://github.com/jiangyksensei/resume-portfolio.git
```

**注意**：
- GitHub Token 保存在安全位置（需要时再设置）
- Cloudflare 会自动检测推送并重新部署（1-2分钟）
- 部署完成后访问 https://kaysensei.com 查看效果

### 手动触发部署

如果需要手动部署（不推送到 GitHub）：
```bash
CLOUDFLARE_API_TOKEN=YOUR_TOKEN npx wrangler pages deploy . --project-name=resume-portfolio
```

---

## 🔑 配置信息

### GitHub
- **仓库**: https://github.com/jiangyksensei/resume-portfolio
- **分支**: main
- **Token**: 保存在密码管理器中

### Cloudflare
- **项目名**: resume-portfolio
- **生产域名**: https://kaysensei.com
- **预览域名**: https://resume-portfolio-1xs.pages.dev
- **Account ID**: f26ade07ec9368ce26568220f433b2de
- **Zone ID**: 9fd9ba93ce4b2c07f914ea71b3d04c8f
- **API Token**: 保存在密码管理器中

---

## 📊 性能优化记录

### 2026-02-10 图片优化
- **avatar.png**: 6.2MB → 1.1MB (↓82%)
- **7_research_cycle.png**: 5.5MB → 413KB (↓93%)
- **7_research_framework.png**: 5.3MB → 485KB (↓91%)
- **总节省**: ~16MB → ~2MB (↓87%)

**优化方法**：转换为 JPEG 格式并调整质量参数

---

## 🛠️ 技术栈

- **前端**: 纯 HTML + CSS (响应式设计)
- **部署**: Cloudflare Pages (静态网站托管)
- **版本控制**: Git + GitHub
- **域名**: Cloudflare DNS
- **SSL**: Cloudflare Universal SSL (自动)

---

## 📋 维护检查清单

### 定期检查（每季度）
- [ ] 检查所有链接是否有效
- [ ] 更新项目案例和数据
- [ ] 检查图片加载速度
- [ ] 更新简历内容
- [ ] 检查移动端显示效果

### 添加新内容时
- [ ] 图片已优化（< 500KB）
- [ ] 所有链接测试通过
- [ ] 移动端显示正常
- [ ] 提交信息清晰
- [ ] 推送后验证部署成功

---

## 🐛 常见问题

### Q: 推送时提示 "could not read Username"
**A**: 需要在 remote URL 中添加 GitHub token：
```bash
git remote set-url origin https://TOKEN@github.com/jiangyksensei/resume-portfolio.git
```

### Q: 网站更新后没有生效
**A**:
1. 清除浏览器缓存（Cmd+Shift+R）
2. 检查 Cloudflare Pages 部署状态
3. 等待 1-2 分钟让 CDN 缓存更新

### Q: 图片加载慢
**A**:
1. 检查图片大小（应 < 500KB）
2. 使用 JPG 格式替代 PNG
3. 使用图片压缩工具优化

### Q: PDF 简历没有更新
**A**: 修改 `resume-jyk.html` 后需要重新生成 PDF（见"重新生成 PDF"章节）

---

## 📞 联系方式

如有问题或需要帮助，可以参考：
- [Cloudflare Pages 文档](https://developers.cloudflare.com/pages/)
- [GitHub 文档](https://docs.github.com/)

---

**最后更新**: 2026-02-10
**维护者**: 蒋云凯 (Kay Sensei)
