# app.py  ·  阿里云（公共云）外部市场 & 客户洞察 · v4
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ---------- 页面与样式 ----------
st.set_page_config(page_title="阿里云公共云 · 市场洞察Demo", layout="wide")

st.markdown("""
<style>
:root { --pri:#0ea5e9; --pri2:#22c55e; --bg:#0b1220; --panel:#0f172a; --txt:#f8fafc; }
html, body, [class*="css"] { background: var(--bg)!important; color: var(--txt)!important; }
.hero {
  background: radial-gradient(1200px 600px at 10% -10%, #1f355a 0%, #F2A36B 60%);
  border: 1px solid rgba(255,255,255,.08); border-radius: 18px; padding: 26px 28px; margin-bottom: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,.35);
}
.hero h1 { color:#f9fafb; font-size: 34px; margin-bottom:6px; }
.hero p { color:#e2e8f0; opacity:.85; margin:0; }
.kpi { background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.03));
  border: 1px solid rgba(255,255,255,.08); border-radius:16px; padding:14px; text-align:center; }
.kpi h2 { margin:6px 0 2px 0; font-size:34px;}
.kpi p { margin:0; opacity:.85 }
.panel { background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.03));
  border:1px solid rgba(255,255,255,.08); border-radius:16px; padding:12px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <h1>阿里云（公共云）2025 Q2 市场洞察 Demo看板 </h1>
   <p style="font-size: 14px;  margin-top: 4px; margin-bottom: 0;">
   *** 仅用于侯良语 阿里云商业分析岗位面试作品展示

</div>
""", unsafe_allow_html=True)

# ---------- 数据（保持你已校准的口径） ----------
# 全球 Q2’2025（Synergy/媒体转述）
global_q2_2025 = pd.DataFrame({
    "云服务商": ["亚马逊 AWS","微软 Azure","谷歌云","阿里云","甲骨文云","其他"],
    "份额": [30,20,13,4,3,30]
})

# 中国 Q1’2025（Canalys/Omdia）
china_q1_2025 = pd.DataFrame({
    "云服务商": ["阿里云","华为云","腾讯云","其他"],
    "份额": [33,18,10,39]
})

# 中国 AI云 1H25（Omdia）
cn_ai_cloud_1h25 = pd.DataFrame({
    "云服务商": ["阿里云","华为云+腾讯云+百度云","其他"],
    "份额": [35.8, 30.0, 34.2]
})

# 落地方法论图用数据（同 v3）
heat = pd.DataFrame([
    ["金融",9.0,8.5,7.0,6.5],
    ["政企/制造",8.5,8.0,6.5,7.5],
    ["零售/电商",8.5,8.0,7.5,6.0],
    ["媒体/文娱",7.0,7.5,8.5,7.0],
    ["出海企业",8.0,7.5,7.0,6.5],
], columns=["行业","效率工具","专业助手","拟人交互","智能终端"])

# 广告与营销（Similarweb · Desktop · 2025-08）
ali_global = pd.DataFrame([
    ["直接访问", 41.48],
    ["原生搜索", 38.37],
    ["其他", 20.15],
], columns=["渠道","份额%"])

ali_cn = pd.DataFrame([
    ["直接访问", 76.04],
    ["原生搜索", 19.01],
    ["其他", 4.95],
], columns=["渠道","份额%"])

# ============== Tab 布局：合并1/3/4 + 保留机会/营销 ==============
tabA, tabB, tabC, tabD = st.tabs([
    "① 市场总览",
    "② 竞对分析",
    "③ 机遇与挑战",
    "④ 阿里云广告与营销"
])

