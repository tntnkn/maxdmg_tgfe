class TGFE_BadUserInSystem(Exception):
    def __init__(self, message, tg_user_id):
        self.message     = message 
        self.tg_user_id  = tg_user_id

        super(TGFE_BadUserInSystem, self).__init__( 
            (self.message, self.tg_user_id) )

    def __reduce__(self):
        return (TGFE_BadUserInSystem, (self.message, self.tg_user_id))


class TGFE_StatsDBError(Exception):
    def __init__(self, message):
        self.message     = message 

        super(TGFE_StatsDBError, self).__init__( 
            (self.message) )

    def __reduce__(self):
        return (TGFE_StatsDBError, (self.message))

