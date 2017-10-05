from pytz import timezone
import arrow


JKT = 'Asia/Jakarta'
JKTTZ = timezone(JKT)


def get_epoch_gmt7():
    """
    because default server on AWS EB using GMT timezone.
    it will look different when its developed locally.
    move to models from utils because utils still need to import models (avoid circular import)
    """
    # epoch_utc_now = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
    # return epoch_utc_now + 25200  # 7 hours
    # print epoch_utc_now + 25200
    # warning('SYSTEM: ' + strftime("%z", gmtime()))
    # warning('EPOCHGMT7Z'+datetime.now(timezone('UTC')).astimezone(timezone('Asia/Jakarta'))
    #     .strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    # warning('EPOCHGMT7Z'+datetime.utcnow().astimezone(timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    # warning('EPOCHGMT7: '+str(arrow.now('Asia/Jakarta').timestamp))
    return arrow.now(JKT).timestamp




def get_today_epoch_gmt7():
    # warning('XXX: '+str(arrow.get(arrow.now(JKT).date(), JKT).timestamp))
    return arrow.get(arrow.now(JKT).date(), JKT).timestamp

