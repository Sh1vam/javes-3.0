try:
    from ub.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String, UnicodeText


class bot_pm_ban(BASE):
    __tablename__ = "bot_pm_ban_sql"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


bot_pm_ban.__table__.create(checkfirst=True)


def is_botpmbanned(sender_id):
    try:
        return SESSION.query(bot_pm_ban).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def botban(sender):
    adder = bot_pm_ban(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def botunban(sender):
    rem = SESSION.query(bot_pm_ban).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
