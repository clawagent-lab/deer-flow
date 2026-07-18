# 思考块功能 (Thought Block)

## 概述

思考块功能允许在计划卡片之前展示 AI 的深度思考过程，以可折叠的方式呈现推理内容。该功能在启用深度思考模式、且模型输出 `reasoning_content` 时激活。

## 功能特性

- **智能展示逻辑**：深度思考过程初始展开，当开始接收计划内容时自动折叠
- **分阶段显示**：思考阶段只显示思考块，思考结束后才显示计划卡片
- **流式支持**：推理内容实时流式展示，静态部分与当前流式分块分别渲染
- **视觉状态反馈**：思考阶段使用 primary 主题色（边框/背景/图标/文字）突出显示，完成后切换为默认主题
- **优雅的动画**：展开/折叠动画、主题切换过渡，计划卡片入场有淡入+上滑动画
- **响应式设计**：适配不同屏幕尺寸

## 交互流程

```
用户发送问题（启用深度思考）
    ↓
开始接收 reasoning_content
    ↓
思考块自动展开 + primary 主题 + 加载动画
    ↓
推理内容流式更新（静态部分 opacity-80，当前分块 prose-primary）
    ↓
开始接收 content（计划内容）
    ↓
思考块自动折叠 + 主题切换为默认
    ↓
计划卡片优雅出现（opacity 0→1，y 20→0，300ms）
    ↓
计划内容保持流式更新（标题 → 思路 → 步骤）
    ↓
完成（用户可手动展开思考块查看推理过程）
```

## 技术实现

### 数据结构扩展

1. `web/src/core/messages/types.ts` — `Message` 接口新增字段：
   ```typescript
   reasoningContent?: string;
   reasoningContentChunks?: string[];
   ```

2. `web/src/core/api/types.ts` — `MessageChunkEvent` 新增字段：
   ```typescript
   reasoning_content?: string;
   ```

### 消息合并逻辑

`web/src/core/messages/merge-message.ts` 中的 `mergeTextMessage` 同时处理常规内容与推理内容：

```typescript
function mergeTextMessage(message: Message, event: MessageChunkEvent) {
  if (event.data.content) {
    message.content += event.data.content;
    message.contentChunks.push(event.data.content);
  }
  if (event.data.reasoning_content) {
    message.reasoningContent = (message.reasoningContent ?? "") + event.data.reasoning_content;
    message.reasoningContentChunks = message.reasoningContentChunks ?? [];
    message.reasoningContentChunks.push(event.data.reasoning_content);
  }
}
```

### 组件结构

- **ThoughtBlock**（`web/src/app/chat/components/message-list-view.tsx`）：可折叠的思考块组件，使用 Radix UI 的 `Collapsible`。内部将内容拆分为静态部分（已完成的分块）与当前流式分块，分别以不同样式渲染。
- **PlanCard**（同文件）：计划卡片，在渲染计划内容前判断并展示 `ThoughtBlock`，自动检测是否存在 `reasoningContent`。

### 状态逻辑

```typescript
const reasoningContent = message.reasoningContent;
const hasMainContent = Boolean(message.content && message.content.trim() !== "");

// 是否正在思考：有推理内容但还没有主要内容
const isThinking = Boolean(reasoningContent && !hasMainContent);

// 是否显示计划：有主要内容就显示，保持流式效果
const shouldShowPlan = hasMainContent;
```

`ThoughtBlock` 接收 `isStreaming={isThinking}`（注意：传入的是思考状态而非消息整体流式状态），并接收 `hasMainContent` 用于触发自动折叠。

### 自动折叠逻辑

```typescript
const [hasAutoCollapsed, setHasAutoCollapsed] = useState(false);
React.useEffect(() => {
  if (hasMainContent && !hasAutoCollapsed) {
    setIsOpen(false);
    setHasAutoCollapsed(true);
  }
}, [hasMainContent, hasAutoCollapsed]);
```

一旦开始接收计划内容，思考块折叠一次，之后不再因状态变化自动展开。

### 计划卡片入场动画

```tsx
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.3, ease: "easeOut" }}
>
```

## 样式特性

- **统一设计语言**：与页面整体设计风格保持一致，详见 `thought-block-design-system.md`
- **字体层次**：`font-semibold` 字体权重，与 CardTitle 一致
- **圆角设计**：`rounded-xl`，与其他卡片组件统一
- **间距规范**：`px-6 py-4` 内边距，`mb-6` 外边距
- **动态主题**：思考阶段使用 primary 色彩系统（非硬编码颜色，随主题切换）
- **图标**：18px `Lightbulb`（灯泡）图标
- **标题文案**：使用翻译键 `chat.research.deepThinking`（中文「深度思考」/ 英文「Deep Thinking」）
- **状态反馈**：流式传输时显示加载动画和 primary 色高亮
- **平滑过渡**：所有状态变化 200ms 过渡

## 使用方法

### 启用深度思考模式

1. 在聊天界面中点击「Deep Thinking」按钮
2. 确保配置了支持推理的模型（如 DeepSeek R1）
3. 发送消息后，若有推理内容，会在计划卡片上方显示思考块

### 查看推理过程

1. 深度思考开始时，思考块自动展开显示
2. 思考阶段使用 primary 主题色，突出显示正在进行的推理
3. 推理内容支持 Markdown 格式渲染，实时流式更新
4. 流式传输过程中显示加载动画
5. 当开始接收计划内容时，思考块自动折叠
6. 计划卡片以入场动画出现
7. 计划内容保持流式输出，逐步显示标题、思路和步骤
8. 用户可随时点击思考块标题栏手动展开/折叠

## 测试数据

可使用 `web/public/mock/reasoning-example.txt` 测试思考块功能，访问 `http://localhost:3000?mock=reasoning-example` 并发送任意消息即可。该文件包含模拟的推理内容（`reasoning_content`）和计划数据（`content`）。

详细测试方法见 `testing-guide.md`。

## 兼容性

- **向后兼容**：没有推理内容的消息不会显示思考块
- **渐进增强**：功能仅在有 `reasoningContent` 时激活
- **优雅降级**：推理内容为空时组件不渲染（`content.trim() === ""` 时返回 `null`）
