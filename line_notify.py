"""
class module
LINE Notify を使うクラスを定義
"""
# coding: utf-8
import requests


class LineNotify():
    """
    LINE通知を行うクラス
    """

    def __init__(self):
        """
        Parameters
        ----------
        url: string
            LineNotifyの送り先
        access_token: string
            LineNotifyのアクセストークン
        """
        self.url = "https://notify-api.line.me/api/notify"
        self.access_token = 'F78NKUuw6BhAytCPpjw2QgXXMmxV58iOxBA0HtQfYzh'

    def post_linenotify(self, message):
        """
        Lineにメッセージを送る

        Parameters
        ----------
        self : self
            クラス自身
        message: string
            実際に送るメッセージ
        """
        headers = {'Authorization': 'Bearer ' + self.access_token}
        payload = {'message': message}
        requests.post(self.url, headers=headers, params=payload,)