# ---------- Tab A：合并总览（重写版，无橘色边框） ----------
with tabA:
    # --- KPI 4卡 ---
    c0, c1, c2, c3 = st.columns([1.1, 1, 1, 1])
    with c0:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">全球云支出 (Q2’25)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">$99B</h2>'
            '<p style="margin: 0; color: #81C533;">YoY ≈ +25%</p>'
            '</div>',
            unsafe_allow_html=True)
    with c1:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">阿里云全球份额(Q2’25)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">~4%</h2>'
            '<p style="margin: 0; color: #81C533;">YoY ≈ 0%</p>'
            '</div>',
            unsafe_allow_html=True)
    with c2:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">中国云市场份额 (Q2’25)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">33%</h2>'
            '<p style="margin: 0; color: #81C533;">YoY ≈ +15%</p>'
            '</div>',
            unsafe_allow_html=True)
    with c3:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">中国AI云市场份额 (Q2’25)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">35.8%</h2>'
            '<p style="margin: 0; color: #81C533;">YoY ≈ +9%</p>'
            '</div>',
            unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ========== 1) 全球份额 Treemap ==========
    col1, col2 = st.columns([1.1,1])
    with col1:
        st.markdown('<div class="panel"><h3>全球云基础设施份额</h3>', unsafe_allow_html=True)

        tm = px.treemap(
            global_q2_2025,
            # path=[px.Constant("全球"), "云服务商"],
            path=["云服务商"],
            values="份额",
            color="云服务商",
            color_discrete_map={
                "阿里云": "#F2A36B",
                "亚马逊 AWS": "#E5E9E9",
                "微软 Azure": "#E5E9E9",
                "谷歌云": "#E5E9E9",
                "甲骨文云": "#E5E9E9",
                "其他": "#E5E9E9"
            }
        )

        # ✅ 关键：通过 update_traces 设置文本字体大小
        tm.update_traces(
            textfont_size=16,  # 设置标签（云服务商名称）字体大小
            textposition="middle center",  # 可选：控制文本位置（有的版本支持）
            textinfo="label+percent entry"  # 显示标签（即 path 名称，如 "阿里云"）【注意：这个在 px.treemap 里其实无效，但无害】
        )
        # 关键：彻底去掉橘色外框
        tm.update_traces(root_color=None)
        tm.update_traces(marker=dict(line=dict(color="white", width=2)))
        tm.update_layout(
            margin=dict(l=0,r=0,t=0,b=0),
            height=430,
            paper_bgcolor="white",
            plot_bgcolor="white",
            treemapcolorway=["#9DC8C8","#A8BCC3"],  # 固定配色
            uniformtext=dict(minsize=14, mode="show")
        )
        # 明确禁用 streamlit 默认主题
        st.plotly_chart(tm, use_container_width=False, theme=None)

        st.caption("来源：Synergy Research（季度规模≈$99B，YoY≈25%）。")
        st.markdown('</div>', unsafe_allow_html=True)

    # ========== 2) 中国公共云 ==========
    with col2:
        st.markdown('<div class="panel"><h3>中国云基础设施份额</h3>', unsafe_allow_html=True)
        color_map_cn = {
            "阿里云": "#F2A36B",
            "华为云": "#E5E9E9",
            "腾讯云": "#E5E9E9",
            "其他": "#E5E9E9"
        }
        pie_cn = px.pie(
            china_q1_2025, names="云服务商", values="份额", hole=0.55,
            color="云服务商", color_discrete_map=color_map_cn
        )

        # ✅ 关键：通过 update_traces 设置文本字体大小
        pie_cn.update_traces(
            textfont_size=16,  # 设置标签（云服务商名称）字体大小
            textposition="auto",  # 可选：控制文本位置（有的版本支持）
            textinfo="label+percent"  # 显示标签（即 path 名称，如 "阿里云"）【注意：这个在 px.treemap 里其实无效，但无害】
            , marker=dict(line=dict(color="white", width=2))
        )

        pie_cn.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=420, showlegend=False)
        st.plotly_chart(pie_cn, use_container_width=True)

        st.caption("来源：Canalys（现属Omdia）公开口径。")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ========== 3) 中国 AI 云 ==========
    st.markdown('<div class="panel"><h3>中国 AI 云市场份额</h3>', unsafe_allow_html=True)
    ai_bar = px.bar(
        cn_ai_cloud_1h25.sort_values("份额", ascending=False),
        x="份额", y="云服务商", orientation="h", text="份额",
        color="云服务商",
        color_discrete_map={
            "阿里云":"#F2A36B",
            "华为云+腾讯云+百度云":"#E5E9E9",
            "其他":"#E5E9E9"
        }
    )
    ai_bar.update_traces(texttemplate='%{x}%', textposition='inside', text = 'label+percent', textfont_size = 16)
    ai_bar.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=360, showlegend=False)
    st.plotly_chart(ai_bar, use_container_width=True)
    st.markdown("**要点**：阿里云 35.8%，高于第2–4名合计；行业复合增速 26.8%，MaaS复合增速 >72%。（Omdia）")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Tab B：竞争对手分析（华为云 / 腾讯云 / 百度智能云） ----------
