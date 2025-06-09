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
            
            "--server.maxUploadSize", "20",
            "--server.maxMessageSize", "200",
            "--server.enableWebsocketCompression", "true",
            "--server.runOnSave", "false",
            "--client.showErrorDetails", "false",
            "--global.dataFrameSerialization", "arrow",
        ],
        'environment': {
            # 設定環境變數以優化效能
            'STREAMLIT_SERVER_MAX_UPLOAD_SIZE': '200',
            'STREAMLIT_SERVER_CONCURRENT_REQUEST_LIMIT': '10',
        },
        'timeout': 60.0,  # timeout 由30增加至60秒，防止資源爭搶造成的timeout
        'launcher_entry': {
            'title': '上課講義',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'notes.svg'),
        }
    }

