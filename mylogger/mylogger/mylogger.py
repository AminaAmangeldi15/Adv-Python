import logging
import sys
from copy import copy


# Определяем, куда будут направляться логи (в данном случае - в стандартный вывод).
_STREAM = sys.stdout

# Создаем кастомный форматтер для логов.
class LogLevelFormatter(logging.Formatter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def validate_log_level(loglevel):
        valid_log_levels = ["debug", "info", "warning", "error", "critical"]
        loglevel = str(loglevel).lower()
        if loglevel not in valid_log_levels:
            raise RuntimeError(f"Invalid log level: {loglevel}")
        return loglevel
    
  
    def format_message_with_loglevel(self,message, loglevel):
        loglevel = self.validate_log_level(loglevel)
        return f"{loglevel.upper()}: {message}"
    
    def format(self, record):
        loglevel = record.levelname
        record.msg = self.format_message_with_loglevel(record.msg, loglevel)
        return super().format(record)
    
# Создаем логгер
_logger = logging.getLogger( __name__)


# Создаем обработчик для вывода логов в стандартный вывод.
_stream_handler = logging.StreamHandler(_STREAM)

# Создаем форматтер для логов.
_formatter = LogLevelFormatter(
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S'
)

# Присваиваем форматтер обработчику.
_stream_handler.setFormatter(_formatter)

# Добавляем обработчик в логгер.
_logger.addHandler(_stream_handler)

# Устанавливаем уровень логирования для логгера (DEBUG).
_logger.setLevel(logging.DEBUG)


# Экспортируем некоторые функции логирования для использования в других модулях.
setLevel = _logger.setLevel
debug = _logger.debug
info = _logger.info
warning = _logger.warning
error = _logger.error
critical = _logger.critical