with tabB:
    # st.subheader("④ 竞争对手分析 · 华为云 / 腾讯云 / 百度智能云（Demo 口径）")

    # ===== 示例数据（按你口径替换；此处为示意） =====
    comp = pd.DataFrame([
        ["华为云", 18.0, 23.0, 0.18],
        ["腾讯云", 10.0, 16.0, 0.12],
        ["百度智能云", 7.0, 19.0, 0.10],
        ["阿里云", 33.0, 15.0, 0.20],  # 参照
    ], columns=["厂商","份额","增速","利润率proxy"])

    radar = pd.DataFrame([
        ["华为云", 9.0, 8.0, 7.0, 9.0, 6.5, 7.0],
        ["腾讯云", 7.5, 7.0, 8.5, 7.5, 6.0, 7.5],
        ["百度智能云", 7.0, 9.0, 6.5, 7.0, 5.5, 7.0],
        ["阿里云", 8.5, 8.0, 8.5, 8.0, 8.0, 8.0],  # 参照
    ], columns=["厂商","算力供给","AI能力","生态与开发者","政企本地化","海外拓展","价格与产品策略"])

    heat_comp = pd.DataFrame([
        ["华为云","金融",8.5],["华为云","制造",9.0],["华为云","政企",9.0],["华为云","互联网",6.5],["华为云","文娱",6.5],
        ["腾讯云","金融",7.5],["腾讯云","制造",7.0],["腾讯云","政企",7.5],["腾讯云","互联网",8.5],["腾讯云","文娱",8.5],
        ["百度智能云","金融",7.0],["百度智能云","制造",7.5],["百度智能云","政企",7.0],["百度智能云","互联网",7.5],["百度智能云","文娱",7.0],
        ["阿里云","金融",8.0],["阿里云","制造",8.0],["阿里云","政企",8.0],["阿里云","互联网",8.5],["阿里云","文娱",7.5],
    ], columns=["厂商","行业","强度"])

    share_slope = pd.DataFrame([
        ["华为云", 17.0, 18.0],
        ["腾讯云", 10.5, 10.0],
        ["百度智能云", 6.5, 7.0],
        ["阿里云", 34.0, 33.0],
    ], columns=["厂商","上一期份额","当前期份额"])

    # 公共色板
    color_line = {"阿里云":"#f2a36b","华为云":"#E5E9E9","腾讯云":"#E5E9E9","百度智能云":"#E5E9E9"}
    color_fill = {"阿里云":"rgba(157,200,200,0.20)","华为云":"rgba(168,188,195,0.35)",
                  "腾讯云":"rgba(168,188,195,0.35)","百度智能云":"rgba(168,188,195,0.35)"}

    # ================= 1) 能力画像 · 雷达图（分面，避免重叠） =================
    st.markdown("### 能力画像 · 雷达图（分家展示，浅线为阿里云对标）")
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    metrics = ["算力供给","AI能力","生态与开发者","政企本地化","海外拓展","价格与产品策略"]
    vendors = ["阿里云","华为云","腾讯云","百度智能云",]  # 展示顺序

    # 2×2 极坐标子图
    fig_radar_grid = make_subplots(
        rows=2, cols=2, specs=[[{'type': 'polar'}, {'type': 'polar'}],
                               [{'type': 'polar'}, {'type': 'polar'}]],
        subplot_titles=vendors
    )

    def vendor_values(name):
        return radar.loc[radar["厂商"]==name, metrics].iloc[0].tolist()

    # 在每格子里：该厂商为粗线+填充；阿里云为细浅虚线参照
    positions = [(1,1),(1,2),(2,1),(2,2)]
    for (row,col), vendor in zip(positions, vendors):
        rv = vendor_values(vendor)
        av = vendor_values("阿里云")
        # 参照（阿里云）——除了阿里云自己的格子也画细线参照
        fig_radar_grid.add_trace(go.Scatterpolar(
            r=av+[av[0]], theta=metrics+[metrics[0]], name="阿里云参照",
            line=dict(color=color_line["阿里云"], width=1.5, dash="dash"),
            opacity=0.8, showlegend=False
        ), row=row, col=col)
        # 该厂商
        fig_radar_grid.add_trace(go.Scatterpolar(
            r=rv+[rv[0]], theta=metrics+[metrics[0]], name=vendor,
            fill="toself", fillcolor=color_fill[vendor],
            line=dict(color=color_line[vendor], width=3),
            mode="lines+markers", marker=dict(size=5),
            showlegend=False
        ), row=row, col=col)

    fig_radar_grid.update_layout(
        height=560, margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    )
    fig_radar_grid.update_polars(
        bgcolor="rgba(0,0,0,0)",
        radialaxis=dict(range=[0,10], tickvals=[2,4,6,8,10],
                        gridcolor="#cbd5e1", gridwidth=1, tickfont=dict(size=10)),
        angularaxis=dict(gridcolor="#e2e8f0", gridwidth=1, tickfont=dict(size=11))
    )
    st.plotly_chart(fig_radar_grid, use_container_width=True, theme=None)

    # ================= 2) 份额×增速×利润 proxy · 气泡图 =================
    st.markdown("### 份额 × 增速 × 利润 proxy · 气泡图（右上更优；点越大≈利润率越高）")
    fig_bubble = px.scatter(
        comp, x="份额", y="增速", size="利润率proxy", text="厂商",
        color="厂商", color_discrete_map=color_line,
        size_max=60, opacity=0.9, height=420
    )
    fig_bubble.update_traces(textposition="top center")
    # 中位线作参考
    fig_bubble.add_hline(y=comp["增速"].median(), line_dash="dot", line_color="#94a3b8")
    fig_bubble.add_vline(x=comp["份额"].median(), line_dash="dot", line_color="#94a3b8")
    fig_bubble.update_layout(margin=dict(l=0,r=0,t=10,b=0), legend_title_text="")
    st.plotly_chart(fig_bubble, use_container_width=True, theme=None)

    # ================= 3) 行业强项 · 热力图 =================
    st.markdown("### 行业强项 · 热力图")

    pivot = (heat_comp.pivot(index="厂商", columns="行业", values="强度")
             .reindex(index=["阿里云", "华为云", "腾讯云", "百度智能云"])
             .reindex(columns=["金融", "制造", "政企", "互联网", "文娱"]))

    z = pivot.values
    x_labels = pivot.columns.tolist()
    y_labels = pivot.index.tolist()

    fig_heat = go.Figure(data=go.Heatmap(
        z=z,
        x=x_labels,  # 横轴：行业
        y=y_labels,  # 纵轴：服务商
        colorscale=[
            [0.0,"black"],
            [0.6,"white"],
            [1.0,"#f2a36b"]
        ],
        zmin=0, zmax=10,
        showscale=True,
        colorbar=dict(
            title="强度评分",
            ticks="outside",
            tickvals=[0, 2, 4, 6, 8, 10],
            tickfont=dict(size=12)
        ),
        xgap=2, ygap=2
    ))

    # 顶部读图说明
    fig_heat.add_annotation(
        xref="paper", yref="paper", x=0, y=1.12, showarrow=False,
        text="读图：横轴=行业，纵轴=服务商；颜色越深=强项；数字=综合评分（0-10）。",
        font=dict(size=13, color="#334155"),
        align="left"
    )

    # 每格文字（高分白字，低分黑字）
    for i, y in enumerate(y_labels):
        for j, x in enumerate(x_labels):
            val = z[i][j]
            if pd.isna(val):
                continue
            color = "white" if val >= 20 else "#111827"
            fig_heat.add_annotation(
                x=x, y=y, text=f"{val:.1f}",
                showarrow=False, font=dict(color=color, size=14)
            )

    fig_heat.update_layout(
        height=460,
        margin=dict(l=80, r=40, t=90, b=40),  # 给刻度留空间
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig_heat, use_container_width=True, theme=None)

    # ================= 4) 份额坡度图（上一期 → 当前期） =================
    st.markdown("### 份额坡度图（上一期 → 当前期）")
    s_long = (share_slope
              .assign(阶段1=share_slope["上一期份额"], 阶段2=share_slope["当前期份额"])
              .melt(id_vars=["厂商"], value_vars=["阶段1","阶段2"], var_name="阶段", value_name="份额"))
    fig_slope = px.line(
        s_long.sort_values(["厂商","阶段"]), x="阶段", y="份额", color="厂商",
        color_discrete_map=color_line, markers=True, height=360
    )
    fig_slope.update_traces(line=dict(width=5))
    fig_slope.update_layout(margin=dict(l=0,r=0,t=10,b=0), legend_title_text="")
    st.plotly_chart(fig_slope, use_container_width=True, theme=None)

    # ===== 结论要点（一句话版，面试/路演用） =====
    st.markdown("### 总结")
    st.markdown("""
    - **华为云**：政企/制造强势，算力与本地化领先；增速高、份额稳步提升。  
    - **腾讯云**：互联网/文娱强，生态/开发者活跃；份额稳定，利润率需控成本结构。  
    - **百度智能云**：AI 能力突出，AIGC/模型服务驱动增速；需强化行业复制与生态深度。  
    - **阿里云（对标）**：海外拓展与生态厚度优势明显；需在政企/本地化场景持续加码。  
    """)

