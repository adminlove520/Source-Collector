---
name: 视频源提交
about: 提交新的视频源配置
title: '新视频源提交：[请输入名称]'
labels: 'video-source'
assignees: ''
---

## 视频源信息

### 适用范围
请选择适用的应用（可多选）：
- [ ] LibreTV
- [ ] MoonTV
- [ ] 小猫影视
- [ ] OmniBox
- [ ] DecoTV
- [ ] LunaTV
- [ ] 其他（请注明）：_________

### 视频源数据
请在此处粘贴JSON格式的视频源数据（使用代码块包装）：

```json
[
  {
    "name": "示例视频源",
    "key": "example_key",
    "api": "https://example.com/api",
    "detail": "https://example.com",
    "disabled": false,
    "is_adult": false
  }
  // 可以添加更多视频源项目
]
```

### 备注信息（可选）
请提供任何其他相关信息，如视频源的特点、更新频率等：

---

> 提交即表示您同意此视频源可被用于本项目，并且内容符合相关法律法规。
> 系统将自动处理您的提交，并将有效的视频源添加到仓库中。