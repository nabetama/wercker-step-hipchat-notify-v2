# coding: utf-8

import hypchat


class HipChat(hypchat.HypChat):
    def __init__(self, config):
        super(HipChat, self).__init__(config['token'])
        self.config = config

    def send_message(self):
        room = self.get_room(self.config['room_id'])
        room.notification(self.config['message'], color=self.config['color'])
