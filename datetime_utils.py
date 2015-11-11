import pytz
import datetime


__doc__ = """

Guidelines

    * All datetimes should be converted to UTC before processing/storage.
    * ISO 8601 format should be used in storage with explicit timezone information ('Z' in case of UTC).
    * Datetime objects with no timezone (timezone unaware) should be considered as a "bug" in the application.

"""


class DateFormats:

    # 2015-11-01T03:36:49Z
    # 2015-11-01T03:36:49.578427Z
    ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
    ISO_FORMAT_PRECISE = '%Y-%m-%dT%H:%M:%S.%fZ'

    # 2015-11-01 03:36:49
    STANDARD_FORMAT = '%Y-%m-%d %H:%M:%S'

    # Nov 11 03:36 AM
    HUMAN_READABLE = '%b %d %-I:%M %p'


class TimeZones:

    # Baseline
    UTC = 'UTC'

    # US timezones
    CENTRAL = 'US/Central'
    EASTERN = 'US/Eastern'
    PACIFIC = 'US/Pacific'
    MOUNTAIN = 'US/Mountain'

    # ASIA timezones
    JAPAN = 'Asia/Tokyo'
    KOREA = 'Asia/Seoul'
    INDIA = 'Asia/Kolkata'
    CHINA = 'Asia/Shanghai'
    SINGAPORE = 'Asia/Singapore'


class DatetimeUtils(object):

    """
        This class provides convenience methods for timezone and date-time format conversions.

        * Currently this class is not thread safe
        * The datetime objects which are not timezone aware are considered bugs

    """

    def __init__(self):
        pass

    def utc_now_tz(self):
        """
            returns timezone aware datetime object in with current date and time in utc
        """
        return pytz.utc.localize(datetime.datetime.utcnow())

    def datetime_to_str(self, datetime_object, output_format=DateFormats.ISO_FORMAT):
        """
            converts datetime object to a datetime-string, defaults to ISO 8601 format
        """
        return datetime_object.strftime(output_format)

    def seconds_since_epoch_to_datetime(seconds_since_epoch):
        """
            returns timezone aware datetime object in UTC
        """
        return pytz.utc.localize(datetime.datetime.utcfromtimestamp(seconds_since_epoch))

    def str_to_datetime(self, datetime_string, input_format=None, input_timezone=None):
        """
            returns timezone aware datetime object from the supplied datetime-string and input_timezone
        """
        if datetime_string is None or datetime_string == '':
            raise Exception("datetime_string is either None or ''")
        if input_format is None:
            raise Exception("Please specify input datetime format. For example: '%Y-%m-%d %H:%M:%S'\n \
                             You can use some common formats from DateFormats class of datetime_utils module")
        if input_timezone is None:
            raise Exception("Please specify input timezone. For example: 'US/Pacific'\n \
                             You can use some common timezones from TimeZones class of datetime_utils module")
        datetime_object = datetime.datetime.strptime(
            datetime_string, input_format)
        return pytz.timezone(input_timezone).localize(datetime_object)

    def convert_timezone(self, datetime_object, target_timezone=None):
        """
            converts timezone for a timezone-aware datetime object
        """
        if datetime_object is None:
            raise Exception("datetime_object is None")
        if datetime_object.tzinfo is None:
            raise Exception(
                "The datetime object supplied for this input is not timezone aware. Please supply timezone aware datetime object")
        if target_timezone is None:
            raise Exception("Please specify target timezone. For example: 'US/Pacific' or 'UTC'\n \
                             You can use some common timezones from TimeZones class of datetime_utils module")
        return datetime_object.astimezone(pytz.timezone(target_timezone))

if __name__ == '__main__':
    dt = DatetimeUtils()
    now = dt.utc_now_tz()
    dt_obj = dt.str_to_datetime(
        '2015-11-11T23:37:30Z', DateFormats.ISO_FORMAT, 'UTC')
    cnv = dt.convert_timezone(dt_obj, TimeZones.PACIFIC)
    print now.strftime(DateFormats.HUMAN_READABLE)
    print dt_obj.strftime(DateFormats.STANDARD_FORMAT)
    print cnv.strftime(DateFormats.STANDARD_FORMAT)
