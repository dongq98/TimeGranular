from datetime import datetime,timedelta
from Heap import Heap
import copy
import json

def validate(date_text):
    try:
        date_object = datetime.strptime(date_text, '%Y-%m-%d %I:%M')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD hh:mm")

def roundTime(dt=None, roundTo=600):
    if dt == None:
        dt = datetime.now()
    seconds = (dt - dt.min).seconds
    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + timedelta(0,rounding-seconds,-dt.microsecond)

def datetimeIterator(from_datetxt=None, to_datetxt=None, delta=timedelta(minutes=10)):
    if from_datetxt != None:
        validate(from_datetxt)
        from_date = roundTime(datetime.strptime(from_datetxt, '%Y-%m-%d %I:%M'))
    else:
        from_date = roundTime()
    if to_datetxt != None:
        validate(to_datetxt)
        to_date = datetime.strptime(to_datetxt, '%Y-%m-%d %I:%M')
    while to_date is None or from_date <= to_date:
        yield from_date
        from_date = from_date + delta
    return


class Main_schedule:
    def __init__(self):
        self._schtable = dict()
        self._maxid = 0
        
    def __len__(self):
        return self._maxid

    def find(self,schedulename):
        return self[schedulename]
        
    def addschedule(self,schedulename,member, start, end, suitable):
        validate(start),validate(end)
        assert start - datetime.now() > timedelta(0) and end - start > timedelta(0)
        newschedule = dict()
        newschedule['name'] = schedulename
        newschedule['member'] = member
        newschedule['start'] = roundTime(start)
        newschedule['end'] = roundTime(end)
        newschedule['startrange'] = startrange
        newschedule['endrange'] = endrange
        newschedule['suitable'] = suitable
        self._schtable.add(self._maxid,newschedule)
        self._maxid += 1
                
                
    def searchbesttime(self,schedulename, member, duration, endrange, startrange=roundTime()):
        counter = Heap()
        for i in self._schtable:
            cur = 0
            for j in i['member']:                
                if j in member:
                    cur += 1
            counter.add(i['start'],cur)
            counter.add(i['end'],-cur)
        base = 0
        listvar=[]
        localmin=[]
        while not counter.is_empty:
            temp = counter.delete
            start = temp[0]
            copied = copy.deepcopy(counter)
            var = copy.deepcopy(temp)
            collide = base * duration
            while var[0] - (start + timedelta(minute=duration)) < timedelta():
                collide += var[1]*(duration+int(start-var[0]))
                var = copied.delete()
            base = temp[1]
            listvar.append([collide,start])
        for i in range(1,len(listvar)-1):
            if listvar[i-1][0]-listvar[i][0] >=0 and listvar[i][0]-listvar[i+1][0]<=0:
                localmin.append(listvar[i])
        suitable = sorted(localmin, key=itemgetter(1))
        return (suitable, schedulename, member, duration, startrange, endrange)


    def editdetail(self,schedulename,member=None,duration=None,endrange=None, startrange=None):
        if member == None and duration == None and endrange == None and startrange == None:
            for i in range(len(self)):
                if schedulename == self._schtable[i]['name']:
                    return self._schtable[i]['suitable']
        else:
            for i in range(len(self)):
                if schedulename == self._schtable[i]['name']:
                    if member == None:
                        member = self._schtable[i]['member']
                    if duration == None:
                        duration = self._schtable[i]['end']-self._schtable[i]['start']
                    if endrange == None:
                        member = self._schtable[i]['endrange']
                    if startrange == None:
                        member = self._schtable[i]['startrange']
                    self.searchbesttime(schedulename, member, duration,endrange, startrange)
    def viewpersonal(self, person):
        schlist = []
        for i in range(len(self)):
            if person in self._schtable[i]['member']:
                schlist.append(self._schtable[i])
        return schlist