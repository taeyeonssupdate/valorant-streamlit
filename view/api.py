import streamlit as st
from .weapons import Weapons


class API(Weapons):
    LANGUAGE = ["ar-AE", "de-DE", "en-US", "es-ES", "es-MX", "fr-FR", "id-ID", "it-IT", "ja-JP", "ko-KR", "pl-PL", "pt-BR", "ru-RU", "th-TH", "tr-TR", "vi-VN", "zh-CN", "zh-TW"]

    def __init__(self) -> None:
        super().__init__()
