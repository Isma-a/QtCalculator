from typing import override

from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QLabel


class AdaptiveLabel(QLabel):

    @override
    def resizeEvent(self, event):

        super().resizeEvent(event)
        currentSize = 11 # Max police size
        font = self.font()
        font.setPointSize(currentSize) # Set back max police size

        while currentSize > 7 and QFontMetrics(font).boundingRect(self.text()).width() > self.width() - 10:
            font.setPointSize(currentSize) # Reduce police size til the text extends after the label (Stop at 7 to make it visible)
            currentSize -= 1

        self.setFont(font)