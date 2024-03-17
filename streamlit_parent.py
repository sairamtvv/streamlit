import os
import re

import streamlit as st
import toml

# Used to identify if the current environment is production or not.
PROD_NAMESPACE_NAMES = ["ai"]
PROD_DATABASE_NAMES = ["BP_S", "DM_S"]


def get_env_type():
    env_type = "NON_PROD"
    if os.getenv("K8S_DEPLOYMENT_NAMESPACE") in PROD_NAMESPACE_NAMES:
        env_type = "PROD"

    pattern = re.compile(r"""(DB_CON).*""")
    for key, val in os.environ.items():
        if pattern.match(key):
            if val in PROD_DATABASE_NAMES:
                env_type = "PROD"
    return env_type


def set_css_color_styles():
    """Compile some hacky CSS to override the theme color."""

    if get_env_type() == "PROD":
        css = """<style>
                   [data-testid|="stDecoration"] {
                        background-image: linear-gradient(90deg, #5387ac, rgba(0,49,83,0.8));
                    }
                   </style>"""
        st.write(css, unsafe_allow_html=True)

    css = """<style>
                [data-testid|="stSidebarNav"] {
                        margin-top: -60px;
                        margin-bottom: 60px;
                    }
                .appview-container .block-container {
                    margin-top: -60px;
                }
                h1 span {
                    font-size: 80%;
                    }
                footer {
                visibility: hidden;
                     display: none;
                }

                footer::before {
                    content: "Provided by EM-PPS";
                    visibility: visible;
                }
                </style>"""
    st.write(css, unsafe_allow_html=True)


def get_env_info():
    info_str = ""

    info_str += "### EM-PPS (AI-Squad) App \n"
    info_str += "### Environment Info \n"
    pattern = re.compile(r"""(DB_CON|DB_USER|K8S_DEPLOYMENT_NAME).*""")
    for key, val in os.environ.items():
        if pattern.match(key):
            info_str += f"- {key}={val} \n"

    return info_str


def set_theme_in_config(name):
    file_path = ".streamlit/config.toml"
    config_dict = toml.load(file_path)
    config_dict["theme"] = config_dict["theme_" + name]
    with open(file_path, "w") as f:
        toml.dump(config_dict, f)


def set_streamlit_config(
    *args,
    page_title="APP",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=None,
    menu_items=None,
    **kwargs,
):
    if menu_items is None:
        menu_items = {
            "Get Help": None,
            "Report a bug": None,
            "About": get_env_info(),
        }

    set_theme_in_config(get_env_type())

    st.set_page_config(
        *args,
        layout=layout,  # Can be "centered" or "wide".
        initial_sidebar_state=initial_sidebar_state,
        # Can be "auto", "expanded", "collapsed"
        page_title=page_title,
        # String or None. Strings get appended with "â€¢ Streamlit".
        page_icon=page_icon,  # String, anything supported by st.image, or None.
        menu_items=menu_items,
        **kwargs,
    )
    set_css_color_styles()


set_theme_in_config(get_env_type())
