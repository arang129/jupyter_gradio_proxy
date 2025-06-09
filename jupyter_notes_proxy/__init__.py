import os

def setup_notes_proxy():
    """ Proxy wrapper to launch Streamlit from JupyterHub """

    return {
        'command': [
            "streamlit", "run", "/home/jupyter-data/notes/teaching_notes.py",
            "--browser.gatherUsageStats", "false",
            "--browser.serverAddress", "0.0.0.0",
            "--server.port", "{port}",
            "--server.headless", "true",
            "--server.enableCORS", "false",
            "--server.enableXsrfProtection", "false",
            "--server.maxUploadSize", "20",       # 限制檔案上傳大小 (MB)
            "--server.maxMessageSize", "200",     # 限制訊息大小 (MB)
        ],
        'environment': {},
        'timeout': 60.0,  # timeout 由30增加至60秒，防止資源爭搶造成的timeout
        'launcher_entry': {
            'title': '上課講義',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'notes.svg'),
        }
    }
