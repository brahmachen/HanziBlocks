<div align="center">
  <!-- 预留给你放游戏动图的地方 -->
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjEx.../giphy.gif" alt="HanziBlocks Demo" width="600">
  
  # 🧱 HanziBlocks (汉字积木)

  **A Physics-Based Interactive Chinese Character Puzzle Engine**  
  基于 **PixiJS (WebGL)** 与 **Matter.js (2D Physics)** 构建的动态汉字解构与游戏化拼搭引擎。

  [Play the Demo](https://brahmachen.github.io/HanziBlocks/) <!-- 预留 GitHub Pages 链接 -->
  ·
  [Report Bug](https://github.com/brahmachen/HanziBlocks/issues)
  ·
  [Request Feature](https://github.com/brahmachen/HanziBlocks/issues)

  <br>
  
  ![PixiJS](https://img.shields.io/badge/PixiJS-v7.3-E34F26?style=flat-square&logo=html5)
  ![Matter.js](https://img.shields.io/badge/Matter.js-v0.19-F7DF1E?style=flat-square&logo=javascript)
  ![SVG Data](https://img.shields.io/badge/Data-SVG_Vector-007ACC?style=flat-square)
  ![License](https://img.shields.io/badge/License-MIT-blue.svg)
</div>

---

## 🌟 理念与起源 (Why HanziBlocks?)

汉字不是一条线性的拼音字符串，而是一组极具建筑美学和空间力学的**二维结构积木** (2D Structural Lego)。

在传统的儿童识字软件中，汉字的拆解往往依赖昂贵且死板的手绘帧动画（Frame-by-frame Animation）。这导致内容生产成本极高，且缺乏真实的交互反馈。

**HanziBlocks 提出了一种降维打击的工程解法：**
我们不画任何一张图片（No PNGs/JPGs）。我们直接提取汉字国标字库中每一笔画的 **SVG Path (矢量路径)**，利用动态掩码与锚点偏移，将它们与 **2D 物理刚体 (Rigid Bodies)** 绑定。

玩家（或孩子）抓起的不是死板的图片，而是带有质量、弹性和碰撞体积的真实“木块”。当两半部首被拖拽至统一的绝对坐标系并触发**“物理吸附 (Snap)”**时，它们会在像素级别完美缝合成一幅出自同一位书法家之手的字，中间绝无任何硬切缝隙。

---

## ✨ 核心特性 (Features)

*   **🧲 像素级严丝合缝 (Seamless Vector Snapping):** 
    基于绝对坐标系的 SVG 拆解方案，放弃遮罩硬切。偏旁部首吸附合并后，渲染结果完美还原原版书法字形。
*   **⚖️ 真实的物理反馈 (Physics Engine):** 
    基于 `Matter.js`。字块在空中具有重力，互相之间会发生碰撞、旋转与反弹，极大地提升了试错和拖拽的乐趣（Juiciness）。
*   **💦 丰富的爽感演出 (Game Feel & Juiciness):**
    *   吸附瞬间的果冻弹簧动画 (Jelly Bounce / Damped Sine Wave)。
    *   纯代码合成的无加载音效 (Web Audio API Oscillator)——清脆的木块咔哒声与胜利和弦。
    *   自带浏览器原生 TTS (Text-to-Speech) 的汉字拼音朗读。
    *   动态全屏粒子爆炸系统。
*   **♾️ 极低的拓展边际成本 (Infinite Scalability):**
    由于渲染层完全解耦，只需接入如 [Make Me A Hanzi](https://github.com/skishore/makemeahanzi) 的开源字库 JSON，通过映射表即可一键生成 8000+ 个高级交互关卡，无需任何美术介入。

---

## 🛠️ 技术栈 (Tech Stack)

*   **渲染层 (Renderer):** [PixiJS (v7.x)](https://pixijs.com/) - 利用 WebGL 提供无限放大的抗锯齿 SVG 渲染与粒子特效。
*   **物理层 (Physics):** [Matter.js](https://brm.io/matter-js/) - 轻量级 2D 刚体物理引擎，处理重力、碰撞与多边形包围盒。
*   **音频层 (Audio):** 纯原生 `window.AudioContext` 代码合成，零外部 MP3 资源依赖。

---

## 🚀 快速开始 (Quick Start)

本项目为纯前端架构，无需任何复杂的 Node.js 或 Webpack 构建环境（MVP 阶段）。

### 1. 克隆项目
```bash
git clone https://github.com/brahmachen/HanziBlocks.git
cd HanziBlocks
```

### 2. 本地运行
由于浏览器存在 CORS 跨域安全策略（影响本地 Canvas 读取 SVG Blob），你必须通过一个本地 HTTP 服务器来运行 HTML 文件。

如果你有 Python环境，最简单的方法是：
```bash
# Python 3
python3 -m http.server 8080

# 或者使用 Node.js 的 http-server
# npx http-server -p 8080
```

### 3. 体验
在浏览器中打开：`http://localhost:8080/v4-juice.html` (或你的主入口文件)。

> **⚠️ 音频策略提示:** 现代浏览器禁止自动播放声音，进入页面后请先**点击屏幕**或**拖拽积木**以激活 Web Audio 引擎。

---

## 🗺️ 路线图 (Roadmap)

- [x] **MVP:** 跑通 PixiJS + Matter.js + SVG 锚点对齐的核心物理拼搭链路。
- [x] **Juice:** 补齐碰撞音效、粒子爆炸、果冻弹跳等感官反馈。
- [ ] **Data Pipeline:** 编写 Node.js 提取脚本，将 `MakeMeAHanzi` 开源字库的 8000 汉字批量转换为组件化的 `level_data.json`。
- [ ] **Level System:** 实现关卡切换、难度分级（左右结构、包围结构、三品结构）。
- [ ] **Mobile Touch:** 优化移动端的触摸拖拽（Touch Events）响应手感与边界阻挡。

---

## 🤝 贡献与灵感 (Acknowledgements)

*   **汉字矢量数据来源:** 感谢 [Make Me A Hanzi](https://github.com/skishore/makemeahanzi) 项目提供的海量开源 SVG 笔画与字形数据。

---

## 📄 开源协议 (License)

Distributed under the MIT License. See `LICENSE` for more information.