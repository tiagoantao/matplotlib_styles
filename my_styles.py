import matplotlib as mpl
styles = {}

styles['low_info'] = {
    'lines.linewidth': 3,
    'axes.labelsize': 'xx-large',
    'axes.titlesize': 'xx-large'
}


def apply_style(style_name: str) -> None:
    mpl.rcParams.update(styles[style_name])
