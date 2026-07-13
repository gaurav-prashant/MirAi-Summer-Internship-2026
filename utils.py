"""
utils.py
---------
Shared utility helpers for AI Multiverse Chat Studio.
"""
from __future__ import annotations

import os
import streamlit as st


# ---------------------------------------------------------------------------
# CSS / styling
# ---------------------------------------------------------------------------

def load_style(css_filename: str) -> None:
    """
    Inject a local CSS file into the Streamlit page.

    The file is looked up relative to this module's directory so the app
    works regardless of the working-directory from which Streamlit is launched.
    """
    css_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), css_filename)
    if not os.path.exists(css_path):
        return  # Gracefully skip if the stylesheet hasn't been created yet
    with open(css_path, "r", encoding="utf-8") as fh:
        css = fh.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

def render_sidebar(
    personalities: dict[str, dict[str, str]],
    languages: list[str],
) -> tuple[str, str, str, str]:
    """
    Render the configuration sidebar and return the user's selections.

    Parameters
    ----------
    personalities : dict
        Mapping of persona display name → ``{emoji, description, behavior}`` dict.
    languages : list[str]
        Ordered list of language options shown in the selector.

    Returns
    -------
    tuple[str, str, str, str]
        ``(personality_name, description, behavior, language)``
    ""    with st.sidebar:
        # ── Section header ──────────────────────────────────────────────────
        st.markdown(
            "<div style='text-align:center; padding: 12px 0 6px;'>"
            "<span style='font-size:1.6rem; font-weight:800; "
            "background: linear-gradient(90deg, #00f2fe, #bd00ff); "
            "-webkit-background-clip:text; -webkit-text-fill-color:transparent; "
            "background-clip:text; letter-spacing: -0.5px;'>🎭 Persona Selector</span>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<hr style='border:none; border-top:1px solid rgba(189,0,255,0.25); margin:8px 0 18px;'>",
            unsafe_allow_html=True,
        )

        # ── Build display list ───────────────────────────────────────────────
        display_names = [
            f"{v.get('emoji', '')} {k}" for k, v in personalities.items()
        ]
        name_map = {
            f"{v.get('emoji', '')} {k}": k for k, v in personalities.items()
        }

        # ── Selectbox ────────────────────────────────────────────────────────
        st.markdown(
            "<p style='font-size:0.75rem; color:#00f2fe; margin-bottom:6px; "
            "text-transform:uppercase; letter-spacing:0.1em; font-weight:700;'>Select Persona</p>",
            unsafe_allow_html=True,
        )
        selected_display: str = st.selectbox(
            label="Choose a Persona",
            options=display_names,
            index=0,
            help="Select the AI personality you want to chat with.",
            label_visibility="collapsed",
        )
        personality_name = name_map[selected_display]
        selected = personalities[personality_name]
        description: str = selected["description"]
        behavior: str = selected["behavior"]
        emoji: str = selected.get("emoji", "🤖")

        # ── Active persona card ──────────────────────────────────────────────
        st.markdown(
            f"""
            <div style='
                background: linear-gradient(135deg, rgba(0, 242, 254, 0.08), rgba(189, 0, 255, 0.08));
                border: 1px solid rgba(0, 242, 254, 0.3);
                border-radius: 16px;
                padding: 22px 18px;
                margin-top: 14px;
                text-align: center;
                box-shadow: 0 8px 32px 0 rgba(0, 242, 254, 0.05), inset 0 0 15px rgba(189, 0, 255, 0.1);
            '>
                <div style='font-size:2.8rem; line-height:1; margin-bottom:10px; filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.3));'>{emoji}</div>
                <div style='font-size:1.15rem; font-weight:800; color:#ffffff;
                            letter-spacing:-0.2px; margin-bottom:8px; text-shadow: 0 0 10px rgba(0, 242, 254, 0.2);'>
                    {personality_name}
                </div>
                <div style='font-size:0.85rem; color:#cbd5e1; line-height:1.6;'>
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<hr style='border:none; border-top:1px solid rgba(189,0,255,0.15); margin:22px 0 16px;'>",
            unsafe_allow_html=True,
        )

        # ── Language selector ────────────────────────────────────────────────
        st.markdown(
            "<p style='font-size:0.75rem; color:#bd00ff; margin-bottom:6px; "
            "text-transform:uppercase; letter-spacing:0.1em; font-weight:700;'>🌐 Response language</p>",
            unsafe_allow_html=True,
        )
        language: str = st.selectbox(
            label="Response Language",
            options=languages,
            index=0,
            help="The language the AI persona will reply in.",
            label_visibility="collapsed",
        )
    return personality_name, description, behavior, language
