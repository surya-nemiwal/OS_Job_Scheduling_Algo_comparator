class Proces:
    def __init__(self):
        self.burst = []
        self.arrival = []
        self.priority = []
        self.tat = []
        self.wt = []

    def calc(self, cmptime):
        length = len(self.arrival)
        tat = [cmptime[i] - self.arrival[i] for i in range(length)]
        wt = [tat[i] - self.burst[i] for i in range(length)]
        tat = sum(tat)/length
        wt = sum(wt)/length
        self.tat.append(tat)
        self.wt.append(wt)
    def fcfs(self):
        arrival = self.arrival
        burst = self.burst
        length = len(arrival)
        cmptime = [0] * length
        for i in range(length - 1):
            for j in range(length - i - 1):
                if (arrival[j] > arrival[j + 1]):
                    arrival[j], arrival[j + 1] = arrival[j + 1], arrival[j]
                    burst[j], burst[j + 1] = burst[j + 1], burst[j]
        #print(burst)
        #print(arrival)
        T = 0
        for i in range(length):
            current = arrival[i]
            if (current > T):
                T = current
            T = T + burst[i]
            cmptime[i] = T
        Proces.calc(self, cmptime)

    def sjfnonprem(self):
        burst = self.burst
        arrival = self.arrival
        tempburst = [i for i in burst]
        length = len(arrival)
        cmptime = [0] * length

        def nextprocess(time):
            temp = 100000000
            index = -1
            for i in range(length):
                if (arrival[i] <= time):
                    if (tempburst[i] < temp and tempburst[i] != 0):
                        temp = tempburst[i]
                        index = i
            return index

        T = 0
        total = sum(tempburst)
        while (total > 0):
            current = nextprocess(T)
            while (current == -1):
                T += 1
                current = nextprocess(T)
            T += tempburst[current]
            cmptime[current] = T
            total -= tempburst[current]
            tempburst[current] = 0
        Proces.calc(self, cmptime)

    def sjfprem(self):
        burst = self.burst
        arrival = self.arrival
        tempburst = [i for i in burst]
        length = len(arrival)
        # maxarrival = max(arrival)
        cmptime = [0] * length

        def nextprocess(time):
            temp = 100000000
            index = -1
            for i in range(length):
                if (arrival[i] <= time):
                    if (tempburst[i] < temp and tempburst[i] != 0):
                        temp = tempburst[i]
                        index = i
            return index

        total = sum(burst)
        T = 0
        while (total > 0):
            current = nextprocess(T)
            while current == -1:
                T += 1
                current = nextprocess(T)
            T += 1
            total -= 1
            tempburst[current] -= 1
            if tempburst[current] == 0:
                cmptime[current] = T

        Proces.calc(self, cmptime)

    def priononprem(self):
        burst = self.burst
        arrival = self.arrival

        tempburst = [i for i in burst]
        priority = self.priority
        length = len(arrival)
        cmptime = [0] * length
        total = sum(tempburst)
        T = 0

        def nextprocess(t):
            prio = -1
            temp = -1
            for i in range(length):
                if (arrival[i] <= t):
                    if (priority[i] > prio and tempburst[i] != 0):
                        prio = priority[i]
                        temp = i
            return temp

        while (total > 0):
            current = nextprocess(T)
            while (current == -1):
                T += 1
                current = nextprocess(T)
            T += tempburst[current]
            cmptime[current] = T
            total -= tempburst[current]
            tempburst[current] = 0

        Proces.calc(self, cmptime)

    def prioprem(self):
        burst = self.burst
        arrival = self.arrival

        tempburst = [i for i in burst]
        priority = self.priority
        length = len(arrival)
        cmptime = [0] * length
        total = sum(tempburst)
        T = 0

        def nextprocess(t):
            prio = -1
            temp = -1
            for i in range(length):
                if (arrival[i] <= t):
                    if (priority[i] > prio and tempburst[i] != 0):
                        prio = priority[i]
                        temp = i
            return temp

        while (total > 0):
            current = nextprocess(T)
            while (current == -1):
                T += 1
                current = nextprocess(T)
            T += 1
            tempburst[current] -= 1
            total -= 1
            if (tempburst[current] == 0):
                cmptime[current] = T

        Proces.calc(self, cmptime)

    def roundrobin(self):
        burst = self.burst
        tempburst = [i for i in burst]
        arrival = self.arrival
        qantum = 2
        length = len(arrival)
        # cmptime=[None]*length
        visited = [0 for i in range(length)]
        cmptime = visited
        queue = []
        maxarrivaltime = max(arrival)

        def queupdate(time):

            if (maxarrivaltime + qantum < time):
                return
            if (time >= qantum):
                time -= qantum
                temp = 1
                while (temp <= qantum):
                    time += 1
                    i = 0
                    while (i < length):
                        if (arrival[i] <= time and tempburst[i] != 0 and visited[i] == 0):
                            queue.append(i)
                            visited[i] = 1
                        i += 1
                    temp += 1
            else:
                i = 0
                while (i < length):
                    if (arrival[i] <= time and tempburst[i] != 0 and visited[i] == 0):
                        queue.append(i)
                        visited[i] = 1
                    i += 1

        T = 0
        queupdate(T)
        total = sum(tempburst)

        while (total > 0):
            # print(queue)
            while queue == []:
                T += qantum
                queupdate(T)
            current = queue.pop(0)
            if (tempburst[current] <= qantum):
                T = T + tempburst[current]
                total -= tempburst[current]
                tempburst[current] = 0
                cmptime[current] = T
                queupdate(T)
                while (queue == [] and total != 0):
                    T += qantum
                    queupdate(T)

            else:
                T += qantum
                tempburst[current] -= qantum
                queupdate(T)
                queue.append(current)
                total -= qantum
        Proces.calc(self, cmptime)

    def control(self):
        self.fcfs()
        self.sjfnonprem()
        self.sjfprem()
        self.priononprem()
        self.prioprem()
        self.roundrobin()



