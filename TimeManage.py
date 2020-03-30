
# Test: python3 -c "from app.TimeManage import TimeManage; ...
class TimeManage:
  # Test: "... print(TimeManage.format('01:00', '01:20'))"
  def format(stime, etime):
    t = TimeManage.split(stime)
    start = t[0]*3600 + t[1]*60 + t[2]
    stime = '{:02d}:{:02d}:{:02d}.0'.format(t[0], t[1], t[2])
    t = TimeManage.split(etime)
    end = t[0]*3600 + t[1]*60 + t[2]
    time = TimeManage.duration(start, end)
    if time == -1:
      return -1
    secs = int(time % 60)
    mins = int(time / 60)
    hours = int(time / 3600)
    t = [hours, mins, secs]
    dtime = '{:02d}:{:02d}:{:02d}.0'.format(t[0], t[1], t[2])
    return [stime, dtime]

  # Test: "... print(TimeManage.duration(50, 80))"
  def duration(start, end):
    time = end - start
    if time <= 0:
      return -1
    return time

  def split(time):
    time = time.split(':')
    if len(time) == 3:
      hours = int(time[0])
      mins = int(time[1])
      secs = int(time[2])
    else:
      hours = 0
      mins = int(time[0])
      secs = int(time[1])
    return [hours, mins, secs]

  # Test: " ... print(TimeManage.shorten('00:10:09.0'))"
  def shorten(time):
    return time.replace(':', '-').strip('0').strip('.').strip('-')
