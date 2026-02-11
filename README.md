# 个人主页 & 作品集

🌐 **在线访问**: [kaysensei.com](https://kaysensei.com)

## 简介

这是我的个人主页和作品集网站，展示了我的产品设计和用户研究项目经验。

## 主要内容

- **个人简介**: 产品设计师 & 用户研究员
- **项目案例**:
  - Yalla Group - VIP用户体验优化
  - 纳里健康 - 居家康养服务平台
  - 微脉 - 医疗健康服务平台
- **在线简历**: HTML 版本和 PDF 下载

## 技术栈

- 纯 HTML + CSS (响应式设计)
- Cloudflare Pages (部署)
- GitHub (版本控制)

## 本地预览

直接在浏览器中打开 `index.html` 即可。

## 部署

推送到 `main` 分支后，Cloudflare Pages 会自动部署（通常需要 1-3 分钟）。

### Git 推送配置

已配置 SSH 密钥认证，推送代码使用：
```bash
git add .
git commit -m "your message"
git push
```

### 故障排除

#### 部署未生效怎么办？

如果推送代码后网站没有更新：

1. **检查线上版本**
   ```bash
   curl -s https://kaysensei.com | grep -o '<title>.*</title>'
   ```

2. **手动触发重新部署**
   ```bash
   git commit --allow-empty -m "chore: trigger Cloudflare Pages redeploy"
   git push
   ```

3. **检查部署状态**
   - GitHub Deployments: https://github.com/jiangyksensei/resume-portfolio/deployments
   - Cloudflare Pages Dashboard: https://dash.cloudflare.com

4. **清除浏览器缓存**
   - Mac: `Cmd + Shift + R` (硬刷新)
   - Windows: `Ctrl + Shift + R` (硬刷新)

#### 部署记录

- **2026-02-11 下午**: 更新网站标题后自动部署未生效，通过空提交手动触发重新部署成功

## 重要说明

### 网站标题
- 当前标题：**蒋云凯-用户研究/体验设计师**
- 更新日期：2026-02-11

### 中国访问性
- **托管平台**：Cloudflare Pages
- **访问情况**：在中国大陆可能存在访问不稳定的情况
- **原因**：Cloudflare IP 在部分地区/运营商可能被屏蔽
- **测试工具**：
  - [17CE 网站测速](https://www.17ce.com)
  - [ViewDNS 防火墙测试](https://viewdns.info/chinesefirewall/)
  - [China Firewall Test](https://www.chinafirewalltest.com)

**注意**：如果遇到 `ERR_PROXY_CONNECTION_FAILED` 错误，通常是本地代理设置问题，需关闭代理或检查 VPN 设置。

## 项目文档

详细的项目指南和维护文档请查看 [PROJECT-GUIDE.md](./PROJECT-GUIDE.md)

---

**License**: MIT
**作者**: 蒋云凯 (Kay Sensei)