# ---------- Tab C：机会与挑战（方法论可视化，炫酷加强） ----------
with tabC:
    st.subheader("机会与挑战 · AI vs Non-AI 战略地图")

    # ---- AI 驱动机遇 ----
    ai_opps = pd.DataFrame([
        ["MaaS 模型服务","~72% 复合增长","高",80,85],
        ["GPUaaS/算力服务","高增长","中",70,75],
        ["行业 GenAI 方案（金融/制造/零售）","高","高",85,90],
        ["数据治理 + 向量数据库","中高","高",75,80]
    ], columns=["机遇","增速/市场信号","执行难度描述","潜在市场规模","可执行性"])

    fig_ai = px.scatter(
        ai_opps,
        x="潜在市场规模", y="可执行性",
        text="机遇", size="潜在市场规模", color="可执行性",
        color_continuous_scale="Greens", size_max=40, height=420
    )
    fig_ai.update_traces(textposition="top center")
    fig_ai.update_layout(title="AI 驱动机遇 (Omdia/IDC 背书)", margin=dict(l=0,r=0,t=40,b=0))
    st.plotly_chart(fig_ai, use_container_width=True)

    st.markdown("**解读**：阿里云在 AI 云份额 35.8% 领先，MaaS 增长最快；结合 GPUaaS、数据治理和行业 GenAI 方案形成“AI 四件套”。")

    # ---- 非AI 基本盘机遇 ----
    non_ai_opps = pd.DataFrame([
        ["传统行业上云（金融/制造/能源）","上云率低","中",85,80],
        ["海外区域拓展（东南亚/中东）","高增长","中高",75,65],
        ["中小企业/开发者生态","长尾市场","低",65,85],
        ["价格/成本优势（飞天+倚天芯片）","成本驱动","中",70,70],
        ["合规与本地化（政企/央国企）","刚需","中高",80,60]
    ], columns=["机遇","增速/市场信号","执行难度描述","潜在市场规模","可执行性"])

    fig_non_ai = px.scatter(
        non_ai_opps,
        x="潜在市场规模", y="可执行性",
        text="机遇", size="潜在市场规模", color="可执行性",
        color_continuous_scale="Blues", size_max=40, height=420
    )
    fig_non_ai.update_traces(textposition="top center")
    fig_non_ai.update_layout(title="非AI 基本盘机遇 (扩大现有份额)", margin=dict(l=0,r=0,t=40,b=0))
    st.plotly_chart(fig_non_ai, use_container_width=True)

    st.markdown("**解读**：除了 AI，阿里云仍可通过扩大传统行业上云、海外拓展、长尾 SME 生态、成本优势与合规资质来增加市场份额。")

    # ---- 挑战与风险矩阵（新增） ----
    st.markdown('<div class="panel"><h3>挑战与风险矩阵（影响度x发生概率）</h3>', unsafe_allow_html=True)

    risks = pd.DataFrame([
        # 风险项, 类别, 影响度(0-100), 发生概率(0-100), 检测/管控难度(0-100, 可做气泡透明度)
        ["高端GPU/算力供给不确定（出口/产能）","供给", 92, 78, 75],
        ["价格战与大客户议价导致ARPU下行","商业", 85, 72, 60],
        ["跨境数据主权/本地合规复杂度","合规", 88, 66, 70],
        ["海外品牌与渠道建设不足（获客成本高）","市场", 76, 69, 55],
        ["行业样板复制难（定制化拖慢规模化）","交付", 73, 64, 50],
        ["生态/伙伴黏性不足（ISV/MCP/渠道）","生态", 70, 62, 58],
    ], columns=["风险项","类别","影响度","发生概率","管控难度"])

    fig_risk = px.scatter(
        risks, x="发生概率", y="影响度", text="风险项",
        size="影响度", color="类别",
        size_max=38, opacity=0.95,
        color_discrete_sequence=px.colors.qualitative.Set2, height=460
    )
    # 四象限辅助线
    fig_risk.add_shape(type="line",
        x0=risks["发生概率"].median(), x1=risks["发生概率"].median(),
        y0=risks["影响度"].min(), y1=risks["影响度"].max(),
        line=dict(dash="dot", color="#94a3b8")
    )
    fig_risk.add_shape(type="line",
        x0=risks["发生概率"].min(), x1=risks["发生概率"].max(),
        y0=risks["影响度"].median(), y1=risks["影响度"].median(),
        line=dict(dash="dot", color="#94a3b8")
    )
    fig_risk.update_traces(textposition="top center")
    fig_risk.update_layout(margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig_risk, use_container_width=True)

    st.caption("读图：右上角=高影响×高概率，应作为优先缓解对象（例如：GPU供给、价格战、合规）。")

    # ---- 缓解策略（新增表格） ----
    st.markdown('<div class="panel"><h3>关键风险的缓解策略</h3>', unsafe_allow_html=True)
    mitigations = pd.DataFrame([
        ["高端GPU/算力供给", "多源采购+自研/国产替代（含推理场景优化）；排产/配额策略；Spot/预留/包年包月组合售卖"],
        ["价格战与ARPU下行", "以“解决方案包”替代单纯算力报价；捆绑数据治理/观测与FinOps；分层折扣+用量阶梯"],
        ["跨境与本地合规", "标准化合规模板（按国别/行业）；专属云/本地化部署；数据边界与审计可视化"],
        ["海外获客成本高", "地区化SEO+SEM（Brand to Demand）；案例/白皮书+试用闭环；LinkedIn/YouTube 技术内容"],
        ["样板复制难", "行业模板化（MaaS微调流水线+参考架构）；交付手册与蓝图；Success KPI可视化"],
        ["生态黏性不足", "ISV激励与Marketplace联运；联合售卖（渠道配额/KPI）；技术集成与认证分级"]
    ], columns=["风险","缓解策略要点"])
    st.dataframe(mitigations, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Tab D：广告与营销（仅阿里云） ----------
with tabD:
    st.markdown('<div class="panel"><h3>阿里云海外站（alibabacloud.com）渠道结构 · 桌面流量</h3>', unsafe_allow_html=True)
    fig_global = px.pie(ali_global, names="渠道", values="份额%", hole=0.55,
                        color_discrete_sequence=px.colors.sequential.Blues)
    fig_global.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=360,showlegend = False)
    fig_global.update_traces(
        textfont_size=15,  # 设置标签（云服务商名称）字体大小
        # textposition="middle center",  # 可选：控制文本位置（有的版本支持）
        textinfo="label+percent"  # 显示标签（即 path 名称，如 "阿里云"）【注意：这个在 px.treemap 里其实无效，但无害】
    )
    st.plotly_chart(fig_global, use_container_width=True)
    st.caption("Similarweb：直接访问 41.48%、原生流量 38.37%、其他 20.15%。注：搜索流量中 原生流量:付费搜索 ≈ 84.1%:15.9%。")

    st.markdown('<div class="panel"><h3>阿里云中国站（aliyun.com）渠道结构 · 桌面流量</h3>', unsafe_allow_html=True)
    fig_cn = px.pie(ali_cn, names="渠道", values="份额%", hole=0.55,
                    color_discrete_sequence=px.colors.sequential.Reds)
    fig_cn.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=360,showlegend = False)
    fig_cn.update_traces(
        textfont_size=15,  # 设置标签（云服务商名称）字体大小
        # textposition="middle center",  # 可选：控制文本位置（有的版本支持）
        textinfo="label+percent"  # 显示标签（即 path 名称，如 "阿里云"）【注意：这个在 px.treemap 里其实无效，但无害】
    )
    st.plotly_chart(fig_cn, use_container_width=True)
    st.caption("Similarweb：直接访问 76.04%、原生流量 19.01%、其他 4.95%。")

    st.markdown('<div class="panel"><h3>策略要点</h3>', unsafe_allow_html=True)
    st.markdown("""
- 海外站：**品牌直达 + SEO** 各占四成，付费搜索占比有限 → 以 **内容/案例/白皮书** 为抓手，**SEM 精准扩量**（地区&行业词）。
- 中国站：**直达 76%** 说明品牌心智强；**SEO 19%** 仍是重要触点 → 加强 **技术文档矩阵与产品专题**。
- 共同增量：**社媒与视频渠道**（LinkedIn/YouTube & 知乎/视频号/小红书）+ 活动（云栖大会/行业黑客松）形成 **Brand→Demand** 的闭环。
""")

st.markdown('<div class="smallcap">© 2025 Liangyu Hou Interview Demo — 仅用于面试演示；以机构/官网原文为准。</div>', unsafe_allow_html=True)