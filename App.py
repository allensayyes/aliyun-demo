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
  <h1>阿里云（公共云）2025 1H 市场洞察 Demo看板 </h1>
   <p style="font-size: 14px;  margin-top: 4px; margin-bottom: 0;">
   *** 仅用于侯良语 阿里云商业分析岗位面试作品展示

</div>
""", unsafe_allow_html=True)

# ---------- 数据（更新至2025 1H，基于Synergy/Omdia/Canalys权威报告） ----------
# 全球 2025 Q2（Synergy Research/Omdia，Q2支出$95.3B，YoY+22%）
global_1h_2025 = pd.DataFrame({
    "云服务商": ["亚马逊 AWS","微软 Azure","谷歌云","阿里云","甲骨文云","其他"],
    "份额": [32,22,11,4,3,28]  # 基于Synergy Research 2025 Q2数据
})

# 中国 2025 1H（Canalys/IDC综合报告）
china_1h_2025 = pd.DataFrame({
    "云服务商": ["阿里云","华为云","腾讯云","百度云","火山引擎","中国电信","AWS中国","其他"],
    "份额": [36,19,16,9,7,5,3,5]  # 基于Canalys 2025 1H数据
})

# 中国 AI云 2025 1H（Omdia 2025H1权威报告，市场规模¥221.9亿元）
cn_ai_cloud_1h_2025 = pd.DataFrame({
    "云服务商": ["阿里云","火山引擎","华为云","腾讯云","百度AI云","中国电信","商汤","其他"],
    "份额": [35.8,14.8,13.1,7.0,6.1,5.1,4.4,13.7]  # Omdia 2025H1确认数据
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

# ============== Tab 布局：合并1/3/4 + 保留机会/营销 + 销售策略分析 ==============
tabA, tabB, tabC, tabD, tabE = st.tabs([
    "① 市场总览",
    "② 竞对分析",
    "③ 机遇与挑战",
    "④ 阿里云广告投放分析",
    "⑤ 一面话题延展：营销策略分析"
])

# ---------- Tab A：合并总览（重写版，无橘色边框） ----------
with tabA:
    # --- KPI 6卡 ---
    c0, c1, c2, c3, c4, c5 = st.columns([1.1, 1, 1, 1, 1, 1])
    with c0:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">全球云支出 (2025 Q2)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">$95.3B</h2>'
            '<p style="margin: 0; color: #81C533;">YoY +22%</p>'
            '</div>',
            unsafe_allow_html=True)
    with c1:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">阿里云全球份额(2025 Q2)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">4%</h2>'
            '<p style="margin: 0; color: #81C533;">排名第4</p>'
            '</div>',
            unsafe_allow_html=True)
    with c2:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">国内AI云市场 (2025 1H)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">¥221.9亿</h2>'
            '<p style="margin: 0; color: #81C533;">CAGR 26.8%</p>'
            '</div>',
            unsafe_allow_html=True)
    with c3:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">阿里云国内总份额(2025 1H)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">36%</h2>'
            '<p style="margin: 0; color: #81C533;">稳居第1</p>'
            '</div>',
            unsafe_allow_html=True)
    with c4:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">阿里云公共云份额(2025 1H)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">36%</h2>'
            '<p style="margin: 0; color: #81C533;">领先第2名17%</p>'
            '</div>',
            unsafe_allow_html=True)
    with c5:
        st.markdown(
            '<div style="background: white; border: 2px solid #F2A36B; border-radius: 12px; padding: 16px; text-align: center;">'
            '<p style="margin: 0; color: #2b2b2b;">阿里云AI云份额(2025 1H)</p>'
            '<h2 style="margin: 8px 0 4px 0; color: #2b2b2b;">35.8%</h2>'
            '<p style="margin: 0; color: #81C533;">超2-4名总和</p>'
            '</div>',
            unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ========== 1) 全球份额 Treemap ==========
    st.markdown('<div class="panel"><h3>全球云基础设施份额</h3>', unsafe_allow_html=True)

    tm = px.treemap(
        global_1h_2025,
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

    tm.update_traces(
        textfont_size=16,
        textposition="middle center",
        textinfo="label+percent entry"
    )
    tm.update_traces(root_color=None)
    tm.update_traces(marker=dict(line=dict(color="white", width=2)))
    tm.update_layout(
            margin=dict(l=0,r=0,t=0,b=0),
            height=430,
            paper_bgcolor="white",
            plot_bgcolor="white",
        treemapcolorway=["#9DC8C8","#A8BCC3"],
            uniformtext=dict(minsize=14, mode="show")
        )
    st.plotly_chart(tm, use_container_width=True, theme=None, key="global_cloud_treemap")

    st.caption("来源：Synergy Research/Omdia（2025 Q2支出$95.3B，YoY+22%，连续4季度超20%增长）")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # ========== 2) 三个饼图：中国云服务、中国公共云、中国AI云 ==========
    col1, col2, col3 = st.columns(3)
    
    # 中国云服务份额
    with col1:
        st.markdown('<div class="panel"><h3>中国云服务份额</h3>', unsafe_allow_html=True)
        color_map_cn = {
            "阿里云": "#F2A36B",
            "华为云": "#E5E9E9",
            "腾讯云": "#E5E9E9",
            "百度云": "#E5E9E9",
            "中国电信": "#E5E9E9",
            "火山引擎": "#E5E9E9",
            "AWS中国": "#E5E9E9",
            "其他": "#E5E9E9"
        }
        pie_cn = px.pie(
            china_1h_2025, names="云服务商", values="份额", hole=0.55,
            color="云服务商", color_discrete_map=color_map_cn
        )
        pie_cn.update_traces(
            textfont_size=12,
            textposition="auto",
            textinfo="label+percent",
            marker=dict(line=dict(color="white", width=2))
        )
        pie_cn.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=400, showlegend=False)
        st.plotly_chart(pie_cn, use_container_width=True, key="china_cloud_service_pie")
        st.caption("来源：Canalys（现属Omdia）2025 1H")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 中国公共云份额（与云服务份额相同，但标题不同）
    with col2:
        st.markdown('<div class="panel"><h3>中国公共云份额</h3>', unsafe_allow_html=True)
        pie_public = px.pie(
            china_1h_2025, names="云服务商", values="份额", hole=0.55,
            color="云服务商", color_discrete_map=color_map_cn
        )
        pie_public.update_traces(
            textfont_size=12,
            textposition="auto",
            textinfo="label+percent",
            marker=dict(line=dict(color="white", width=2))
        )
        pie_public.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=400, showlegend=False)
        st.plotly_chart(pie_public, use_container_width=True, key="china_public_cloud_pie")
        st.caption("来源：Canalys（现属Omdia）2025 1H")
        st.markdown('</div>', unsafe_allow_html=True)

    # 中国AI云份额
    with col3:
        st.markdown('<div class="panel"><h3>中国AI云份额</h3>', unsafe_allow_html=True)
        color_map_ai = {
            "阿里云": "#F2A36B",
            "火山引擎": "#E5E9E9",
            "华为云": "#E5E9E9",
            "其他": "#E5E9E9",
            "腾讯云": "#E5E9E9",
            "百度AI云": "#E5E9E9",
            "中国电信": "#E5E9E9",
            "商汤": "#E5E9E9"
        }
        ai_pie = px.pie(
            cn_ai_cloud_1h_2025, names="云服务商", values="份额", hole=0.4,
            color="云服务商", color_discrete_map=color_map_ai
        )
        ai_pie.update_traces(
            textfont_size=12,
            textposition="auto",
            textinfo="label+percent"
        )
        ai_pie.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=400, showlegend=False)
        st.plotly_chart(ai_pie, use_container_width=True, key="china_ai_cloud_pie")
        st.caption("来源：Omdia 2025H1（市场规模¥221.9亿元，CAGR 26.8%）")
        st.markdown("**要点**：阿里云 35.8% 领先AI云市场，超过第2-4名总和；火山引擎 14.8% 异军突起；华为云 13.1%、腾讯云 7.0%、百度 6.1% 紧随其后。")
        st.markdown('</div>', unsafe_allow_html=True)

    # ========== 3) 关键洞察 ==========
    st.markdown('<div class="panel"><h3>关键洞察</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**全球市场洞察**")
        st.markdown("""
        - **全球云市场**：2025 Q2支出$95.3B，YoY+22%，连续4季度超20%增长
        - **阿里云全球地位**：份额4%，排名第4，稳定全球前四
        - **竞争格局**：AWS(32%)、Azure(22%)、谷歌云(11%)三强格局
        - **市场趋势**：全球云市场持续高速增长，AI驱动新一轮增长周期
        """)
    
    with col2:
        st.markdown("**中国市场洞察**")
        st.markdown("""
        - **国内市场**：2025 1H AI云市场规模¥221.9亿元，CAGR 26.8%（至2030）
        - **阿里云领先**：国内总份额36%，公共云36%，AI云35.8%，全面领先
        - **竞争态势**：华为云(19%)、腾讯云(16%)、百度云(9%)紧随其后
        - **AI云机遇**：阿里云AI云份额35.8%，超过第2-4名总和；火山引擎(14.8%)异军突起
        """)
    
    st.markdown("""
    **战略要点**：
    1. **全球稳定**：阿里云全球份额4%，排名第4，在全球市场保持稳定地位
    2. **国内领先**：在国内市场保持绝对领先，份额36%，领先第2名17个百分点
    3. **AI云领跑**：AI云份额35.8%（Omdia 2025H1），超过第2-4名总和，技术优势明显
    4. **增长驱动**：AI云市场CAGR 26.8%，MaaS层CAGR超72%，未来增长潜力巨大
    5. **基础设施投入**：阿里巴巴未来3年投入¥380B建设云和AI硬件基础设施
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Tab B：竞争对手分析（华为云 / 腾讯云 / 百度智能云） ----------
with tabB:
    # st.subheader("④ 竞争对手分析 · 华为云 / 腾讯云 / 百度智能云（Demo 口径）")

    # ===== 更新至Q3'2025数据 =====
    comp = pd.DataFrame([
        ["华为云", 18.0, 15.0, 0.18],
        ["腾讯云", 15.0, 12.0, 0.16],
        ["百度智能云", 10.0, 30.0, 0.14],
        ["阿里云", 40.0, 11.0, 0.24],  # 参照
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
    st.plotly_chart(fig_radar_grid, use_container_width=True, theme=None, key="competitor_radar")

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
    st.plotly_chart(fig_bubble, use_container_width=True, theme=None, key="competitor_bubble")

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

    st.plotly_chart(fig_heat, use_container_width=True, theme=None, key="competitor_heatmap")

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
    st.plotly_chart(fig_ai, use_container_width=True, key="ai_opportunities")

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
    st.plotly_chart(fig_non_ai, use_container_width=True, key="non_ai_opportunities")

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
    st.plotly_chart(fig_risk, use_container_width=True, key="risk_matrix")

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

# ---------- Tab D：阿里云国内市场营销分析 ----------
with tabD:
    # st.markdown("### 阿里云国内市场营销渠道与投放策略分析")
    
    # 国内市场营销渠道结构
    st.markdown('<div class="panel"><h3>阿里云流量渠道结构</h3>', unsafe_allow_html=True)
    
    # 国内营销渠道数据
    cn_marketing_channels = pd.DataFrame([
        ["直接访问", 76.04, "品牌直达"],
        ["搜索引擎", 19.01, "SEO+SEM"],
        ["社交媒体", 3.50, "微信/微博/抖音"],
        ["合作伙伴", 1.45, "ISV/渠道"]
    ], columns=["渠道类型", "流量占比(%)", "主要平台"])
    
    fig_channels = px.pie(cn_marketing_channels, names="渠道类型", values="流量占比(%)", 
                         hole=0.55, color_discrete_sequence=px.colors.sequential.Oranges)
    fig_channels.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=360, showlegend=False)
    fig_channels.update_traces(textfont_size=15, textinfo="label+percent")
    st.plotly_chart(fig_channels, use_container_width=True, key="marketing_channels")
    
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 投放策略分析
    st.markdown('<div class="panel"><h3>投放策略与效果分析</h3>', unsafe_allow_html=True)
    
    # 投放策略矩阵
    marketing_strategy = pd.DataFrame([
        ["品牌营销", "云栖大会、技术峰会", "高", "品牌影响力", "长期价值"],
        ["内容营销", "技术博客、白皮书", "中", "专业形象", "获客转化"],
        ["SEM投放", "行业关键词", "高", "精准获客", "ROI优化"],
        ["社交媒体", "微信、抖音、知乎", "中", "年轻用户", "品牌传播"],
        ["合作伙伴", "ISV、渠道分销", "低", "生态建设", "规模扩张"]
    ], columns=["策略类型", "主要渠道", "投入强度", "核心目标", "预期效果"])
    
    st.dataframe(marketing_strategy, use_container_width=True)
    
    # 营销效果评估
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**营销效果指标**")
        effectiveness_metrics = pd.DataFrame([
            ["品牌认知度", 85, "行业领先"],
            ["获客成本(CAC)", 1200, "同比下降15%"],
            ["转化率", 12.5, "高于行业平均"],
            ["客户留存率", 88, "高粘性"]
        ], columns=["指标", "数值", "行业对比"])
        
        fig_metrics = px.bar(
            effectiveness_metrics, x="数值", y="指标", orientation="h",
            color="指标", color_discrete_sequence=px.colors.qualitative.Set3,
            text=[f"{85}%", f"¥{1200}", f"{12.5}%", f"{88}%"]
        )
        fig_metrics.update_layout(height=300, showlegend=False, margin=dict(l=0,r=0,t=0,b=0))
        st.plotly_chart(fig_metrics, use_container_width=True, key="marketing_metrics")
    
    with col2:
        st.markdown("**投放预算分配**")
        budget_allocation = pd.DataFrame([
            ["品牌营销", 35],
            ["SEM投放", 25],
            ["内容营销", 20],
            ["社交媒体", 12],
            ["合作伙伴", 8]
        ], columns=["渠道", "预算占比(%)"])
        
        fig_budget = px.pie(budget_allocation, values="预算占比(%)", names="渠道",
                        color_discrete_sequence=px.colors.sequential.Blues)
        fig_budget.update_layout(height=300, showlegend=False, margin=dict(l=0,r=0,t=0,b=0))
        fig_budget.update_traces(textfont_size=12, textinfo="label+percent")
        st.plotly_chart(fig_budget, use_container_width=True, key="marketing_budget")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    
    # 机场大屏广告策略分析
    st.markdown('<div class="panel"><h3>🛫 机场大屏广告战略分析</h3>', unsafe_allow_html=True)
    
    st.markdown("**现象**：阿里云和火山引擎在各大机场投放大屏广告")
    
    # 渠道对比
    st.markdown("**营销渠道效果对比**")
    channel_comparison = pd.DataFrame([
        ["机场大屏", "高", "极低", "¥500-1000万/年", "品牌认知"],
        ["云栖大会", "极高", "中", "¥200-300万/年", "技术影响力"],
        ["SEM投放", "中", "极高", "¥100-200万/年", "精准获客"],
        ["技术社区", "中", "高", "¥50-100万/年", "开发者生态"]
    ], columns=["渠道", "决策者触达", "转化效率", "年度预算", "核心价值"])
    
    st.dataframe(channel_comparison, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**战略价值**")
        st.markdown("""
        - 精准触达高价值决策者
        - 品牌心智占领（日均10万+人次）
        - 竞争壁垒（优质点位稀缺）
        """)
        
        st.markdown("**潜在风险**")
        st.markdown("""
        - ROI难量化，归因困难
        - 受众局限（仅10-15%决策者）
        - 可能引发成本战
        """)
    
    with col2:
        st.markdown("**核心洞察**")
        st.markdown("""
        机场广告本质是**防御性投资**：
        - 防止认知流失
        - 维持领导者形象
        - 阻击竞争对手
        """)
        
        st.markdown("**战略建议**")
        st.markdown("""
        - 机场广告：适度投入（≤20%预算）
        - 主战场：云栖大会、技术社区、精准SEM
        - 核心竞争力：技术领先+生态深度+客户成功
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 营销策略建议
    # st.markdown('<div class="panel"><h3>营销策略优化建议</h3>', unsafe_allow_html=True)
    
    # col1, col2 = st.columns(2)
    
    # with col1:
    #     st.markdown("**短期优化（3-6个月）**")
    #     st.markdown("""
    #     - SEO优化：技术文档+行业关键词
    #     - SEM精准投放：行业定向+ROI优化
    #     - 社交媒体：抖音+知乎+微信生态
    #     """)
    
    # with col2:
    #     st.markdown("**长期策略（6-12个月）**")
    #     st.markdown("""
    #     - 品牌影响力：云栖大会+行业峰会
    #     - 内容生态：技术博客+案例研究
    #     - 合作伙伴：ISV生态+渠道体系
    #     """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Shapley Value多点归因模型
    st.markdown('<div class="panel"><h3>🎯 Shapley Value多点归因模型</h3>', unsafe_allow_html=True)
    
    st.markdown("**模型说明**：Shapley Value归因模型能够公平分配各营销渠道对最终转化的贡献度，解决传统归因模型的数据孤岛问题。")
    
    # 客户旅程可视化
    st.markdown("**客户旅程与触点归因分析**")
    
    # 创建客户旅程可视化
    fig_journey = go.Figure()
    
    # 客户旅程路径（波浪线）
    journey_x = [0, 2, 4, 6, 8, 10, 12, 14, 16]
    journey_y = [0, 0.5, -0.3, 0.8, -0.5, 0.6, -0.2, 0.4, 0]
    
    # 绘制波浪路径
    fig_journey.add_trace(go.Scatter(
        x=journey_x, y=journey_y,
        mode='lines',
        line=dict(color='#F2A36B', width=4),
        name='客户旅程',
        showlegend=False
    ))
    
    # 触点位置和贡献度
    touchpoints = [
        {"name": "机场大屏", "x": 2, "y": 1.5, "contribution": 18.5, "icon": "📺"},
        {"name": "云栖大会", "x": 4, "y": -1.0, "contribution": 35.2, "icon": "🎤"},
        {"name": "SEM投放", "x": 6, "y": 1.8, "contribution": 28.8, "icon": "🔍"},
        {"name": "技术社区", "x": 8, "y": -1.2, "contribution": 12.3, "icon": "💻"},
        {"name": "社交媒体", "x": 10, "y": 1.3, "contribution": 5.2, "icon": "📱"},
        {"name": "转化", "x": 16, "y": 0, "contribution": 100, "icon": "🎯"}
    ]
    
    # 添加触点
    for tp in touchpoints:
        # 触点圆圈
        fig_journey.add_trace(go.Scatter(
            x=[tp["x"]], y=[tp["y"]],
            mode='markers+text',
            marker=dict(
                size=40,
                color='#F2A36B' if tp["name"] != "转化" else '#22c55e',
                line=dict(width=3, color='white')
            ),
            text=tp["icon"],
            textfont=dict(size=16, color='white'),
            name=tp["name"],
            hovertemplate=f"<b>{tp['name']}</b><br>贡献度: {tp['contribution']}%<extra></extra>",
            showlegend=False
        ))
        
        # 触点标签
        fig_journey.add_annotation(
            x=tp["x"], y=tp["y"] - 0.8,
            text=f"<b>{tp['name']}</b><br>{tp['contribution']}%",
            showarrow=False,
            font=dict(size=10, color='#374151'),
            align="center"
        )
        
        # 从触点到路径的连接线
        if tp["name"] != "转化":
            fig_journey.add_trace(go.Scatter(
                x=[tp["x"], tp["x"]], y=[tp["y"], 0],
                mode='lines',
                line=dict(color='#F2A36B', width=2, dash='dot'),
                showlegend=False,
                hoverinfo='skip'
            ))
    
    # 布局设置
    fig_journey.update_layout(
        title="客户旅程与Shapley Value归因模型",
        height=500,
        margin=dict(l=0, r=0, t=60, b=0),
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        showlegend=False
    )
    
    # 设置坐标轴范围
    fig_journey.update_xaxes(range=[-1, 17])
    fig_journey.update_yaxes(range=[-2, 2.5])
    
    st.plotly_chart(fig_journey, use_container_width=True, key="customer_journey")
    
    # 归因贡献度详细分析
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Shapley Value归因贡献度分析**")
        shapley_attribution = pd.DataFrame([
            ["云栖大会", 35.2, "品牌认知建立，长期影响"],
            ["SEM投放", 28.8, "精准触达，即时转化"],
            ["机场大屏", 18.5, "决策者心智占领"],
            ["技术社区", 12.3, "开发者生态建设"],
            ["社交媒体", 5.2, "品牌年轻化传播"]
        ], columns=["营销渠道", "贡献度(%)", "核心价值"])
        
        fig_shapley = px.bar(
            shapley_attribution, x="贡献度(%)", y="营销渠道", orientation="h",
            color="贡献度(%)", color_continuous_scale="Viridis",
            text="贡献度(%)"
        )
        fig_shapley.update_traces(texttemplate="%{text}%", textposition="outside")
        fig_shapley.update_layout(
            height=350, margin=dict(l=0,r=0,t=20,b=0),
            showlegend=False
        )
        st.plotly_chart(fig_shapley, use_container_width=True, key="shapley_attribution")
    
    with col2:
        st.markdown("**模型优势**")
        st.markdown("""
        - **公平性**：满足效率性、对称性、虚拟性公理
        - **可解释性**：清晰展示各渠道贡献度
        - **动态调整**：支持实时归因计算
        - **多触点**：解决跨渠道协同效应
        """)
        
        st.markdown("**商业价值**")
        st.markdown("""
        - **预算优化**：精准分配营销预算
        - **ROI提升**：避免重复计算和遗漏
        - **策略调整**：基于数据驱动决策
        - **效果评估**：量化各渠道真实贡献
        """)
    
    st.markdown("---")
    
    # 为什么阿里云商业分析适合使用这个模型
    st.markdown("**为什么阿里云商业分析适合使用Shapley Value归因模型？**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**1. 多触点营销场景**")
        st.markdown("""
        - 云栖大会→SEM→技术社区→转化
        - 机场大屏→官网访问→试用→签约
        - 跨渠道协同效应明显
        """)
    
    with col2:
        st.markdown("**2. 长周期决策流程**")
        st.markdown("""
        - B2B采购周期3-12个月
        - 多次接触影响最终决策
        - 传统归因模型失效
        """)
    
    with col3:
        st.markdown("**3. 数据驱动优化**")
        st.markdown("""
        - 精细化预算分配
        - 渠道组合优化
        - 营销效率提升
        """)
    
    st.markdown("---")
    
    st.markdown("""
    **实施建议**：
    1. **数据整合**：打通各营销渠道数据，建立统一归因体系
    2. **模型训练**：基于历史转化数据训练Shapley Value模型
    3. **实时应用**：将归因结果实时反馈到预算分配和策略调整
    4. **效果验证**：通过A/B测试验证模型准确性和商业价值
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Tab E：营销策略分析 ----------
with tabE:
    st.markdown("### 基于一面讨论内容的延展分析")
    
    # 问题1：增量vs存量市场判断
    st.markdown('<div class="panel"><h3>问题1：如何判断国内公有云是增量还是存量市场？</h3>', unsafe_allow_html=True)
    
    # 市场判断指标体系
    market_indicators = pd.DataFrame([
        ["上云渗透率", "中国企业上云率~60%", "美国~90%", "增量空间大", "IDC报告"],
        ["AI云采用率", "AI云渗透率~15%", "传统云~85%", "AI驱动增量", "Omdia数据"],
        ["中小企业上云", "渗透率~30%", "大企业~80%", "长尾增量市场", "艾瑞咨询"],
        ["行业云化深度", "平均云化~40%", "目标~70%", "存量升级空间", "信通院"],
        ["出海企业需求", "海外云服务需求增长", "YoY+35%", "新增市场", "阿里云内部"],
        ["政企数字化", "政府云化率~25%", "目标~60%", "政策驱动增量", "政府采购网"]
    ], columns=["判断维度", "当前状态", "对标基准", "市场性质", "数据来源"])
    
    st.dataframe(market_indicators, use_container_width=True)
    
    # 增量vs存量分析图表
    col1, col2 = st.columns(2)
    
    with col1:
        # 增量市场分析
        incremental_market = pd.DataFrame([
            ["AI云服务", 72, "MaaS复合增长"],
            ["中小企业上云", 45, "长尾市场开发"],
            ["出海企业云服务", 35, "海外拓展"],
            ["行业深度云化", 28, "存量升级"],
            ["政企数字化", 25, "政策驱动"],
            ["边缘计算", 20, "新技术应用"]
        ], columns=["增量市场", "增长率(%)", "驱动因素"])
        
        fig_incremental = px.bar(
            incremental_market.sort_values("增长率(%)", ascending=True),
            x="增长率(%)", y="增量市场", orientation="h",
            color="增长率(%)", color_continuous_scale="Greens",
            title="增量市场增长率分析"
        )
        fig_incremental.update_layout(height=400, margin=dict(l=0,r=0,t=40,b=0))
        st.plotly_chart(fig_incremental, use_container_width=True, key="incremental_market")
    
    with col2:
        # 存量市场分析
        existing_market = pd.DataFrame([
            ["大企业云优化", 15, "成本优化"],
            ["多云管理", 12, "架构升级"],
            ["安全合规", 18, "政策要求"],
            ["数据治理", 22, "价值挖掘"],
            ["自动化运维", 25, "效率提升"],
            ["混合云部署", 20, "架构演进"]
        ], columns=["存量市场", "增长率(%)", "驱动因素"])
        
        fig_existing = px.bar(
            existing_market.sort_values("增长率(%)", ascending=True),
            x="增长率(%)", y="存量市场", orientation="h",
            color="增长率(%)", color_continuous_scale="Blues",
            title="存量市场增长率分析"
        )
        fig_existing.update_layout(height=400, margin=dict(l=0,r=0,t=40,b=0))
        st.plotly_chart(fig_existing, use_container_width=True, key="existing_market")
    
    st.markdown("""
    **结论：国内公有云市场呈现"增量为主，存量升级"的双轮驱动格局**
    - **增量市场**：AI云、中小企业、出海企业等新需求驱动，增长率20-72%
    - **存量市场**：大企业云优化、多云管理等升级需求，增长率12-25%
    - **策略建议**：增量市场快速扩张，存量市场深度经营
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 问题2：收入增长与利润率平衡
    st.markdown('<div class="panel"><h3>问题2：如何在提高收入的同时确保利润率？</h3>', unsafe_allow_html=True)
    
    # 收入-利润平衡策略矩阵
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**收入增长策略**")
        revenue_strategy = pd.DataFrame([
            ["新客户获取", "中小企业", "长尾市场", "低单价高量", "获客成本优化"],
            ["现有客户扩增", "大企业", "存量升级", "高单价深度", "客户成功管理"],
            ["AI云服务", "全行业", "增量市场", "高单价新兴", "技术差异化"],
            ["出海服务", "跨国企业", "新市场", "高单价溢价", "海外资源投入"],
            ["行业解决方案", "垂直行业", "专业化", "打包定价", "行业know-how"]
        ], columns=["策略", "目标客户", "市场类型", "定价策略", "关键成功因素"])
        
        st.dataframe(revenue_strategy, use_container_width=True)
    
    with col2:
        st.markdown("**利润率保障策略**")
        profit_strategy = pd.DataFrame([
            ["成本结构优化", "基础设施", "规模效应", "自研芯片降本", "倚天+飞天"],
            ["产品组合优化", "高毛利产品", "AI+数据", "解决方案打包", "交叉销售"],
            ["客户分层管理", "大客户", "高价值", "专属服务", "客户成功"],
            ["运营效率提升", "自动化", "AI运维", "人力成本控制", "工具化"],
            ["价格策略优化", "动态定价", "用量阶梯", "长期合约", "粘性提升"]
        ], columns=["策略", "优化维度", "实施方式", "具体措施", "预期效果"])
        
        st.dataframe(profit_strategy, use_container_width=True)
    
    # 收入-利润平衡模型
    st.markdown("**收入-利润平衡模型**")
    
    balance_model = pd.DataFrame([
        ["新客户获取", 85, 15, "高收入增长，初期利润率低"],
        ["现有客户扩增", 70, 30, "稳定收入增长，利润率较高"],
        ["AI云服务", 90, 25, "高收入增长，技术溢价"],
        ["出海服务", 75, 35, "中高收入增长，地域溢价"],
        ["行业解决方案", 80, 40, "高收入增长，最高利润率"]
    ], columns=["策略", "收入增长潜力", "利润率预期", "特点描述"])
    
    fig_balance = px.scatter(
        balance_model, x="收入增长潜力", y="利润率预期",
        size="收入增长潜力", color="利润率预期",
        text="策略", size_max=60,
        color_continuous_scale="RdYlGn",
        title="收入增长 vs 利润率平衡模型"
    )
    fig_balance.update_traces(textposition="top center")
    fig_balance.update_layout(height=500, margin=dict(l=0,r=0,t=40,b=0))
    st.plotly_chart(fig_balance, use_container_width=True, key="revenue_profit_balance")
    
    # 具体实施策略
    st.markdown("**具体实施策略**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**短期策略（6-12个月）**")
        st.markdown("""
        1. **客户分层管理**
           - 大客户：专属服务，高毛利产品组合
           - 中客户：标准化服务，批量管理
           - 小客户：自助服务，低成本获客
        
        2. **产品组合优化**
           - 推广AI云等高毛利产品
           - 打包销售降低获客成本
           - 交叉销售提升客单价
        
        3. **价格策略调整**
           - 用量阶梯定价
           - 长期合约优惠
           - 竞争性定价策略
        """)
    
    with col2:
        st.markdown("**长期策略（1-3年）**")
        st.markdown("""
        1. **技术差异化**
           - 自研芯片降本增效
           - AI能力技术壁垒
           - 行业解决方案深度
        
        2. **生态体系建设**
           - ISV合作伙伴网络
           - 开发者生态
           - 客户成功体系
        
        3. **市场拓展**
           - 海外市场布局
           - 垂直行业深耕
           - 新兴技术应用
        """)
    
    # 关键指标监控
    st.markdown('<div class="panel"><h3>关键指标监控体系</h3>', unsafe_allow_html=True)
    
    kpi_monitoring = pd.DataFrame([
        ["客户获取成本(CAC)", "< 客户生命周期价值(LTV)的1/3", "获客效率", "月度监控"],
        ["客户生命周期价值(LTV)", "目标增长20% YoY", "客户价值", "季度分析"],
        ["毛利率", "> 30%", "盈利能力", "月度监控"],
        ["客户留存率", "> 85%", "客户粘性", "月度监控"],
        ["平均客单价(ARPU)", "增长15% YoY", "收入质量", "季度分析"],
        ["销售转化率", "> 25%", "销售效率", "月度监控"]
    ], columns=["指标", "目标值", "业务意义", "监控频率"])
    
    st.dataframe(kpi_monitoring, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 风险控制措施
    st.markdown('<div class="panel"><h3>风险控制与应对措施</h3>', unsafe_allow_html=True)
    
    risk_control = pd.DataFrame([
        ["价格战风险", "差异化定位，价值销售", "避免纯价格竞争"],
        ["客户流失风险", "客户成功管理，续约激励", "提升客户粘性"],
        ["成本上升风险", "技术降本，规模效应", "控制运营成本"],
        ["竞争加剧风险", "技术壁垒，生态建设", "建立竞争优势"],
        ["市场饱和风险", "新市场开拓，产品创新", "寻找增长点"]
    ], columns=["风险类型", "应对策略", "具体措施"])
    
    st.dataframe(risk_control, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="smallcap">© 2025 Liangyu Hou Interview Demo — 仅用于面试演示；以机构/官网原文为准。</div>', unsafe_allow_html=True)