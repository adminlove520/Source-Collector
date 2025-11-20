# source-collector

本项目收集并整理了适用于不同影视应用的配置文件，方便用户快速导入和使用。

## 文件说明

### 1. 适用于 LibreTV / MoonTV 的配置
- `config_isadult.json` - 适用于 [LibreTV](https://github.com/LibreSpark/LibreTV) 和 [MoonTV](https://github.com/samqin123/MoonTV)
- `configplus_isadult.json` - 适用于 [LibreTV](https://github.com/LibreSpark/LibreTV) 和 [MoonTV](https://github.com/samqin123/MoonTV)

### 2. 适用于 OmniBox 的配置
- `sites_export_2025-0929.json` - 适用于 OmniBox (v1.2.7)

### 3. 适用于 小猫影视 的配置
- `Sites.json` - 适用于 [小猫影视](https://github.com/waifu-project/movie)
- `yoyo.json` - 适用于 [小猫影视](https://github.com/waifu-project/movie)
- `Sites.json`、`yoyo.json`自动更新地址：
- https://cdn.jsdelivr.net/gh/waifu-project/v1@latest/yoyo.json
- https://cdn.jsdelivr.net/gh/cuiocean/ZY-Player-Resources/Sites/Sites.json

> **自动更新说明**：本仓库已配置GitHub Actions工作流，每天23:00会自动从上述URL拉取最新的视频源配置并更新到仓库中，确保配置文件始终保持最新状态。

### 4. 适用于 DecoTV / LunaTV 的配置
- `video_sources_2025-11-19T09-22-39.json` - 适用于 [DecoTV](https://github.com/Decohererk/DecoTV) 和 [LunaTV](https://github.com/SzeMeng76/LunaTV)

## 免责声明

请不要在 B站、小红书、微信公众号、抖音、今日头条或其他中国大陆社交平台发布视频或文章宣传本项目，不授权任何"科技周刊/月刊"类项目或站点收录本项目。

本项目仅供学习和个人使用，为避免版权纠纷，请严格遵守相关法律法规。请勿将配置用于商业用途或公开服务。

## 鸣谢

感谢以下项目提供的参考和启发：

- [LibreTV](https://github.com/LibreSpark/LibreTV)
- [MoonTV](https://github.com/samqin123/MoonTV)
- [小猫影视](https://github.com/waifu-project/movie)
- [DecoTV](https://github.com/Decohererk/DecoTV)
- [LunaTV](https://github.com/SzeMeng76/LunaTV)

## TODO 📋

### 进行中 🔄
1. ✅ 收集并整理各影视应用配置文件
2. ⚠️ 优化README文档结构

### 后续计划 📝
1. 🔄 加入自动更新workflow
2. 📦 增加更多影视应用的配置文件支持
3. 📄 完善配置文件使用说明文档

## 注意事项

使用前请确保你已了解并接受相关软件的许可协议和使用条款。所有配置文件仅供参考，请自行承担使用风险。

## 贡献视频源

本项目支持通过GitHub Issue自动处理新的视频源提交！

### 如何贡献

1. **创建新Issue**：在GitHub仓库页面点击「Issues」→「New issue」
2. **选择模板**：选择「视频源提交」模板
3. **填写信息**：
   - 选择适用的应用范围
   - 在代码块中粘贴JSON格式的视频源数据
   - 可选择性提供备注信息
4. **提交Issue**：点击「Submit new issue」

### 自动处理流程

- 系统会自动验证您提交的JSON格式是否正确
- 自动提取视频源信息并保存到新文件中
- 更新README.md以包含新的配置文件信息
- 提交变更到仓库
- 在您的Issue下回复处理结果

### JSON格式要求

每个视频源项目应包含以下字段：
- `name`：视频源名称（必需）
- `api`：API地址（必需）
- `key`：标识符（可选，系统会自动生成）
- `detail`：详情页地址（可选）
- `disabled`：是否禁用（可选，默认为false）
- `is_adult`：是否为成人内容（可选，默认为false）

### 其他
- 已失效
    - **小猫影视**已闭源，相关配置文件也出现问题，因此在下个版本将考虑移除