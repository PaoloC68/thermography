import os

import thermography as tg
from thermography.io import setup_logger, LogLevel


def _main():
    SETTINGS_DIR = tg.settings.get_settings_dir()
    camera_param_file = os.path.join(SETTINGS_DIR, "camera_parameters.json")

    tg.settings.set_data_dir("/Users/paolo/thermography/")
    IN_FILE_NAME = os.path.join(tg.settings.get_data_dir(), "calvi1.mov")

    app = tg.App(input_video_path=IN_FILE_NAME, camera_param_file=camera_param_file)

    app.load_video(start_frame=0, end_frame=399)
    app.run()


if __name__ == '__main__':
    setup_logger(console_log_level=LogLevel.INFO, file_log_level=LogLevel.DEBUG)
    _main()
