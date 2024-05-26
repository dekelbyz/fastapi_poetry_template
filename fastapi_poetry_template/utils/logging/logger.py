import datetime
import inspect
import logging
import logging.config

# Define the color codes for different log levels
COLORS = {
    "WARNING": "\033[33m",  # ORANGE
    "INFO": "\033[32m",  # GREEN
    "DEBUG": "\033[35m",  # PURPLE
    "ERROR": "\033[31m",  # RED
    "DATE": "\033[33m",  # YELLOW
    "FUNCNAME": "\033[36m",  # CYAN
    "BOLD": "\033[1m",  # BOLD
    "RESET": "\033[0m",  # RESET
}


class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_color = COLORS.get(record.levelname, COLORS["RESET"])
        date_color = COLORS["DATE"]
        func_name_color = COLORS["FUNCNAME"]
        bold_color = COLORS["BOLD"]
        reset_color = COLORS["RESET"]
        log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Get the caller's file path and function name
        frame = inspect.currentframe()
        # Move up the stack to find the correct frame
        while frame:
            frame_info = inspect.getframeinfo(frame)
            if frame_info.filename == record.pathname:
                break
            frame = frame.f_back

        file_path = frame_info.filename if frame else ""
        function_name = frame_info.function if frame else ""

        # Split the file path to apply color to the filename
        file_path_parts = file_path.split("/")
        filename = file_path_parts[-1]

        # Construct the colored function and filename
        colored_func_file = (
            f"{bold_color}{func_name_color}{
                filename}/{function_name}{reset_color}"
        )

        log_message = (
            f"[{log_color}{record.levelname}{reset_color}] "
            f"{date_color}{log_time}{reset_color}  "
            f"{record.getMessage()}\n"
            f"[Function: {colored_func_file} > /{'/'.join(file_path_parts)}]"
        )
        return log_message


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {"()": CustomFormatter},
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "custom",
        }
    },
    "loggers": {"": {"handlers": ["default"], "level": "INFO", "propagate": False}},
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
