# -*- coding: utf-8 -*-
"""Qwen2.5-3B-Instruct 对话与文本生成 WebUI 演示（不加载真实模型权重）。"""
from __future__ import annotations

import gradio as gr


def fake_load_model():
    """模拟加载 Qwen2.5-3B-Instruct 模型，仅用于界面演示。"""
    return "模型状态：Qwen2.5-3B-Instruct 已就绪（演示模式，未加载真实权重）"


def fake_generate(user_input: str, max_tokens: int, temperature: float) -> str:
    """模拟对话生成与可视化结果。"""
    if not (user_input or "").strip():
        return "请输入对话内容以进行生成。"
    tokens = max(1, min(2048, int(max_tokens) if isinstance(max_tokens, (int, float)) else 512))
    temp = max(0.0, min(2.0, float(temperature) if isinstance(temperature, (int, float)) else 0.7))
    lines = [
        "[演示] 已对输入进行 Qwen2.5-3B-Instruct 文本生成（未加载真实模型）。",
        f"输入：{user_input[:200]}{'...' if len(user_input) > 200 else ''}",
        f"参数：max_tokens={tokens}, temperature={temp:.2f}",
        "",
        "示例输出（占位）：",
        "作为通义千问助手，我理解您的问题。在演示模式下，此处将显示模型生成的回复。",
        "加载真实 Qwen2.5-3B-Instruct 模型后，将在此展示真实的对话与生成结果。",
    ]
    return "\n".join(lines)


def build_ui():
    with gr.Blocks(title="Qwen2.5-3B-Instruct WebUI") as demo:
        gr.Markdown("## Qwen2.5-3B-Instruct · 对话与文本生成 WebUI 演示")
        gr.Markdown(
            "本界面以交互方式展示 Qwen2.5-3B-Instruct 的典型使用流程："
            "模型加载、对话输入及生成结果可视化（演示模式，未加载真实模型）。"
        )

        with gr.Row():
            load_btn = gr.Button("加载模型（演示）", variant="primary")
            status_box = gr.Textbox(label="模型状态", value="尚未加载", interactive=False)
        load_btn.click(fn=fake_load_model, outputs=status_box)

        with gr.Tabs():
            with gr.Tab("对话生成"):
                gr.Markdown("输入对话内容与生成参数，模型将进行文本生成并展示结果。")
                user_in = gr.Textbox(
                    label="对话输入",
                    placeholder="例如：请用简单语言解释什么是大语言模型。",
                    lines=3,
                )
                max_tokens = gr.Slider(64, 2048, value=512, step=64, label="最大生成长度 (tokens)")
                temperature = gr.Slider(0.1, 2.0, value=0.7, step=0.1, label="Temperature")
                gen_btn = gr.Button("生成（演示）")
                gen_out = gr.Textbox(
                    label="生成结果说明",
                    lines=12,
                    interactive=False,
                )
                gen_btn.click(
                    fn=fake_generate,
                    inputs=[user_in, max_tokens, temperature],
                    outputs=gen_out,
                )

            with gr.Tab("模型信息"):
                gr.Markdown(
                    "Qwen2.5-3B-Instruct 为指令微调后的 3B 参数因果语言模型，"
                    "支持 32K 上下文与 8K 生成，具备多语言与代码能力。"
                )
                info_out = gr.Textbox(
                    label="模型信息",
                    value=(
                        "[演示] 模型：Qwen2.5-3B-Instruct\n"
                        "参数量：3.09B | 层数：36 | 注意力：GQA 16/2\n"
                        "上下文：32,768 tokens | 生成：8,192 tokens\n"
                        "架构：RoPE, SwiGLU, RMSNorm"
                    ),
                    lines=6,
                    interactive=False,
                )

        gr.Markdown(
            "---\n*说明：当前为轻量级演示界面，未实际下载与加载 Qwen2.5-3B-Instruct 模型参数。*"
        )
    return demo


def main():
    app = build_ui()
    app.launch(server_name="127.0.0.1", server_port=8766, share=False)


if __name__ == "__main__":
    main()
