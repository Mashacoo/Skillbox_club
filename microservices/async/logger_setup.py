
dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": " %(name)s | %(asctime)s| %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",

        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "base",
            "filename": "app.log",
            "level": "DEBUG",
        },
    },

    "loggers": {
        "general_logger": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": True,
        },

    },
}

