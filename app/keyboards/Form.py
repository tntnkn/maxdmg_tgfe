class Form():
    def __init__(self, tg_user_id):
        self.tg_user_id = tg_user_id
        self.groups     = list()
        self.is_visible = False

    def AddGroup(self, group):
        if not group:
            return
        self.groups.append(group)

    async def Display(self):
        if self.IsVisible():
            return
        for group in self.groups:
            await group.Display()
        else:
            self.is_visible = True

    async def Hide(self):
        if not self.IsVisible():
            return
        for group in self.groups:
            await group.Hide()
        else:
            self.is_visible = False

    def IsVisible(self):
        return self.is_visible

