# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
# 默认按钮颜色是 secondary
from toolbox import clear_line_break


def get_core_scenes():
    return {
        "无": {},
        "研究选题": {},
        "背景知识": {},
        "研究思路": {},
        "实验设计": {"hidder": True,
                 },
    }
